import template from './not-found.template.html';


function stateProviderConfig ($stateProvider) {
  'ngInject';

  $stateProvider.state('not-found', {
    'template': template
  });
}

export default stateProviderConfig;
