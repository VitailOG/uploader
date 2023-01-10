import boto3

from config import settings
from .base import BaseUploader


class S3Uploader(BaseUploader):
    AWS_BUCKET = "test.vit.zak"  # name your bucket
    upload_name = "s3"

    def __init__(self):
        self.s3 = boto3.resource(
            's3',
            aws_access_key_id=settings.ACCESS_ID,
            aws_secret_access_key=settings.ACCESS_KEY
        )
        self.bucket = self.s3.Bucket(self.AWS_BUCKET)

    def upload(self, content: bytes, key: str) -> None:
        self.bucket.put_object(Key=key, Body=content)

    def get(self, key: str):
        return self.s3.Object(bucket_name=self.AWS_BUCKET, key=key).get()['Body'].read()
