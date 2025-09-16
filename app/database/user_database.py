import asyncio
from fastapi.encoders import jsonable_encoder
from app.config.config import DATABASE_NAME, MONGODB_CON_STR
from motor.motor_asyncio import AsyncIOMotorClient

class AuthenticationData():
    client = AsyncIOMotorClient(MONGODB_CON_STR)
    client.get_io_loop = asyncio.get_running_loop
    auth_user_collection = client[DATABASE_NAME]["auth_user"]


    async def register(self,payload):
        document = jsonable_encoder(payload)
        await self.auth_user_collection.inser_one(document)
        return document

def get_by_where_clouse(self,where_clouse):
    return self.auth_user_collection.find_one(where_clouse)



