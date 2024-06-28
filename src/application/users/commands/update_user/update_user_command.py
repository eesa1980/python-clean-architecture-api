from src.application.common.exceptions import NotFoundException
from src.application.common.interfaces import IUserRepository
from .update_user_command_validator import RequestBodySchema
from src.domain.entities import User


class UpdateUserCommand:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    @staticmethod
    class UpdateUserRequestBody(RequestBodySchema):
        pass

    async def execute(self, user_id: int, request_body: RequestBodySchema) -> None:
        validated = RequestBodySchema(
            email=request_body.email,
            firstname=request_body.firstname,
            lastname=request_body.lastname
        )

        user = await self.user_repository.get_user(user_id)

        if not user:
            raise NotFoundException(f"User with id {user_id} not found")

        await self.user_repository.update_user(
            User(
                _id=user_id,
                email=validated.email or user.email,
                firstname=validated.firstname or user.firstname,
                lastname=validated.lastname or user.lastname
            )
        )
