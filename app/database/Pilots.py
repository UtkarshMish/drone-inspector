

from pydantic import Field

from app.database.util import SafeDocument


class Pilots(SafeDocument):
    id: int = Field(...)
    name: str = Field(...)
    address: str = Field(...)
    phone: str = Field(...)
    experience: int = Field(...)
    skill: int = Field(...)
    country: str = Field(...)

    def __init__(self,
                 id: int,
                 name: str,
                 address: str,
                 phone: str,
                 experience: int,
                 skill: int,
                 country: str,
                 *args, **kwargs):
        super().__init__(
            id=int(id),
            name=str(name),
            address=str(address),
            phone=str(phone),
            experience=int(experience),
            skill=int(skill),
            country=str(country), *args, **kwargs)
