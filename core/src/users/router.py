from fastapi import APIRouter

from schema import User, CreateUser


user_router = APIRouter(
    prefix="/user"
)

user_router.post(
    path="/"
)
async def create_user(user:CreateUser):
    pass


user_router.get(
    path="/{user_id}"
)
async def get_user(user_id: str):
    pass
