from flask import Blueprint, jsonify, abort, current_app
from http import HTTPStatus
from webargs import fields
from webargs.flaskparser import use_kwargs

from . import service

task_routes = Blueprint('task', __name__)


@task_routes.route('/tasks')
def get_tasks():
  try:
    tasks = service.get_tasks()
    return jsonify({'result': tasks}), HTTPStatus.OK
  except Exception as e:
    current_app.logger.error('get task list error: ', e)
    abort(HTTPStatus.BAD_REQUEST)


@task_routes.route('/task', methods=['POST'])
@use_kwargs({ 'name': fields.Str(required=True) })
def add_task(name: str):
  try:
    task = service.add_task(name)
    return jsonify({'result': task}), HTTPStatus.CREATED
  except Exception as e:
    current_app.logger.error('create task error: ', e)
    abort(HTTPStatus.BAD_REQUEST)
