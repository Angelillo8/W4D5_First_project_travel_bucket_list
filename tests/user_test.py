import unittest

from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_1 = User("Angel", "Gonzalez", 90)
        self.user_2 = User("Patricia", "Garcia", 3)


    def test_user_has_first_name(self):
        self.assertEqual("Angel", self.user_1.first_name)

    def test_user_has_last_name(self):
        self.assertEqual("Garcia", self.user_2.last_name)

    def test_user_has_id(self):
        self.assertEqual(3, self.user_2.id)