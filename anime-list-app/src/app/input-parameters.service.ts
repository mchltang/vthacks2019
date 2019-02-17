import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { ResultsAccessService } from './results-access.service';

@Injectable({
  providedIn: 'root'
})
export class InputParametersService implements OnInit{

  constructor(private http: HttpClient, private rService: ResultsAccessService) { }

  url = 'http://localhost:5000/';
  url2;
  url1;
  ngOnInit() {

  }
  getRecommendations(subPath) {
    this.url1 = this.url + subPath;
    console.log(this.url1);
    return this.http.get(this.url1).subscribe(res => {
      console.log(res);
      this.rService.sendRecommendationResults(res);
    });
  }

  getAnimeList(subPath) {
    this.url2 = this.url + subPath;
    console.log(this.url2);
    return this.http.get(this.url2);
  }
}
