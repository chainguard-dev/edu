const autoprefixer = require("autoprefixer");
const purgecss = require("@fullhuman/postcss-purgecss");
const whitelister = require("purgecss-whitelister");

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
        ...whitelister([
          "./assets/scss/*.scss",
          "./assets/scss/common/*.scss",
          "./assets/scss/components/*.scss",
          // Excluded to keep the purged CSS unchanged
          "!./assets/scss/common/_fonts.scss",
          "!./assets/scss/common/_global.scss",
          "!./assets/scss/components/_comments.scss",
          "!./assets/scss/components/_details.scss",
          "!./assets/scss/components/_forms.scss",
          "!./assets/scss/components/_images.scss",
          "!./assets/scss/components/_mermaid.scss",
          "!./assets/scss/components/_tables.scss",
          "./node_modules/@docsearch/css/dist/modal.css",
        ]),
      ],
    }),
  ],
}
