from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    fristname: str
    lastname: str
    discord_id: str = None
