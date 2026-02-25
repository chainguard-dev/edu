import docsearch from "@docsearch/js";

docsearch({
  container: "#docsearch",
  appId: "P6WD6RQSFQ",          
  indexName: "chainguard",  
  apiKey: "9846ce061788834124713a47b1cfd2f7", // the Search-Only key (not admin)
  insights: true,
});

const onClick = function () {
  document.getElementsByClassName("DocSearch-Button")[0].click();
};

document.getElementById("searchToggleMobile").onclick = onClick;
document.getElementById("searchToggleDesktop").onclick = onClick;