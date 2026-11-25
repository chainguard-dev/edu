#!/bin/sh
# Build the site for the two Vercel projects that deploy this repository:
# chainguard-docs-preview, which builds every branch for review (DOCS-133), and
# chainguard-docs, which builds main for www.chainguard.dev/docs.
#
# Mirrors the production build in .github/workflows/cloud-run.yaml, then sets
# the base URL each project serves the site from. Canonical links, sitemaps,
# and redirects are built from it, so the wrong base URL sends readers and
# search engines to the wrong host.
set -eu

# Anchor to the repo root so the paths below hold wherever this is invoked
# from, and put the local hugo binary on PATH. hugo-extended is a devDependency,
# so `npm run` finds it and a direct run of this script otherwise would not.
cd "$(dirname "$0")/.."
PATH="$PWD/node_modules/.bin:$PATH"

# Refresh the dfc package mappings the way the production workflow does.
curl -sfL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
  -o data/package-mappings.yaml

# A preview is served from its own branch host, but a production deployment is
# served from the project's production domain. Using the branch host for both
# made every page on the production domain fetch its CSS cross-origin, which
# worked only because Vercel sends "access-control-allow-origin: *".
#
# Both variables require "Enable access to System Environment Variables" in the
# project settings. Fail loudly if it is off: the alternative is a silent build
# whose every canonical link and alias reads "https://".
#
# The chainguard-docs production project sets DOCS_PRODUCTION_BASE_URL to
# https://www.chainguard.dev/docs/, the address www.chainguard.dev serves these
# files at through a rewrite. Only that build:
#   - leaves out future-dated pages, as the edu.chainguard.dev build does
#   - lets search engines index it (HUGO_PARAMS_INDEXABLE, read by
#     layouts/index.vercelconfig.json; every other build sends noindex)
#
# A preview is built the way production is, under /docs/ and without trailing
# slashes, so it shows problems that appear only there, such as a file loaded
# from the host root. Nothing sits in front of a preview the way www sits in
# front of production, so a preview serves its files under /docs/ itself, and
# HUGO_PARAMS_EMULATEWWW adjusts its routes to match
# (see layouts/index.vercelconfig.json).
if [ -n "${DOCS_PRODUCTION_BASE_URL:-}" ]; then
  HUGO_PARAMS_INDEXABLE=true hugo --gc --minify -b "$DOCS_PRODUCTION_BASE_URL"
  node scripts/strip-trailing-slashes.mjs public "$DOCS_PRODUCTION_BASE_URL"
  static_dir=.vercel/output/static
else
  if [ "${VERCEL_ENV:-}" = "production" ]; then
    host="${VERCEL_PROJECT_PRODUCTION_URL:?not set - enable System Environment Variables in the Vercel project}"
  else
    host="${VERCEL_BRANCH_URL:?not set - enable System Environment Variables in the Vercel project}"
  fi
  HUGO_PARAMS_EMULATEWWW=true hugo --gc --minify --buildFuture -b "https://$host/docs/"
  node scripts/strip-trailing-slashes.mjs public "https://$host/docs/"
  static_dir=.vercel/output/static/docs
fi

# Publish through Vercel's Build Output API, whose config.json carries the
# routing table Hugo generated from the same redirect rules production nginx
# uses (layouts/index.vercelconfig.json). When .vercel/output exists after the
# build, Vercel serves it and ignores the project's Output Directory setting.
rm -rf .vercel/output
mkdir -p "$(dirname "$static_dir")"
mv public/vercel-config.json .vercel/output/config.json
mv public "$static_dir"

# Vercel serves the 404 page from the root of the output, so a preview, whose
# files are under /docs/, needs a copy there.
if [ "$static_dir" != .vercel/output/static ]; then
  cp "$static_dir/404.html" .vercel/output/static/404.html
fi
