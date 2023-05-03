import unittest

from models.continent import Continent


class TestContinent(unittest.TestCase):

    def setUp(self):
        self.continent_1 = Continent("Oceania")
        self.continent_2 = Continent("South America", 3)


    def test_continent_has_name(self):
        self.assertEqual("Oceania", self.continent_1.name)

    def test_continent_has_country(self):
        self.assertEqual(3, self.continent_2.id)
