import { Component, OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';


import { InputParametersService } from './../input-parameters.service';

@Component({
  selector: 'app-menu-bar',
  templateUrl: './menu-bar.component.html',
  styleUrls: ['./menu-bar.component.css']
})
export class MenuBarComponent implements OnInit {
  animeList:any = [];
  arguments: String;
  constructor(private inputService: InputParametersService ) { }

  ngOnInit() { //runs on load
    this.getAnimeList();
    console.log(this.animeList);
  }
  getRecommendations() { //only runs when when user submits
    this.arguments = 'getRecommendations';
    this.arguments += '?animeName=' + this.selected;
    return this.inputService.getRecommendations(this.arguments);
  }

  getAnimeList() { //runs on ignite and on trigger reset
    return this.inputService.getAnimeList('getAnimeList').subscribe(res => {this.animeList = res});
    // console.log(this.data1);
  }
  selected: string;
  noResult = false;


  typeaheadNoResults(event: boolean): void {
    this.noResult = event;
  }
}
