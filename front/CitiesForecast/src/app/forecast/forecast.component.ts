import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA, MatSnackBar } from '@angular/material';
import { ForecastData, Forecast } from 'src/model/model';
import { DataService } from 'src/service/data-service.service';

@Component({
  selector: 'app-forecast',
  templateUrl: './forecast.component.html',
  styleUrls: ['./forecast.component.scss']
})
export class ForecastComponent implements OnInit {

    constructor(private dataService: DataService, private dialogRef: MatDialogRef<ForecastComponent>,
        @Inject(MAT_DIALOG_DATA) private data: ForecastData, private snackBar: MatSnackBar) { 
    }

    displayedColumns: string[] = ['city', 'country', 'date', 'description', 'temperature', 'pressure', 'humidity', 'cloudness', 'windSpeed', 'windDirection'];
    dataSource: Forecast[] = []
    
    ngOnInit() {
        this.loadForecast();
    }

    async loadForecast(){
        try {
            let result = await this.dataService.getForecast(this.data.cityId);
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


}
