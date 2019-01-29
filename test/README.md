```bash
$ sh test.sh

fake_obj: Group(id=-1, worker_map={999: Worker(id=999, tasks=[Task(id=727, status=0, action=888, valid=True, msgs={'msg'})])})

to_json: {"id": -1, "worker_map": {"999": {"id": 999, "tasks": [{"id": 727, "status": 0, "action": "UP", "valid": true, "msgs": {"null": ["msg"]}}]}}}

to_obj: Group(id=-1, worker_map={999: Worker(id=999, tasks=[Task(id=727, status=0, action=888, valid=True, msgs={'msg'})])})
```
