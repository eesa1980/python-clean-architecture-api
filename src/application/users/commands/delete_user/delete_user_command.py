from src.application.common.exceptions import NotFoundException
from src.application.common.interfaces import IUserRepository
from .delete_user_command_validator import QuerySchema


class DeleteUserCommand:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    @staticmethod
    class ValidateQuery(QuerySchema):
        pass

    async def execute(self, user_id: int) -> None:
        validated = DeleteUserCommand.ValidateQuery(
            user_id=user_id
        )
        
        user = await self.user_repository.get_user(validated.user_id)

        if not user:
            raise NotFoundException(f"User with id {validated.user_id} not found")

        await self.user_repository.delete_user(validated.user_id)
