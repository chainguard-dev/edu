document.addEventListener('DOMContentLoaded', function() {
  const feedbackContainers = document.querySelectorAll('.feedback-container');
  
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
    
    function handlePositiveFeedback() {
      // Update button appearance
      const clickedBtnText = yesBtn.querySelector('.feedback-btn-text');
      clickedBtnText.textContent = '👍';
      yesBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
      
      // Show thank you message
      responseDiv.style.display = 'block';
      setTimeout(() => {
        responseDiv.classList.add('feedback-response-visible');
      }, 100);
    }
    
    function handleNegativeFeedback() {
      // Update button appearance
      const clickedBtnText = noBtn.querySelector('.feedback-btn-text');
      clickedBtnText.textContent = '👎';
      noBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
      
      // Create and show embedded Google Form
      const pageData = getPageData();
      const formUrl = `https://docs.google.com/forms/d/e/1FAIpQLScaZRQAfqr0CL9fsJ4y4oTdt1A6UQVazmEXw-wibcrqr0UFhg/viewform?embedded=true&entry.561897852=${pageData.url}&entry.408557657=${pageData.title}`;
      
      const iframe = document.createElement('iframe');
      iframe.src = formUrl;
      iframe.style.width = '100%';
      iframe.style.height = '500px';
      iframe.style.border = 'none';
      iframe.style.marginTop = '1rem';
      iframe.setAttribute('frameborder', '0');
      iframe.setAttribute('marginheight', '0');
      iframe.setAttribute('marginwidth', '0');
      iframe.innerHTML = 'Loading feedback form...';
      
      feedbackForm.innerHTML = '';
      feedbackForm.appendChild(iframe);
      feedbackForm.style.display = 'block';
      
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