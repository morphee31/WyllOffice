from fastapi import APIRouter, HTTPException

from users.models import CreateUserModel, UpdateUserModel
from users.service import create_user_service, list_users_service, update_user_service, get_user_service, add_date_to_user, remove_date_to_user, get_users_by_date
from users.schemas import InsertOneResult, UserResult, UsersResult

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from users.schemas import Planning

from datetime import datetime

BASE_PATH = Path(__file__).resolve().parent
user_templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
# user_templates = Jinja2Templates("templates")


user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@user_router.post(
    path="",
    response_model=InsertOneResult
)
async def create_user(user: CreateUserModel):
    result: InsertOneResult = await create_user_service(user)
    return result



@user_router.get(
    path="/{user_id}",
    response_model=UserResult,
    response_model_exclude_unset=True,
    response_model_exclude_none=True
)
async def get_user(user_id: str):
    find_result = await get_user_service(user_id)
    if find_result == None:
        raise HTTPException(status_code=404, detail="User not founded")
    return find_result



@user_router.get(
    path="",
    response_model=list[UsersResult]
)
async def get_users(request: Request):
    find_results = await list_users_service()
    return find_results

@user_router.put(
    path="/{user_id}",
    response_model=UserResult,
    response_model_exclude_unset=True,
    response_model_exclude_none=True
)
async def update_user(user_id:str, user: UpdateUserModel):
    update_result = await update_user_service(user_id, user)
    if not update_result:
        raise HTTPException(status_code=404, detail="User not found")
    return update_result
    

@user_router.delete(
    path="/{user_id}",
    response_model=UserResult,
    response_model_exclude_unset=True,
    response_model_exclude_none=True
)
async def disable_user(user_id: str):
    user = UpdateUserModel(disabled=True)
    update_result = await update_user_service(user_id, user)
    return update_result


