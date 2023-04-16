from pydantic import BaseModel, EmailStr, SecretStr


class User(BaseModel):
    email: EmailStr
    fristname: str
    lastname: str
    discord_id: str = None


class CreateUser(User)
    password: SecretStr
