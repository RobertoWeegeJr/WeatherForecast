import { Component } from '@angular/core';
import { FormControl, Validators, ValidatorFn } from '@angular/forms';
import { Observable } from 'rxjs';
import { Country, City, CityForecast } from 'src/model/model';
import {map, startWith} from 'rxjs/operators';

import {  MatDialog, MatSnackBar } from '@angular/material';
import { DataService } from 'src/service/data-service.service';
import { ForecastComponent } from './forecast/forecast.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

    constructor(private dataService: DataService, private dialog: MatDialog, private snackBar: MatSnackBar) {}

    title = 'CitiesForecast';

    countriesControl = new FormControl('', [Validators.required, this.contriesValidation().bind(this)]);
    citiesControl = new FormControl('', [Validators.required, this.citiesValidation().bind(this)]);

    countries: Country[] = []
    cities: City[] = []
  
    filteredCountries: Observable<Country[]>;
    filteredCities: Observable<City[]>;

    displayedColumns: string[] = ['id', 'name', 'country', 'forecast', 'delete'];
    dataSource: CityForecast[] = [];

    ngOnInit() {
        this.loadAllCountries();
        this.loadCitiesToForecast();
        this.filteredCities = this.citiesControl.valueChanges
        .pipe(
            startWith<string | City>(''),
            map(value => typeof value === 'string' ? value : (value ? value.name : null)),
            map(name => name ? this._filterCities(name) : this.cities.slice())
        );

    }

    displayCountriesFn(country?: Country): string | undefined {
        return country ? country.name : undefined;
    }

    displayCitiesFn(city?: City): string | undefined {
        return city ? city.name : undefined;
    }

    _filterCountries(name: string): Country[] {
        const filterValue = name.toLowerCase();
        return this.countries.filter(option => option.name.toLowerCase().indexOf(filterValue) === 0);
    }

    _filterCities(name: string): City[] {
        const filterValue = name.toLowerCase();
        return this.cities.filter(option => option.name.toLowerCase().indexOf(filterValue) === 0);
    }

    contriesValidation() {
        
        return (control: FormControl) => {
            try {
                if (!control.value || !control.value.code || this.countries.findIndex((value) => {return value.code == control.value.code}) < 0) {
                    return {
                        "country": true
                    };
                }
                this.manageCitiesList(control.value.code);
                return null;
            } catch (e) {
                return {
                    "validation_error": true
                };
            }
        } 
    }    

    citiesValidation() {
        
        return (control: FormControl) => {
            try {
                if (!control.value || !control.value.id || this.cities.findIndex((value) => {return value.id == control.value.id}) < 0) {
                    return {
                        "city": true
                    };
                }
                if (!this.countriesControl.value || !this.countriesControl.value.code || this.cities.findIndex((value) => {return value.country.code == this.countriesControl.value.code}) < 0 ) {
                    return {
                        "country_city": true
                    };
                }
                this.manageCitiesList(control.value.code);
                return null;
            } catch (e) {
                return {
                    "validation_error": true
                };
            }
        } 
    }    

    async manageCitiesList(countryCode: string) {
        if (countryCode) {

            try {
                let result = await this.dataService.getCountryCities(countryCode);
                if (result['errorCode'] != 0) {
                    throw new Error(result['errorMessage'])
                }
                this.cities = result['result']
            } catch (e) {
                this.snackBar.open(e.message ? e.message : 'Unknown Error', null, {
                    duration: 3000,
                });
            }
        } 
        
        this.filteredCities = this.citiesControl.valueChanges
        .pipe(
            startWith<string | City>(''),
            map(value => typeof value === 'string' ? value : (value ? value.name : null)),
            map(name => name ? this._filterCities(name) : this.cities.slice())
        );
    }

    countryChange() {
        this.citiesControl.setValue(null)
    }

    async loadAllCountries(){
        try {
            let result = await this.dataService.getAllCountries();
            if (result['errorCode'] != 0) {
                throw new Error(result['errorMessage'])
            }
            this.countries = result['result']
        } catch (e) {
            this.snackBar.open(e.message ? e.message : 'Unknown Error', null, {
                duration: 3000,
            });
        }
        this.filteredCountries = this.countriesControl.valueChanges
        .pipe(
            startWith<string | Country>(''),
            map(value => typeof value === 'string' ? value : (value ? value.name : null)),
            map(name => name ? this._filterCountries(name) : this.countries.slice())
        );
    }

    async loadCitiesToForecast() {
        try {
            let result = await this.dataService.getCitiesToForecast();
            if (result['errorCode'] != 0) {
                throw new Error(result['errorMessage'])
            }
            this.dataSource = result['result']
        } catch (e) {
            this.snackBar.open(e.message ? e.message : 'Unknown Error', null, {
                duration: 3000,
            });
        }
        
    }

    async addForecast(city: City) {
        if (city) {
            try {
                let result = await this.dataService.addCityToForecast(city.id);
                if (result['errorCode'] != 0) {
                    throw new Error(result['errorMessage'])
                }
            } catch (e) {
                this.snackBar.open(e.message ? e.message : 'Unknown Error', null, {
                    duration: 3000,
                });
            }
            this.loadCitiesToForecast();
        }
    }

    async removeForecast(cityId: number) {
        if (cityId) {
            try {
                let result = await this.dataService.deleteCityToForecast(cityId);
                if (result['errorCode'] != 0) {
                    throw new Error(result['errorMessage'])
                }
            } catch (e) {
                this.snackBar.open(e.message ? e.message : 'Unknown Error', null, {
                    duration: 3000,
                });
            }
            
            this.loadCitiesToForecast();
        }
    }

    openForecast(cityId: number) {
        this.dialog.open(ForecastComponent, {
            data: {cityId: cityId}
        });
    }

    getCountriesErrorMessage() {
        return this.countriesControl.hasError('required') ? 'You must enter a value' :
                this.countriesControl.hasError('country') ? 'Country not found' :
                '';
    }   
      
    getCitiesErrorMessage() {
        return this.citiesControl.hasError('required') ? 'You must enter a value' :
                this.citiesControl.hasError('city') ? 'City not found' :
                this.citiesControl.hasError('country_city') ? 'City not in country' :
                '';
    }   
}