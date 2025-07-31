/**
 * Feedback Widget JavaScript
 * Handles interactive feedback collection and Google Forms submission
 */

class FeedbackWidget {
  constructor(container) {
    this.container = container;
    this.data = this.loadFeedbackData();
    this.currentState = 'initial'; // initial, thanks, form, status
    
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
      positiveFormUrl: 'https://docs.google.com/forms/d/e/1FAIpQLSdnnnllDa3BpWSjuS5rax2glIMrOYSEF8rP3pqDss3bSwbchQ/formResponse',
      negativeFormUrl: 'https://docs.google.com/forms/d/e/1FAIpQLScaZRQAfqr0CL9fsJ4y4oTdt1A6UQVazmEXw-wibcrqr0UFhg/formResponse'
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
    this.setState('thanks');
    this.submitPositiveFeedback();
  }

  handleNegativeFeedback() {
    this.updateButtonState(this.elements.noBtn, '👎');
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

  setState(newState) {
    this.currentState = newState;
    
    // Hide all sections
    this.elements.prompt.style.display = 'none';
    this.elements.thanks.style.display = 'none';
    this.elements.form.style.display = 'none';
    this.elements.status.style.display = 'none';

    // Show the appropriate section
    switch (newState) {
      case 'initial':
        this.elements.prompt.style.display = 'block';
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
      await this.submitToGoogleForm(this.data.positiveFormUrl, {
        'entry.1436583328': this.data.pageUrl, // URL field
        'entry.776814152': this.data.pageTitle // Title field
      });
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
      await this.submitToGoogleForm(this.data.negativeFormUrl, {
        'entry.906974735': this.data.pageUrl, // URL field
        'entry.1319083678': this.data.pageTitle, // Title field
        'entry.775804475': feedbackText // Feedback field
      });
      
      this.showStatus('success');
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

  async submitToGoogleForm(formUrl, data) {
    const formData = new FormData();
    
    // Add form fields
    Object.entries(data).forEach(([key, value]) => {
      formData.append(key, value);
    });

    // Submit to Google Form
    const response = await fetch(formUrl, {
      method: 'POST',
      body: formData,
      mode: 'no-cors' // Google Forms requires no-cors mode
    });

    // Since no-cors mode doesn't allow reading the response,
    // we assume success if no error was thrown
    return response;
  }

  showStatus(type) {
    this.setState('status');
    
    if (type === 'success') {
      this.elements.statusSuccess.style.display = 'block';
      this.elements.statusError.style.display = 'none';
    } else {
      this.elements.statusSuccess.style.display = 'none';
      this.elements.statusError.style.display = 'block';
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