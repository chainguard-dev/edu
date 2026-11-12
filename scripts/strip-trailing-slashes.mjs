// Rewrites a built site so its page URLs have no trailing slash
// (/docs/page instead of /docs/page/), matching the rest of www.chainguard.dev.
// scripts/build-vercel.sh runs it for the chainguard-docs production project.
// The files stay where Hugo wrote them: Vercel serves a directory's index.html
// at the slash-free URL.
//
// In every built file it:
//   1. Resolves page-relative src and href values (a bundle image such as
//      src="diagram.png") to root paths, because without the trailing slash a
//      browser would resolve them against the parent directory.
//   2. Removes the trailing slash from page URLs under the base path, both
//      root paths (/docs/page/) and absolute URLs (https://www.../docs/page/).
//      File URLs, such as /docs/page/index.md, don't end in "/" and keep their
//      form. The home page becomes /docs.
//   3. Removes the trailing slash from redirect targets in config.json, drops
//      the route that adds one, and keeps alias routes from capturing it.
//
// Usage: node scripts/strip-trailing-slashes.mjs <output dir> <base URL>
//   for example: node scripts/strip-trailing-slashes.mjs public https://www.chainguard.dev/docs/

import console from "node:console";
import { readdirSync, readFileSync, writeFileSync, statSync } from "node:fs";
import { join, relative, sep } from "node:path";
import process from "node:process";
import { URL } from "node:url";

const [outputDir, baseUrl] = process.argv.slice(2);
if (!outputDir || !baseUrl) {
  console.error("usage: strip-trailing-slashes.mjs <output dir> <base URL>");
  process.exit(2);
}

const base = new URL(baseUrl);
const basePath = base.pathname; // "/docs/"
// The patterns below treat the base path as a prefix that every page URL
// starts with. A base URL at the root of its host has none, so the home page
// pattern would match every "/" and empty out links to it.
if (basePath === "/") {
  console.error(`strip-trailing-slashes: base URL ${baseUrl} has no path; expected one such as https://www.chainguard.dev/docs/`);
  process.exit(2);
}
const siteOrigin = base.origin; // "https://www.chainguard.dev"
const textExtensions = [".html", ".xml", ".txt", ".md", ".json"];

function escapeRegex(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

// A page URL under the base path that ends in "/", optionally followed by a
// query or fragment. Group 1 is the URL without its trailing slash.
const pageUrl = new RegExp(
  `((?:${escapeRegex(siteOrigin)})?${escapeRegex(basePath)}(?:[^\\s"'<>()#?]*[^\\s"'<>()#?/])?)/(?=[#?"'\\s<>)]|$)`,
  "g",
);

// The home page itself, /docs/ or https://www.../docs/, followed by a
// delimiter. Group 1 is the URL without its trailing slash.
const homeUrl = new RegExp(
  `((?:${escapeRegex(siteOrigin)})?${escapeRegex(basePath.slice(0, -1))})/(?=[#?"'\\s<>)]|$)`,
  "g",
);

function stripPageSlashes(text) {
  // A URL that ends in "/" is always a page, even when its name has a dot
  // (openssl-3.6/). File URLs such as index.md never end in "/".
  return text.replace(pageUrl, "$1").replace(homeUrl, "$1");
}

// An HTML start tag, and a src or href attribute inside one. Matching only
// inside tags leaves inline JavaScript such as a.href=url alone. Hugo minifies
// HTML, so attribute values may be unquoted.
const startTag = /<[a-z][^<>]*>/gi;
const relativeAttribute = /(\s)(src|href)=("?)([^"\s>]+)\3/g;

function isPageRelative(value) {
  return !/^(\/|#|\?|[a-z][a-z0-9+.-]*:|\{)/i.test(value);
}

function resolveRelativeAttributes(html, pageDirectory) {
  return html.replace(startTag, (tag) =>
    tag.replace(relativeAttribute, (match, space, attribute, quote, value) => {
      if (!isPageRelative(value)) {
        return match;
      }
      const resolved = new URL(value, `https://placeholder${pageDirectory}`).pathname;
      return `${space}${attribute}=${quote}${resolved}${quote}`;
    }),
  );
}

function listFiles(directory) {
  const files = [];
  for (const name of readdirSync(directory)) {
    const path = join(directory, name);
    if (statSync(path).isDirectory()) {
      files.push(...listFiles(path));
    } else {
      files.push(path);
    }
  }
  return files;
}

let changedFiles = 0;
for (const file of listFiles(outputDir)) {
  if (!textExtensions.some((extension) => file.endsWith(extension))) {
    continue;
  }
  const original = readFileSync(file, "utf8");
  let text = original;

  if (file.endsWith(".html")) {
    // The directory URL this page is served at, such as /docs/chainguard/x/.
    const relativeDir = relative(outputDir, join(file, "..")).split(sep).join("/");
    const pageDirectory = basePath + (relativeDir ? `${relativeDir}/` : "");
    text = resolveRelativeAttributes(text, pageDirectory);
  }

  if (file.endsWith("config.json")) {
    // Drop the route that adds a trailing slash, then drop the trailing slash
    // from any other redirect target that has no capture group after it.
    const config = JSON.parse(text);
    const addSlashLocation = `${basePath.slice(0, -1)}$1/`;
    config.routes = config.routes.filter(
      (route) => route.headers?.Location !== addSlashLocation,
    );
    for (const route of config.routes) {
      // An alias route matches ^/alias(/.*)?$ and redirects to <target>$1. The
      // proxy adds a trailing slash, so $1 would carry it into the target.
      // Capture the child path without a trailing slash instead.
      if (route.src?.endsWith("(/.*)?$")) {
        route.src = route.src.replace(/\(\/\.\*\)\?\$$/, "(/.+?)?/?$");
      }
      const location = route.headers?.Location;
      if (location && location.length > 1 && location.endsWith("/")) {
        route.headers.Location = location.slice(0, -1);
      }
      // Strip page URLs in the redirect target only. A route's src is a
      // pattern, not a URL: on a preview it starts with the base path, and
      // removing the "/" before "?" in ^/docs/page/?$ would make the page
      // name's last letter optional.
      if (route.headers?.Location) {
        route.headers.Location = stripPageSlashes(route.headers.Location);
      }
    }
    text = JSON.stringify(config, null, 2);
  } else {
    text = stripPageSlashes(text);
  }

  if (text !== original) {
    writeFileSync(file, text);
    changedFiles += 1;
  }
}
console.log(`strip-trailing-slashes: rewrote ${changedFiles} files under ${outputDir}`);
