import pdb
from models.album import Album
from models.label import Label

import repositories.album_repository as album_repository
import repositories.label_repository as label_repository

album_repository.delete_all()
label_repository.delete_all()

label1 = Label("Matador", "sales@matador.com")
label_repository.save(label1)
label2 = Label("4AD", "sales@4ad.com")
label_repository.save(label2)

label_repository.select_all()

album_1 = Album("Crooked Rain Crooked Rain", "Pavement", 4, 2, 5.00, 10.00, "Alternative", label1)
album_repository.save(album_1)

album_2 = Album("Doolittle", "Pixies", 3, 3, 4.00, 10.00, "Alternative", label2)
album_repository.save(album_2)

album_3 = Album("Surfer Rosa", "Pixies", 6, 4, 3.00, 5.00, "Alternative", label2)
album_repository.save(album_3)

pdb.set_trace()

