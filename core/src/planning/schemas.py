from pydantic import BaseModel, Field

class PlanningResult(BaseModel):
    user_id: str = Field(..., description="Unique id of user")
    firstname: str = Field(..., description="Firstname of user")
    lastname: str = Field(..., description="Lastname of user")
    