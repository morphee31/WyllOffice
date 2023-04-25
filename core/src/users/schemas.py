from pydantic import BaseModel, Field, EmailStr
import datetime
from models import BaseDBModel
from typing import Literal


class Planning(BaseModel):
    day: datetime.date
    period: Literal["am", "pm", "day"]


class InsertOneResult(BaseDBModel):
    acknowledged: bool

class UserResult(BaseModel):
    user_id: str = Field(..., description="Unique id of user")
    email: EmailStr = Field(..., description="Email of user")
    firstname: str = Field(..., description="Firstname of user")
    lastname: str = Field(..., description="Lastname of user")
    planning: None | Planning = Field(default=None, description="Day of presence")
    disabled: bool = None 

