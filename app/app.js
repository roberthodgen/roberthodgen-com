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

// import {RhContainer} from './rh-container';
// APP.controller('RhContainer', RhContainer);
//
// import {rhContainerDirective} from './rh-container';
// APP.directive('rhContainer', rhContainerDirective);
//
// import {RhContainerFluid} from './rh-container';
// APP.controller('RhContainerFluid', RhContainerFluid);
//
// import {rhContainerFluidDirective} from './rh-container';
// APP.directive('rhContainerFluid', rhContainerFluidDirective);
//
// import {rhHeroDirective} from './rh-hero';
// APP.directive('rhHero', rhHeroDirective);
//
// import {rhParallaxDirective} from './rh-parallax';
// APP.directive('rhParallax', rhParallaxDirective);


/*
 * Bootstrap it!
 */
let strictDi = true;
angular.bootstrap(document, ['roberthodgen-com'], {strictDi});

export default APP;
