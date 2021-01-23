from db.run_sql import run_sql

from models.album import Album
from models.label import Label

import repositories.album_bastard as album_repository

def save(label):
    sql = "INSERT INTO labels (name, email, active) VALUES (%s, %s, %s) RETURNING *"
    values = [label.name, label.email, label.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    label.id = id
    return label


def select_all():
    labels = []

    sql = "SELECT * FROM labels"
    results = run_sql(sql)

    for row in results:
        label = Label(row['name'], row['email'], row['active'], row['id'] )
        labels.append(label)
    return labels


def select(id):
    label = None
    sql = "SELECT * FROM labels WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        label = Label(result['name'], result['email'], result['active'], result['id'])
    return label


def update(label):
    sql = "UPDATE labels SET (name, email, active) = (%s, %s, %s) WHERE id = %s"
    values = [label.name, label.email, label.active, label.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE  FROM labels"
    run_sql(sql)


def delete(id):
    sql = 'DELETE  FROM labels WHERE id = %s'
    values= [id]
    run_sql(sql, values)

def artists(id):
    artists = []

    sql = 'SELECT artist FROM albums WHERE album.label.id = %s'
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        label = label_repository.select(row['label_id'])
        album = Album(row['title'], row['artist'], row['amount_units'], row['ideal_units'], row['cost'], row['sell_price'], row['genre'], label, row['id'])
        albums.append(album)
    return albums