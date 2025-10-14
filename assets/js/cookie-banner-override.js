// Force override HubSpot cookie banner styles with JavaScript
// This is a workaround for HubSpot's aggressive inline styles that CSS can't override

(function() {
  'use strict';

  // Function to apply custom styles
  function applyCustomStyles() {
    const isDarkMode = document.documentElement.hasAttribute('data-dark-mode');

    // Target the parent container
    const bannerParent = document.getElementById('hs-banner-parent');
    if (bannerParent) {
      bannerParent.style.setProperty('position', 'fixed', 'important');
      bannerParent.style.setProperty('bottom', '0', 'important');
      bannerParent.style.setProperty('top', 'auto', 'important');
      bannerParent.style.setProperty('left', '0', 'important');
      bannerParent.style.setProperty('right', '0', 'important');
      bannerParent.style.setProperty('transform', 'none', 'important');
    }

    // Target the Accept button
    const acceptButton = document.getElementById('hs-eu-confirmation-button');
    if (acceptButton) {
      acceptButton.style.setProperty('background-color', '#7545fb', 'important');
      acceptButton.style.setProperty('background', '#7545fb', 'important');
      acceptButton.style.setProperty('color', '#ffffff', 'important');
      acceptButton.style.setProperty('border', 'none', 'important');
    }

    // Target the Cookie Settings button
    const settingsButton = document.getElementById('hs-eu-cookie-settings-button');
    if (settingsButton) {
      if (isDarkMode) {
        settingsButton.style.setProperty('background-color', '#2a2a3e', 'important');
        settingsButton.style.setProperty('background', '#2a2a3e', 'important');
        settingsButton.style.setProperty('color', '#e0e0e0', 'important');
        settingsButton.style.setProperty('border', '2px solid #444458', 'important');
      } else {
        settingsButton.style.setProperty('background-color', '#f5f5f5', 'important');
        settingsButton.style.setProperty('background', '#f5f5f5', 'important');
        settingsButton.style.setProperty('color', '#1a1a1a', 'important');
        settingsButton.style.setProperty('border', '2px solid #e0e0e0', 'important');
      }
    }

    return !!(bannerParent || acceptButton || settingsButton);
  }

  // Wait for the banner to appear in the DOM
  function waitForBanner() {
    const maxAttempts = 50; // Try for 5 seconds (50 * 100ms)
    let attempts = 0;

    const checkInterval = setInterval(function() {
      attempts++;

      if (applyCustomStyles()) {
        clearInterval(checkInterval);
        setupMutationObserver();
      } else if (attempts >= maxAttempts) {
        clearInterval(checkInterval);
      }
    }, 100);
  }

  // Watch for HubSpot re-applying inline styles
  function setupMutationObserver() {
    const bannerParent = document.getElementById('hs-banner-parent');
    const acceptButton = document.getElementById('hs-eu-confirmation-button');
    const settingsButton = document.getElementById('hs-eu-cookie-settings-button');

    const observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
          applyCustomStyles();
        }
      });
    });

    const config = { attributes: true, attributeOldValue: true };

    if (bannerParent) observer.observe(bannerParent, config);
    if (acceptButton) observer.observe(acceptButton, config);
    if (settingsButton) observer.observe(settingsButton, config);
  }

  // Watch for dark mode changes
  const darkModeObserver = new MutationObserver(function() {
    applyCustomStyles();
  });

  darkModeObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-dark-mode']
  });

  // Start when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', waitForBanner);
  } else {
    waitForBanner();
  }
})();
