from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.label import Label
import repositories.label_repository as label_repository
import repositories.album_repo as album_repository

labels_blueprint = Blueprint("labels", __name__)



#CREATE

@labels_blueprint.route("/labels/new", methods=["GET"])
def new_label():
    return render_template("labels/new.html")



@labels_blueprint.route("/labels", methods=["POST"])
def create_label():
    name = request.form["name"]
    email = request.form["email"]
    active = request.form["active"]

    new_label = Label(name, email, active)
    label_repository.save(new_label)
    return redirect('/labels')





#REVIEW

@labels_blueprint.route("/labels")
def labels():
    albums = album_repository.select_all()
    labels = label_repository.select_all()
    return render_template("labels/index.html", labels = labels, albums = albums)

@labels_blueprint.route("/labels/<id>/show")
def show(id):
    label = label_repository.select(id)
    return render_template("labels/show.html", label = label)




#UPDATE

@labels_blueprint.route("/labels/<id>/edit", methods = ["GET"])
def edit_label(id):
    label = label_repository.select(id)
    return render_template("labels/edit.html", label = label)

@labels_blueprint.route("/labels/<id>", methods = ["POST"])
def update_label(id):
    name = request.form["name"]
    email = request.form["email"]
    active = request.form["active"]

    label_update = Label(name, email, active, id)
    label_repository.update(label_update)
    return redirect('/labels')


#DELETE

@labels_blueprint.route("/labels/<id>/delete", methods=["GET"])
def delete_label(id):
    label_repository.delete(id)
    return redirect('/labels')


#OTHER STUFF

@labels_blueprint.route("/labels/<id>")
def label_artists(id):
    album = album_repository.select_all()
    label = label_repository.select(id)
    return render_template('labels/label-artists', albums = albums, label = label)