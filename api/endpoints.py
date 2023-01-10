from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import Response

from services import BaseUploader
from .schemas import FileSchema

router = APIRouter(tags=['s3'])


@router.put('/')
def upload(file: UploadFile, uploader: str = Form(...)):
    filename = file.filename
    content = file.file.read()
    BaseUploader.handler(uploader).upload(content, filename)
    return {"uploaded": True, "key": filename}


@router.post('/')
def get(data_upload: FileSchema):
    file = BaseUploader.handler(data_upload.uploader).get(data_upload.key)
    return Response(
        content=file,
        headers={
            "Content-Disposition": f"attachment;filename={data_upload.key}",
            "Content-Type": "application/octet-stream"
        }
    )
