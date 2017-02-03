import './app.html';

import './app.style.scss';

import angular from 'angular';

/*
 * Import and declare AngularJS module dependencies
 */
import home from './home';
import notFound from './not-found';
import ageFilter from './age-filter';

const REQUIRES = [
  home,
  notFound,
  ageFilter
];


/*
 * Setup the app
 * Import each module component and provide it to the new AngularJS module
 */
const APP = angular.module('roberthodgen-com', REQUIRES);

import locationProviderConfig from './location-provider.config';
APP.config(locationProviderConfig);


/*
 * Bootstrap it!
 */
let strictDi = true;
angular.bootstrap(document, ['roberthodgen-com'], {strictDi});

export default APP;
