import { TestBed } from '@angular/core/testing';

import { ResultsAccessService } from './results-access.service';

describe('ResultsAccessService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ResultsAccessService = TestBed.get(ResultsAccessService);
    expect(service).toBeTruthy();
  });
});
