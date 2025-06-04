// Store the nonce value for use in dynamically created scripts
window.CSP_NONCE = document.querySelector('script[nonce]').getAttribute('nonce');

// Override the createElement method to automatically add nonce to script elements
(function() {
  const originalCreateElement = document.createElement;
  
  document.createElement = function() {
    const element = originalCreateElement.apply(document, arguments);
    
    if (arguments[0].toLowerCase() === 'script' && window.CSP_NONCE) {
      element.setAttribute('nonce', window.CSP_NONCE);
    }
    
    return element;
  };
})();
