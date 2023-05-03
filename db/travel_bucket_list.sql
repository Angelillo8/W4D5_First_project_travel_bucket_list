DROP TABLE IF EXISTS visited_cities;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE continents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent_id INT NOT NULL REFERENCES continents(id) ON DELETE CASCADE
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE visited_cities (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    is_visited BOOLEAN NOT NULL,
    notes TEXT
);