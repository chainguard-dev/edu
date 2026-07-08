---
title: "Automating with chainctl"
linktitle: "Automating chainctl"
type: "article"
lead: "Practical shell and CI/CD snippets for using chainctl beyond the interactive command line."
description: "Learn how to use chainctl in scripts and pipelines with a set of example snippets"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
draft: false
tags: ["chainctl"]
images: []
menu:
  docs:
    parent: "chainctl-usage"
weight: 100
toc: true
---

`chainctl` works well at the command line for interactive use, but it is equally suited to automation. Most `chainctl` commands accept an `--output=json` flag, which lets you pipe their output to `jq` and build reliable scripting patterns around the results.

This page collects practical snippets you can adapt for shell scripts, scheduled jobs, and CI/CD pipelines. Each snippet is a self-contained building block; combine them to fit your workflow.

{{< note >}}
The `jq` field names used in these examples reflect the expected JSON output structure. Run `chainctl <command> --output=json | jq '.'` to inspect the exact structure for your version of chainctl.
{{< /note >}}

## Prerequisites

Before running any of these snippets, you need:

- `chainctl` [installed](/chainguard/chainctl-usage/how-to-install-chainctl/)
- An active [Chainguard account](/chainguard/chainguard-registry/authenticating/)
- `jq` installed (`brew install jq` or `apt install jq`)
- For CI/CD use, a [Chainguard assumable identity](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/) configured for your pipeline

Many `chainctl` commands drop into an interactive selection menu when run without enough arguments. In scripts and pipelines, always supply flags like `--parent` explicitly so the command runs without waiting for input.

## Get a non-interactive auth token

Every automated workflow that touches Chainguard's registry or API needs a credential. The process is two steps: authenticate with `chainctl auth login`, then capture the resulting token with `chainctl auth token`.

To authenticate non-interactively, you need the UIDP of an assumable identity configured to trust your CI platform's OIDC issuer. Find it with:

```bash
chainctl iam identities list --output=json \
  | jq -r '.items[] | select(.name == "my-ci-identity") | .id'
```

Then authenticate using the identity and your platform's OIDC token, and export the result:

```bash
chainctl auth login \
  --identity="$IDENTITY_ID" \
  --identity-token="$PATH_TO_OIDC_TOKEN"

export CHAINGUARD_TOKEN=$(chainctl auth token)
```

`$PATH_TO_OIDC_TOKEN` is the path to a file containing the OIDC token provided by your CI platform. See the OIDC-aware CI platforms section below for platform-specific examples.

Pass the token to Docker or `crane` to authenticate to `cgr.dev`:

```bash
echo "$CHAINGUARD_TOKEN" | docker login cgr.dev \
  --username=_token \
  --password-stdin
```

### Use in OIDC-aware CI platforms

Many CI platforms can provide a short-lived OIDC token that `chainctl` uses to authenticate without storing long-lived credentials. You configure a Chainguard assumable identity that trusts your platform's OIDC issuer, and your pipeline exchanges the token for registry access at run time.

Tested examples are available for the following platforms:

- [Authenticating with GitHub Actions](/chainguard/chainguard-registry/authenticating/#authenticating-with-github-actions)
- [Authenticating with CircleCI OIDC Token](/chainguard/chainguard-registry/authenticating/#authenticating-with-circleci-oidc-token)
- [Authenticating with Microsoft Entra ID OIDC Token](/chainguard/chainguard-registry/authenticating/#authenticating-with-microsoft-entra-id-oidc-token)

## Pin an image by its digest

Mutable tags like `latest` can silently change. Pinning to a digest prevents unexpected changes from reaching production. This snippet retrieves the current digest for a given tag and rewrites a Kubernetes manifest in place.

```bash
#!/usr/bin/env bash
ORG="your-org.example.com"
IMAGE="python"
TAG="3.13"
MANIFEST="deployment.yaml"

DIGEST=$(chainctl images history "$IMAGE:$TAG" \
  --parent="$ORG" --output=json \
  | jq -r '.[0].digest')

echo "Pinning $IMAGE:$TAG to $DIGEST"
sed -i "s|cgr.dev/$ORG/$IMAGE:.*|cgr.dev/$ORG/$IMAGE@$DIGEST|g" "$MANIFEST"
```

Add this as a pipeline step that runs after each image update notification to keep your manifests pinned to the most recent verified build.

## Detect when an image has been updated

This script compares the current digest for an image tag against the last known digest and runs a notification when the image changes. Schedule it on a cron or in a recurring GitHub Actions workflow.

```bash
#!/usr/bin/env bash
ORG="your-org.example.com"
IMAGE="nginx"
TAG="latest"
STATE_FILE="/tmp/.${IMAGE}-${TAG}-digest"

CURRENT=$(chainctl images history "$IMAGE:$TAG" \
  --parent="$ORG" --output=json \
  | jq -r '.[0].digest')

if [[ -f "$STATE_FILE" && "$(cat "$STATE_FILE")" != "$CURRENT" ]]; then
  echo "Image updated: cgr.dev/$ORG/$IMAGE:$TAG"
  echo "New digest: $CURRENT"
  # Add your notification logic here: webhook, Slack, GitHub dispatch, etc.
fi

printf '%s' "$CURRENT" > "$STATE_FILE"
```

If you run this in a stateless CI environment, store `STATE_FILE` in a persistent cache between runs — for example, a GitHub Actions cache keyed on the image name.

## Compare images before promotion

Before promoting a new image version to production, use `chainctl images diff` to surface changed packages and CVE-count deltas. This gives you an audit trail for the promotion decision. This command requires [grype](https://github.com/anchore/grype) to be installed and available on the system PATH.

```bash
#!/usr/bin/env bash
ORG="your-org.example.com"
IMAGE="python"
OLD_TAG="3.12"
NEW_TAG="3.13"

echo "Comparing $OLD_TAG -> $NEW_TAG for $IMAGE"
chainctl images diff \
  "cgr.dev/$ORG/$IMAGE:$OLD_TAG" \
  "cgr.dev/$ORG/$IMAGE:$NEW_TAG"
```

Capture the output with `| tee diff-report.txt` to attach it to a pull request or deployment ticket. See [Compare Chainguard Containers with chainctl diff](/chainguard/chainguard-images/how-to-use/comparing-images/) for details on reading the diff output.

## Audit role bindings for compliance

This snippet exports a snapshot of all current role bindings to a JSON file. Diff the output against a prior snapshot to detect unexpected access changes — useful for periodic security reviews or SOC 2 evidence collection.

```bash
#!/usr/bin/env bash
DATE=$(date +%Y-%m-%d)
SNAPSHOT="role-bindings-${DATE}.json"

chainctl iam role-bindings list --output=json > "$SNAPSHOT"
echo "Snapshot written to $SNAPSHOT"

# Summarize: binding count per role
jq -r '.items[].role_name' "$SNAPSHOT" | sort | uniq -c | sort -rn
```

Archive snapshots to an S3 bucket or similar to build a durable audit trail. You can compare two snapshots with `diff <(jq -S . previous.json) <(jq -S . current.json)`.

## Batch-onboard new users

When a new team joins or a project kicks off, generate all the invite codes at once from a CSV file rather than creating each one by hand. The CSV should have one `email,role` pair per line with a header row.

```bash
#!/usr/bin/env bash
# Usage: ./onboard-users.sh users.csv your-org.example.com
CSV_FILE="${1:?provide a CSV file}"
ORG="${2:?provide an org name}"

while IFS=',' read -r EMAIL ROLE; do
  [[ "$EMAIL" == "email" ]] && continue   # skip header row
  echo "Creating invite: $EMAIL with role $ROLE"
  chainctl iam invite create "$ORG" \
    --role="$ROLE" \
    --email="$EMAIL" \
    --ttl=7d \
    --single-use
done < "$CSV_FILE"
```

The `--single-use` flag ensures each invite code can only be redeemed once. Adjust `--ttl` to match your onboarding window.

## Revoke a user's access

When someone leaves your organization, remove their Chainguard identity to prevent further authentication. This script looks up the identity by email address using role bindings and prints the delete command for you to confirm before running.

```bash
#!/usr/bin/env bash
# Usage: ./offboard.sh jane@example.com
EMAIL="${1:?provide an email address}"

IDENTITY_ID=$(chainctl iam role-bindings list --output=json \
  | jq -r --arg email "$EMAIL" \
    '.items[] | select(.email == $email) | .identity_id' | head -1)

if [[ -z "$IDENTITY_ID" ]]; then
  echo "No identity found for: $EMAIL"
  exit 1
fi

echo "Found identity: $IDENTITY_ID"
echo "Run the following to delete it:"
echo "  chainctl iam identities delete $IDENTITY_ID --yes"
```

The script prints the delete command rather than running it, so you can verify the identity ID before committing. Replace the final two lines with `chainctl iam identities delete "$IDENTITY_ID"` once you are confident in the match.

## Manage event subscriptions as code

Event subscriptions route Chainguard platform events — such as new vulnerability detections — to an external endpoint. Rather than creating subscriptions by hand, treat them as managed configuration and verify their existence in your infrastructure provisioning pipeline.

```bash
#!/usr/bin/env bash
# Usage: ./ensure-subscription.sh your-org.example.com https://hooks.example.com/chainguard
ORG="${1:?provide an org name}"
ENDPOINT="${2:?provide a webhook URL}"

EXISTING=$(chainctl events subscriptions list --output=json \
  | jq -r --arg url "$ENDPOINT" \
    '.items[] | select(.sink == $url) | .id')

if [[ -n "$EXISTING" ]]; then
  echo "Subscription already present (id: $EXISTING)"
else
  echo "Creating subscription: $ORG -> $ENDPOINT"
  chainctl events subscriptions create "$ENDPOINT" \
    --parent="$ORG"
fi
```

Run this script idempotently during infrastructure provisioning. If the subscription already exists, it exits cleanly without creating a duplicate.

---

For a full reference of every `chainctl` command and flag, see the [chainctl Reference](/chainguard/chainctl/).
