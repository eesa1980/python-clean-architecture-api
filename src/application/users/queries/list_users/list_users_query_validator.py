import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    id: int = Field(..., description="The id of the user")
    email: str = Field(..., description="The email of the user")
    firstname: str = Field(..., description="The firstname of the user")
    lastname: str = Field(..., description="The lastname of the user")
    created_at: datetime.datetime = Field(..., description="The date the user was created")
    updated_at: Optional[datetime.datetime] = Field(..., description="The date the user was last updated")

    class Config:
        extra = "forbid"
