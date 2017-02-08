
function notFoundCtrlDirective () {
  function compile (tElement) {
    tElement.addClass('not-found-ctrl');
  }

  return {
    'restrict': 'A',
    'compile': compile
  };
}

export default notFoundCtrlDirective;
