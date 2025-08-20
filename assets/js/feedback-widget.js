/**
 * Feedback Widget JavaScript
 * Handles interactive feedback collection and Google Forms submission
 */

class FeedbackWidget {
  constructor(container) {
    this.container = container;
    this.data = this.loadFeedbackData();
    this.currentState = 'initial'; // initial, thanks, form
    this.retryCount = 0;
    this.maxRetries = 2;
    
    this.elements = {
      prompt: container.querySelector('.feedback-prompt'),
      thanks: container.querySelector('.feedback-thanks'),
      form: container.querySelector('.feedback-form'),
      yesBtn: container.querySelector('[data-feedback="yes"]'),
      noBtn: container.querySelector('[data-feedback="no"]'),
      textarea: container.querySelector('.feedback-textarea'),
      charCount: container.querySelector('.char-count'),
      submitBtn: container.querySelector('.feedback-submit-btn'),
      cancelBtn: container.querySelector('.feedback-cancel-btn')
    };

    this.bindEvents();
    this.checkExistingFeedback();
  }

  checkExistingFeedback() {
    // Check if user has already provided feedback for this page
    const pageKey = `feedback-${this.data.pageUrl}`;
    const existingFeedback = localStorage.getItem(pageKey);
    
    if (existingFeedback) {
      const feedbackData = JSON.parse(existingFeedback);
      const daysSinceFeedback = (Date.now() - feedbackData.timestamp) / (1000 * 60 * 60 * 24);
      
      // Show existing feedback state if less than 30 days old
      if (daysSinceFeedback < 30) {
        if (feedbackData.type === 'positive') {
          this.updateButtonState(this.elements.yesBtn, '👍');
          this.disableButton(this.elements.noBtn);
        } else if (feedbackData.type === 'negative') {
          this.updateButtonState(this.elements.noBtn, '👎');
          this.disableButton(this.elements.yesBtn);
        }
        this.setState('thanks');
      } else {
        // Clear old feedback
        localStorage.removeItem(pageKey);
      }
    }
  }

  saveFeedbackState(type) {
    const pageKey = `feedback-${this.data.pageUrl}`;
    const feedbackData = {
      type: type,
      timestamp: Date.now()
    };
    try {
      localStorage.setItem(pageKey, JSON.stringify(feedbackData));
    } catch (e) {
      console.warn('Failed to save feedback state:', e);
    }
  }

  loadFeedbackData() {
    const dataScript = document.getElementById('feedback-data');
    if (dataScript) {
      try {
        return JSON.parse(dataScript.textContent);
      } catch (e) {
        console.error('Failed to parse feedback data:', e);
      }
    }
    return {
      pageTitle: document.title,
      pageUrl: window.location.href,
      appsScriptUrl: 'YOUR_APPS_SCRIPT_URL_HERE' // Will be replaced with actual URL
    };
  }

  bindEvents() {
    // Feedback button clicks
    this.elements.yesBtn?.addEventListener('click', () => this.handlePositiveFeedback());
    this.elements.noBtn?.addEventListener('click', () => this.handleNegativeFeedback());

    // Form interactions
    this.elements.textarea?.addEventListener('input', (e) => this.updateCharCount(e.target.value));
    this.elements.submitBtn?.addEventListener('click', () => this.submitNegativeFeedback());
    this.elements.cancelBtn?.addEventListener('click', () => this.cancelFeedback());

    // Keyboard accessibility
    this.elements.textarea?.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.cancelFeedback();
      }
    });
  }

  handlePositiveFeedback() {
    this.updateButtonState(this.elements.yesBtn, '👍');
    this.disableButton(this.elements.noBtn);
    this.setState('thanks');
    this.submitPositiveFeedback();
  }

  handleNegativeFeedback() {
    this.updateButtonState(this.elements.noBtn, '👎');
    this.disableButton(this.elements.yesBtn);
    this.setState('form');
    // Focus the textarea for better UX
    setTimeout(() => {
      this.elements.textarea?.focus();
    }, 100);
  }

  updateButtonState(button, emoji) {
    if (button) {
      button.classList.add('feedback-selected');
      const textSpan = button.querySelector('.feedback-btn-text');
      if (textSpan) {
        textSpan.textContent = emoji;
      }
      button.setAttribute('aria-pressed', 'true');
    }
  }

  disableButton(button) {
    if (button) {
      button.disabled = true;
      button.classList.add('feedback-disabled');
      button.style.opacity = '0.5';
      button.style.cursor = 'not-allowed';
    }
  }

  enableButton(button) {
    if (button) {
      button.disabled = false;
      button.classList.remove('feedback-disabled');
      button.style.opacity = '';
      button.style.cursor = '';
    }
  }

  setState(newState) {
    this.currentState = newState;
    
    // Always keep prompt visible
    this.elements.prompt.style.display = 'block';
    
    // Hide secondary sections with fade out
    const sections = [this.elements.thanks, this.elements.form];
    sections.forEach(section => {
      if (section) {
        section.style.display = 'none';
        section.classList.remove('feedback-fade-in');
      }
    });

    // Show the appropriate section below the prompt with fade in
    let targetElement = null;
    switch (newState) {
      case 'initial':
        // Only prompt is visible
        break;
      case 'thanks':
        targetElement = this.elements.thanks;
        break;
      case 'form':
        targetElement = this.elements.form;
        break;
    }
    
    if (targetElement) {
      targetElement.style.display = 'block';
      // Trigger reflow to ensure animation plays
      void targetElement.offsetWidth;
      targetElement.classList.add('feedback-fade-in');
    }
  }

  updateCharCount(text) {
    const count = text.length;
    if (this.elements.charCount) {
      this.elements.charCount.textContent = count;
    }
    
    // Update submit button state
    if (this.elements.submitBtn) {
      this.elements.submitBtn.disabled = count === 0 || count > 1000;
    }
  }

  async submitPositiveFeedback() {
    try {
      await this.submitToAppsScript({
        pageTitle: this.data.pageTitle,
        pageUrl: this.data.pageUrl,
        feedbackType: 'positive',
        feedbackText: ''
      });
      this.saveFeedbackState('positive');
    } catch (error) {
      console.error('Failed to submit positive feedback:', error);
      // Don't show error for positive feedback since user already saw success
      // Still save the state locally even if submission failed
      this.saveFeedbackState('positive');
    }
  }

  async submitNegativeFeedback() {
    const feedbackText = this.elements.textarea?.value?.trim();
    
    if (!feedbackText) {
      this.elements.textarea?.focus();
      return;
    }

    // Show loading state
    this.showLoadingState();

    try {
      const result = await this.submitToAppsScriptWithRetry({
        pageTitle: this.data.pageTitle,
        pageUrl: this.data.pageUrl,
        feedbackType: 'negative',
        feedbackText: feedbackText
      });
      
      if (result.success) {
        this.saveFeedbackState('negative');
        this.hideLoadingState();
        this.setState('thanks');
      } else {
        // Even if submission fails, thank the user and save state locally
        this.saveFeedbackState('negative');
        this.hideLoadingState();
        this.setState('thanks');
      }
    } catch (error) {
      console.error('Failed to submit negative feedback:', error);
      // Even if submission fails, thank the user and save state locally
      this.saveFeedbackState('negative');
      this.hideLoadingState();
      this.setState('thanks');
    }
  }

  showLoadingState() {
    if (this.elements.submitBtn) {
      this.elements.submitBtn.disabled = true;
      this.elements.submitBtn.textContent = 'Submitting...';
    }
  }

  hideLoadingState() {
    if (this.elements.submitBtn) {
      this.elements.submitBtn.disabled = false;
      this.elements.submitBtn.textContent = 'Submit';
    }
  }

  async submitToAppsScriptWithRetry(data) {
    this.retryCount = 0;
    
    while (this.retryCount <= this.maxRetries) {
      try {
        const result = await this.submitToAppsScript(data);
        return result;
      } catch (error) {
        this.retryCount++;
        
        if (this.retryCount > this.maxRetries) {
          throw error;
        }
        
        // Wait before retrying (exponential backoff)
        const delay = Math.min(1000 * Math.pow(2, this.retryCount - 1), 4000);
        await new Promise(resolve => setTimeout(resolve, delay));
        
        console.log(`Retrying submission (attempt ${this.retryCount + 1}/${this.maxRetries + 1})...`);
      }
    }
  }

  async submitToAppsScript(data) {
    if (!this.data.appsScriptUrl || this.data.appsScriptUrl === 'YOUR_APPS_SCRIPT_URL_HERE' || this.data.appsScriptUrl === '') {
      throw new Error('Apps Script URL not configured');
    }

    // Create an AbortController for timeout
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 second timeout

    try {
      const response = await fetch(this.data.appsScriptUrl, {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'text/plain;charset=utf-8',
        },
        body: JSON.stringify(data),
        redirect: 'follow',
        signal: controller.signal
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error('Failed to submit feedback. Please try again.');
      }

      const result = await response.json();
      return result;
    } catch (error) {
      clearTimeout(timeoutId);
      
      if (error.name === 'AbortError') {
        throw new Error('Request timeout - please try again');
      }
      throw error;
    }
  }

  cancelFeedback() {
    // Reset form
    if (this.elements.textarea) {
      this.elements.textarea.value = '';
    }
    this.updateCharCount('');
    
    // Reset button states
    this.elements.yesBtn?.classList.remove('feedback-selected');
    this.elements.noBtn?.classList.remove('feedback-selected');
    this.elements.yesBtn?.setAttribute('aria-pressed', 'false');
    this.elements.noBtn?.setAttribute('aria-pressed', 'false');
    
    // Re-enable both buttons
    this.enableButton(this.elements.yesBtn);
    this.enableButton(this.elements.noBtn);
    
    // Reset button text
    const yesText = this.elements.yesBtn?.querySelector('.feedback-btn-text');
    const noText = this.elements.noBtn?.querySelector('.feedback-btn-text');
    if (yesText) yesText.textContent = 'Yes';
    if (noText) noText.textContent = 'No';
    
    // Return to initial state
    this.setState('initial');
  }

}

// Initialize feedback widgets when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  const feedbackWidgets = document.querySelectorAll('.feedback-widget');
  
  feedbackWidgets.forEach(widget => {
    new FeedbackWidget(widget);
  });
});

// Handle page navigation for single-page apps (if applicable)
window.addEventListener('popstate', function() {
  // Reinitialize if needed
  const feedbackWidgets = document.querySelectorAll('.feedback-widget');
  feedbackWidgets.forEach(widget => {
    if (!widget.feedbackWidget) {
      widget.feedbackWidget = new FeedbackWidget(widget);
    }
  });
});