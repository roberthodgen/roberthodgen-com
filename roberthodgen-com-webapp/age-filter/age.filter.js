import {isString, isDate, isNumber} from 'angular';

import timediff from 'timediff';


const TIMEDIFF_OPTIONS = {
  'units': 'Y'
};

function ageCalculator(input) {
  if (!isString(input) && !isDate(input) && !isNumber(input)) {
    return null;
  }

  return timediff(input, Date.now(), TIMEDIFF_OPTIONS).years;
}

function ageFilter() {
  return ageCalculator;
}

export default ageFilter;
