from pydantic import EmailStr, SecretStr

from ..models import BaseDBModel


class UserModel(BaseDBModel):
    email: EmailStr
    firstname: str
    lastname: str


class UserCreationModel(UserModel):
    password: SecretStr
