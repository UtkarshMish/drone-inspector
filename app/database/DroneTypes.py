from typing import Optional

from app.database.util import SafeDocument
from pydantic import Field


class DroneTypes(SafeDocument):
    id: int = Field(...)
    model_name: str = Field(...)
    brand: str = Field(...)
    model_year: str = Field(...)
    endurance_min: str = Field(...)
    sl_no: str = Field(...)
    type: str = Field(...)

    def __init__(self, model_name: str, brand: str, model_year: str,
                 endurance_min: str, sl_no: str, type: str, *args, **kwargs):

        super().__init__(model_name=str(model_name),
                         brand=str(brand),
                         model_year=str(model_year),
                         endurance_min=str(endurance_min),
                         sl_no=str(sl_no),
                         type=str(type),
                         *args,
                         **kwargs)
