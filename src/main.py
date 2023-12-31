from flask import Flask
from task import task_routes

app = Flask(__name__)
app.register_blueprint(task_routes)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)