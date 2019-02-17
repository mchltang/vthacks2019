import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { TypeaheadModule } from 'ngx-bootstrap/typeahead';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { InputParametersService } from './input-parameters.service';

import { AppComponent } from './app.component';
import { MenuBarComponent } from './menu-bar/menu-bar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatCardModule, MatToolbarModule, MatDividerModule, MatSlideToggleModule, MatSliderModule, MatInputModule, MatButtonModule, MatSelectModule} from '@angular/material';
import { MatAutocompleteModule} from '@angular/material/autocomplete';
import { SearchResultsComponent } from './search-results/search-results.component';




@NgModule({
  declarations: [
    AppComponent,
    MenuBarComponent,
    SearchResultsComponent
  ],
  imports: [
    MatCardModule,
    MatToolbarModule,
    BrowserModule,
    MatDividerModule,
    MatInputModule,
    MatButtonModule,
    MatSliderModule,
    MatSelectModule,
    MatSlideToggleModule,
    FormsModule,
    MatAutocompleteModule,
    HttpClientModule,
    TypeaheadModule.forRoot(),
    BrowserAnimationsModule
  ],
  providers: [InputParametersService],
  bootstrap: [AppComponent]
})
export class AppModule { }
