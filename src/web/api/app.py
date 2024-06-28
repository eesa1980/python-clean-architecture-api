from fastapi import FastAPI
from tortoise import Tortoise

from src.web.api.controllers import users_controller
from src.web.api.crosscutting.containers import ApplicationContainer
import src.web.api.middlewares as middlewares


def create_app() -> FastAPI:
    app = FastAPI()
    container = ApplicationContainer()

    middlewares.on_request(app)
    middlewares.db_handler(app, db_url=container.env.get("database_url"))

    # Wire dependencies
    container.wire(modules=[users_controller])

    # Register routes
    app.include_router(users_controller.router, prefix="/api/v1/users")

    middlewares.on_response(app)

    @app.on_event("shutdown")
    async def shutdown_event():
        print("Shutting down...")
        await Tortoise.close_connections()

    return app
