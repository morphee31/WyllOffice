from fastapi import APIRouter

from users.models import CreateUserModel
from users.service import create_user_service, list_users_service
from users.schemas import InsertOneResult, FindOneResult



user_router = APIRouter(
    prefix="/user"
)


@user_router.post(
    path="/",
    response_model=InsertOneResult
)
async def create_user(user: CreateUserModel):
    result: InsertOneResult = await create_user_service(user)
    return result



@user_router.get(
    path="/{user_id}"
)
async def get_user(user_id: str):
    return {"message": f"user_id={user_id}"}


@user_router.get(
    path="/",
    response_model=list[FindOneResult]
)
async def list_user():
    find_results = list_users_service()
    return find_results


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
