thrift_converter
============

A python implemented tool for converting between json and thrift.


Install
------------

```bash
pip install thrift-converter
```


Why build this tool:
------------

1. Class in thrift gen-py use `thrift_spec()` to deserialize, but the `Enum` object is simply treated as `I32`, while in json, it's stored as string of name.   
2. `set` is not json serializable in standard json, we can treat `{'a', 'b', ..}` as `{None: ['a', 'b', ...]}` for distinction.


How to:
-----------
1. Parsing thrift ast by [ptsd](https://github.com/wickman/ptsd)
2. Deserializing thrift object by walking through ast recursively.


Todo:
-----------
- [ ] learn `ply` from [ptsd](https://github.com/wickman/ptsd)


Others
-----------

* [introspection-of-thrift-enums-in-python](https://grokbase.com/t/thrift/user/13614a6xd1/introspection-of-thrift-enums-in-python) discussed end with waiting for thrift upgrade(support for python enums)
* [thrift_json_decoder in twitter.common](https://github.com/twitter/commons/blob/master/src/python/twitter/thrift/text/thrift_json_decoder.py) can't handle with Enum
* [thrift_json_convertor based on thriftpy](https://github.com/xuanyuanking/thrift_json_convertor) too heavy


Usage
------------
example: [demo](https://github.com/shiyuan/thrift_converter/blob/master/test/)

```py
import json
from thrift_converter import JsonThriftConverter, ThriftJsonConverter

thrift_file = 'demo.thrift'
object_name = 'Group'

json2thrift = JsonThriftConverter(thrift_file).convert
thrift2json = ThriftJsonConverter(thrift_file).convert

obj = gen_fake_obj()
# Group(id=-1, worker_map={999: Worker(id=999, tasks=[Task(id=727, status=0, action=888, valid=True, msgs={'msg'})])})

js = thrift2json(obj, object_name)
js_str = json.dumps(js)
# {"id": -1, "worker_map": {"999": {"id": 999, "tasks": [{"id": 727, "status": 0, "action": "UP", "valid": true, "msgs": {"null": ["msg"]}}]}}}

obj = json2thrift(json.loads(js_str), object_name)
# Group(id=-1, worker_map={999: Worker(id=999, tasks=[Task(id=727, status=0, action=888, valid=True, msgs={'msg'})])})

```

