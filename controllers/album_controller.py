from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums = albums)

@albums_blueprint.route("/albums/<id>")
def show(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album = album)