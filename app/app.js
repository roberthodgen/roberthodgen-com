import './app.html';

import angular from 'angular';

/*
 * Import and declare AngularJS module dependencies
 */
import 'angular-ui-router';
import home from './home';

const REQUIRES = [
  'ui.router',
  home
];


/*
 * Setup the app
 * Import each module component and provide it to the new AngularJS module
 */
const APP = angular.module('roberthodgen-com', REQUIRES);

import locationProviderConfig from './location-provider.config';
APP.config(locationProviderConfig);



// import {rhParallaxDirective} from './rh-parallax';
// APP.directive('rhParallax', rhParallaxDirective);


/*
 * Bootstrap it!
 */
let strictDi = true;
angular.bootstrap(document, ['roberthodgen-com'], {strictDi});

export default APP;
