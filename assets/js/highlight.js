import hljs from "highlight.js/lib/core";

import bash from "highlight.js/lib/languages/bash";
import go from "highlight.js/lib/languages/go";
import ini from "highlight.js/lib/languages/ini";
import javascript from "highlight.js/lib/languages/javascript";
import json from "highlight.js/lib/languages/json";
import markdown from "highlight.js/lib/languages/markdown";
import php from "highlight.js/lib/languages/php";
import python from "highlight.js/lib/languages/python";
import shell from "highlight.js/lib/languages/shell";
import yaml from "highlight.js/lib/languages/yaml";

hljs.registerLanguage("javascript", javascript);
hljs.registerLanguage("json", json);
hljs.registerLanguage("bash", bash);
hljs.registerLanguage("ini", ini);
hljs.registerLanguage("toml", ini);
hljs.registerLanguage("yaml", yaml);
hljs.registerLanguage("md", markdown);
hljs.registerLanguage("shell", shell);
hljs.registerLanguage("php", php);
hljs.registerLanguage("python", python);
hljs.registerLanguage("go", go);

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre code").forEach((block) => {
    hljs.highlightElement(block);
  });
});
