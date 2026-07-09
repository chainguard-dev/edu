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
      ecmaVersion: 2022,
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
  {
    // The rumble scripts are concatenated at build time (Hugo resources.Concat
    // of base.js + comparison.js / vulnerability.js), so symbols defined in one
    // fragment are referenced from another. eslint lints each file in isolation
    // and cannot see that, so disable the cross-file rules for these fragments.
    files: ["assets/js/rumble/**/*.js"],
    rules: {
      "no-unused-vars": "off",
      "no-undef": "off",
    },
  },
];
