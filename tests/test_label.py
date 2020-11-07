import unittest

from models.label import *

class TestLabel(unittest.TestCase):
    def setUp(self):
        self.label_1 = Label(1, "Matador", "sales@matador.com")
        self.label_2 = Label(2, "4AD", "sales@4ad.com")

    def test_label_has_name(self):
        self.assertEqual("Matador", self.label_1.name)

    def test_label_on_email(self):
        self.assertEqual("sales@4ad.com", self.label_2.email)
