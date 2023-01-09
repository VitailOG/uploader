from abc import abstractmethod

from register import Register


class BaseUploader(metaclass=Register):

    @abstractmethod
    def upload(self, content: bytes):
        pass

    @abstractmethod
    def get(self, key: str):
        pass
