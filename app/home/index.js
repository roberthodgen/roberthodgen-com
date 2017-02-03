import angular from 'angular';

import uiRouter from 'angular-ui-router';


const MODULE_NAME = 'roberthodgen-com.home',
  MODULE = angular.module(MODULE_NAME, [uiRouter]);

import stateProviderConfig from './state-provider.config';
MODULE.config(stateProviderConfig);

import notFoundCtrlDirective from './home-ctrl.directive';
MODULE.directive('homeCtrl', notFoundCtrlDirective);

export default MODULE_NAME;
