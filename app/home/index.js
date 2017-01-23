import angular from 'angular';

import './home.style.scss';

const MODULE_NAME = 'roberthodgen-com.home',
  MODULE = angular.module(MODULE_NAME, []);

import stateProviderConfig from './state-provider.cofig';
MODULE.config(stateProviderConfig);

export default MODULE_NAME;
