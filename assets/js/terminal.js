var now = new Date().getTime();
var end = now + (1000 * 60 * 60);
var interval = null;

function timer() {
  var t = end - now;
  var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((t % (1000 * 60)) / 1000);
  document.getElementById('timer').innerHTML = minutes + 'm ' + seconds + 's ';
  now = now + 1000;
  if (t == 1000 * 60 * 5) { // 5 minutes, 300 seconds
    alert('Terminal will close in 5 minutes')
  }
  if (t <= 0) {
    window.clearInterval(interval);
    alert('Terminal closed after 1 hour');
    window.terminal.exit();
  }
}

(function () {
  window.terminal = this;

  window.terminal.load = () => {
    let t = document.getElementById('terminal-init'),
      image = t.attributes.getNamedItem('data-image').nodeValue,
      iframe = `<div id="terminal-container"><iframe id="terminal" frameBorder="0" rel="opener" src="https://terminal.inky.wtf/?image=${image}"></iframe></div>`;
    t.insertAdjacentHTML('afterend', iframe);
    interval = window.setInterval(timer, 1000);
  };

  window.terminal.exit = () => {
    document.getElementById('terminal-container').remove();
    document.getElementById('terminal-nav').remove();
  };

})();

window.terminal.load();
