from typing import Optional

from app.database.util import SafeDocument
from pydantic import Field


class Pilots(SafeDocument):
    id: int = Field(...)
    name: str = Field(...)
    address: str = Field(...)
    phone: str = Field(...)
    experience: int = Field(...)
    skill: int = Field(...)
    country: str = Field(...)

    def __init__(self, name: str, address: str, phone: str, experience: int,
                 skill: int, country: str, *args, **kwargs):

        super().__init__(name=str(name),
                         address=str(address),
                         phone=str(phone),
                         experience=int(experience),
                         skill=int(skill),
                         country=str(country),
                         *args,
                         **kwargs)
