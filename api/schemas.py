from pydantic import BaseModel


class FileSchema(BaseModel):
    uploader: str
    key: str
