import unittest

from models.label import *

class TestLabel(unittest.TestCase):
    def setUp(self):
        self.label_1 = Label("Matador", "sales@matador.com", True)
        self.label_2 = Label("4AD", "sales@4ad.com", False)

    def test_label_has_name(self):
        self.assertEqual("Matador", self.label_1.name)

    def test_label_on_email(self):
        self.assertEqual("sales@4ad.com", self.label_2.email)
