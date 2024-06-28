from src.application.common.exceptions import NotFoundException
from src.application.common.interfaces import IUserRepository
from .get_user_query_validator import QuerySchema, ResponseSchema


class GetUserByIdQuery:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    @staticmethod
    class ValidateQuery(QuerySchema):
        pass

    @staticmethod
    class ValidateResponse(ResponseSchema):
        pass

    async def execute(self, user_id: int) -> ResponseSchema:
        GetUserByIdQuery.ValidateQuery(user_id=user_id)

        user = await self.user_repository.get_user(user_id)

        if not user:
            raise NotFoundException(f"User with id {user_id} not found")

        return GetUserByIdQuery.ValidateResponse(
            id=user.id,
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
