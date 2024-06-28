from abc import ABC
from datetime import datetime

from src.application.common.interfaces import IUserRepository
from src.domain.entities import User
from src.infrastructure.models import UserModel


class UserRepository(IUserRepository, ABC):
    def __init__(self, user_model=UserModel):
        self.user_model = user_model

    async def get_user(self, user_id) -> User or None:
        user_model = await self.user_model.get_or_none(id=user_id)
        if user_model:
            return User(
                _id=user_model.id,
                firstname=user_model.firstname,
                lastname=user_model.lastname,
                email=user_model.email,
                created_at=user_model.created_at,
                updated_at=user_model.updated_at
            )

        return None

    async def list_users(self):
        users = []
        users_list = await self.user_model.all()

        for user_model in users_list:
            users.append(User(
                _id=user_model.id,
                firstname=user_model.firstname,
                lastname=user_model.lastname,
                email=user_model.email
            ))

        return users

    async def create_user(self, user):
        user_model = await self.user_model.create(
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            created_at=datetime.now()
        )

        return User(
            _id=user_model.id,
            firstname=user_model.firstname,
            lastname=user_model.lastname,
            email=user_model.email,
            created_at=user_model.created_at
        )

    async def update_user(self, user):
        user_model = await self.user_model.get(id=user.id)
        user_model.firstname = user.firstname
        user_model.lastname = user.lastname
        user_model.email = user.email
        user_model.updated_at = datetime.now()
        await user_model.save()

    async def delete_user(self, user_id: str):
        user_model = await self.user_model.get_or_none(id=user_id)
        if user_model:
            await user_model.delete()
