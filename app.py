from flask import Flask, render_template

from app import controllers
from app import models
from app import repositories

from app.controllers.album_controller import albums_blueprint
from app.controllers.label_controller import labels_blueprint

from app.models.album import Album
from app.models.label import Label
import app.repositories.album_repository as album_repository
import app.repositories.label_repository as label_repository


app = Flask(__name__)

app.register_blueprint(albums_blueprint)
app.register_blueprint(labels_blueprint)


@app.route('/')
def home():
    albums = album_repository.select_all()
    return render_template('index.html', albums = albums)

if __name__ == '__main__':
    app.run(debug=True)