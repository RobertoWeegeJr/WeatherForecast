from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import database
import forecast
import model

app = Flask('CitiesForecast')
CORS(app)
api = Api(app)

class Countries(Resource):
    def get(self):
        try:
            code = request.args.get('code')
            name = request.args.get('name')
            return database.getCountries(code, name, True)
        except Exception as err:
            return {
                        'errorCode': 2,
                        'errorMessage': str(err)
                    }

class Cities(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            name = request.args.get('name')
            country = request.args.get('country')
            return database.getCities(id, name, country,  True)
        except Exception as err:
            return {
                        'errorCode': 2,
                        'errorMessage': str(err)
                    }

class CitiesForecast(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            return database.getCitiesForecast(id, True)
        except Exception as err:
            return {
                        'errorCode': 2,
                        'errorMessage': str(err)
                    }

    def post(self):
        try:
            id = request.args.get('id')
            return database.insertCityForecast(id)
        except Exception as err:
            return {
                        'errorCode': 2,
                        'errorMessage': str(err)
                    }

    def delete(self):
        try:
            id = request.args.get('id')
            return database.deleteCityForecast(id)
        except Exception as err:
            return {
                        'errorCode': 2,
                        'errorMessage': str(err)
                    }

class Forecast(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            cities = database.getCitiesForecast(id, True)
            if cities['errorCode'] != 0:
                raise Exception(cities['errorMessage'])
            if len(cities['result']) <= 0:
                raise AttributeError('The city ' + str(id) + ' is not in cities forecast list.')
            return forecast.getFiveDaysForecast(id)
        except Exception as err:
            return {
                        'errorCode': 2,
                        'errorMessage': str(err)
                    }
        
api.add_resource(Countries, '/countries')
api.add_resource(Cities, '/cities')
api.add_resource(CitiesForecast, '/cities_forecast')
api.add_resource(Forecast, '/forecast')

app.run()