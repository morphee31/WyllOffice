from fastapi import APIRouter

from users.models import UserCreationModel
from users.service import create_user_service

user_router = APIRouter(
    prefix="/user"
)


@user_router.post(
    path="/"
)
async def create_user(user: UserCreationModel):
    await create_user_service(user)


@user_router.get(
    path="/{user_id}"
)
async def get_user(user_id: str):
    return {"message": f"user_id={user_id}"}


@user_router.get(
    path="/"
)
async def list_user():
    # TODO document why this method is empty
    pass


@user_router.put(
    path="/{user_id}"
)
async def update_user(user_id: str):
    # TODO document why this method is empty
    pass

@user_router.delete(
    path="/{user_id}"
)
async def disable_user(user_id: str):
    # TODO document why this method is empty
    pass
