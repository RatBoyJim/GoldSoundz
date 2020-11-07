import unittest

from models.album import *

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album_1 = Album("Crooked Rain Crooked Rain", "Pavement", 4, 2, 5.00, 10.00, "Alternative", 1)
        self.album_2 = Album("Surfer Rosa", "Pixies", 6, 4, 3.00, 5.00, "Alternative", 1)

    def test_album_has_title(self):
        self.assertEqual("Crooked Rain Crooked Rain", self.album_1.title)

    def test_album_has_artist(self):
        self.assertEqual("Pixies", self.album_2.artist)

    def test_album_has_genre(self):
        self.assertEqual("Alternative", self.album_1.genre)

    def test_album_has_ideal_units(self):
        self.assertEqual(4, self.album_2.ideal_units)

    def test_album_has_cost(self):
        self.assertEqual(5.00, self.album_1.cost)