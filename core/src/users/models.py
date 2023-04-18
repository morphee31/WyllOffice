from ..models import OID, BaseDBModel
from pydantic import EmailStr, SecretStr

class UserModel(BaseDBModel):
    email: EmailStr
    firstname: str
    lastname: str

class UserCreationModel(UserModel):
    password: SecretStr