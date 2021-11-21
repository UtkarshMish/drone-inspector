from pymongo.errors import BulkWriteError
from json import loads
from math import ceil
from typing import List
from flask import Blueprint, request

from app.database import Drones, init_DB
from app.database.DroneTypes import DroneTypes
from app.database.Drones import DroneObject
from app.database.Pilots import Pilots
from app.database.util import BaseIdModel, BaseRegIdModel
from app.utils import CustomDecoder

api_route = Blueprint("api", __name__, url_prefix="/api")


@api_route.get("/drones")
async def get_drones():
    await init_DB()
    pageNo: int = int(request.args["page"]) if request.args.get(
        "page") and str(request.args["page"]).isnumeric() else 1
    return {"result": await Drones.getAll(pageNo), "total_pages": ceil(await Drones.all().count()/20)}


@api_route.post("/upload-data")
async def get_pilot():
    await init_DB()
    file = request.files.get("json_file")
    if file:
        json_item = loads(file.stream.read().decode("utf8"), cls=CustomDecoder)
        try:
            isWritten = await writeJSONData(json_item)
            if isWritten:
                return {"success": True}
        except BulkWriteError as BulkErr:
            return {"success": False, "error": BulkErr.code}
    return {"success": False}


@api_route.post("/drones")
async def set_drone_details():
    await init_DB()
    item: List[DroneObject] = request.get_json()
    try:
        isWritten = await writeJSONData(item)
        if isWritten:
            return {"success": True}

    except BulkWriteError as BulkErr:
        return {"success": False, "error": BulkErr.code}
    return {"success": False}


def check_if_droneObject(item) -> bool:
    return isinstance(item, list) and all([isinstance(element, DroneObject) for element in item])


async def writeJSONData(item) -> bool:
    isDocument: bool = check_if_droneObject(item)
    if isDocument:
        drone_list: List[Drones] = list()
        pilot_list: List[Pilots] = list()
        drone_type_list: List[DroneTypes] = list()
        pilot_id_list: List[int] = list(map(lambda item: item.id,
                                            await Pilots.all(
                                                projection_model=BaseIdModel).to_list()))
        drone_type_id_list: List[int] = list(map(lambda item: item.id,
                                                 await DroneTypes.all(
                                                     projection_model=BaseIdModel).to_list()))
        drone_reg_id_list: List[int] = list(map(lambda item: item.reg_id,
                                                await Drones.all(
                                                    projection_model=BaseRegIdModel).to_list()))
        for object in item:

            if not object.reg_id in drone_reg_id_list:
                drone_list.append(
                    Drones(
                        object.drone_name,
                        object.location, object.last_seen,
                        object.first_launch, object.total_flight_time_min,
                        object.reg_id, object.drone_type.id, object.pilot.id)
                )
            if not object.pilot.id in pilot_id_list:
                pilot_list.append(object.pilot)
                pilot_id_list.append(object.pilot.id)

            if not object.drone_type.id in drone_type_id_list:
                drone_type_list.append(object.drone_type)
                drone_type_id_list.append(object.drone_type.id)

            await DroneTypes.insert_many(drone_type_list)
            await Pilots.insert_many(pilot_list)
            await Drones.insert_many(drone_list)
    return isDocument
