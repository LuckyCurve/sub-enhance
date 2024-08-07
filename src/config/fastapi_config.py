import fastapi
from fastapi.requests import Request
from fastapi.responses import Response
from starlette.middleware.cors import CORSMiddleware

import src.utils.constant


def init(app: fastapi.FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=src.utils.constant.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next) -> Response:
        uri = request.url.path
        auth = request.query_params.get("auth")

        if uri not in src.utils.constant.white_list_uri and auth != src.utils.constant.auth_str:
            return Response(content="auth failed!")
        response = await call_next(request)
        return response
