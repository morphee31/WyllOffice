from pydantic import EmailStr, SecretStr, Field, BaseModel
from enum import Enum
from models import BaseDBModel
import datetime
from typing import Literal




class Planning(BaseModel):
    day: datetime.date
    period: Literal["am", "pm", "day"]


class UserModel(BaseDBModel):
    planning: None | Planning = Field(default=None, description="Day of presence")


class CreateUserModel(UserModel):
    email: EmailStr
    firstname: str
    lastname: str
    # password: SecretStr


class ReadUserModel(UserModel):
    email: EmailStr = None
    firstname: str = None
    lastname:str = None


class UpdateUserModel(BaseModel):
    email: EmailStr = None
    firstname: str = None
    lastname:str = None
    planning: None | Planning = Field(default=None, description="Day of presence")
    

class UpdateUserPasswordModel(BaseDBModel):
    email : EmailStr
    password: SecretStr
