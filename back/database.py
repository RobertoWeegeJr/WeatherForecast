import model
import mysql.connector
import json

with open('database_connection.json') as fl:
    dataConnection = json.load(fl)

def getNewConnection():
    return mysql.connector.connect (**dataConnection)

def runSql(connection, statement):
    cursor = connection.cursor(buffered=True)
    cursor.execute(statement)
    return cursor

def finishConnection(connection):
    connection.close()

def finishCursor(cursor):
    cursor.close()

def getCountries(countryCode, countryName, returnJson):
    connection = None
    try:
        connection = getNewConnection()
        contries = _getContries(connection, countryCode, countryName, returnJson)
        return {
                    'errorCode': 0,
                    'result': contries
                }
    except Exception as err:
        return {
                    'errorCode': 1,
                    'errorMessage': str(err)
                }
    finally:
        if connection:
            finishConnection(connection)

def _getContries(connection, countryCode, countryName, returnJson):
    
    statement = "SELECT code, name FROM t_countries"
    where = ""
    
    if countryCode or countryName:
         
        if countryCode:
            if where:
                where += " AND" 
            else:
                where += " WHERE"
            where += " code = '" + countryCode + "'"
        
        if countryName:
            if where:
                where += " AND" 
            else:
                where += " WHERE"
            where += " name = '" + countryName + "'"

    statement += where + ";"
    cursor = runSql(connection, statement)
    
    countries = []
    for (code, name) in cursor:
        country = model.Country(code, name)
        if returnJson:
            countries.append(country.getJsonObject())
        else:
            countries.append(country)

    cursor = runSql(connection, statement)

    return countries

def getCities(cityId, cityName, cityCountry, returnJson):
    connection = None
    try:
        connection = getNewConnection()
        cities = _getCities(connection, cityId, cityName, cityCountry, returnJson)
        return {
                    'errorCode': 0,
                    'result': cities
                }
    except Exception as err:
        return {
                    'errorCode': 1,
                    'errorMessage': str(err)
                }
    finally:
        if connection:
            finishConnection(connection)
    
def _getCities(connection, cityId, cityName, cityCountry, returnJson):
    
    statement = "SELECT id, name, country FROM t_cities"
    where = ""
    
    if cityId or cityName or cityCountry:
         
        if cityId:
            if where:
                where += " AND" 
            else:
                where += " WHERE"
            where += " id = " + str(cityId) + ""
        
        if cityName:
            if where:
                where += " AND" 
            else:
                where += " WHERE"
            where += " name = '" + cityName + "'"
       
        if cityCountry:
            if where:
                where += " AND" 
            else:
                where += " WHERE"
            where += " country = '" + cityCountry + "'"

    statement += where + ";"

    cursor = runSql(connection, statement)
    
    cities = []
    countries = {}
    for (id, name, country) in cursor:
        
        if country not in countries:
            countries[country] = _getContries(connection, country, None, False)[0]
        
        city = model.City(id, name, countries[country])

        if returnJson:
            cities.append(city.getJsonObject())
        else:
            cities.append(city)

    finishCursor(cursor)

    return cities


def getCitiesForecast(cityId, returnJson):
    connection = None
    try:
        connection = getNewConnection()
        citiesForecast = _getCitiesForecast(connection, cityId, returnJson)
        return {
                    'errorCode': 0,
                    'result': citiesForecast
                }
    except Exception as err:
        return {
                    'errorCode': 1,
                    'errorMessage': str(err)
                }
    finally:
        if connection:
            finishConnection(connection)

def _getCitiesForecast(connection, cityId, returnJson):
    
    statement = "SELECT id FROM t_cities_to_forecast"
    where = ""
    
    if cityId:
         
        if cityId:
            if where:
                where += " AND" 
            else:
                where += " WHERE"
            where += " id = " + str(cityId) + ""
    
    statement += where + ";"

    cursor = runSql(connection, statement)
    citiesForecast = []
    for (id) in cursor:
        
        city = model.CityToForecast(_getCities(connection, id[0], None, None, False)[0])

        if returnJson:
            citiesForecast.append(city.getJsonObject())
        else:
            citiesForecast.append(city)

    finishCursor(cursor)

    return citiesForecast


def insertCityForecast(cityId):
    connection = None
    cursor = None
    try:
        statement = "INSERT INTO t_cities_to_forecast (id) VALUES (" + str(cityId) + ");"
        connection = getNewConnection()
        cursor = runSql(connection, statement)
        connection.commit()
        return {
                    'errorCode': 0,
                }
    except Exception as err:
        return {
                    'errorCode': 1,
                    'errorMessage': str(err)
                }
    finally:
        if cursor:
            finishCursor(cursor)
        if connection:
            finishConnection(connection)
    
def deleteCityForecast(cityId):
    connection = None
    cursor = None
    try:
        statement = "DELETE FROM t_cities_to_forecast WHERE id = " + str(cityId) + ";"
        connection = getNewConnection()
        cursor = runSql(connection, statement)
        connection.commit()
        return {
                    'errorCode': 0,
                }
    except Exception as err:
        return {
                    'errorCode': 1,
                    'errorMessage': str(err)
                }
    finally:
        if cursor:
            finishCursor(cursor)
        if connection:
            finishConnection(connection)