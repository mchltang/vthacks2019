import { Component, OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';

import { ResultsAccessService } from './../results-access.service';
import { InputParametersService } from './../input-parameters.service';

@Component({
  selector: 'app-menu-bar',
  templateUrl: './menu-bar.component.html',
  styleUrls: ['./menu-bar.component.css']
})
export class MenuBarComponent implements OnInit {
  animeList:any = [];
  tVCheck = false;
  completedCheck = false;
  minScore = 0;
  arguments: String;
  selectedAnime: String;
  constructor(private inputService: InputParametersService, private sendDataService: ResultsAccessService ) { }

  ngOnInit() { //runs on load
    this.getAnimeList();
    // console.log(this.animeList);
  }

  getAnimeList() { //runs on ignite and on trigger reset
    return this.inputService.getAnimeList('getAnimeList').subscribe(res => {this.animeList = res});
    // console.log(this.data1);
  }

  getRecommendations() { //only runs when when user submits
    this.arguments = 'getRecommendations?anime=' + this.selectedAnime + '&tVCheck=';
    if (this.tVCheck == true) {
      this.arguments += 'yes';
    }
    else {
      this.arguments += 'no';
    }
    this.arguments += '&completedCheck=';
    if (this.completedCheck == true) {
      this.arguments += 'yes';
    }
    else {
      this.arguments += 'no';
    }
    this.arguments += '&minScore=' + this.minScore;
    this.sendDataService.sendRecommendationResults(this.inputService.getRecommendations(this.arguments));
  }
}
