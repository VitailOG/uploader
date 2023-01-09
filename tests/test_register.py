import pytest

from abc import abstractmethod

from exceptions import UploaderDoesNotExist
from register import Register


@pytest.fixture
def base_class():
    class Base(metaclass=Register):
        @abstractmethod
        def __call__(self, *args, **kwargs):
            pass

    return lambda: Base


def test_without_upload_name(base_class):
    Base = base_class()
    with pytest.raises(ValueError):
        class A(Base):
            def __call__(self, *args, **kwargs):
                pass


def test_handler(base_class):
    Base = base_class()

    class A(Base):
        upload_name = "a"

        def __call__(self, *args, **kwargs):
            pass

    assert isinstance(Base.handler("a"), A)


def test_handler_error(base_class):
    Base = base_class()

    class A(Base):
        upload_name = "a"

        def __call__(self, *args, **kwargs):
            pass

    with pytest.raises(UploaderDoesNotExist):
        assert isinstance(Base.handler("b"), A)


def test_ok(base_class):

    Base = base_class()

    class A(Base):
        upload_name = "a"

        def __call__(self, *args, **kwargs):
            pass

    class B(Base):
        upload_name = "b"

        def __call__(self, *args, **kwargs):
            pass

    assert len(Base.UPLOADERS) == 2
