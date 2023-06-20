const themeButtons = document.getElementsByClassName("bottom-mode");

if (themeButtons.length !== 0) {
  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", (event) => {
      if (event.matches) {
        localStorage.setItem("theme", "dark");
        document.documentElement.setAttribute("data-dark-mode", "");
      } else {
        localStorage.setItem("theme", "light");
        document.documentElement.removeAttribute("data-dark-mode");
      }
    });

  for (const themeButton of themeButtons) {
    themeButton.addEventListener("click", () => {
      document.documentElement.toggleAttribute("data-dark-mode");
      localStorage.setItem(
        "theme",
        document.documentElement.hasAttribute("data-dark-mode")
          ? "dark"
          : "light"
      );
    });
  }

  if (localStorage.getItem("theme") === "dark") {
    document.documentElement.setAttribute("data-dark-mode", "");
  } else {
    document.documentElement.removeAttribute("data-dark-mode");
  }
}

if (
  window.location.search &&
  window.location.search.includes("forcedarkmode=true")
) {
  document.documentElement.setAttribute("data-dark-mode", "");
}

document.documentElement.setAttribute("mode-loaded", "");
