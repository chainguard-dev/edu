document.addEventListener('DOMContentLoaded', function() {
  const feedbackContainers = document.querySelectorAll('.feedback-container');
  
  // Configuration - Replace these with your Google Forms IDs and entry IDs h
  const POSITIVE_FORM_ID = '1TksNn5V0uVXm3lNprFISg07ZzB7S89eKn8Iqs4II7fU';
  const NEGATIVE_FORM_ID = '1wRsf83llItanGKnZ7tZ2VcUZn83hcnjBruUIn77wxiU';
  
  const POSITIVE_ENTRIES = {
    url: 'entry.1628915989',
    title: 'entry.420806943'
  };
  
  const NEGATIVE_ENTRIES = {
    url: 'entry.561897852',
    title: 'entry.408557657',
    feedback: 'entry.1934740315'
  };
  
  feedbackContainers.forEach(container => {
    const yesBtn = container.querySelector('.feedback-yes');
    const noBtn = container.querySelector('.feedback-no');
    const questionDiv = container.querySelector('.feedback-question');
    const feedbackForm = container.querySelector('.feedback-form');
    const textarea = container.querySelector('.feedback-textarea');
    const submitBtn = container.querySelector('.feedback-submit-btn');
    const responseDiv = container.querySelector('.feedback-response');
    const thanksDiv = container.querySelector('.feedback-thanks');
    
    function getPageData() {
      return {
        url: window.location.href,
        title: document.title
      };
    }
    
    function submitToGoogleForm(formId, entries, data) {
      const params = new URLSearchParams();
      
      // Add the form entry data
      Object.keys(entries).forEach(key => {
        if (data[key]) {
          params.append(entries[key], data[key]);
        }
      });
      
      // Add required Google Forms hidden fields
      const timestamp = Date.now().toString();
      const fbzx = Math.floor(Math.random() * -9000000000000000000).toString();
      
      params.append('dlut', timestamp);
      params.append('fvv', '1');
      params.append('partialResponse', `[null,null,"${fbzx}"]`);
      params.append('pageHistory', '0');
      params.append('fbzx', fbzx);
      params.append('submissionTimestamp', timestamp);
      
      // Use direct Google Forms URL since we added it to CSP
      const baseUrl = 'https://docs.google.com/forms/d/e';
      
      const finalUrl = `${baseUrl}/${formId}/formResponse`;
      
      
      // Submit silently - ignore response/errors
      fetch(finalUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: params.toString(),
        mode: 'no-cors'
      }).then(() => {
        // Submission completed
      }).catch((error) => {
        // Submission failed, but we ignore errors in no-cors mode
      });
    }
    
    function showThankYou() {
      feedbackForm.style.display = 'none';
      responseDiv.style.display = 'block';
      
      setTimeout(() => {
        responseDiv.classList.add('feedback-response-visible');
      }, 100);
    }
    
    function handlePositiveFeedback() {
      // Update button appearance
      const clickedBtnText = yesBtn.querySelector('.feedback-btn-text');
      clickedBtnText.textContent = '👍';
      yesBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
      
      // Submit to Google Form
      const pageData = getPageData();
      submitToGoogleForm(POSITIVE_FORM_ID, POSITIVE_ENTRIES, pageData);
      
      // Show thank you
      showThankYou();
    }
    
    function handleNegativeFeedback() {
      // Update button appearance
      const clickedBtnText = noBtn.querySelector('.feedback-btn-text');
      clickedBtnText.textContent = '👎';
      noBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
      
      // Show feedback form
      feedbackForm.style.display = 'block';
      
      setTimeout(() => {
        feedbackForm.classList.add('feedback-form-visible');
        textarea.focus();
      }, 100);
    }
    
    function handleSubmitFeedback() {
      const feedbackText = textarea.value.trim();
      
      if (!feedbackText) {
        textarea.focus();
        return;
      }
      
      // Disable submit button
      submitBtn.disabled = true;
      submitBtn.textContent = 'Submitting...';
      
      // Submit to Google Form
      const pageData = getPageData();
      pageData.feedback = feedbackText;
      submitToGoogleForm(NEGATIVE_FORM_ID, NEGATIVE_ENTRIES, pageData);
      
      // Show thank you
      showThankYou();
    }
    
    if (yesBtn) {
      yesBtn.addEventListener('click', handlePositiveFeedback);
    }
    
    if (noBtn) {
      noBtn.addEventListener('click', handleNegativeFeedback);
    }
    
    if (submitBtn) {
      submitBtn.addEventListener('click', handleSubmitFeedback);
    }
    
    // Handle Enter key in textarea
    if (textarea) {
      textarea.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          handleSubmitFeedback();
        }
      });
    }
  });
});