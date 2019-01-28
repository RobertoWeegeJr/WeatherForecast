import requests
import model
import database

fiveDaysForecastURL = "http://api.openweathermap.org/data/2.5/forecast"
fiveDaysForecastParams = "?units=metric&APPID=eb8b1a9405e659b2ffc78f0a520b1a46"

def getFiveDaysForecast(cityId):
    
    try:
            
        response = requests.get(fiveDaysForecastURL + fiveDaysForecastParams + "&id=" + str(cityId))

        jsonResponse = response.json()
        
        if (response.status_code != 200):
            raise Exception('Invalid status code from openweathermap.')

        country = database.getCountries(jsonResponse['city']['country'], None, False)['result'][0]
        city = model.City(jsonResponse['city']['id'], jsonResponse['city']['name'], country)
        forecastLines = []
        
        for line in jsonResponse['list']:

            if 'main' in line:
                forecastListMain = model.ForecastListMain(
                    line['main']['temp'] if 'temp' in line['main'] else None, 
                    line['main']['temp_min'] if 'temp_min' in line['main'] else None, 
                    line['main']['temp_max'] if 'temp_max' in line['main'] else None, 
                    line['main']['pressure'] if 'pressure' in line['main'] else None, 
                    line['main']['sea_level'] if 'sea_level' in line['main'] else None, 
                    line['main']['grnd_level'] if 'grnd_level' in line['main'] else None, 
                    line['main']['humidity'] if 'humidity' in line['main'] else None
                    )
            else:
                forecastListMain = None

            if 'weather' in line:
                forecastListWeather = []
                for weatherLine in line['weather']:
                    forecastListWeather.append(model.ForecastListWeather(
                        weatherLine['main'] if 'main' in weatherLine else None, 
                        weatherLine['description'] if 'description' in weatherLine else None, 
                        weatherLine['icon']) if 'icon' in weatherLine else None
                        )
            else:
                forecastListWeather = None

            if 'clouds' in line:
                forecastListClouds = model.ForecastListClouds(
                    line['clouds']['all'] if 'all' in line['clouds'] else None
                    )
            else:
                forecastListClouds = None

            if 'wind' in line:
                forecastListWind = model.ForecastListWind(
                    line['wind']['speed'] if 'speed' in line['wind'] else None, 
                    line['wind']['deg'] if 'deg' in line['wind'] else None
                    )
            else:
                forecastListWind = None
            
            if 'rain' in line:
                forecastListRain = model.ForecastListRain(
                    line['rain']['3h'] if '3h' in line['rain'] else None
                    )
            else:
                forecastListRain = None
                    
            if 'snow' in line:
                forecastListSnow = model.ForecastListSnow(
                    line['snow']['3h'] if '3h' in line['snow'] else None
                    )
            else:
                forecastListSnow = None

            forecastListLine = model.ForecastListLine(line['dt'] if 'dt' in line else None, forecastListMain, forecastListWeather, 
                forecastListClouds, forecastListWind, forecastListRain, forecastListSnow, line['dt_txt'] if 'dt_txt' in line else None)

            forecastLines.append(forecastListLine)

        forecast = model.Forecast(city, forecastLines)

        return { 'errorCode': 0, 'result': forecast.getJsonObject()}

    except Exception as err:
        return {
            'errorCode': 3,
            'errorMessage': str(err)
        }