import inspect

from typing import final
from abc import ABCMeta

from exceptions import UploaderDoesNotExist


class Register(ABCMeta):
    UPLOADERS: dict[str, 'Register'] = {}

    def __new__(cls, name, bases, attrs, **extra_kwargs):
        ins = super().__new__(cls, name, bases, attrs, **extra_kwargs)
        if inspect.isabstract(ins):
            return ins

        if "upload_name" not in attrs:
            raise ValueError

        return cls.register_handler(attrs['upload_name'])(ins)

    @classmethod
    @final
    def register_handler(cls, name: str):
        def inner(klass):
            cls.UPLOADERS[name] = klass
            return klass
        return inner

    @classmethod
    @final
    def handler(cls, name: str, *args, **kwargs):
        try:
            print(type(cls.UPLOADERS[name](*args, **kwargs)))
            return cls.UPLOADERS[name](*args, **kwargs)
        except KeyError:
            raise UploaderDoesNotExist(f"Uploader with name {name} doesn't exist!!!")
