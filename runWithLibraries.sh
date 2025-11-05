#!/bin/bash
set -efo pipefail

# deleting the lock file actually cause the site to not work even without using libraries
# some dependency update breaks it
#rm package-lock.json || true 
rm -rf node_modules || true
rm .npmrc || true
echo "Clean up done"

# Direct access
#source ~/.env
#npm config set registry https://libraries.cgr.dev/javascript/ --location=project
#export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64)
#npm config set //libraries.cgr.dev/javascript/:_auth "${token}" --location=project

# Local Nexus
#npm config set registry http://localhost:8081/repository/javascript-chainguard/ --location=project
npm config set registry http://localhost:8081/repository/javascript-all/ --location=project

npm install --verbose
npm run start
