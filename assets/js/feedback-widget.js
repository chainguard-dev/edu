/**
 * Feedback Widget JavaScript
 * Handles interactive feedback collection and Google Forms submission
 */

class FeedbackRateLimiter {
  constructor() {
    this.storageKey = 'feedback-submissions';
    this.maxSubmissions = 3; // Max submissions per time window
    this.timeWindow = 15 * 60 * 1000; // 15 minutes in milliseconds
    this.submissions = this.loadSubmissions();
  }

  loadSubmissions() {
    try {
      const stored = localStorage.getItem(this.storageKey);
      if (stored) {
        const submissions = JSON.parse(stored);
        // Clean up old submissions
        const now = Date.now();
        return submissions.filter(timestamp => now - timestamp < this.timeWindow);
      }
    } catch (e) {
      console.warn('Failed to load submission history:', e);
    }
    return [];
  }

  saveSubmissions() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.submissions));
    } catch (e) {
      console.warn('Failed to save submission history:', e);
    }
  }

  canSubmit() {
    // To disable rate limiting for testing, uncomment the line below and comment out the rest:
    // return true;
    
    this.cleanOldSubmissions();
    return this.submissions.length < this.maxSubmissions;
  }

  recordSubmission() {
    const now = Date.now();
    this.submissions.push(now);
    this.saveSubmissions();
  }

  cleanOldSubmissions() {
    const now = Date.now();
    this.submissions = this.submissions.filter(timestamp => now - timestamp < this.timeWindow);
    this.saveSubmissions();
  }

  getTimeUntilNextSubmission() {
    if (this.canSubmit()) {
      return 0;
    }
    
    // Find the oldest submission that will expire first
    const oldestSubmission = Math.min(...this.submissions);
    const timeUntilExpiry = this.timeWindow - (Date.now() - oldestSubmission);
    return Math.max(0, timeUntilExpiry);
  }

  getRemainingSubmissions() {
    this.cleanOldSubmissions();
    return Math.max(0, this.maxSubmissions - this.submissions.length);
  }
}

class FeedbackWidget {
  constructor(container) {
    this.container = container;
    this.data = this.loadFeedbackData();
    this.currentState = 'initial'; // initial, thanks, form, status
    this.rateLimiter = new FeedbackRateLimiter();
    
    this.elements = {
      prompt: container.querySelector('.feedback-prompt'),
      thanks: container.querySelector('.feedback-thanks'),
      form: container.querySelector('.feedback-form'),
      status: container.querySelector('.feedback-status'),
      yesBtn: container.querySelector('[data-feedback="yes"]'),
      noBtn: container.querySelector('[data-feedback="no"]'),
      textarea: container.querySelector('.feedback-textarea'),
      charCount: container.querySelector('.char-count'),
      submitBtn: container.querySelector('.feedback-submit-btn'),
      cancelBtn: container.querySelector('.feedback-cancel-btn'),
      statusSuccess: container.querySelector('.feedback-status-success'),
      statusError: container.querySelector('.feedback-status-error')
    };

    this.bindEvents();
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
    if (!this.rateLimiter.canSubmit()) {
      this.showRateLimitError();
      return;
    }
    
    this.updateButtonState(this.elements.yesBtn, '👍');
    this.disableButton(this.elements.noBtn);
    this.setState('thanks');
    this.submitPositiveFeedback();
  }

  handleNegativeFeedback() {
    if (!this.rateLimiter.canSubmit()) {
      this.showRateLimitError();
      return;
    }
    
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
    
    // Hide secondary sections
    this.elements.thanks.style.display = 'none';
    this.elements.form.style.display = 'none';
    this.elements.status.style.display = 'none';

    // Show the appropriate section below the prompt
    switch (newState) {
      case 'initial':
        // Only prompt is visible
        break;
      case 'thanks':
        this.elements.thanks.style.display = 'block';
        break;
      case 'form':
        this.elements.form.style.display = 'block';
        break;
      case 'status':
        this.elements.status.style.display = 'block';
        break;
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
      this.rateLimiter.recordSubmission();
    } catch (error) {
      console.error('Failed to submit positive feedback:', error);
      // Don't show error for positive feedback since user already saw success
    }
  }

  async submitNegativeFeedback() {
    const feedbackText = this.elements.textarea?.value?.trim();
    
    if (!feedbackText) {
      this.elements.textarea?.focus();
      return;
    }

    // Disable submit button during submission
    if (this.elements.submitBtn) {
      this.elements.submitBtn.disabled = true;
      this.elements.submitBtn.textContent = 'Submitting...';
    }

    try {
      const result = await this.submitToAppsScript({
        pageTitle: this.data.pageTitle,
        pageUrl: this.data.pageUrl,
        feedbackType: 'negative',
        feedbackText: feedbackText
      });
      
      if (result.success) {
        this.rateLimiter.recordSubmission();
        this.setState('thanks');
      } else {
        this.showStatus('error', result.error);
      }
    } catch (error) {
      console.error('Failed to submit negative feedback:', error);
      this.showStatus('error');
    } finally {
      // Reset submit button
      if (this.elements.submitBtn) {
        this.elements.submitBtn.disabled = false;
        this.elements.submitBtn.textContent = 'Submit';
      }
    }
  }

  async submitToAppsScript(data) {
    if (!this.data.appsScriptUrl || this.data.appsScriptUrl === 'YOUR_APPS_SCRIPT_URL_HERE') {
      throw new Error('Apps Script URL not configured');
    }

    const response = await fetch(this.data.appsScriptUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain;charset=utf-8',
      },
      body: JSON.stringify(data),
      redirect: 'follow'
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  }

  showStatus(type, errorMessage = null) {
    this.setState('status');
    
    if (type === 'success') {
      this.elements.statusSuccess.style.display = 'block';
      this.elements.statusError.style.display = 'none';
    } else {
      this.elements.statusSuccess.style.display = 'none';
      this.elements.statusError.style.display = 'block';
      
      // Update error message if provided
      if (errorMessage) {
        const errorText = this.elements.statusError.querySelector('.feedback-text');
        if (errorText) {
          errorText.textContent = errorMessage;
        }
      }
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

  showRateLimitError() {
    const timeLeft = this.rateLimiter.getTimeUntilNextSubmission();
    const minutes = Math.ceil(timeLeft / 60000);
    
    // Show error below the prompt instead of replacing it
    this.setState('status');
    this.elements.statusSuccess.style.display = 'none';
    this.elements.statusError.style.display = 'block';
    
    const errorText = this.elements.statusError.querySelector('.feedback-text');
    if (errorText) {
      errorText.textContent = `Please wait ${minutes} minute${minutes > 1 ? 's' : ''} before submitting feedback again.`;
    }
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