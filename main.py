from fastapi import FastAPI

from api import router
from errors import does_not_exist_uploader_error_handler, global_error_handler
from exceptions import UploaderDoesNotExist


def get_application() -> FastAPI:
    application = FastAPI()

    # register error router
    application.include_router(router)

    # register error handlers
    application.add_exception_handler(UploaderDoesNotExist, does_not_exist_uploader_error_handler)
    application.add_exception_handler(Exception, global_error_handler)
    return application


app = get_application()
