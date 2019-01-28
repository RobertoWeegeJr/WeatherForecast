
export class Country {

    private _code: string;
    private _name: string;

    constructor (code: string, name: string) {
        this.code = code
        this.name = name
    }

    public get code(): string {
        return this._code;
    }
    public set code(value: string) {
        this._code = value;
    }
    
    public get name(): string {
        return this._name;
    }
    public set name(value: string) {
        this._name = value;
    }

}

export class City {

    private _id: number;
    private _name: string;
    private _country: Country;

    constructor (id: number, name: string, country: Country) {
        this.id = id
        this.name = name
        this.country = country
    }

    public get id(): number {
        return this._id;
    }
    public set id(value: number) {
        this._id = value;
    }
    public get name(): string {
        return this._name;
    }
    public set name(value: string) {
        this._name = value;
    }
     
    public get country(): Country {
        return this._country;
    }
    public set country(value: Country) {
        this._country = value;
    }

    getTableView(): CityForecast{
        return {
            'id': this.id,
            'name': this.name,
            'country': this.country.name
        }
    }

}

export interface CityForecast {
    id: number;
    name: string;
    country: string;
  }

export interface ForecastData {
    cityId: number;
}

export interface Forecast {
    city: string;
    country: string;
    date: Date;
    description: string;
    temperature: number;
    pressure: number;
    humidity: number;
    cloudness: number;
    windSpeed: number;
    windDirection: number;
}