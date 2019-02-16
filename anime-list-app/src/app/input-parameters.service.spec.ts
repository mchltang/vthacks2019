import { TestBed } from '@angular/core/testing';

import { InputParametersService } from './input-parameters.service';

describe('InputParametersService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: InputParametersService = TestBed.get(InputParametersService);
    expect(service).toBeTruthy();
  });
});
