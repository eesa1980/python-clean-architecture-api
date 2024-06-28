from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def on_request(app: FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request, call_next):
        response = await call_next(request)
        response.headers["X-Process-Time"] = "0.1"
        return response

    @app.middleware("http")
    async def add_cors_header(request, call_next):
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    @app.middleware("http")
    async def health_check_middleware(request: Request, call_next):
        if request.url.path == "/health":
            return JSONResponse({"status": "ok"}, 200)
        return await call_next(request)

