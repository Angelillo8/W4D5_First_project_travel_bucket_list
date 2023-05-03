import unittest

from models.visited_city import Visited_city


class TestVisited_city(unittest.TestCase):

    def setUp(self):
        self.visited_city_1 = Visited_city(23, 123, False, "Muy bueno", 12)


    def test_visited_city_has_user_id(self):
        self.assertEqual(23, self.visited_city_1.user)

    def test_visited_city_has_city_id(self):
        self.assertEqual(123, self.visited_city_1.city)

    def test_visited_city_is_visited(self):
        self.assertEqual(False, self.visited_city_1.is_visited)

    def test_visited_city_has_notes(self):
        self.assertEqual("Muy bueno", self.visited_city_1.notes)

    def test_visited_city_id(self):
        self.assertEqual(12, self.visited_city_1.id)