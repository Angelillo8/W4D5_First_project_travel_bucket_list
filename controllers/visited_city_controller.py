from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.continent import Continent
from models.country import Country
from models.city import City
from models.visited_city import Visited_city
import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo
import repositories.visited_city_repository as visited_city_repo

visited_cities_blueprint = Blueprint("visited_cities", __name__)
