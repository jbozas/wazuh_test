from .models import User, Task
from flask import jsonify, request, Flask
from app import app

# docker build --file=backend/Dockerfile  -t wazuh-backend .


@app.route('/tasks', methods=["GET"])
def tasks():
    """
    Retrieve a list of tasks
    @filters:
        -title: task title.
        -completed: task boolean completed.
    """
    qs = Task.query.filter_by(**request.args.to_dict()).all()
    if len(qs) == 0:
        return jsonify({"error": "Tasks not found"}), 422
    return jsonify(total_items=len(qs), data=[i.serialize for i in qs])


@app.route('/tasks/<int:id>', methods=['GET'])
def task(id):
    """
    Returns an individual task.
    @params:
        -id: primary key
    """
    model = Task
    result = model.query.get(id)
    if not result:
        return jsonify({"error": "Task ID not found"}), 422
    return jsonify(result.serialize)


@app.route('/users', methods=['GET'])
def users():
    """
    Returns all users.
    """
    model = User
    queryset = model.query.all()
    return jsonify(total_items=len(queryset), data=[i.serialize for i in queryset])


@app.route('/users/<int:id>', methods=['GET'])
def user(id):
    """
    Returns an individual User.
    @params:
        -id: primary key
    """
    model = User
    result = model.query.get(id)
    if not result:
        return jsonify({"error": "User ID not found"}), 422
    return jsonify(result.serialize)


@app.route('/users/<int:id>/tasks', methods=['GET'])
def users_tasks(id):
    """
    Returns the users Tasks.
    @params:
        -id: user primary key
    @filters:
        -title: task title.
        -completed: task boolean completed.
    """
    model = User
    result = model.query.get(id)
    if not result:
        return jsonify({"error": "User ID not found"}), 422
    tasks = result.retrieve_tasks(filters=request.args)
    return jsonify(total_items=len(tasks), data=[i.serialize for i in tasks])
