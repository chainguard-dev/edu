let now = new Date().getTime();
let interval = null;
const end = now + 1000 * 60 * 60;

function timer() {
  const t = end - now;
  now = now + 1000;
  if (t === 1000 * 60 * 5) {
    // 5 minutes, 300 seconds
    alert("Terminal will close in 5 minutes");
  }
  if (t <= 0) {
    window.clearInterval(interval);
    window.terminal.exit();
    alert("Terminal closed after 1 hour");
  }
}

(function () {
  window.terminal = this;
  window.terminal.load = () => {
    const t = document.getElementById("terminal-init");
    const image = t.attributes.getNamedItem("data-image").nodeValue;
    const color_scheme = localStorage.getItem("theme") || "dark";
    const bg_light = "background: white;";
    const bg_dark = "background: #0E0E0E;";
    const bg = color_scheme === "dark" ? bg_dark : bg_light;

    const iframe = `<div id="terminal-container"><iframe id="terminal" frameBorder="0" rel="opener" src="https://terminal.inky.wtf/?image=${image}&color-scheme=${color_scheme}" style="${bg}"></iframe></div>`;
    t.insertAdjacentHTML("afterend", iframe);
    document
      .getElementById("close-button")
      .addEventListener("click", window.terminal.exit);

    const container = document.getElementById("terminal-container");
    if (container) {
      container.addEventListener("mouseenter", () => {
        if (window.gtag) {
          window.gtag("event", "terminal-mouseenter");
        }
      });
    }

    interval = window.setInterval(timer, 1000);
  };

  window.terminal.exit = () => {
    if (window.gtag) {
      window.gtag("event", "terminal-close");
    }

    document.getElementById("terminal-init").remove();
    document.getElementById("terminal-container").remove();
    document.getElementById("terminal-nav").remove();
    document.querySelector(".terminal").remove();
    document.querySelector("footer").style.marginBottom = 0;
    window.clearInterval(interval);
  };
})();

document.addEventListener("DOMContentLoaded", async () => {
  const response = await fetch(
    "https://storage.googleapis.com/chainguard-academy/terminal/status.json"
  );
  const status = await response.json();
  if (status.enabled == false) {
    return;
  }

  document.querySelector(".terminal-top-container").style.display = "flex";

  window.terminal.load();
  // For resizing
  const resizable = document.querySelector(".resizable");
  window
    .interact(".resizable")
    .resizable({
      edges: {
        left: false,
        right: false,
        bottom: false,
        top: ".grab-container",
      },
      invert: "none",
      modifiers: [
        window.interact.modifiers.restrictSize({
          min: { width: 0, height: resizable.getBoundingClientRect().height },
        }),
      ],
    })
    .on("resizestart", function (event) {
      event.target.classList.add("moving");
    })
    .on("resizemove", function (event) {
      var handlerEl = event.target.querySelector(".resizable-handler"),
        y = parseFloat(handlerEl.getAttribute("data-y")) || 0;
      y += event.deltaRect.top;
      handlerEl.setAttribute("data-y", y);
      handlerEl.style.transform = "translateY(" + y + "px)";
    })
    .on("resizeend", function (event) {
      const target = event.target;
      const handlerEl = target.querySelector(".resizable-handler");
      target.classList.remove("moving");
      target.style.height = event.rect.height + "px";
      handlerEl.setAttribute("data-y", 0);
      handlerEl.style.transform = "none";
    });
});
