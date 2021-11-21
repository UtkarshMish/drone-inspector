
from beanie import Document
from pydantic import BaseModel, Field


class SafeDocument(Document):
    async def saveWithChecks(self, session=None):
        if await self.find_one({"_id": self.id}):
            return None
        return await super().save(session=session)


class BaseIdModel(BaseModel):
    id: int = Field(alias="_id")


class BaseRegIdModel(BaseModel):
    reg_id: int
