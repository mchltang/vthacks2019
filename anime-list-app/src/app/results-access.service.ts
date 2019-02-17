import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResultsAccessService {
  myMethod: Observable<any>;
  private myMethodSubject = new Subject<any>();
  constructor() {
    this.myMethod = this.myMethodSubject.asObservable();
  }

  sendRecommendationResults(recommendationData) {
    console.log(recommendationData);
    this.myMethodSubject.next(recommendationData);
  }

}
