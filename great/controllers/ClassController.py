from flask import session, render_template, redirect, request

from app import app
from great.models.Class import Class
from great.models.User import User
from great.models.Task import Task

@app.route("/classroom/classes/", methods=["POST"])
def create_class():
    try:
        name = request.form.get("name")
        description = request.form.get("description")
        createdAt = request.form.get("createdAt")
        creator = User().getUserById(session["_id"])

        classe = Class(name=name, description=description, creator=creator, createdAt=createdAt)

        classe.createClass(classe)

        return "OK", 200
    except:
        return "Error", 400


@app.route("/classroom/classes/<class_id>/", methods=["GET"])
def get_class(class_id):
    if "_id" in session:
        classe = Class().getClassById(class_id)
        tasks = Task().getAllTasksByClassId(class_id)

        if str(classe["creator"]["_id"]) == session["_id"]:
            return render_template("classes/classes.html", classe=classe, tasks=tasks)

    return "error", 400

@app.route("/classroom/classes/<class_id>/", methods=["PUT"])
def update_class(class_id):
    name = request.form.get("name")
    description = request.form.get("description")

    print(name)
    print(description)

    classe = Class(id=class_id, name=name, description=description)

    if classe.updateClass(classe):
        return "OK", 200
    else:
        return "Error", 400

@app.route("/classroom/classes/<class_id>/", methods=["DELETE"])
def delete_class(class_id):
    try:
        Class().deleteClassById(class_id)

        return "OK", 200
    except:
        return "Error", 400
