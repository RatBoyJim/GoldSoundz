from flask import Flask, render_template

import controllers

from controllers.album_controller import albums_blueprint
from controllers.label_controller import labels_blueprint

from models.album import Album
from models.label import Label
import repositories.album_repository as album_repository
import repositories.label_repository as label_repository


app = Flask(__name__)

app.register_blueprint(albums_blueprint)
app.register_blueprint(labels_blueprint)


@app.route('/')
def home():
    albums = album_repository.select_all()
    return render_template('index.html', albums = albums)

if __name__ == '__main__':
    app.run(debug=True)