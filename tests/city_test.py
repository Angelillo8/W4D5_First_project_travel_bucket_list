import unittest

from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city_1 = City("London", "UK")
        self.city_2 = City("Madrid", "Spain", 23)


    def test_city_has_name(self):
        self.assertEqual("London", self.city_1.name)

    def test_city_has_country(self):
        self.assertEqual("Spain", self.city_2.country)

    def test_city_has_id(self):
        self.assertEqual(23, self.city_2.id)
