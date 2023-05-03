from db.run_sql import run_sql
from models.continent import Continent
from models.country import Country
from models.city import City

def save(continent):
    sql = "INSERT INTO continents(name) VALUES (%s) RETURNING id"
    values = [continent.name]
    results = run_sql(sql,values)
    continent.id = results[0]['id']
    return continent

def select_all():
    continents = []

    sql = "SELECT * FROM continents"
    results = run_sql(sql)
    for row in results:
        continent = Continent(row['name'], row['id'])
        continents.append(continent)
    return continents


def select(id):
    continent = None
    sql = "SELECT * FROM continents WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        continent = Continent(result['name'], result['id'] )
    return continent

def delete_all():
    sql = "DELETE FROM continents"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM continents WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(continent):
    sql = "UPDATE continents SET (name) = (%s) WHERE id = %s"
    values = [continent.name, continent.id]
    run_sql(sql, values)
