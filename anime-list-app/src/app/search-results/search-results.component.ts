import { Component} from '@angular/core';

// import { InputParametersService } from './../input-parameters.service';
import { ResultsAccessService } from './../results-access.service';

@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrls: ['./search-results.component.css']
})
export class SearchResultsComponent {
  recList:any = [];

  constructor(private receiveDataService: ResultsAccessService, ) {
    this.receiveDataService.myMethod.subscribe(data => {
      this.recList = [data];
    });
  }

}
