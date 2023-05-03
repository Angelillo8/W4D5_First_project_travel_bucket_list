from flask import Flask, render_template

from controllers.visited_city_controller import visited_cities_blueprint
from controllers.user_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(visited_cities_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)