from fastapi import APIRouter, HTTPException

from users.models import CreateUserModel, UpdateUserModel
from users.service import create_user_service, list_users_service, update_user_service, get_user_service
from planning.service import add_date_to_user, remove_date_to_user, get_users_by_date
from users.schemas import InsertOneResult, UserResult

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from users.schemas import Planning
from planning.schemas import PlanningResult

from datetime import datetime

#BASE_PATH = Path(__file__).resolve().parent
#user_templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
# user_templates = Jinja2Templates("templates")


planning_router = APIRouter(
    prefix="/planning",
    tags=["planning"]
)

@planning_router.post(
    path="/{user_id}/add_date",
    response_model=UserResult,
    response_model_exclude_unset=True,
    response_model_exclude_none=True
)
async def add_date(user_id: str, date:Planning):
    result = await add_date_to_user(user_id, date)
    return result


@planning_router.delete(
    path="/{user_id}/remove_date",
    response_model=UserResult,
    response_model_exclude_unset=True,
    response_model_exclude_none=True
)
async def remove_date(user_id: str, date:str):
    date = datetime.strptime(date, '%d/%m/%Y')
    result = await remove_date_to_user(user_id, date)
    return result


@planning_router.get(
    path="/{date}",
    response_model= list[PlanningResult]
)
async def list_users_by_date(date:str):
    date = datetime.strptime(date, '%d-%m-%Y')
    users = await get_users_by_date(date)
    return users
