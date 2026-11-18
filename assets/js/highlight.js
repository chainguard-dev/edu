import hljs from "highlight.js/lib/core";

import bash from "highlight.js/lib/languages/bash";
import diff from "highlight.js/lib/languages/diff";
import dockerfile from "highlight.js/lib/languages/dockerfile";
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
hljs.registerLanguage("diff", diff);
hljs.registerLanguage("dockerfile", dockerfile);
hljs.registerLanguage("ini", ini);
hljs.registerLanguage("toml", ini);
hljs.registerLanguage("yaml", yaml);
hljs.registerLanguage("md", markdown);
hljs.registerLanguage("shell", shell);
hljs.registerLanguage("php", php);
hljs.registerLanguage("python", python);
hljs.registerLanguage("go", go);

// Placeholders: Hugo renders <^>NAME<^> as <var class="placeholder">NAME</var>
// (layouts/partials/placeholders/render.html). highlightElement() rebuilds a
// block from its text, which drops those elements, so this plugin swaps each
// one for sentinel characters before highlighting and wraps the text between
// them in a new <var> afterward. The sentinels are Unicode private-use
// characters, which don't appear in code samples.
const PLACEHOLDER_START = "";
const PLACEHOLDER_END = "";

function restorePlaceholders(el) {
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
  const marks = [];
  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    for (let offset = 0; offset < node.data.length; offset++) {
      const char = node.data[offset];
      if (char === PLACEHOLDER_START || char === PLACEHOLDER_END) {
        marks.push({ node, offset, char });
      }
    }
  }

  const pairs = [];
  for (let i = 0; i + 1 < marks.length; i++) {
    if (marks[i].char === PLACEHOLDER_START && marks[i + 1].char === PLACEHOLDER_END) {
      pairs.push([marks[i], marks[i + 1]]);
      i++;
    }
  }

  // Work from the last pair to the first, so that splitting text nodes
  // doesn't move the positions of pairs that haven't been handled yet.
  for (let i = pairs.length - 1; i >= 0; i--) {
    const [start, end] = pairs[i];
    end.node.deleteData(end.offset, 1);
    const range = document.createRange();
    range.setStart(start.node, start.offset + 1);
    range.setEnd(end.node, end.offset);
    const placeholder = document.createElement("var");
    placeholder.className = "placeholder";
    placeholder.append(range.extractContents());
    range.insertNode(placeholder);
    start.node.deleteData(start.offset, 1);
  }
}

hljs.addPlugin({
  "before:highlightElement": ({ el, language }) => {
    // highlight.js doesn't highlight a language that isn't registered, and
    // the after hook doesn't run for it, so leave those blocks as Hugo
    // rendered them.
    if (language && !hljs.getLanguage(language)) return;
    el.querySelectorAll("var.placeholder").forEach((placeholder) => {
      placeholder.replaceWith(PLACEHOLDER_START + placeholder.textContent + PLACEHOLDER_END);
    });
  },
  "after:highlightElement": ({ el }) => restorePlaceholders(el),
});

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre code").forEach((block) => {
    hljs.highlightElement(block);
  });
});
