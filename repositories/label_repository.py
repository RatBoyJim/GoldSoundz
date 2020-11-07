from db.run_sql import run_sql

from models.album import Album
from models.label import Label

import repositories.album_repository as album_repository

def save(label):
    sql = "INSERT INTO labels (name, email) VALUES (%s, %s) RETURNING *"
    values = [label.name, label.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    label.id = id
    return label


def select_all():
    labels = []

    sql = "SELECT * FROM labels"
    results = run_sql(sql)

    for row in results:
        label = Label(row['name'], row['email'], row['id'] )
        labels.append(label)
    return labels


def select(id):
    label = None
    sql = "SELECT * FROM labels WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        label = Label(result['name'], result['email'], result['id'])
    return label


def update(label):
    sql = "UPDATE labels SET (name, email) = (%s, %s) WHERE id = %s"
    values = [label.first_name, label.email, label.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE  FROM labels"
    run_sql(sql)


def delete(id):
    sql = 'DELETE  FROM tasks WHERE id = %s'
    values= [id]
    run-sql(sql, values)