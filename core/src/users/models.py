from pydantic import EmailStr, SecretStr, Field
from enum import Enum
from models import BaseDBModel
import datetime
from typing import Literal




class Planning(BaseDBModel):
    day: datetime.date
    period: Literal["am", "pm", "day"]


class UserModel(BaseDBModel):
    email: EmailStr
    firstname: str
    lastname: str
    planning: None | Planning = Field(default=None, description="Day of presence")


class UserCreationModel(UserModel):
    password: SecretStr