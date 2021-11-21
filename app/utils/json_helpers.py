from pydantic import BaseModel

from app.database import DroneTypes
from app.database.Drones import Location
from app.database.Drones import DroneObject
from app.database.Pilots import Pilots

from json import JSONDecoder
from beanie import PydanticObjectId
from bson import ObjectId
import typing as t
from flask.json import JSONEncoder


class CustomEncoder(JSONEncoder):
    def default(self, o: t.Any) -> t.Any:
        if isinstance(o, PydanticObjectId) or isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, BaseModel):
            return o.dict(exclude={"_id", "revision_id"})
        return super().default(o)


class CustomDecoder(JSONDecoder):
    def __init__(self,
                 *,
                 parse_float: t.Callable[[str], t.Any] = None,
                 parse_int: t.Callable[[str], t.Any] = None,
                 parse_constant: t.Callable[[str], t.Any] = None,
                 strict: bool = None,
                 object_pairs_hook: t.Callable[[
                     list[tuple[str, t.Any]]], t.Any] = None,
                 object_hook: t.Callable[[(dict[str, t.Any])], t.Any] = None) -> None:
        self.old_hook = object_hook
        super().__init__(object_hook=self.object_hook,
                         parse_float=parse_float,
                         parse_int=parse_int,
                         parse_constant=parse_constant,
                         strict=strict,
                         object_pairs_hook=object_pairs_hook)

    def object_hook(self, dct: any):
        if isinstance(dct, dict) and \
                'drone_name' in dct and \
                dct.get("location") and isinstance(dct["location"], dict) and \
                dct.get("drone_type") and isinstance(dct['drone_type'], dict) and \
                dct.get("pilot") and isinstance(dct['pilot'], dict):
            location = Location(dct["location"]["latitude"],
                                dct["location"]["longitude"])
            drone_type = DroneTypes(
                dct['drone_type']["id"], dct['drone_type']["model_name"],
                dct['drone_type']["brand"], dct['drone_type']["model_year"],
                dct['drone_type']["endurance_min"], dct['drone_type']["sl_no"],
                dct['drone_type']["type"]
            )
            pilot = Pilots(
                dct['pilot']["id"],
                dct['pilot']["name"],
                dct['pilot']["address"], dct['pilot']["phone"],
                dct['pilot']["experience"], dct['pilot']["skill"],
                dct['pilot']["country"]

            )
            drone = DroneObject(
                dct['drone_name'],
                location,
                dct['last_seen'],
                dct['first_launch'],
                dct['total_flight_time_min'],
                dct['reg_id'],
                drone_type,
                pilot,
            )
            return drone
        return dct
