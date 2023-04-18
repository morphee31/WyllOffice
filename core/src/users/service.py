from models import UserCreationModel

from database import db

async def create_user_service(user : UserCreationModel):
    result = await db.insert_one(user.dict())
    return result.inserted_id
