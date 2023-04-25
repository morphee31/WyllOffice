from fastapi import APIRouter, HTTPException

from users.models import CreateUserModel, UpdateUserModel
from users.service import create_user_service, list_users_service, update_user_service
from users.schemas import InsertOneResult, FindOneResult

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent
user_templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
# user_templates = Jinja2Templates("templates")


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
    response_class=HTMLResponse
)
async def list_user(request: Request):
    find_results = await list_users_service()
    return user_templates.TemplateResponse("users_list.j2", {"request": request, "users" : find_results})


@user_router.put(
    path="/{user_id}"
)
async def update_user(user_id:str, user: UpdateUserModel):
    update_result = await update_user_service(user_id, user)
    if not update_result:
        raise HTTPException(status_code=404, detail="User not found")
    return update_result
    

@user_router.delete(
    path="/{user_id}"
)
async def disable_user(user_id: str):
    user = UpdateUserModel(disabled=True)
    update_result = await update_user_service(user_id, user)
    return update_result
