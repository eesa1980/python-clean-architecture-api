from typing import Optional

from .base_entity import BaseEntity


class User(BaseEntity):
    def __init__(self,  firstname: str, lastname: str, email: str, created_at: Optional[
        str] = None, _id: Optional[int] = None,
                 updated_at: Optional[str] = None):
        super().__init__(_id, created_at, updated_at)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at


