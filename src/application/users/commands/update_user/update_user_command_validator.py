from typing import Optional

from src.application.common.exceptions import ValidationException
from pydantic import BaseModel, EmailStr, Field, ValidationError


class RequestBodySchema(BaseModel):
    email: Optional[EmailStr] = Field(None, description="The email of the user")
    firstname: Optional[str] = Field(None, description="The firstname of the user")
    lastname: Optional[str] = Field(None, description="The lastname of the user")

    class Config:
        extra = "forbid"

