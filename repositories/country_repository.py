from db.run_sql import run_sql
from models.continent import Continent
from models.country import Country
from models.city import City
import repositories.continent_repository as continent_repo

def save(country):
    sql = "INSERT INTO countries (name, continent_id) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries ORDER BY countries.name DESC"
    results = run_sql(sql)

    for row in results:
        continent = continent_repo.select(row['continent_id'])
        country = Country(row['name'], continent, row['id'] )
        countries.append(country)
    return countries



def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        continent = continent_repo.select(result['continent_id'])
        country = Country(result['name'], continent, result['id'] )
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, continent_id) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent.id, country.id]
    run_sql(sql, values)

def country_for_continent(continent_id):
    countries = []
    sql = "SELECT * FROM countries WHERE continent_id = %s"
    values = [continent_id]
    results = run_sql(sql, values)
    for row in results:
        continent = continent_repo.select(row['continent_id'])
        country = Country(row['name'], continent, row['id'] )
        countries.append(country)
    return countries