from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import Response

from services import BaseUploader
from .schemas import FileSchema

router = APIRouter(tags=['s3'])


@router.put('/')
def upload(file: UploadFile, uploader: str = Form(...)):
    content = file.file.read()
    BaseUploader.handler(uploader).upload(content)
    return {"uploaded": True}


@router.post('/')
def get(data_upload: FileSchema):
    file = BaseUploader.handler(data_upload.uploader).get(data_upload.key)
    return Response(
        content=file,
        headers={
            "Content-Disposition": "attachment;filename=test.pdf",
            "Content-Type": "application/octet-stream"
        }
    )
