import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
// import { Observable } from ''

@Injectable({
  providedIn: 'root'
})
export class InputParametersService implements OnInit{

  constructor(private http: HttpClient) { }

  url = 'http://localhost:5000/';
  url2: String;
  url1: String;

  ngOnInit() {

  }
  getRecommendations(subPath) {
    url1 = this.url + subPath;
    console.log(this.url1);
    return this.http.get(this.url1).subscribe(res => {
      console.log(res);
    });
  }

  getAnimeList(subPath) {
    url2 = this.url + subPath;
    console.log(this.url2);
    return this.http.get(this.url2);
  }
}
