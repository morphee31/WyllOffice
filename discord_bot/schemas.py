from pydantic import BaseModel, EmailStr, validator
from typing import Literal

from datetime import datetime

class InitUser(BaseModel):
    user_id:str
    firstname: str
    lastname: str
    email: EmailStr = None

class PlanningDate(BaseModel):
    day: str
    period: Literal["am", "pm", "day"] = "day"