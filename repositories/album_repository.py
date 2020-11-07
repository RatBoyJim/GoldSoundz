from db.run_sql import run_sql

from models.album import Album
from models.label import Label

def save(album):
    sql = "INSERT INTO albums (title, artist, label, amount_units, ideal_units, cost, sell_price, genre, label_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [album.title, album.label, album.amount, album.amount_units, album.ideal_units, album.cost, album.sell_price, album.label.id]
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
        album = Album(row['title'], row['artist'], row['label'], row['amount_units'], row['ideal_units'], row['cost'], row['sell_price'], row['genre'], row['label_id'], row['id'] )
        albums.append(album)
    return albums

