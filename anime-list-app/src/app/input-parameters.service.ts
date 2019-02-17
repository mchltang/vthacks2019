import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
// import { Observable } from ''

@Injectable({
  providedIn: 'root'
})
export class InputParametersService implements OnInit{

  constructor(private http: HttpClient) { }

  url = 'http://localhost:5000/';

  ngOnInit() {

  }
  getRecommendations(subPath) {
    this.url += subPath;
    return this.http.get(this.url);
  }

  getAnimeList(subPath) {
    this.url += subPath;
    console.log(this.url);
    return this.http.get(this.url);
  }
}
