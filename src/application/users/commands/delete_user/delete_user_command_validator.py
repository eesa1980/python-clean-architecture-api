from pydantic import BaseModel, Field


class QuerySchema(BaseModel):
    user_id: int = Field(..., description="The id of the user")

    class Config:
        extra = "forbid"
