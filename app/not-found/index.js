import angular from 'angular';
import uiRouter from 'angular-ui-router';

import './not-found.style.scss';


const MODULE_NAME = 'roberthodgen-com.not-found',
    MODULE = angular.module(MODULE_NAME, [uiRouter]);

import stateProviderConfig from './state-provider.config';
MODULE.config(stateProviderConfig);

import urlRouterProviderConfig from './url-router-provider.config';
MODULE.config(urlRouterProviderConfig);

import notFoundCtrlDirective from './not-found-ctrl.directive';
MODULE.directive('notFoundCtrl', notFoundCtrlDirective);

export default MODULE_NAME;
