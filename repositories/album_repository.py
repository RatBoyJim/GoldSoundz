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

def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        label = label_repository.select(row['label_id'])
        album = Album(row['title'], row['artist'], row['amount_units'], row['ideal_units'], row['cost'], row['sell_price'], row['genre'], row['label_id'], row['id'] )
        albums.append(album)
    return albums

