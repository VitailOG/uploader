from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from exceptions import UploaderDoesNotExist


async def does_not_exist_uploader_error_handler(
        _: Request,
        exc: UploaderDoesNotExist
) -> JSONResponse:
    return JSONResponse({"errors": True, "message": str(exc)})


async def global_error_handler(
        _: Request,
        exc: Exception
) -> JSONResponse:
    return JSONResponse(
        {"errors": "Internal Server Error"},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR
    )
