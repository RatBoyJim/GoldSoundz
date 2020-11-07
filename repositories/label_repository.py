from models.album import Album
from models.label import Label

def save(label):
    sql = "INSERT INTO labels (name, email) VALUES (%s, %s) RETURNING *"
    values = [label.name, label.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    label.id = id
    return label

def delete_all():
    sql = "DELETE  FROM labels"
    run_sql(sql)

def select_all():
    labels = []

    sql = "SELECT * FROM labels"
    results = run_sql(sql)

    for row in results:
        label = Label(row['name'], row['email'], row['id'] )
        labels.append(label)
    return labels