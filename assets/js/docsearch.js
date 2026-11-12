import docsearch from "@docsearch/js/docsearch";

docsearch({
  container: "#docsearch",
  appId: "P6WD6RQSFQ",
  indices: ["chainguard"],
  apiKey: "9846ce061788834124713a47b1cfd2f7",
});

function openDocSearch() {
  const btn = document.querySelector(".DocSearch-Button");
  if (btn) btn.click();
}

document.addEventListener("DOMContentLoaded", () => {
  const triggers = document.getElementsByClassName("is-search");
  for (const trigger of triggers) {
    trigger.addEventListener("click", openDocSearch);
  }
});
