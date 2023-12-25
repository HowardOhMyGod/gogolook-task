from .model import *
from typing import Dict, List
import uuid

tasks_map: Dict[str, TaskSchema] = {}

def add_task(name: str) -> TaskSchema:
  task = TaskSchema().load({
    'id': uuid.uuid4(),
    'name': name,
    'status': 0,
  })
  tasks_map[str(task['id'])] = task

  return task

def get_tasks() -> List[TaskSchema]:
  return list(tasks_map.values())

def update_task(task_id: str, updates: dict) -> TaskSchema:
  if task_id not in tasks_map:
    return None

  tasks_map[task_id] |= updates
  return tasks_map[task_id]

def delete_task(task_id: str) -> None:
  return tasks_map.pop(task_id, None)