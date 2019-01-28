from abc import ABCMeta, abstractmethod

class GenericModel(metaclass=ABCMeta):

     @abstractmethod
     def getJsonObject(self):
          pass

class Country(GenericModel):

    def __init__(self, code: str, name: str):
        self._code = code
        self._name = name
    
    @property
    def code(self) -> str:
         return self._code

    @code.setter
    def code(self, value: str):
         self._code = value

    @property
    def name(self):
         return self._name

    @name.setter
    def name(self, value: str):
         self._name = value

    def getJsonObject(self) -> any:
        return {
            "code": self.code,
            "name": self.name
        }
    
class City(GenericModel):

    def __init__(self, id, name, country):
        self._id = id
        self._name = name
        self._country = country
    
    @property
    def id(self):
         return self._id

    @id.setter
    def id(self, value):
         self._id = value

    @property
    def name(self):
         return self._name

    @name.setter
    def name(self, value):
         self._name = value

    @property
    def country(self):
         return self._country

    @country.setter
    def country(self, value):
         self._country = value

    def getJsonObject(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country.getJsonObject() if self.country else None
        }
    
class CityToForecast(GenericModel):

     def __init__(self, city):
          self._city = city
    
     @property
     def city(self):
          return self._city

     @city.setter
     def city(self, value):
          self._city = value

     def getJsonObject(self):
          return {
               "city": self.city.getJsonObject() if self.city else None
          }

class Forecast(GenericModel):
     def __init__(self, city, forecastList):
          self._city = city
          self._forecastList = forecastList
          
     @property
     def city(self):
          return self._city

     @city.setter
     def city(self, value):
          self._city = value

     @property
     def forecastList(self):
          return self._forecastList

     @forecastList.setter
     def forecastList(self, value):
          self._forecastList = value

     def getJsonObject(self):
          forecastJsonList = []

          for line in self.forecastList:
               forecastJsonList.append(line.getJsonObject())

          return {
               "city": self.city.getJsonObject() if self.city else None,
               "forecastList": forecastJsonList
          }

class ForecastListLine(GenericModel):
     
     def __init__(self, dateUTC, main, weather, clouds, wind, rain, snow, calculationDateUTC):
          self._dateUTC = dateUTC
          self._main = main
          self._weather = weather
          self._clouds = clouds
          self._wind = wind
          self._rain = rain
          self._snow = snow
          self._calculationDateUTC = calculationDateUTC
    
     @property
     def dateUTC(self):
          return self._dateUTC

     @dateUTC.setter
     def dateUTC(self, value):
          self._dateUTC = value

     @property
     def main(self):
          return self._main

     @main.setter
     def main(self, value):
          self._main = value

     @property
     def weather(self):
          return self._weather

     @weather.setter
     def weather(self, value):
          self._weather = value

     @property
     def clouds(self):
          return self._clouds

     @clouds.setter
     def clouds(self, value):
          self._clouds = value

     @property
     def wind(self):
          return self._wind

     @wind.setter
     def wind(self, value):
          self._wind = value
 
     @property
     def rain(self):
          return self._rain

     @rain.setter
     def rain(self, value):
          self._rain = value
     
     @property
     def snow(self):
          return self._snow

     @snow.setter
     def snow(self, value):
          self._snow = value

     @property
     def calculationDateUTC(self):
          return self._calculationDateUTC

     @calculationDateUTC.setter
     def calculationDateUTC(self, value):
          self._calculationDateUTC = value

     def getJsonObject(self):
          weatherJsonList = []

          for line in self.weather:
               weatherJsonList.append(line.getJsonObject())
          
          return {
               "dateUTC": self.dateUTC,
               "main": self.main.getJsonObject() if self.main else None,
               "weather": weatherJsonList,
               "clouds": self.clouds.getJsonObject() if self.clouds else None,
               "wind": self.wind.getJsonObject() if self.wind else None,
               "rain": self.rain.getJsonObject() if self.rain else None,
               "snow": self.snow.getJsonObject() if self.snow else None,
               "calculationDateUTC": self.calculationDateUTC
          }

class ForecastListMain(GenericModel):
     def __init__(self, temperature, temperatureMin, temperatureMax, pressure, pressureSeaLevel, pressureGroundLevel, humidity):
          self._temperature = temperature
          self._temperatureMin = temperatureMin
          self._temperatureMax = temperatureMax
          self._pressure = pressure
          self._pressureSeaLevel = pressureSeaLevel
          self._pressureGroundLevel = pressureGroundLevel
          self._humidity = humidity 
    
     @property
     def temperature(self):
          return self._temperature

     @temperature.setter
     def temperature(self, value):
          self._temperature = value

     @property
     def temperatureMin(self):
          return self._temperatureMin

     @temperatureMin.setter
     def temperatureMin(self, value):
          self._temperatureMin = value
     
     @property
     def temperatureMax(self):
          return self._temperatureMax

     @temperatureMax.setter
     def temperatureMax(self, value):
          self._temperatureMax = value

     @property
     def pressure(self):
          return self._pressure

     @pressure.setter
     def pressure(self, value):
          self._pressure = value

     @property
     def pressureSeaLevel(self):
          return self._pressureSeaLevel

     @pressureSeaLevel.setter
     def pressureSeaLevel(self, value):
          self._pressureSeaLevel = value

     @property
     def pressureGroundLevel(self):
          return self._pressureGroundLevel

     @pressureGroundLevel.setter
     def pressureGroundLevel(self, value):
          self._pressureGroundLevel = value

     @property
     def humidity(self):
          return self._humidity

     @humidity.setter
     def humidity(self, value):
          self._humidity = value

     def getJsonObject(self):
          return {
               "temperature": self.temperature,
               "temperatureMin": self.temperatureMin,
               "temperatureMax": self.temperatureMax,
               "pressure": self.pressure,
               "pressureSeaLevel": self.pressureSeaLevel,
               "pressureGroundLevel": self.pressureGroundLevel,
               "humidity": self.humidity
          }
     
class ForecastListWeather(GenericModel):
     
     def __init__(self, main, description, icon):
        self._main = main
        self._description = description
        self._icon = icon
    
     @property
     def main(self):
          return self._main

     @main.setter
     def main(self, value):
          self._main = value
    
     @property
     def description(self):
          return self._description

     @description.setter
     def description(self, value):
          self._description = value
    
     @property
     def icon(self):
          return self._icon

     @icon.setter
     def icon(self, value):
          self._icon = value

     def getJsonObject(self):
          return {
               "main": self.main,
               "description": self.description,
               "icon": self.icon
          }

class ForecastListClouds(GenericModel):
     
     def __init__(self, cloudness):
          self._cloudness = cloudness
    
     @property
     def cloudness(self):
          return self._cloudness

     @cloudness.setter
     def cloudness(self, value):
          self._cloudness = value

     def getJsonObject(self):
          return {
               "cloudness": self.cloudness
          }

class ForecastListWind(GenericModel):
     
     def __init__(self, speed, direction):
          self._speed = speed
          self._direction = direction

     @property
     def speed(self):
          return self._speed

     @speed.setter
     def speed(self, value):
          self._speed = value

     @property
     def direction(self):
          return self._direction

     @direction.setter
     def direction(self, value):
          self._direction = value

     def getJsonObject(self):
          return {
               "speed": self.speed,
               "direction": self.direction
          }
  
class ForecastListRain(GenericModel):
     
     def __init__(self, threeHoursVolume):
          self._threeHoursVolume = threeHoursVolume
    
     @property
     def threeHoursVolume(self):
          return self._threeHoursVolume

     @threeHoursVolume.setter
     def threeHoursVolume(self, value):
          self._threeHoursVolume = value

     def getJsonObject(self):
          return {
               "threeHoursVolume": self.threeHoursVolume
          }       
     
class ForecastListSnow(GenericModel):
     def __init__(self, threeHoursVolume):
          self._threeHoursVolume = threeHoursVolume
    
     @property
     def threeHoursVolume(self):
          return self._threeHoursVolume

     @threeHoursVolume.setter
     def threeHoursVolume(self, value):
          self._threeHoursVolume = value

     def getJsonObject(self):
          return {
               "threeHoursVolume": self.threeHoursVolume
          }