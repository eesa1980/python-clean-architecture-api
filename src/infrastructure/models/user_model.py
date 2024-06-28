from tortoise import fields
from tortoise.models import Model


class UserModel(Model):
    id = fields.IntField(pk=True)
    firstname = fields.CharField(max_length=50)
    lastname = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=False, null=True)

    class Meta:
        table = "users"
