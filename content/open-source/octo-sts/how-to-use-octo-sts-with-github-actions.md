---
title: "How to Use Octo STS with GitHub Actions"
linktitle: "GitHub Actions Integration"
type: "article"
lead: "Integrate octo-sts into GitHub Actions workflows to eliminate Personal Access Tokens while running automated tasks like dependency updates, releases, and repository management"
description: "Learn about Octo STS with GitHub Actions for common automation tasks including Renovate dependency updates, release workflows, and repository management without Personal Access Tokens"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "GitHub Actions", "Procedural"]
draft: false
images: []
menu:
  docs:
    parent: "octo-sts"
weight: 20
toc: true
---

GitHub Actions workflows often need access to the GitHub API beyond what the default `GITHUB_TOKEN` provides. The standard `GITHUB_TOKEN` has limitations, most notably that it cannot trigger other workflows and lacks permissions for certain operations like updating workflow files. The typical solution is to create a Personal Access Token (PAT), but PATs are long-lived credentials that create security risks.

This guide demonstrates how to use Chainguard's Octo STS with GitHub Actions to obtain tokens with enhanced permissions without relying on PATs.

## Prerequisites

Before you begin, ensure you have:

- Completed the [Getting Started with Octo STS](/open-source/octo-sts/getting-started-with-octo-sts/) guide
- The octo-sts GitHub App installed on your repository or organization
- Admin access to the repository to configure workflows and branch protection

## Understanding the Default GitHub Token Limitations

The `GITHUB_TOKEN` automatically provided to GitHub Actions workflows has several limitations:

- Cannot update GitHub Actions workflow files (`.github/workflows/`)
- Cannot trigger other workflow runs (by design, to prevent recursive workflows)
- Has restricted permissions that cannot be expanded beyond a limited set
- May not have access to all repository permissions available to GitHub Apps

These limitations make the default token insufficient for tasks like:
- Running Renovate to update dependencies including Actions
- Creating release workflows that trigger deployment pipelines
- Automated repository configuration that modifies workflow files

Octo STS solves these issues by providing tokens with exactly the permissions you specify in your trust policy.

## Pattern: Using the octo-sts Action

The simplest way to integrate Octo STS into GitHub Actions is using the official octo-sts action. This action handles the token exchange automatically.

### Basic Integration

```yaml
name: Example Workflow

on:
  workflow_dispatch:

permissions:
  contents: read
  id-token: write  # Required for OIDC token generation

jobs:
  example:
    runs-on: ubuntu-latest

    permissions:
      id-token: write  # Required for octo-sts
      contents: write  # For subsequent steps that need write access

    steps:
      - name: Exchange token with Octo STS
        uses: octo-sts/action@f603d3be9d8dd9871a265776e625a27b00effe05 # v1.1.1
        id: octo-sts
        with:
          scope: ${{ github.repository }}
          identity: example

      - name: Use the token
        env:
          GITHUB_TOKEN: ${{ steps.octo-sts.outputs.token }}
        run: |
          # The token is now available for use
          gh repo view ${{ github.repository }}
```

The octo-sts action:
1. Generates an OIDC token from GitHub Actions
2. Exchanges it with the Octo STS service
3. Returns a short-lived GitHub token in `outputs.token`

This token can then be used in subsequent steps via `${{ steps.octo-sts.outputs.token }}`.

### Corresponding Trust Policy

For the above workflow, create `.github/chainguard/example.sts.yaml`:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: write
  issues: write
  pull_requests: write
```

## Use Case: Running Renovate Without a PAT

Renovate is a popular tool for keeping dependencies up-to-date. When run as a GitHub Action, it traditionally requires a PAT. Using Octo STS eliminates this requirement.

### Step 1 — Create the Renovate Trust Policy

Create `.github/chainguard/renovate.sts.yaml`:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  checks: write
  contents: write
  issues: write
  members: read
  pull_requests: write
  statuses: write
  workflows: write
```

These permissions allow Renovate to:
- Read dependency files (`contents: write`)
- Create pull requests (`pull_requests: write`)
- Update GitHub Actions workflows (`workflows: write`)
- Manage PR checks and statuses (`checks: write`, `statuses: write`)

### Step 2 — Create the Renovate Workflow

Create `.github/workflows/renovate.yaml`:

```yaml
name: Renovate

on:
  workflow_dispatch:
  schedule:
    - cron: "0 3 * * *"  # Run at 3 AM daily

permissions:
  contents: read

jobs:
  renovate:
    runs-on: ubuntu-latest

    permissions:
      id-token: write  # Required for octo-sts
      contents: write

    steps:
      - name: Get token from octo-sts
        uses: octo-sts/action@f603d3be9d8dd9871a265776e625a27b00effe05 # v1.1.1
        id: octo-sts
        with:
          scope: ${{ github.repository }}
          identity: renovate

      - name: Run Renovate
        uses: renovatebot/github-action@822441559e94f98b67b82d97ab89fe3003b0a247 # v44.2.0
        env:
          RENOVATE_TOKEN: ${{ steps.octo-sts.outputs.token }}
          RENOVATE_REPOSITORIES: ${{ github.repository }}
```

### Step 3 — Configure Renovate

Create `renovate.json` in your repository root:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:best-practices",
    "helpers:pinGitHubActionDigestsToSemver"
  ],
  "minimumReleaseAge": "1 day",
  "prHourlyLimit": 0,
  "automergeType": "pr",
  "packageRules": [
    {
      "description": "Automerge safe updates",
      "matchUpdateTypes": ["patch", "minor", "digest"],
      "automerge": true
    }
  ]
}
```

Key configuration options:
- **minimumReleaseAge**: Wait 1 day before updating to mitigate supply chain attacks
- **helpers:pinGitHubActionDigestsToSemver**: Pin Actions to digests for security while showing semantic versions
- **automerge**: Automatically merge patch and minor updates (optional, adjust for your risk tolerance)

### Step 4 — Enable Branch Protection

To prevent Renovate (or any octo-sts client) from bypassing review processes:

1. Go to **Settings** → **Branches** in your repository
2. Add a branch protection rule for `main`:
   - Enable **Require a pull request before merging**
   - Enable **Require approvals** (at least 1)
   - Enable **Require status checks to pass**
3. Save the rule

With branch protection enabled, even with `contents: write` permission, Renovate must create pull requests that go through your review process.

## Use Case: Automated Releases

Many projects use GitHub Actions to create releases, which requires additional permissions.

### Release Trust Policy

Create `.github/chainguard/release.sts.yaml`:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: write
  pull_requests: write
  issues: write
```

### Release Workflow

Create `.github/workflows/release.yaml`:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: read

jobs:
  release:
    runs-on: ubuntu-latest

    permissions:
      id-token: write
      contents: write

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Get octo-sts token
        uses: octo-sts/action@f603d3be9d8dd9871a265776e625a27b00effe05 # v1.1.1
        id: octo-sts
        with:
          scope: ${{ github.repository }}
          identity: release

      - name: Create Release
        env:
          GITHUB_TOKEN: ${{ steps.octo-sts.outputs.token }}
        run: |
          gh release create ${{ github.ref_name }} \
            --title "${{ github.ref_name }}" \
            --generate-notes
```

## Use Case: Cross-Repository Automation

Some workflows need to interact with multiple repositories. Octo STS supports organization-level policies for this purpose.

### Organization Trust Policy

For organization-wide policies, create `.github/chainguard/multi-repo.sts.yaml` in a repository within your organization:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: read
  issues: write
  pull_requests: write

repositories:
  - YOUR-ORG/repo-one
  - YOUR-ORG/repo-two
  - YOUR-ORG/repo-three
```

The `repositories` field specifies which repositories the token can access.

### Multi-Repository Workflow

```yaml
name: Cross-Repository Sync

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  sync:
    runs-on: ubuntu-latest

    permissions:
      id-token: write

    steps:
      - name: Get octo-sts token
        uses: octo-sts/action@f603d3be9d8dd9871a265776e625a27b00effe05 # v1.1.1
        id: octo-sts
        with:
          scope: ${{ github.repository }}
          identity: multi-repo

      - name: Sync across repositories
        env:
          GITHUB_TOKEN: ${{ steps.octo-sts.outputs.token }}
        run: |
          # Access multiple repositories with one token
          gh issue list --repo YOUR-ORG/repo-one
          gh issue list --repo YOUR-ORG/repo-two
          gh issue list --repo YOUR-ORG/repo-three
```

## Pattern: Manual Token Exchange

If you need more control over the token exchange process, you can implement it manually:

```yaml
steps:
  - name: Manual token exchange
    id: token-exchange
    run: |
      # Get OIDC token
      OIDC_TOKEN=$(curl -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
        "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://github.com/${{ github.repository }}" | jq -r '.value')

      # Exchange with Octo STS
      RESPONSE=$(curl -s -H "Authorization: Bearer $OIDC_TOKEN" \
        "https://octo-sts.dev/sts/exchange?scope=${{ github.repository }}&identity=custom")

      # Extract token
      GITHUB_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')

      echo "::add-mask::$GITHUB_TOKEN"
      echo "token=$GITHUB_TOKEN" >> $GITHUB_OUTPUT

  - name: Use token
    env:
      GITHUB_TOKEN: ${{ steps.token-exchange.outputs.token }}
    run: |
      # Use the token
      gh repo view
```

This approach is useful for:
- Custom error handling
- Logging token exchange for debugging
- Integration with tools that don't support the octo-sts action

## Trust Policy Patterns for GitHub Actions

### Pattern: Restrict to Main Branch

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: write
```

Only workflows running on the `main` branch can obtain tokens.

### Pattern: Restrict to Specific Workflow

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main:workflow:renovate.yaml

permissions:
  contents: write
```

Only the `renovate.yaml` workflow can obtain tokens (not yet supported by GitHub Actions OIDC tokens as of this writing, but shown for future reference).

### Pattern: Allow Any Branch with Pattern Matching

```yaml
issuer: https://token.actions.githubusercontent.com
subject_pattern: "repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/.*"

permissions:
  contents: read
  issues: write
```

Workflows on any branch can obtain tokens with these permissions.

### Pattern: Multiple Workflows with Different Permissions

Create separate trust policies for different workflows:

`.github/chainguard/ci.sts.yaml` (read-only):
```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: read
  checks: write
```

`.github/chainguard/deploy.sts.yaml` (read-write):
```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: write
  deployments: write
```

## Security Best Practices

**Use branch protection**: Always enable branch protection rules to prevent direct commits to protected branches, even with write permissions from octo-sts.

**Scope policies narrowly**: Create separate trust policies for different workflows rather than one policy with broad permissions.

**Pin action versions to digests**: Use commit SHA digests when referencing GitHub Actions, including the octo-sts action, for supply chain security.

**Limit automerge**: Be cautious with Renovate's automerge feature. Consider requiring manual approval for dependency updates in production-critical repositories.

**Monitor workflow runs**: Regularly audit which workflows are obtaining tokens from octo-sts and what they're doing with them.

**Use workflow_dispatch for testing**: When setting up new workflows with Octo STS, use `workflow_dispatch` triggers for testing before enabling automated triggers.

## Troubleshooting

### Token exchange fails with authentication error

Verify that:
- The workflow has `id-token: write` permission
- The trust policy exists at `.github/chainguard/{identity}.sts.yaml`
- The `subject` in the trust policy matches the workflow's branch/ref
- The octo-sts app has access to the repository

### Token works but operations fail

Check if:
- The trust policy grants sufficient permissions for the operation
- Branch protection rules are blocking the operation (this is often intentional)
- The repository has additional restrictions (e.g., required status checks)

### Renovate cannot update workflow files

Ensure:
- The trust policy includes `workflows: write` permission
- The workflow files are in `.github/workflows/` and have correct permissions
- Renovate configuration includes Actions in the update scope

## Next Steps

- [Using Octo STS with Kubernetes](/open-source/octo-sts/how-to-use-octo-sts-with-kubernetes/) - Federate Kubernetes workloads with GitHub
- [Using Octo STS with Cloud Providers](/open-source/octo-sts/how-to-use-octo-sts-with-cloud-providers/) - Connect cloud workloads to GitHub
- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/) - Advanced trust policy syntax and patterns
- [FAQ](/open-source/octo-sts/faq/) - Common questions and troubleshooting
