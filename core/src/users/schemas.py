from models import BaseDBModel
from pydantic import BaseModel, Field


class Planning(BaseModel):
    day: datetime.date
    period: Literal["am", "pm", "day"]

class InsertOneResult(BaseDBModel):
    acknowledged: bool

class FindOneResult():
    email: EmailStr = Field(..., description="Email of user")
    firstname: str = Field(..., description="Firstname of user")
    lastname: str = Field(..., description="Lastname of user")
    planning: None | Planning = Field(default=None, description="Day of presence")
