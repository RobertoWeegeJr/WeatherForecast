import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Country, City, CityForecast, Forecast } from 'src/model/model';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DataService {

    constructor(private http: HttpClient) { }

    async getAllCountries() {
        try {
            let response = await this.http.get(environment.host + '/countries').toPromise()
            
            if (response['errorCode'] != 0) {
                return response
            }

            let countries: Country[] = []
            for (let line in response['result']) {
                countries.push(new Country(response['result'][line].code, response['result'][line].name))
            }

            countries.sort((a, b) => {
                if(a.name < b.name) { return -1; }
                if(a.name > b.name) { return 1; }
                return 0;
            })

            return {errorCode: 0, result: countries};
        } catch (e) {
            return {errorCode: 4, errorMessage: e.message};
        }
    }

    async getCountryCities(countryCode: string) {
        try {
            let response = await this.http.get(environment.host + '/cities?country=' + countryCode).toPromise()
            
            if (response['errorCode'] != 0) {
                return response
            }
            
            let result = response['result']

            let cities: City[] = []
            for (let line in result) {
                cities.push(new City(result[line].id, result[line].name, new Country(result[line].country.code, result[line].country.name)))
            }

            cities.sort((a, b) => {
                if(a.name < b.name) { return -1; }
                if(a.name > b.name) { return 1; }
                return 0;
            })

            return {errorCode: 0, result: cities};
        
        } catch (e) {
            return {errorCode: 4, errorMessage: e.message};
        }
    }

    async addCityToForecast(cityId: number) {
        try {
            let response = await this.http.post(environment.host + '/cities_forecast?id=' + cityId, null).toPromise()
            
            if (response['errorCode'] != 0) {
                return response
            }
            
            return {errorCode: 0};

        } catch (e) {
            return {errorCode: 4, errorMessage: e.message};
        }
    }

    async deleteCityToForecast(cityId: number) {
        try {
            let response = await this.http.delete(environment.host + '/cities_forecast?id=' + cityId).toPromise()
            
            if (response['errorCode'] != 0) {
                return response
            }
            
            return {errorCode: 0};
        
        } catch (e) {
            return {errorCode: 4, errorMessage: e.message};
        }
    }

    async getCitiesToForecast() {
        try {
            let response = await this.http.get(environment.host + '/cities_forecast').toPromise()

            if (response['errorCode'] != 0) {
                return response
            }
            
            let result = response['result']
            let cities: CityForecast[] = []
            for (let line in result) {
                cities.push({'id': result[line].city.id, 'name': result[line].city.name, 'country': result[line].city.country.name})
            }

            cities.sort((a, b) => {
                if(a.name < b.name) { return -1; }
                if(a.name > b.name) { return 1; }
                return 0;
            })
            
            return {errorCode: 0, result: cities};

        } catch (e) {
            return {errorCode: 4, errorMessage: e.message};
        }
    }
    
    async getForecast(cityId: number) {
        try {
            let response = await this.http.get(environment.host + '/forecast?id=' + cityId).toPromise()
            
            if (response['errorCode'] != 0) {
                return response
            }
            
            let result = response['result']

            let forecasts: Forecast[] = []

            let city = (result['city'] ? result['city'].name : null)
            let country = (result['city'] && result['city'].country ? result['city'].country.name : null)
            
            for (let line in result['forecastList']) {
                let forecastLine = result['forecastList'][line];
                
                let date = new Date(0);
                date.setUTCSeconds(forecastLine.dateUTC);

                let temperature = (forecastLine.main ? forecastLine.main.temperature : null);
                let pressure = (forecastLine.main ? forecastLine.main.pressure : null);
                let humidity = (forecastLine.main ? forecastLine.main.humidity : null);

                let cloudness = (forecastLine.clouds ? forecastLine.clouds.cloudness : null); 
                let windSpeed = (forecastLine.wind ? forecastLine.wind.speed : null);
                let windDirection = (forecastLine.wind ? forecastLine.wind.direction : null);

                for (let weatherLine in forecastLine.weather) {
                    let description = (forecastLine.weather[weatherLine] ? forecastLine.weather[weatherLine].description : null);
                    forecasts.push(
                        {
                            city: city,
                            country: country,
                            date: date,
                            temperature: temperature,
                            pressure: pressure,
                            humidity: humidity,
                            cloudness: cloudness,
                            windSpeed: windSpeed,
                            windDirection: windDirection,
                            description: description
                        })
                }
            }
            return {errorCode: 0, result: forecasts};
        } catch (e) {
            return {errorCode: 4, errorMessage: e.message};
        }
    }
}