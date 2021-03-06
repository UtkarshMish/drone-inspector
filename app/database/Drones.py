from __future__ import annotations

from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from app.database.DroneTypes import DroneTypes
from app.database.Pilots import Pilots
from app.database.util import SafeDocument
from beanie import Link, PydanticObjectId
from beanie.odm.operators.find.comparison import GTE
from pydantic import UUID4, BaseModel, Field


class Location(BaseModel):

    latitude: float = Field(...)

    longitude: float = Field(...)

    def __init__(self, latitude: float, longitude: float) -> None:

        super().__init__(latitude=float(latitude), longitude=float(longitude))


class DroneModel(BaseModel):

    drone_name: str = Field(...)

    location: Location = Field(...)

    last_seen: datetime = Field(default_factory=datetime.now)

    first_launch: datetime = Field(...)

    total_flight_time_min: int = Field(...)


class DroneObject():

    drone_type: DroneTypes

    pilot: Pilots

    reg_id: int
    drone_name: str

    location: Location
    last_seen: datetime

    first_launch: datetime

    total_flight_time_min: int

    def __init__(self, drone_name: str, location: Location,
                 last_seen: datetime, first_launch: datetime,
                 total_flight_time_min: int, reg_id: int,
                 drone_type: DroneTypes, pilot: Pilots):

        self.drone_name = drone_name

        self.location = location

        self.last_seen = last_seen

        self.first_launch = first_launch

        self.total_flight_time_min = total_flight_time_min

        self.reg_id = reg_id

        self.drone_type = drone_type

        self.pilot = pilot

    def dict(self):
        return self.__dict__

    def __str__(self) -> str:

        return str(self.dict())


class Drones(SafeDocument, DroneModel):

    id: PydanticObjectId = Field(default_factory=PydanticObjectId)

    reg_id: int = Field(...)

    drone_type: Link[DroneTypes] = Field(...)

    pilot: Link[Pilots] = Field(...)

    @staticmethod
    async def findByFirstLaunch(date_time: datetime):
        response_dict = dict()
        response_dict["date_time"] = date_time
        response_dict["traditional_find_many"] = await Drones.find_many({
            "first_launch": {
                "$gte": date_time
            }
        }).to_list()
        response_dict["using_GTE_operator"] = await Drones.find_many(
            GTE(Drones.first_launch, date_time)).to_list()
        response_dict["using_find_one"] = await Drones.find_one(
            Drones.first_launch == date_time)
        response_dict["using_all_then_filter"] = [
            *filter(lambda item: item.first_launch == date_time, await
                    Drones.all().to_list())
        ]

        return response_dict

    def __init__(self, drone_name: str, location: Location,
                 last_seen: datetime, first_launch: datetime,
                 total_flight_time_min: int, reg_id: int, drone_type: int,
                 pilot: int, *args, **kwargs):

        super().__init__(drone_name=drone_name,
                         location=location,
                         last_seen=last_seen,
                         first_launch=first_launch,
                         total_flight_time_min=total_flight_time_min,
                         reg_id=reg_id,
                         drone_type=drone_type,
                         pilot=pilot,
                         *args,
                         **kwargs)

    @staticmethod
    async def getAll(pageNo: int) -> List[Drones]:

        LIMIT = 20

        OFFSET = LIMIT * pageNo if pageNo > 1 else 0

        return await Drones.find_many(
            skip=OFFSET,
            limit=LIMIT,
            fetch_links=True,
        ).to_list()
