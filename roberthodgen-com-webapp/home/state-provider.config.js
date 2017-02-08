import template from './home.template.html';


function stateProviderConfig ($stateProvider) {
  'ngInject';

  $stateProvider.state('home', {
    'url': '/',
    'template': template
  });
}

export default stateProviderConfig;
