document.addEventListener('DOMContentLoaded', function() {
  const feedbackContainers = document.querySelectorAll('.feedback-container');
  
  // Configuration for embedded form
  const NEGATIVE_FORM_ID = '1FAIpQLScaZRQAfqr0CL9fsJ4y4oTdt1A6UQVazmEXw-wibcrqr0UFhg';
  const URL_FIELD = 'entry.561897852';
  const TITLE_FIELD = 'entry.408557657';
  
  feedbackContainers.forEach(container => {
    const yesBtn = container.querySelector('.feedback-yes');
    const noBtn = container.querySelector('.feedback-no');
    const feedbackForm = container.querySelector('.feedback-form');
    const responseDiv = container.querySelector('.feedback-response');
    
    function getPageData() {
      return {
        url: encodeURIComponent(window.location.href),
        title: encodeURIComponent(document.title)
      };
    }
    
    function createEmbeddedForm() {
      const pageData = getPageData();
      const formUrl = `https://docs.google.com/forms/d/e/${NEGATIVE_FORM_ID}/viewform?embedded=true&${URL_FIELD}=${pageData.url}&${TITLE_FIELD}=${pageData.title}`;
      
      const iframe = document.createElement('iframe');
      iframe.src = formUrl;
      iframe.width = '100%';
      iframe.height = '500';
      iframe.frameBorder = '0';
      iframe.marginHeight = '0';
      iframe.marginWidth = '0';
      iframe.style.border = 'none';
      iframe.style.borderRadius = '8px';
      iframe.loading = 'lazy';
      iframe.setAttribute('aria-label', 'Feedback form');
      
      return iframe;
    }
    
    function handlePositiveFeedback() {
      // Update button appearance
      const clickedBtnText = yesBtn.querySelector('.feedback-btn-text');
      clickedBtnText.textContent = '👍';
      yesBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
    }
    
    function handleNegativeFeedback() {
      // Update button appearance
      const clickedBtnText = noBtn.querySelector('.feedback-btn-text');
      clickedBtnText.textContent = '👎';
      noBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
      
      // Create and show embedded form
      const iframe = createEmbeddedForm();
      feedbackForm.innerHTML = '';
      feedbackForm.appendChild(iframe);
      feedbackForm.style.display = 'block';
      
      // Hide the thank you message since Google Forms will show its own confirmation
      responseDiv.style.display = 'none';
      
      setTimeout(() => {
        feedbackForm.classList.add('feedback-form-visible');
      }, 100);
    }
    
    if (yesBtn) {
      yesBtn.addEventListener('click', handlePositiveFeedback);
    }
    
    if (noBtn) {
      noBtn.addEventListener('click', handleNegativeFeedback);
    }
  });
});