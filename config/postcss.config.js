const autoprefixer = require("autoprefixer");
const purgecss = require("@fullhuman/postcss-purgecss");

module.exports = {
  plugins: [
    autoprefixer(),
    purgecss({
      // Keep aria-selected (used by DocSearch dropdown)
      dynamicAttributes: [
        "aria-selected",
        "data-theme",
        "data-dark-mode",
        "mode-loaded",
      ],
      content: [
        "./layouts/**/*.html",
        "./content/**/*.md",
        // Runtime classes; new Bootstrap components need their js/src file here
        "./assets/js/*.js",
        "./node_modules/bootstrap/js/src/alert.js",
        "./node_modules/bootstrap/js/src/collapse.js",
        "./node_modules/bootstrap/js/src/dropdown.js",
        "./node_modules/bootstrap/js/src/offcanvas.js",
      ],
      // PurgeCSS's HTML parser misses classes inside Hugo template syntax
      extractors: [
        {
          extractor: (content) => content.match(/[A-Za-z0-9_-]+/g) || [],
          extensions: ["html", "md", "js"],
        },
      ],
      safelist: [
        // Changelog type-tag color classes are generated from a shortcode
        // ({{< changelog-label >}}), so the modifier names never appear as
        // literals in scanned content. Keep them all.
        /^changelog-label/,
        "lazyloaded",
        "table",
        "thead",
        "tbody",
        "tr",
        "th",
        "td",
        "h5",
        "alert-link",
        "container-xxl",
        "container-fluid",
        // Absent from scanned content; keeps dropdown styles from being purged
        "dropdown-menu-main",
        "dropdown-toggle",
        // Pagination markup comes from Hugo's embedded template, not layouts
        "page-item",
        "page-link",
      ],
    }),
  ],
}
