import unittest
import database

class DatabaseTests(unittest.TestCase):
    
    #Country
    def test_country_getAll(self):
        countries = database.getCountries(None, None, True)
        self.assertEqual(countries['errorCode'], 0)
        self.assertEqual(len(countries['result']), 250)
    
    def test_country_getByCode(self):
        countries = database.getCountries('BR', None, True)
        self.assertEqual(countries['errorCode'], 0)
        self.assertEqual(len(countries['result']), 1)
        self.assertEqual(countries['result'][0]['code'], "BR")
        self.assertEqual(countries['result'][0]['name'], "Brazil")
    
    def test_country_getByName(self):
        countries = database.getCountries(None, 'Brazil', True)
        self.assertEqual(countries['errorCode'], 0)
        self.assertEqual(len(countries['result']), 1)
        self.assertEqual(countries['result'][0]['code'], "BR")
        self.assertEqual(countries['result'][0]['name'], "Brazil")

    def test_country_getByCodeName(self):
        countries = database.getCountries('BR', 'Brazil', True)
        self.assertEqual(countries['errorCode'], 0)
        self.assertEqual(len(countries['result']), 1)
        self.assertEqual(countries['result'][0]['code'], "BR")
        self.assertEqual(countries['result'][0]['name'], "Brazil")        
    
    def test_country_getByCodeName_nothing(self):
        countries = database.getCountries('BR', 'Brasil', True)
        self.assertEqual(countries['errorCode'], 0)
        self.assertEqual(len(countries['result']), 0)

    #City
    def test_city_getAll(self):
        cities = database.getCities(None, None, None, True)
        self.assertEqual(cities['errorCode'], 0)
        self.assertEqual(len(cities['result']), 209571)
    
    def test_city_getById(self):
        cities = database.getCities(3465330, None, None, True)
        self.assertEqual(cities['errorCode'], 0)
        self.assertEqual(cities['result'][0]['id'], 3465330)
        self.assertEqual(len(cities['result']), 1)
        self.assertEqual(cities['result'][0]['name'], "Corupa")
        self.assertEqual(cities['result'][0]['country']['code'], "BR")
        self.assertEqual(cities['result'][0]['country']['name'], "Brazil")
    
    def test_city_getByName(self):
        cities = database.getCities(None, 'Corupa', None, True)
        self.assertEqual(cities['errorCode'], 0)
        self.assertEqual(cities['result'][0]['id'], 3465330)
        self.assertEqual(len(cities['result']), 1)
        self.assertEqual(cities['result'][0]['name'], "Corupa")
        self.assertEqual(cities['result'][0]['country']['code'], "BR")
        self.assertEqual(cities['result'][0]['country']['name'], "Brazil")

    def test_city_getByCountry(self):
        cities = database.getCities(None, None, 'BR', True)
        self.assertEqual(cities['errorCode'], 0)
        self.assertEqual(len(cities['result']), 3621)

    def test_city_getByIdNameCountry(self):
        cities = database.getCities(3465330, 'Corupa', 'BR', True)
        self.assertEqual(cities['errorCode'], 0)
        self.assertEqual(len(cities['result']), 1)
        self.assertEqual(cities['result'][0]['id'], 3465330)
        self.assertEqual(cities['result'][0]['name'], "Corupa")
        self.assertEqual(cities['result'][0]['country']['code'], "BR")
        self.assertEqual(cities['result'][0]['country']['name'], "Brazil")

    def test_city_getByIdNameCountry_nothing(self):
        cities = database.getCities(3465330, 'Corup', 'BR', True)
        self.assertEqual(cities['errorCode'], 0)
        self.assertEqual(len(cities['result']), 0)

    #city to forecast
    def test_cityForecast_CRDCity(self):
        #delete
        cities = database.deleteCityForecast(3465330)
        self.assertEqual(cities['errorCode'], 0)
        #select
        cities2 = database.getCitiesForecast(3465330, True)
        self.assertEqual(cities2['errorCode'], 0)
        self.assertEqual(len(cities2['result']), 0)
        #insert
        cities3 = database.insertCityForecast(3465330)
        self.assertEqual(cities3['errorCode'], 0)
        #select
        cities4 = database.getCitiesForecast(3465330, True)
        self.assertEqual(cities4['errorCode'], 0)
        self.assertEqual(len(cities4['result']), 1)
        self.assertEqual(cities4['result'][0]['city']['id'], 3465330)
        self.assertEqual(cities4['result'][0]['city']['name'], "Corupa")
        self.assertEqual(cities4['result'][0]['city']['country']['code'], "BR")
        self.assertEqual(cities4['result'][0]['city']['country']['name'], "Brazil")
        
    
    def test_cityForecast_getByAll(self):
        #delete
        cities = database.deleteCityForecast(3465330)
        self.assertEqual(cities['errorCode'], 0)
        #insert
        cities2 = database.insertCityForecast(3465330)
        self.assertEqual(cities2['errorCode'], 0)
        #select
        cities = database.getCitiesForecast(None, True)
        self.assertGreaterEqual(len(cities['result']), 1)