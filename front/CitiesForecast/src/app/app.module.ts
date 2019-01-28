import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatCardModule, MatAutocompleteModule, MatInputModule, MatTableModule, MatButtonModule, MatIconModule, MatDialogModule, MatSnackBarModule} from '@angular/material';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

import { HttpClientModule } from '@angular/common/http';
import { ForecastComponent } from './forecast/forecast.component';

@NgModule({
  declarations: [
    AppComponent,
    ForecastComponent
  ],
  imports: [
    MatCardModule,
    BrowserModule,
    MatAutocompleteModule,
    MatInputModule,
    MatTableModule,
    MatButtonModule, 
    MatDialogModule,
    MatIconModule,
    MatSnackBarModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule
  ],
  entryComponents: [
    ForecastComponent
  ],
  exports: [MatCardModule, MatAutocompleteModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
