import sys
sys.path.append('gen-py')
sys.path.append('../')

import json
from thrift_converter import JsonThriftConverter, ThriftJsonConverter

thrift_file = 'demo.thrift'
json2thrift = JsonThriftConverter(thrift_file).convert
thrift2json = ThriftJsonConverter(thrift_file).convert


def fake_obj():
    from space.demo.ttypes import Enum, Task, Worker, Group
    task = Task(id=727, msgs={"msg"}, status=0, action=Enum.UP, valid=True)
    worker = Worker(id=999, tasks=[task])
    group = Group(worker_map={worker.id : worker})
    return group

def test():
    obj = fake_obj()
    print('fake_obj:', obj)

    js = thrift2json(obj, 'Group')
    js_str = json.dumps(js)
    print('to_json:', js_str)

    obj = json2thrift(json.loads(js_str), 'Group')
    print('to_obj:', obj)

if __name__ == '__main__':
    test()
