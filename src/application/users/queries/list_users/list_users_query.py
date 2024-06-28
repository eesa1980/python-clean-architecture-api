from typing import List
from src.application.common.interfaces import IUserRepository
from .list_users_query_validator import ResponseSchema

from src.domain.entities import User


class ListUsersQuery:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    class ValidateResponse(ResponseSchema):
        pass

    async def execute(self) -> List[User]:
        users: List[User] = await self.user_repository.list_users()
        return users
