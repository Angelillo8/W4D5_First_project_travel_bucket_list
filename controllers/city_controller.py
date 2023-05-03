from flask import Flask, render_template, request, redirect
from flask import Blueprint
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

cities_blueprint = Blueprint("cities", __name__)