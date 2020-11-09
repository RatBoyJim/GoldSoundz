from db.run_sql import run_sql

from models.album import Album
from models.label import Label

import repositories.label_repository as label_repository

def save(album):
    sql = "INSERT INTO albums (title, artist, amount_units, ideal_units, cost, sell_price, genre, label_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [album.title, album.artist, album.amount_units, album.ideal_units, album.cost, album.sell_price, album.genre, album.label.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        label = label_repository.select(row['label_id'])
        album = Album(row['title'], row['artist'], row['amount_units'], row['ideal_units'], row['cost'], row['sell_price'], row['genre'], label, row['id'])
        albums.append(album)
    return albums


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        label = label_repository.select(result['label_id'])
        album = Album(result['title'], result['artist'], result['amount_units'], result['ideal_units'], result['cost'], result['sell_price'], result['genre'], label, result['id'])
    return album

def update(album):
    sql = "UPDATE albums SET (title, artist, amount_units, ideal_units, cost, sell_price, genre, label_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist, album.amount_units, album.ideal_units, album.cost, album.sell_price, album.genre, album.label.id, album.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)

def delete(id):
    sql = 'DELETE  FROM albums WHERE id = %s'
    values = [id]
    run_sql(sql, values)


def albums(artist):
    albums = []

    sql = 'SELECT * FROM albums WHERE artist = %s'
    values = [artist]
    results = run_sql(sql)

    for row in results:
        label = label_repository.select(row['label_id'])
        album = Album(row['title'], row['artist'], row['amount_units'], row['ideal_units'], row['cost'], row['sell_price'], row['genre'], label, row['id'])
        albums.append(album)
    return albums

