from flask import Flask, render_template, request, redirect, url_for
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

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/")
def users():
    users = user_repo.select_all()
    return render_template("index.jinja", all_users = users)

@users_blueprint.route("/new_user")
def new_user():
    return render_template("new_user.jinja")

@users_blueprint.route("/",  methods=['POST'])
def create_new_user():
    first_name     = request.form['first_name']
    last_name     = request.form['last_name']
    new_user = User(first_name, last_name)
    user_repo.save(new_user)
    return redirect(url_for('users.users'))

@users_blueprint.route("/users/<user_id>")
def display_user(user_id):
    user = user_repo.select(user_id)
    visited_cities_by_user = visited_city_repo.visited_cities_for_user(user_id)
    return render_template("users/index.jinja", user=user, visited_cities=visited_cities_by_user)

# @users_blueprint.route("/users/<user_id>/<visited_city_id>")
# def show_visited_city(user_id, visited_city_id):
#     user = user_repo.select(user_id)
#     visited_city = visited_city_repo.select(visited_city_id)
#     return render_template("users/show_travel.jinja", user=user, visited_this_city=visited_city)

@users_blueprint.route("/users/<user_id>/<visited_city_id>/delete", methods = ['POST'])
def delete_visited_city(user_id, visited_city_id):
    visited_city = visited_city_repo.select(visited_city_id)
    # city_id = visited_city.city.id
    city_repo.delete(visited_city.city.id)
    visited_city_repo.delete(visited_city_id)
    return redirect(url_for('users.display_user', user_id=user_id))

@users_blueprint.route("/users/<user_id>/add_new")
def add_new_visited_city(user_id):
    user = user_repo.select(user_id)
    countries = country_repo.select_all()
    # visited_cities_by_user = visited_city_repo.visited_cities_for_user(user_id)
    return render_template("users/add_new_visited_city.jinja",  user=user,countries=countries)

@users_blueprint.route("/users/<user_id>",  methods=['POST'])
def create_visited_city(user_id):
    user = user_repo.select(user_id)
    country     = request.form['country_id']
    city     = request.form['city']
    is_visited    = request.form['is_visited']
    notes   = request.form['notes']
    country_selected = country_repo.select(country)
    new_city = City(city, country_selected)
    city_repo.save(new_city)
    new_visited_city = Visited_city(user, new_city, is_visited, notes)
    visited_city_repo.save(new_visited_city)
    return redirect(url_for('users.display_user', user_id=user_id))

@users_blueprint.route("/users/<user_id>/<visited_city_id>/edit")
def edit_visited_city(user_id, visited_city_id):
    user = user_repo.select(user_id)
    visited_city = visited_city_repo.select(visited_city_id)
    # visited_cities_by_user = visited_city_repo.visited_cities_for_user(user_id)
    return render_template("users/edit_visited_city.jinja",  user=user, visited_this_city=visited_city)

@users_blueprint.route("/users/<user_id>/<visited_city_id>", methods=['POST'])
def update_visited_city(user_id, visited_city_id):
    user = user_repo.select(user_id)
    visited_city_for_updating = visited_city_repo.select(visited_city_id)
    country_id = visited_city_for_updating.city.country.id
    country_selected = country_repo.select(country_id)

    city_name_updated = request.form['city']
    is_visited_updated     = request.form['is_visited']
    notes_updated    = request.form['notes']

    city_id = visited_city_for_updating.city.id
    city_updated = City(city_name_updated, country_selected, city_id)
    city_repo.update(city_updated)

    visited_city_updated = Visited_city(user, city_updated, is_visited_updated, notes_updated, visited_city_id)
    visited_city_repo.update(visited_city_updated)
    return redirect(url_for('users.display_user', user_id=user_id))

@users_blueprint.route("/users/<user_id>/profile")
def profile(user_id):
    user = user_repo.select(user_id)
    return render_template("users/profile.jinja",  user=user)

@users_blueprint.route("/users/<user_id>/profile/edit")
def edit_profile(user_id):
    user = user_repo.select(user_id)
    return render_template("users/edit_profile.jinja",  user=user)

@users_blueprint.route("/users/<user_id>/profile", methods=['POST'])
def update_user(user_id):
    user = user_repo.select(user_id)

    first_name = request.form['first_name']
    last_name     = request.form['last_name']

    user_updated = User(first_name, last_name, user.id)
    user_repo.update(user_updated)

    return redirect(url_for('users.profile', user_id=user_id))

@users_blueprint.route("/users/<user_id>/profile/delete", methods=['POST'])
def delete_user(user_id):
    visited_cities_to_delete = visited_city_repo.visited_cities_for_user(user_id)
    for visited_city in visited_cities_to_delete:
        city_repo.delete(visited_city.city.id)
        visited_city_repo.delete(visited_city.id)
    user_repo.delete(user_id)
    return redirect(url_for('users.users'))

# @users_blueprint.route("/users/<user_id>/<visited_city_id>")
# def show_visited_city(user_id, visited_city_id):
#     user = user_repo.select(user_id)
#     visited_city = visited_city_repo.select(visited_city_id)
#     return render_template("users/show_travel.jinja", user=user, visited_this_city=visited_city)

# redirect(url_for('users.display_user', user_id=user_id))

# @users_blueprint.route("/users/<user_id>/<visited_city_id>/edit")
# def edit_visited_city(user_id, visited_city_id):
#     user = user_repo.select(user_id)
#     visited_city = visited_city_repo.select(visited_city_id)
#     continents = continent_repo.select_all()
#     countries = country_repo.select_all()
#     return render_template("users/edit_travel.jinja", user=user, visited_this_city=visited_city, countries=countries, continents=continents)

# @users_blueprint.route("/users/<user_id>/<visited_city_id>/edit")
# def edit_visited_city(user_id, visited_city_id):
#     user = user_repo.select(user_id)
#     visited_city = visited_city_repo.select(visited_city_id)
#     continents = continent_repo.select_all()
#     countries = country_repo.select_all()
#     return render_template("users/edit_travel.jinja", user=user, visited_this_city=visited_city, countries=countries, continents=continents)

# @users_blueprint.route("/users/<user_id>/<visited_city_id>/edit", methods=['GET', 'POST'])
# def edit_visited_city(user_id, visited_city_id):
#     user = user_repo.select(user_id)
#     visited_city = visited_city_repo.select(visited_city_id)
#     continents = continent_repo.select_all()
#     countries = country_repo.select_all()
#     if request.method == 'POST':
#         # Retrieve the selected value from the first dropdown menu
#         selected_continent = request.form.get('continent')

#         # Generate the options for the second dropdown menu based on the selected value
#         # In this example, we will just hardcode some options
#         countries_for_looping = country_repo.country_for_continent(selected_continent.id)

#         # Render the HTML template with the updated second dropdown menu options
#         return render_template("users/edit_travel.jinja", user=user, visited_this_city=visited_city, continents=continents,countries_for_looping=countries_for_looping)

#     # Render the initial HTML template with the first dropdown menu options
#     # dropdown1_options = ['option1', 'option2', 'option3']
#     return render_template("users/edit_travel.jinja", user=user, visited_this_city=visited_city, countries=countries, continents=continents)



