from . import service

class TestAddTask:
  def test_add_task(self):
    task = service.add_task('howard')

    assert task['name'] == 'howard'
    assert task['status'] == 0
    assert 'id' in task
    assert service.tasks_map[task['id']] == task


class TestGetTasks:
  def test_get_tasks_empty(self):
    service.tasks_map = {}
    tasks = service.get_tasks()

    assert len(tasks) == 0

  def test_get_tasks_one(self):
    task = {'name': 'Howard', 'status': 0, 'id': '1'}
    service.tasks_map = {'1': task}
    tasks = service.get_tasks()

    assert len(tasks) == 1
    assert tasks[0] == task

  def test_get_tasks_many(self):
    task1 = {'name': 'Howard', 'status': 0, 'id': '1'}
    task2 = {'name': 'Eat', 'status': 0, 'id': '2'}
    service.tasks_map = {'1': task1, '2': task2}
    tasks = service.get_tasks()

    assert len(tasks) == 2
