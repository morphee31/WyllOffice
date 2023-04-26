from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from models import BaseDBModel
from typing import Literal


class Planning(BaseModel):
    day: datetime
    period: Literal["am", "pm", "day"] = "day"

    @validator("day", pre=True)
    def parse_day(cls, value):
        return datetime.strptime(value, '%d/%m/%Y')

class InsertOneResult(BaseDBModel):
    acknowledged: bool

class UserResult(BaseModel):
    user_id: str = Field(..., description="Unique id of user")
    email: EmailStr = Field(..., description="Email of user")
    firstname: str = Field(..., description="Firstname of user")
    lastname: str = Field(..., description="Lastname of user")
    planning: list | list[Planning] = Field(default=list(), description="List of presence day")
    disabled: bool  = None 




