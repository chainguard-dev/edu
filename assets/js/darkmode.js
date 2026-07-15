const themeButtons = document.getElementsByClassName("bottom-mode");

function applyTheme(dark) {
  if (dark) {
    document.documentElement.setAttribute("data-dark-mode", "");
    document.documentElement.setAttribute("data-theme", "dark");
  } else {
    document.documentElement.removeAttribute("data-dark-mode");
    document.documentElement.removeAttribute("data-theme");
  }
}

if (themeButtons.length !== 0) {
  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", (event) => {
      localStorage.setItem("theme", event.matches ? "dark" : "light");
      applyTheme(event.matches);
    });

  for (const themeButton of themeButtons) {
    themeButton.addEventListener("click", () => {
      const dark = !document.documentElement.hasAttribute("data-dark-mode");
      applyTheme(dark);
      localStorage.setItem("theme", dark ? "dark" : "light");
    });
  }

  const storedTheme = localStorage.getItem("theme");
  applyTheme(
    storedTheme
      ? storedTheme === "dark"
      : window.matchMedia("(prefers-color-scheme: dark)").matches
  );
}

if (
  window.location.search &&
  window.location.search.includes("forcedarkmode=true")
) {
  applyTheme(true);
}

document.documentElement.setAttribute("mode-loaded", "");
