#!/bin/sh
# Build the site for the chainguard-docs-preview Vercel project (DOCS-133).
#
# Mirrors the production build in .github/workflows/cloud-run.yaml, then points
# Hugo at the host this deployment is actually served from. Hugo writes the main
# stylesheet as an absolute URL, so the wrong base URL gives an unstyled site
# rather than an obviously broken one.
set -eu

# Anchor to the repo root so the paths below hold wherever this is invoked
# from, and put the local hugo binary on PATH. hugo-extended is a devDependency,
# so `npm run` finds it and a direct run of this script otherwise would not.
cd "$(dirname "$0")/.."
PATH="$PWD/node_modules/.bin:$PATH"

# Refresh the dfc package mappings the way the production workflow does.
# Netlify builds from the committed copy instead.
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
if [ "${VERCEL_ENV:-}" = "production" ]; then
  host="${VERCEL_PROJECT_PRODUCTION_URL:?not set - enable System Environment Variables in the Vercel project}"
else
  host="${VERCEL_BRANCH_URL:?not set - enable System Environment Variables in the Vercel project}"
fi

hugo --gc --minify --buildFuture -b "https://$host"
