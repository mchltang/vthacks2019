import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrls: ['./search-results.component.css']
})
export class SearchResultsComponent implements OnInit {
  recList: string[] = ['Alabama', 'Virginia', 'Washington', 'A','B', 'c', 'd', 'e', 'f', 'g'];

  constructor() { }


  ngOnInit() {
  }

}
