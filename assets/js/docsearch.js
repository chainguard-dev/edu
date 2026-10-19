import docsearch from "@docsearch/js/docsearch";
import * as params from "@params";

// The search index stores edu.chainguard.dev URLs. When the docs are served
// under a base path, such as www.chainguard.dev/docs/, rewrite each result to
// the same page under that path, so results stay on the site being browsed.
// With the production base path, "/", results are left as they are.
const INDEXED_SITE = "https://edu.chainguard.dev/";
const basePath = params.basePath;

function toSitePath(url) {
  if (basePath === "/" || !url || !url.startsWith(INDEXED_SITE)) {
    return url;
  }
  return basePath + url.slice(INDEXED_SITE.length);
}

docsearch({
  container: "#docsearch",
  appId: "P6WD6RQSFQ",
  indices: ["chainguard"],
  apiKey: "9846ce061788834124713a47b1cfd2f7",
  transformItems(items) {
    return items.map((item) => ({
      ...item,
      url: toSitePath(item.url),
      url_without_anchor: toSitePath(item.url_without_anchor),
    }));
  },
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
