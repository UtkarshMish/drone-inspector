
from beanie import Document


class SafeDocument(Document):
    async def saveWithChecks(self, session=None):
        if await self.find_one({"_id": self.id}):
            return None
        return await super().save(session=session)
