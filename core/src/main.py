import uvicorn
from fastapi import FastAPI
from loguru import logger

from config import get_config
from database import db
from users.router import user_router
from planning.router import planning_router

from fastapi import APIRouter, HTTPException

from users.models import CreateUserModel, UpdateUserModel
from users.service import create_user_service, list_users_service, update_user_service, get_user_service, add_date_to_user, remove_date_to_user, get_users_by_date
from users.schemas import InsertOneResult, UserResult

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from users.schemas import Planning

from datetime import datetime

BASE_PATH = Path(__file__).resolve().parent
user_templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI()
app.include_router(user_router)
app.include_router(planning_router)

@app.on_event("startup")
async def startup():
    config = get_config()
    logger.info(f"Statup {config.app_name}")
    if config.env == "prod":
        DB_PATH = f"mongodb://{config.mongo_user}:{config.mongo_password}@{config.mongo_host}:{config.mongo_port}"
    else:
        DB_PATH = f"mongodb://{config.mongo_host}:{config.mongo_port}"
    await db.connect_to_database(path=DB_PATH)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


@app.get(
    path="/"
)
async def home():
    return "Welcome on WOOP"

@app.get(
    path="",
    response_class=HTMLResponse
)
async def list_users(request: Request):
    find_results = await list_users_service()
    return user_templates.TemplateResponse("users_list.j2", {"request": request, "users" : find_results})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
