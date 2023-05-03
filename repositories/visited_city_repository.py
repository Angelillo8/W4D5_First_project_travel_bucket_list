from db.run_sql import run_sql
from models.user import User
from models.continent import Continent
from models.country import Country
from models.city import City
from models.visited_city import Visited_city
import repositories.city_repository as city_repo
import repositories.user_repository as user_repo

def save(visited_city):
    sql = "INSERT INTO visited_cities (user_id, city_id, is_visited, notes) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [visited_city.user.id, visited_city.city.id, visited_city.is_visited, visited_city.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    visited_city.id = id
    return visited_city


def select_all():
    visited_cities = []

    sql = "SELECT * FROM visited_cities"
    results = run_sql(sql)

    for row in results:
        user = user_repo.select(row['user_id'])
        city = city_repo.select(row['city_id'])
        visited_city = Visited_city(user, city, row['is_visited'], row['notes'], row['id'])
        visited_cities.append(visited_city)
    return visited_cities



def select(id):
    visited_city = None
    sql = "SELECT * FROM visited_cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = user_repo.select(result['user_id'])
        city = city_repo.select(result['city_id'])
        visited_city = Visited_city(user, city, result['is_visited'], result['notes'], result['id'])
    return visited_city


def delete_all():
    sql = "DELETE FROM visited_cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM visited_cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(visited_city):
    sql = "UPDATE visited_cities SET (user_id, city_id, is_visited, notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [visited_city.user.id, visited_city.city.id, visited_city.is_visited, visited_city.notes, visited_city.id]
    run_sql(sql, values)

def visited_cities_for_user(user_id):
    visited_cities = []
    sql = "SELECT * FROM visited_cities WHERE user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)
    for row in results:
        user = user_repo.select(row['user_id'])
        city = city_repo.select(row['city_id'])
        visited_city = Visited_city(user, city, row['is_visited'], row['notes'], row['id'])
        visited_cities.append(visited_city)
    return visited_cities
