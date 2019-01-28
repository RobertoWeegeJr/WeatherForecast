/*DROP DATABASE CitiesForecast;*/
CREATE DATABASE CitiesForecast;
USE CitiesForecast;

CREATE TABLE t_countries (
	code CHAR(2),
    name VARCHAR(250) NOT NULL,
    CONSTRAINT pk_countries PRIMARY KEY (code)
);

CREATE TABLE t_cities (
	id INTEGER,
    name VARCHAR(250) NOT NULL,
    country CHAR(2) NOT NULL,
    CONSTRAINT pk_cities PRIMARY KEY (id),
    CONSTRAINT fk_cities_country FOREIGN KEY (country) REFERENCES t_countries(code)
);

CREATE TABLE t_cities_to_forecast (
	id INTEGER,
    CONSTRAINT pk_cities_to_forecast PRIMARY KEY (id),
    CONSTRAINT fk_cities_to_forecast FOREIGN KEY (id) REFERENCES t_cities(id)
);