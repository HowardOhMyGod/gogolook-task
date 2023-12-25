from . import service

class TestAddTask:
  def test_add_task(self):
    task = service.add_task('howard')
    assert task['name'] == 'howard'
    assert task['status'] == 0
    assert 'id' in task
    assert service.tasks_map[task['id']] == task