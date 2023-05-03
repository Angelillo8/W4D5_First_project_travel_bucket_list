from db.run_sql import run_sql
from models.continent import Continent
from models.country import Country
from models.city import City
import repositories.country_repository as country_repo

def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (%s, %s) RETURNING *"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repo.select(row['country_id'])
        city = City(row['name'], country, row['id'] )
        cities.append(city)
    return cities



def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = country_repo.select(result['country_id'])
        city = City(result['name'], country, result['id'] )
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country_id) = (%s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.id]
    run_sql(sql, values)