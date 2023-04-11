from fastapi import APIRouter

from models import User


user_router = APIRouter(
    prefix="/user"
)

user_router.post(
    path="/"
)
async def create_user(user:User):
    pass


user_router.get(
    path="/{user_id}"
)
async def get_user(user_id: str):
    pass
