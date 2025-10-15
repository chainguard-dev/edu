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
      bannerParent.style.setProperty('opacity', '1', 'important');
    }

    // Target the main banner confirmation element
    const confirmation = document.getElementById('hs-eu-cookie-confirmation');
    if (confirmation) {
      confirmation.style.setProperty('opacity', '1', 'important');
      if (isDarkMode) {
        confirmation.style.setProperty('background-color', '#1a1a2e', 'important');
        confirmation.style.setProperty('background', '#1a1a2e', 'important');
      } else {
        confirmation.style.setProperty('background-color', '#ffffff', 'important');
        confirmation.style.setProperty('background', '#ffffff', 'important');
      }
    }

    // Target the cookie settings modal
    const cookieSettings = document.getElementById('hs-eu-cookie-settings');
    if (cookieSettings) {
      cookieSettings.style.setProperty('opacity', '1', 'important');
      if (isDarkMode) {
        cookieSettings.style.setProperty('background-color', '#1a1a2e', 'important');
        cookieSettings.style.setProperty('background', '#1a1a2e', 'important');
      } else {
        cookieSettings.style.setProperty('background-color', '#ffffff', 'important');
        cookieSettings.style.setProperty('background', '#ffffff', 'important');
      }
    }

    // Target the Accept button
    const acceptButton = document.getElementById('hs-eu-confirmation-button');
    if (acceptButton) {
      acceptButton.style.setProperty('background-color', '#7545fb', 'important');
      acceptButton.style.setProperty('background', '#7545fb', 'important');
      acceptButton.style.setProperty('color', '#ffffff', 'important');
      acceptButton.style.setProperty('border', 'none', 'important');
      acceptButton.style.setProperty('opacity', '1', 'important');
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
      settingsButton.style.setProperty('opacity', '1', 'important');
    }

    // Target the Decline button (if present)
    const declineButton = document.getElementById('hs-eu-decline-button');
    if (declineButton) {
      if (isDarkMode) {
        declineButton.style.setProperty('background-color', '#2a2a3e', 'important');
        declineButton.style.setProperty('background', '#2a2a3e', 'important');
        declineButton.style.setProperty('color', '#e0e0e0', 'important');
        declineButton.style.setProperty('border', '2px solid #444458', 'important');
      } else {
        declineButton.style.setProperty('background-color', '#f5f5f5', 'important');
        declineButton.style.setProperty('background', '#f5f5f5', 'important');
        declineButton.style.setProperty('color', '#1a1a1a', 'important');
        declineButton.style.setProperty('border', '2px solid #e0e0e0', 'important');
      }
      declineButton.style.setProperty('opacity', '1', 'important');
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
    const confirmation = document.getElementById('hs-eu-cookie-confirmation');
    const cookieSettings = document.getElementById('hs-eu-cookie-settings');
    const acceptButton = document.getElementById('hs-eu-confirmation-button');
    const settingsButton = document.getElementById('hs-eu-cookie-settings-button');
    const declineButton = document.getElementById('hs-eu-decline-button');

    const observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
          applyCustomStyles();
        }
      });
    });

    const config = { attributes: true, attributeOldValue: true };

    if (bannerParent) observer.observe(bannerParent, config);
    if (confirmation) observer.observe(confirmation, config);
    if (cookieSettings) observer.observe(cookieSettings, config);
    if (acceptButton) observer.observe(acceptButton, config);
    if (settingsButton) observer.observe(settingsButton, config);
    if (declineButton) observer.observe(declineButton, config);
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
