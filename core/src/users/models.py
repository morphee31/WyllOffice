from pydantic import EmailStr, SecretStr, Field, BaseModel

from models import BaseDBModel
from users.schemas import Planning


class UserModel(BaseDBModel):
    planning: None | Planning = Field(default=None, description="Day of presence")


class CreateUserModel(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    planning: None | Planning = Field(default=None, description="Day of presence")

    # password: SecretStr


class ReadUserModel(UserModel):
    email: EmailStr = None
    firstname: str = None
    lastname: str = None


class UpdateUserModel(BaseModel):
    email: EmailStr = None
    firstname: str = None
    lastname: str = None
    planning: None | Planning = Field(default=None, description="Day of presence")


class UpdateUserPasswordModel(BaseDBModel):
    email: EmailStr
    password: SecretStr
