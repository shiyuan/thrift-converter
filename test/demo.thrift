namespace cpp space.demo
namespace java space.demo
namespace py space.demo

enum Enum {
  DOWN = 666
  UP = 888
}

typedef i64 Id

struct Task {
  1: required Id id,
  2: required i32 status,
  3: required Enum action,
  4: required bool valid,
  5: required set<string> msgs,
}

struct Worker {
  1: required Id id,
  2: required list<Task> tasks
}

struct Group {
  1: optional i64 id = -1,
  2: required map<Id, Worker> worker_map,
}

