import mermaid from "mermaid";

var config = {
  theme: "default",
};

document.addEventListener("DOMContentLoaded", () => {
  mermaid.initialize(config);
  mermaid.init(undefined, ".language-mermaid");
});
