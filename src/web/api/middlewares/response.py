from fastapi import FastAPI

from src.web.api.middlewares.exception_handler import exception_handler


def on_response(app: FastAPI):
    exception_handler(app)


