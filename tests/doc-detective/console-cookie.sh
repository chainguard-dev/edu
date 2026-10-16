#!/usr/bin/env bash
# Runs Doc Detective with a Chainguard Console session. Tests sign in by
# loading the chainguard-session cookie from $CHAINGUARD_SESSION_COOKIE
# instead of logging in. The token stays in this process's environment and is
# never written to disk.
#
# $CHAINGUARD_CONSENT_COOKIE holds OneTrust's OptanonAlertBoxClosed cookie,
# which marks the cookie banner as answered. The banner appears only
# sometimes, so tests load this cookie instead of clicking Reject All.
#
# Run from anywhere in the repo. Arguments go to Doc Detective; with none, it
# runs console-cookie.spec.json:
#   tests/doc-detective/console-cookie.sh
#   tests/doc-detective/console-cookie.sh --input tests/doc-detective/cve-visualizations.spec.json
#
# When --input is a Markdown page or a JSON spec file, each test in it runs in
# its own Doc Detective process. Doc Detective reuses one browser for every test in a run,
# and on Console pages a test that follows another can find its chart data
# requests failing. The Console doesn't retry them, and Doc Detective's find
# then waits past its timeout. A fresh process per test avoids both.
#
# The token comes from `chainctl auth token`. Set CHAINGUARD_TOKEN_COMMAND to
# use another source.
#
# Each Doc Detective process stops after DOC_DETECTIVE_MAX_SECONDS
# (default 120, about three times the slowest test), in case a step stalls
# anyway. A test that fails or stops runs again in a fresh process, up to
# DOC_DETECTIVE_RETRIES more times (default 1). The summary marks tests that passed only on a retry, so
# flaky tests stay visible.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
repo="$(git -C "$here" rev-parse --show-toplevel)"

token="$(${CHAINGUARD_TOKEN_COMMAND:-chainctl auth token})"

# Print the claims that decide whether the Console accepts the token, but not
# the token itself.
python3 - "$token" <<'PY'
import base64, json, sys, time
payload = sys.argv[1].split(".")[1]
claims = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
print("iss:", claims.get("iss"))
print("aud:", claims.get("aud"))
print("sub:", claims.get("sub"))
print("email present:", "email" in claims)
print("expires in:", int(claims.get("exp", 0) - time.time()), "seconds")
PY

CHAINGUARD_SESSION_COOKIE="$(python3 -c '
import json, sys
print(json.dumps({
    "name": "chainguard-session",
    "value": sys.argv[1],
    "domain": ".chainguard.dev",
    "path": "/",
    "secure": True,
    "sameSite": "Strict",
}))' "$token")"
export CHAINGUARD_SESSION_COOKIE

CHAINGUARD_CONSENT_COOKIE="$(python3 -c '
import datetime, json
print(json.dumps({
    "name": "OptanonAlertBoxClosed",
    "value": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    "domain": ".chainguard.dev",
    "path": "/",
    "secure": True,
    "sameSite": "Lax",
}))')"
export CHAINGUARD_CONSENT_COOKIE

if [ "$#" -eq 0 ]; then
  set -- --input "$here/console-cookie.spec.json"
fi

max_seconds="${DOC_DETECTIVE_MAX_SECONDS:-120}"
retries="${DOC_DETECTIVE_RETRIES:-1}"

# Runs one Doc Detective process and prints nothing extra. Returns its exit
# status, or 124 if it ran out of time.
run_doc_detective() {
  local status=0
  timeout --kill-after=10 "$max_seconds" \
    npx --yes doc-detective@4.38.1 --config .doc-detective.json "$@" || status=$?
  if [ "$status" -eq 124 ] || [ "$status" -eq 137 ]; then
    echo "Doc Detective ran longer than ${max_seconds}s and was stopped." >&2
    # Its browser and Appium processes outlive the killed npx.
    pkill -f '[/]tmp/doc-detective/browsers/' || true
    pkill -f '[d]oc-detective/runtime/node_modules/appium' || true
    status=124
  fi
  return "$status"
}

# Find a page or spec --input; every other argument passes through unchanged.
page=""
passthrough=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --input | -i)
      if [[ "${2:-}" == *.md || "${2:-}" == *.json ]]; then
        page="$2"
        shift 2
        continue
      fi
      ;;
  esac
  passthrough+=("$1")
  shift
done

if [ -n "$page" ]; then
  page="$(realpath "$page")"
fi
cd "$repo"

if [ -z "$page" ]; then
  run_doc_detective "${passthrough[@]}"
  exit
fi

specs_dir="$(mktemp -d)"
trap 'rm -rf "$specs_dir"' EXIT
mapfile -t specs < <(python3 "$here/split-tests.py" "$page" "$specs_dir")
if [ "${#specs[@]}" -eq 0 ]; then
  echo "No Doc Detective tests found in $page." >&2
  exit 1
fi

summary=()
overall=0
for spec in "${specs[@]}"; do
  name="$(basename "$spec" .spec.json)"
  attempt=0
  while :; do
    attempt=$((attempt + 1))
    echo "===== ${name#??-} (attempt $attempt)"
    status=0
    started=$SECONDS
    run_doc_detective --input "$spec" "${passthrough[@]}" || status=$?
    elapsed=$((SECONDS - started))
    if [ "$status" -eq 0 ] || [ "$attempt" -gt "$retries" ]; then
      break
    fi
  done
  case "$status" in
    0) result="PASS" ;;
    124) result="STOPPED after ${max_seconds}s" ;;
    *) result="FAIL" ;;
  esac
  if [ "$attempt" -gt 1 ]; then
    result="$result on attempt $attempt"
  fi
  summary+=("$result (${elapsed}s)  ${name#??-}")
  if [ "$status" -ne 0 ]; then
    overall=1
  fi
done

echo
echo "===== Results for ${page#"$repo"/}"
printf '%s\n' "${summary[@]}"
exit "$overall"
