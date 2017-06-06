# json-objects
Python package for objects serialization

Install
-------

```
pip install json-objects
```

Usage
-----

```python
from json_objects import loads, dumps, Serializable


class Foo(Serializable):
    def __init__(self, bar):
        self.bar = bar
        self._bar = bar


foo = Foo('str')
print(dumps(foo))  # {"__type__": "Foo", "__module__": "__main__", "bar": "str"}

foo_ = loads(dumps(foo))
print(type(foo_).__name__, foo_.bar)  # Foo str
```

How it works
------------

* On serialization all public fields from __dict__ are serialized to json dictionary, \_\_type\_\_ and \_\_module\_\_ attributes are added
* On deserialization new object is created with type and module got from json object properties. Other fields are passed to \_\_dict\_\_ of new object
* Package is registered in kombu.serializers so it can be used as 'json_object' serializer in kombu
