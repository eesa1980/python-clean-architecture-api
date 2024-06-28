from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.infrastructure.models import user_model


def db_handler(app: FastAPI, db_url: str):
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": [user_model]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

