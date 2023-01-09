from .base import BaseUploader


class FileUploader(BaseUploader):
    upload_name = "file"

    def upload(self, content):
        f = open('test.pdf', 'wb')
        f.write(content)

    def get(self, key: str):
        with open(key, 'rb') as f:
            return f.read()
