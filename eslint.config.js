// Copyright 2026 Chainguard, Inc.
// SPDX-License-Identifier: Apache-2.0

// Flat config (ESLint 9+). Migrated from the legacy .eslintrc.json; rules are
// kept equivalent. Lints the theme's own JavaScript under assets/js and config.
const js = require("@eslint/js");
const globals = require("globals");

module.exports = [
  // Ignores replace the former .eslintignore.
  {
    ignores: [
      "**/*.min.js",
      "assets/js/index.js",
      "assets/js/katex.js",
      "assets/js/vendor/**",
      "node_modules/**",
    ],
  },
  js.configs.recommended,
  {
    files: ["assets/js/**/*.js", "config/**/*.js"],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: "module",
      globals: {
        ...globals.browser,
        ...globals.node,
        Atomics: "readonly",
        SharedArrayBuffer: "readonly",
      },
    },
    rules: {
      "no-console": "off",
      quotes: ["error", "double"],
      "comma-dangle": [
        "error",
        {
          arrays: "always-multiline",
          objects: "always-multiline",
          imports: "always-multiline",
          exports: "always-multiline",
          functions: "ignore",
        },
      ],
    },
  },
];
