from typing import Optional

from src.application.common.exceptions import InternalServerErrorException
from src.application.common.interfaces import IUserRepository
from .create_user_command_validator import RequestBodySchema, ResponseSchema
from src.domain.entities import User


class RequestBody:
    def __init__(self, firstname: Optional[str], lastname: Optional[str], email: Optional[str]):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class CreateUserCommand:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    @staticmethod
    class ValidateBody(RequestBodySchema):
        pass

    @staticmethod
    class ValidateResponse(ResponseSchema):
        pass

    async def execute(self, request_body: RequestBodySchema):

        validated = CreateUserCommand.ValidateBody(
            firstname=request_body.firstname,
            lastname=request_body.lastname,
            email=request_body.email
        )

        user: User = await self.user_repository.create_user(User(
            firstname=validated.firstname,
            lastname=validated.lastname,
            email=validated.email
        ))

        if not user:
            raise InternalServerErrorException("User not created")

        return CreateUserCommand.ValidateResponse(
            id=user.id,
        )
