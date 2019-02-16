import { Component, OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';

import { InputParametersService } from './../input-parameters.service';

@Component({
  selector: 'app-menu-bar',
  templateUrl: './menu-bar.component.html',
  styleUrls: ['./menu-bar.component.css']
})
export class MenuBarComponent implements OnInit {

  data1:any = [];

  constructor(private inputService: InputParametersService ) { }

  ngOnInit() {
    this.data1 = this.getParams();
    console.log(this.data1);
  }

  getParams() {
    return this.inputService.getParams('get-recommendations');
    // console.log(this.data1);
  }
  selected: string;
  noResult = false;


  typeaheadNoResults(event: boolean): void {
    this.noResult = event;
  }
}
