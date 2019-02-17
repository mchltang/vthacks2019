//IMPORT LIBS
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


//IMPORT SERVICES
import { InputParametersService } from './input-parameters.service';
import { ResultsAccessService } from './results-access.service';


//IMPORT COMPONENTS
import { AppComponent } from './app.component';
import { MenuBarComponent } from './menu-bar/menu-bar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatListModule, MatCardModule, MatToolbarModule, MatDividerModule, MatSlideToggleModule, MatSliderModule, MatInputModule, MatButtonModule, MatSelectModule} from '@angular/material';
import { SearchResultsComponent } from './search-results/search-results.component';




@NgModule({
  declarations: [
    AppComponent,
    MenuBarComponent,
    SearchResultsComponent
  ],
  imports: [
    MatListModule,
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
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [InputParametersService,
              ResultsAccessService],
  bootstrap: [AppComponent]
})
export class AppModule { }
