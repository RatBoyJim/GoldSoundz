from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
from models.label import Label
import repositories.album_repository as album_repository
import repositories.label_repository as label_repository

albums_blueprint = Blueprint("albums", __name__)



#CREATE

@albums_blueprint.route("/albums/new", methods=["GET"])
def new_album():
    labels = label_repository.select_all()
    return render_template("albums/new.html", labels = labels)


@albums_blueprint.route("/albums", methods=["POST"])
def create_album():
    title = request.form["title"]
    artist = request.form["artist"]
    amount_units = request.form["amount_units"]
    ideal_units = request.form["ideal_units"]
    cost = request.form["cost"]
    sell_price = request.form["sell_price"]
    genre = request.form["genre"]
    label_id = request.form["label_id"]

    label = label_repository.select(label_id)#makes a label OBJECT
    new_album = Album(title, artist, amount_units, ideal_units, cost, sell_price, genre, label)
    album_repository.save(new_album)
    return redirect('/albums')

#REVIEW

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums = albums)

@albums_blueprint.route("/albums/<id>")
def show(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album = album)

#UPDATE

@albums_blueprint.route("/albums/<id>/edit", methods = ["GET"])
def edit_album(id):
    album = album_repository.select(id)
    labels = label_repository.select_all()
    return render_template("albums/edit.html", album = album, labels = labels)


@albums_blueprint.route("/albums/<id>", methods = ["POST"])
def update_album(id):
    title = request.form["title"]
    artist = request.form["artist"]
    amount_units = request.form["amount_units"]
    ideal_units = request.form["ideal_units"]
    cost = request.form["cost"]
    sell_price = request.form["sell_price"]
    genre = request.form["genre"]
    label_id = request.form["label_id"]

    label = label_repository.select(label_id)
    new_album = Album(title, artist, amount_units, ideal_units, cost, sell_price, genre, label, id)
    album_repository.update(new_album)
    return redirect('/albums')


#DELETE

@albums_blueprint.route("/albums/<id>/delete", methods=["GET"])
def delete_album(id):
    album_repository.delete(id)
    return redirect('/albums')