// Force override HubSpot cookie banner styles with JavaScript
// This is a workaround for HubSpot's aggressive inline styles that CSS can't override

(function() {
  'use strict';

  // Create or update backdrop overlay
  function createBackdrop() {
    let backdrop = document.getElementById('cookie-banner-backdrop');
    if (!backdrop) {
      backdrop = document.createElement('div');
      backdrop.id = 'cookie-banner-backdrop';
      document.body.appendChild(backdrop);
    }

    backdrop.style.setProperty('position', 'fixed', 'important');
    backdrop.style.setProperty('top', '0', 'important');
    backdrop.style.setProperty('left', '0', 'important');
    backdrop.style.setProperty('right', '0', 'important');
    backdrop.style.setProperty('bottom', '0', 'important');
    backdrop.style.setProperty('background-color', 'rgba(0, 0, 0, 0.5)', 'important');
    backdrop.style.setProperty('z-index', '9999', 'important');
    backdrop.style.setProperty('pointer-events', 'none', 'important');
    backdrop.style.setProperty('display', 'block', 'important');

    return backdrop;
  }

  // Function to apply custom styles
  function applyCustomStyles() {
    const isDarkMode = document.documentElement.hasAttribute('data-dark-mode');

    // Create backdrop overlay
    const backdrop = createBackdrop();

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
      bannerParent.style.setProperty('z-index', '10000', 'important');
    }

    // Target the main banner confirmation element
    const confirmation = document.getElementById('hs-eu-cookie-confirmation');
    if (confirmation) {
      confirmation.style.setProperty('opacity', '1', 'important');
      if (isDarkMode) {
        confirmation.style.setProperty('background-color', 'rgb(26, 26, 46)', 'important');
        confirmation.style.setProperty('background', 'rgb(26, 26, 46)', 'important');
      } else {
        confirmation.style.setProperty('background-color', 'rgb(255, 255, 255)', 'important');
        confirmation.style.setProperty('background', 'rgb(255, 255, 255)', 'important');
      }

      // Fix all text colors in the banner
      const allTextElements = confirmation.querySelectorAll('p, span, a, div, h1, h2, h3, h4, h5, h6');
      allTextElements.forEach(function(el) {
        if (!el.closest('button')) { // Don't style text inside buttons
          if (isDarkMode) {
            el.style.setProperty('color', '#e0e0e0', 'important');
          } else {
            el.style.setProperty('color', '#1a1a1a', 'important');
          }
        }
      });
    }

    // Target the cookie settings modal
    const cookieSettings = document.getElementById('hs-eu-cookie-settings');
    if (cookieSettings) {
      cookieSettings.style.setProperty('opacity', '1', 'important');
      cookieSettings.style.setProperty('z-index', '10001', 'important');
      if (isDarkMode) {
        cookieSettings.style.setProperty('background-color', 'rgb(26, 26, 46)', 'important');
        cookieSettings.style.setProperty('background', 'rgb(26, 26, 46)', 'important');
      } else {
        cookieSettings.style.setProperty('background-color', 'rgb(255, 255, 255)', 'important');
        cookieSettings.style.setProperty('background', 'rgb(255, 255, 255)', 'important');
      }

      // Fix all text colors in the modal
      const allModalText = cookieSettings.querySelectorAll('p, span, a, div, h1, h2, h3, h4, h5, h6, label');
      allModalText.forEach(function(el) {
        if (!el.closest('button')) { // Don't style text inside buttons
          if (isDarkMode) {
            el.style.setProperty('color', '#e0e0e0', 'important');
          } else {
            el.style.setProperty('color', '#1a1a1a', 'important');
          }
        }
      });
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

  // Remove backdrop when banner is closed
  function removeBackdrop() {
    const backdrop = document.getElementById('cookie-banner-backdrop');
    if (backdrop) {
      backdrop.remove();
    }
  }

  // Check if banner is still visible
  function isBannerVisible() {
    const bannerParent = document.getElementById('hs-banner-parent');
    return bannerParent && bannerParent.offsetParent !== null;
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
        setupBannerVisibilityWatcher();
      } else if (attempts >= maxAttempts) {
        clearInterval(checkInterval);
      }
    }, 100);
  }

  // Watch for banner removal/hiding
  function setupBannerVisibilityWatcher() {
    const checkVisibility = setInterval(function() {
      if (!isBannerVisible()) {
        removeBackdrop();
        clearInterval(checkVisibility);
      }
    }, 500);
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
