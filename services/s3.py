import boto3

from .base import BaseUploader


class S3Uploader(BaseUploader):
    AWS_BUCKET = "My-Bucket"
    upload_name = "s3"

    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(self.AWS_BUCKET)

    def upload(self, content):
        self.bucket.put_object(Key="dsf.pdf", Body=content)

    def get(self, key: str):
        return self.s3.Object(bucket_name=self.AWS_BUCKET, key=key)
