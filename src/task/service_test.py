from . import service

class TestAddTask:
  def test_add_task(self):
    task = service.add_task('howard')

    assert task['name'] == 'howard'
    assert task['status'] == 0
    assert 'id' in task
    assert service.tasks_map[str(task['id'])] == task


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


class TestUpdateTask:
  def test_update_not_found_task(self):
    service.tasks_map = {}
    task = service.update_task('123', {'name': 'Noo', 'status': 0})

    assert task is None

  def test_update_task_name(self):
    service.tasks_map = {'1': {'name': 'Howard', 'status': 0, 'id': '1'}}
    task = service.update_task('1', {'name': 'Howard666'})

    assert task['name'] == 'Howard666'
    assert task['id'] == '1'
    assert task['status'] == 0

  def test_update_task_all(self):
    service.tasks_map = {'1': {'name': 'Howard', 'status': 0, 'id': '1'}}
    task = service.update_task('1', {'name': 'Howard666', 'status': 1})

    assert task['name'] == 'Howard666'
    assert task['status'] == 1
    assert task['id'] == '1'

  def test_update_task_empty(self):
    service.tasks_map = {'1': {'name': 'Howard', 'status': 0, 'id': '1'}}
    task = service.update_task('1', {})

    assert task['name'] == 'Howard'
    assert task['status'] == 0
    assert task['id'] == '1'