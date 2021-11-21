
from beanie import Document
from pydantic import BaseModel


class SafeDocument(Document):
    async def saveWithChecks(self, session=None):
        if await self.find_one({"_id": self.id}):
            return None
        return await super().save(session=session)


class BaseIdModel(BaseModel):
    id: int


class BaseRegIdModel(BaseModel):
    reg_id: int
