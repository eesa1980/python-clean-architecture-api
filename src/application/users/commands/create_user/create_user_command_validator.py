from pydantic import BaseModel, EmailStr, Field, ValidationError

from src.application.common.exceptions import ValidationException


class RequestBodySchema(BaseModel):
    email: EmailStr = Field(..., description="The email of the user")
    firstname: str = Field(..., description="The firstname of the user")
    lastname: str = Field(..., description="The lastname of the user")

    class Config:
        extra = "forbid"

    @staticmethod
    def validate(self):
        try:
            return RequestBodySchema(email=self.email, firstname=self.firstname,
                                     lastname=self.lastname)
        except ValidationError as e:
            raise ValidationException("Invalid request body", e.json())


class ResponseSchema(BaseModel):
    id: int = Field(..., description="The id of the user")

    class Config:
        extra = "forbid"

    @staticmethod
    def validate(self):
        try:
            return ResponseSchema(id=self.id)
        except ValidationError as e:
            raise ValidationException("Invalid response body", e.json())

