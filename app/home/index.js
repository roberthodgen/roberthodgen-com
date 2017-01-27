import angular from 'angular';

import './home.style.scss';

const MODULE_NAME = 'roberthodgen-com.home',
  MODULE = angular.module(MODULE_NAME, []);

import stateProviderConfig from './state-provider.config';
MODULE.config(stateProviderConfig);

export default MODULE_NAME;
