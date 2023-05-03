import requests
from bs4 import BeautifulSoup
import random
from models.user import User
from models.continent import Continent
from models.country import Country
from models.city import City
from models.visited_city import Visited_city

import repositories.user_repository as user_repo
import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo
import repositories.visited_city_repository as visited_city_repo

north_america_url = "https://en.wikipedia.org/wiki/List_of_North_American_countries_by_population"
south_america_url = "https://en.wikipedia.org/wiki/List_of_South_American_countries_by_population"
africa_url = "https://en.wikipedia.org/wiki/List_of_African_countries_by_GDP_(nominal)"
asia_url = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP"
europe_url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_in_Europe_by_GDP_(nominal)"
oceanin_url = "https://en.wikipedia.org/wiki/List_of_Oceanian_countries_by_GDP_(nominal)"


def web_scrapper(url):
    html = requests.get(url)
    html_soup = BeautifulSoup(html.content,"html.parser")
    # print(html_soup.prettify())
    countries = []

    for a in html_soup.find_all("a"):
        if a.parent.name == 'td':
            countries.append(a)›

    countries_l = [i.get_text() for i in countries]

    return countries_l

north_america = web_scrapper(north_america_url)
south_america = web_scrapper(south_america_url)
africa = web_scrapper(africa_url)
asia = web_scrapper(asia_url)
oceania = web_scrapper(oceanin_url)
europe = web_scrapper(europe_url)


asia1 = Continent("Asia")
continent_repo.save(asia1)
africa1 = Continent("Africa")
continent_repo.save(africa1)
south_america1 = Continent("South America")
continent_repo.save(south_america1)
north_americat1 = Continent("North America")
continent_repo.save(north_americat1)
europe1 = Continent("Europe")
continent_repo.save(europe1)
oceania1 = Continent("Oceania")
continent_repo.save(oceania1)

def country_saver(lista, continente):
    for country in lista:
        countries = Country(country, continente)
        country_repo.save(countries)

country_saver(north_america, north_americat1)
country_saver(asia, asia1)
country_saver(africa, africa1)
country_saver(south_america, south_america1)
country_saver(europe, europe1)
country_saver(oceania, oceania1)

# country1 = Country("Venezuela", continent4)
# country_repo.save(country1)
# country2 = Country("China", continent1)
# country_repo.save(country2)
# country3 = Country("Nigeria", continent2)
# country_repo.save(country3)
# country4 = Country("Australia", continent7)
# country_repo.save(country4)
# country5 = Country("Yugoslavia", continent6)
# country_repo.save(country5)
