import angular from 'angular';


const MODULE_NAME = 'roberthodgen.age-filter',
    MODULE = angular.module(MODULE_NAME, []);

import ageFilter from './age.filter';
MODULE.filter('age', ageFilter);

export default MODULE_NAME;
