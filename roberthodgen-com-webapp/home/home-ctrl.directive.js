
function homeCtrlDirective () {
  function compile (tElement) {
    tElement.addClass('home-ctrl');
  }

  return {
    'restrict': 'A',
    'compile': compile
  };
}

export default homeCtrlDirective;
