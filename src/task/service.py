from .model import *
from typing import Dict
import uuid

tasks_map: Dict[str, TaskSchema] = {}

def add_task(name: str) -> TaskSchema:
  task = TaskSchema().load({
    'id': uuid.uuid4(),
    'name': name,
    'status': 0,
  })
  tasks_map[task['id']] = task

  return task