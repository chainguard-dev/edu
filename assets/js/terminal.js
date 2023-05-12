let now = new Date().getTime();
let interval = null;
const end = now + (1000 * 60 * 60);

function timer () {
  const t = end - now;
  const minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
  document.getElementById('timer').innerHTML = minutes + 'm remaining';
  now = now + 1000;
  if (t === 1000 * 60 * 5) { // 5 minutes, 300 seconds
    alert('Terminal will close in 5 minutes');
  }
  if (t <= 0) {
    window.clearInterval(interval);
    window.terminal.exit();
    alert('Terminal closed after 1 hour');
  }
}

(function () {
  window.terminal = this;
  window.terminal.load = () => {
    const t = document.getElementById('terminal-init');
    const image = t.attributes.getNamedItem('data-image').nodeValue;
    const color_scheme = localStorage.getItem("theme") || "dark";
    const bg_light = "background: white;"
    const bg_dark = "background: #0E0E0E;"
    let bg = new String;
    if (color_scheme == "dark") {
      bg = bg_dark;
    } else {
      bg = bg_light;
    }
    const iframe = `<div id="terminal-container"><iframe id="terminal" frameBorder="0" rel="opener" src="https://terminal.inky.wtf/?image=${image}&color-scheme=${color_scheme}" style="${bg}"></iframe></div>`;
    t.insertAdjacentHTML('afterend', iframe);
    document.getElementById('close-button').addEventListener('click', window.terminal.exit);
    interval = window.setInterval(timer, 1000);
  }

  window.terminal.exit = () => {
    document.getElementById('terminal-init').remove();
    document.getElementById('terminal-container').remove();
    document.getElementById('terminal-nav').remove();
    document.querySelector('footer').style.marginBottom = 0;
    window.clearInterval(interval);
  }
})();

window.terminal.load();
