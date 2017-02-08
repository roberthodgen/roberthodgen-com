
function urlRouterProviderConfig ($urlRouterProvider) {
  'ngInject';

  $urlRouterProvider.otherwise(otherwiseHandler);
}

function otherwiseHandler ($injector) {
  const $state = $injector.get('$state');
  $state.go('not-found');
}

export default urlRouterProviderConfig;
