from fastapi import FastAPI

from users.router import user_router

app = FastAPI()
app.include_router(user_router)