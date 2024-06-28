import json

from fastapi import FastAPI
import fastapi.exceptions as fastapi_exceptions
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

import src.application.common.exceptions as exceptions


def exception_handler(app: FastAPI):
    @app.exception_handler(exceptions.BadRequestException)
    async def bad_request_exception_handler(request, exc):
        return _bad_request_exception_response(exc)

    @app.exception_handler(exceptions.NotFoundException)
    async def not_found_exception_handler(request, exc):
        return _not_found_exception_response(exc)

    @app.exception_handler(exceptions.ValidationException)
    async def validation_exception_handler(request, exc):
        return validation_exception_response(exc)

    @app.exception_handler(fastapi_exceptions.RequestValidationError)
    async def fast_api_request_validation_exception_handler(request, exc):
        return request_validation_exception_response(exc)

    @app.exception_handler(fastapi_exceptions.ResponseValidationError)
    async def fast_api_response_validation_exception_handler(request, exc):
        return request_validation_exception_response(exc)

    @app.exception_handler(ValidationError)
    async def validation_exception_handler(request, exc):
        return validation_exception_response(exc)

    # Not Found exceptions not raised by the application for non-existent routes
    @app.exception_handler(404)
    async def not_found_exception_handler(request, exc):
        return _not_found_exception_response(exc)

    # All other exceptions are treated as internal server errors
    @app.exception_handler(Exception)
    async def internal_server_error_exception_handler(request, exc):
        return _internal_server_error_exception_response(exc)


class _ExceptionResponse:
    def __init__(self, message: str, error_name: str, status_code: int, title: str, type: str, meta: dict = None):
        self.message = message
        self.error_name = error_name
        self.status_code = status_code
        self.title = title
        if meta:
            self.meta = meta
        self.type = type


def _bad_request_exception_response(exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=_ExceptionResponse(
            message=exc.__str__(),
            error_name=exc.__class__.__name__,
            status_code=exc.status_code,
            title="Bad Request",
            type="https://tools.ietf.org/html/rfc7231#section-6.5.1",
        ).__dict__)


def _not_found_exception_response(exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=_ExceptionResponse(
            message=exc.__str__(),
            error_name=exc.__class__.__name__,
            status_code=exc.status_code,
            title="Not Found",
            type="https://tools.ietf.org/html/rfc7231#section-6.5.4",
        ).__dict__)


def _internal_server_error_exception_response(exc):
    return JSONResponse(
        status_code=500,
        content=_ExceptionResponse(
            message=exc.__str__(),
            error_name=exc.__class__.__name__,
            status_code=500,
            title="Internal Server Error",
            type="https://tools.ietf.org/html/rfc7231#section-6.6.1",
        ).__dict__)


def validation_exception_response(exc):
    return JSONResponse(
        status_code=422,
        content=_ExceptionResponse(
            message=exc.__str__(),
            error_name=exc.__class__.__name__,
            status_code=422,
            title="Validation Error",
            # meta=json.loads(exc.meta) if exc.meta else None,
            type="https://tools.ietf.org/html/rfc7231#section-6.5.1",
        ).__dict__)


def request_validation_exception_response(exc):
    return JSONResponse(
        status_code=422,
        content=_ExceptionResponse(
            message="Api Request Validation Error",
            error_name=exc.__class__.__name__,
            status_code=422,
            title="Validation Error",
            meta=exc.errors() if exc.errors() else None,
            type="https://tools.ietf.org/html/rfc7231#section-6.5.1",
        ).__dict__)


def response_validation_exception_response(exc):
    return JSONResponse(
        status_code=422,
        content=_ExceptionResponse(
            message="Api Response Validation Error",
            error_name=exc.__class__.__name__,
            status_code=422,
            title="Validation Error",
            meta=exc.errors() if exc.errors() else None,
            type="https://tools.ietf.org/html/rfc7231#section-6.5.1",
        ).__dict__)
