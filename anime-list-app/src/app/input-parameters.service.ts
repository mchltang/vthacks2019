import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class InputParametersService implements OnInit{

  constructor(private http: HttpClient) { }

  url = 'http://localhost:5000/';

  ngOnInit() {

  }

  getParams(subPath) {
    this.url += subPath;
    console.log(this.url);
    this.http.get(this.url).subscribe(data => {
      console.log(data);
    });
  }
}
