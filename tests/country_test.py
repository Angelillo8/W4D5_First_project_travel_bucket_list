import unittest

from models.country import Country


class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country_1 = Country("Solomon Islands", "Oceania")
        self.country_2 = Country("Venezuela", "South America", 3)


    def test_country_has_name(self):
        self.assertEqual("Solomon Islands", self.country_1.name)

    def test_country_has_continent(self):
        self.assertEqual("Oceania", self.country_1.continent)

    def test_country_has_id(self):
        self.assertEqual(3, self.country_2.id)