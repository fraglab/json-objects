import pytest

from json_objects import *


def test_basic_types():
    assert dumps(0) == '0'
    assert dumps(None) == 'null'


def test_empty_containers():
    assert dumps([]) == '[]'
    assert dumps({}) == '{}'


def test_datetime():
    d = datetime.now()

    assert loads(dumps(d)) == d


def test_dict():
    d = {
        '1': 1,
        '2': None,
        '3': 'str',
        '4': []
    }
    assert loads(dumps(d)) == d


def test_list():
    l = [1, 'str', None, []]
    assert loads(dumps(l)) == l


def test_unserializable():
    class A:
        pass
    with pytest.raises(UnserializableException):
        dumps(A())


def serializable_class(**kwargs):
    class A(Serializable):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
    return A(**kwargs)


def test_class_serialization():
    a = serializable_class(a=1)
    assert loads(dumps(a)).a == 1


def test_class_encode_decode():
    a = serializable_class(a=1)
    assert a.__class__.decode(a.encode())


def test_transitive():
    a = serializable_class(a=1)

    assert loads(dumps(loads(dumps(a)))).a == a.a


def test_nested():
    d = datetime.now()
    a = serializable_class(c=serializable_class(a=1, d=d))

    assert loads(dumps(a)).c.a == a.c.a
    assert loads(dumps(a)).c.d == a.c.d
