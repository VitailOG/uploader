import inspect

from typing import final
from abc import ABCMeta

from exceptions import UploaderDoesNotExist


class Register(ABCMeta):
    UPLOADERS: dict[str, "Register"] = {}

    def __new__(cls, name, bases, attrs, **extra_kwargs):
        ins = super().__new__(cls, name, bases, attrs, **extra_kwargs)

        if inspect.isabstract(ins):
            return ins

        if "upload_name" not in attrs:
            raise AttributeError(f"{name} must be have attribute `upload_name`")

        if not isinstance(attrs["upload_name"], str):
            raise TypeError("Attribute upload_name must be str")

        return cls.register_handler(attrs["upload_name"])(ins)

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
            return cls.UPLOADERS[name](*args, **kwargs)
        except KeyError:
            raise UploaderDoesNotExist(f"Uploader with name {name} doesn't exist!!!")
