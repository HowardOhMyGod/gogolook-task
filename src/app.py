from flask import Flask
from task import task_routes

app = Flask(__name__)
app.register_blueprint(task_routes)