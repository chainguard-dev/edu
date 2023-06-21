document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("h2, .page-links a").forEach((h2) => {
    const match = /Step (\d+) [—–]/.exec(h2.innerHTML);
    if (match) {
      h2.innerHTML = `<div class="step-container">${h2.innerHTML.replace(
        match[0],
        `<span class="step">${match[1]}</span>`
      )}</div>`;
    }
  });
});
