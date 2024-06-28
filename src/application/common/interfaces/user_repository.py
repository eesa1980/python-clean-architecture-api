from abc import ABC, abstractmethod
from typing import List

from src.domain.entities import User


class IUserRepository(ABC):
    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def list_users(self) -> List[User]:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def update_user(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass
