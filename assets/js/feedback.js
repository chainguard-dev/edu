document.addEventListener('DOMContentLoaded', function() {
  const feedbackContainers = document.querySelectorAll('.feedback-container');
  
  feedbackContainers.forEach(container => {
    const yesBtn = container.querySelector('.feedback-yes');
    const noBtn = container.querySelector('.feedback-no');
    const questionDiv = container.querySelector('.feedback-question');
    const responseDiv = container.querySelector('.feedback-response');
    const thanksDiv = container.querySelector('.feedback-thanks');
    const linkDiv = container.querySelector('.feedback-link');
    
    function handleFeedback(isPositive) {
      // Update button appearance
      const clickedBtn = isPositive ? yesBtn : noBtn;
      const clickedBtnText = clickedBtn.querySelector('.feedback-btn-text');
      
      // Show emoji in clicked button
      clickedBtnText.textContent = isPositive ? '👍' : '👎';
      
      // Add success state to clicked button
      clickedBtn.classList.add('feedback-clicked');
      
      // Disable both buttons
      yesBtn.disabled = true;
      noBtn.disabled = true;
      
      // Show response section
      responseDiv.style.display = 'block';
      thanksDiv.style.display = 'block';
      
      // Show link only for negative feedback
      if (!isPositive) {
        linkDiv.style.display = 'block';
      }
      
      // Add fade-in animation
      setTimeout(() => {
        responseDiv.classList.add('feedback-response-visible');
      }, 100);
    }
    
    if (yesBtn) {
      yesBtn.addEventListener('click', () => handleFeedback(true));
    }
    
    if (noBtn) {
      noBtn.addEventListener('click', () => handleFeedback(false));
    }
  });
});