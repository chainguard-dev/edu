import { createApiReference } from "@scalar/api-reference";

const appEl = document.getElementById("app");
if (appEl && appEl.dataset.specUrl) {
  createApiReference("#app", {
    agent: {
      disabled: true,
    },
    mcp: {
      disabled: true,
    },
    hideSearch: true,
    telemetry: false,
    showDeveloperTools: "never",
    hideClientButton: true,
    hideTestRequestButton: true,
    hiddenClients: true,
    hideDarkModeToggle: true,
    darkMode: localStorage.getItem("theme") === "dark",
    theme: "none",
    withDefaultFonts: false,
    url: appEl.dataset.specUrl,
  });
}
