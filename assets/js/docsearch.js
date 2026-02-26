import docsearch from "@docsearch/js";

docsearch({
  container: "#docsearch",
  appId: "P6WD6RQSFQ",
  indexName: "chainguard",
  apiKey: "9846ce061788834124713a47b1cfd2f7",
});

function openDocSearch() {
  const btn = document.querySelector(".DocSearch-Button");
  if (btn) btn.click();
}

document.addEventListener("DOMContentLoaded", () => {
  const trigger = document.getElementById("searchToggleDesktop");
  if (trigger) trigger.addEventListener("click", openDocSearch);
});