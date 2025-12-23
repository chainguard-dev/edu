---
title: "Getting Started with Octo STS"
linktitle: "Getting Started"
type: "article"
lead: "Set up octo-sts and create your first trust policy to eliminate GitHub Personal Access Tokens"
description: "Learn about Octo STS GitHub App, creating trust policies, and exchanging OIDC tokens for short-lived GitHub access tokens"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "Getting Started", "Procedural"]
draft: false
images: []
menu:
  docs:
    parent: "octo-sts"
weight: 10
toc: true
---

This guide walks you through setting up Chainguard's Octo STS for the first time. By the end of this tutorial, you'll have installed the octo-sts GitHub App, created a trust policy, and successfully exchanged an OIDC token for a short-lived GitHub access token.

## Prerequisites

Before you begin, you need:

- **GitHub organization or repository access**: You must have admin permissions to install GitHub Apps
- **OIDC token source**: A way to generate OIDC tokens (this guide uses GitHub Actions, but Octo STS supports any OIDC provider)
- **Basic understanding of OIDC**: Familiarity with OpenID Connect concepts is helpful but not required

## Step 1 — Install the octo-sts GitHub App

The first step is to install the octo-sts GitHub App into your organization or repository.

1. Navigate to the [octo-sts GitHub App installation page](https://github.com/apps/octo-sts)
2. Click **Install** or **Configure** if you've previously installed the app
3. Select the organization or user account where you want to install Octo STS
4. Choose repository access:
   - **All repositories**: Grants octo-sts access to all current and future repositories
   - **Only select repositories**: Limits access to specific repositories you choose

**Important**: The octo-sts app requests a superset of GitHub permissions to support various use cases. However, it only creates tokens with the specific permissions defined in your trust policies. The app requires `contents: read` permission to read trust policy files from your repositories.

After installation, you'll be redirected to GitHub. The app is now installed but won't issue any tokens until you create trust policies.

## Step 2 — Understand Trust Policy Basics

Trust policies are YAML files stored in your repository at `.github/chainguard/{name}.sts.yaml`. Each policy defines:

1. **Identity validation**: Which OIDC tokens are trusted (issuer, subject, custom claims)
2. **Permissions**: What the identity can do with GitHub (read, write, etc.)
3. **Scope**: Which repositories the policy applies to (repository-level policies only)

A trust policy has three main components:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:org-name/repo-name:ref:refs/heads/main

permissions:
  contents: read
  issues: write
```

- **issuer**: The OIDC provider that issued the token (e.g., GitHub Actions, Google, AWS)
- **subject**: The specific identity being granted access (can be exact match or pattern)
- **permissions**: GitHub API permissions to grant

## Step 3 — Create Your First Trust Policy

Let's create a simple trust policy that allows GitHub Actions workflows running on the `main` branch to read repository contents and write to issues.

1. In your repository, create the directory structure for trust policies:

```shell
mkdir -p .github/chainguard
```

2. Create a trust policy file named `.github/chainguard/example.sts.yaml`:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main

permissions:
  contents: read
  issues: write
```

Replace `YOUR-ORG` and `YOUR-REPO` with your actual organization and repository names.

This policy allows any GitHub Actions workflow running on the `main` branch of your repository to:
- Read repository contents
- Create and update issues

3. Commit and push the trust policy:

```shell
git add .github/chainguard/example.sts.yaml
git commit -m "Add octo-sts trust policy for main branch"
git push origin main
```

## Step 4 — Test the Token Exchange

Now that you have a trust policy, you can test the token exchange. You'll create a GitHub Actions workflow that exchanges its OIDC token for a GitHub token via octo-sts.

1. Create a workflow file at `.github/workflows/test-octo-sts.yaml`:

```yaml
name: Test octo-sts

on:
  workflow_dispatch:

permissions:
  contents: read
  id-token: write  # Required to generate OIDC tokens

jobs:
  test-token-exchange:
    runs-on: ubuntu-latest

    steps:
      - name: Exchange OIDC token for GitHub token
        id: octo-sts
        run: |
          # Get the OIDC token from GitHub Actions
          OIDC_TOKEN=$(curl -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
            "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://github.com/${{ github.repository }}" | jq -r '.value')

          # Exchange it with Octo STS
          RESPONSE=$(curl -s -H "Authorization: Bearer $OIDC_TOKEN" \
            "https://octo-sts.dev/sts/exchange?scope=${{ github.repository }}&identity=example")

          # Extract the token
          GITHUB_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')

          echo "::add-mask::$GITHUB_TOKEN"
          echo "token=$GITHUB_TOKEN" >> $GITHUB_OUTPUT

      - name: Verify token works
        env:
          GITHUB_TOKEN: ${{ steps.octo-sts.outputs.token }}
        run: |
          # Test the token by reading repository information
          curl -H "Authorization: Bearer $GITHUB_TOKEN" \
            "https://api.github.com/repos/${{ github.repository }}" | jq '.name'

          echo "Token exchange successful!"
```

2. Commit and push the workflow:

```shell
git add .github/workflows/test-octo-sts.yaml
git commit -m "Add octo-sts test workflow"
git push origin main
```

3. Run the workflow:
   - Go to your repository on GitHub
   - Click the **Actions** tab
   - Select **Test octo-sts** from the workflow list
   - Click **Run workflow** and select the `main` branch
   - Click **Run workflow** to start

4. Monitor the workflow execution and check that it completes successfully.

If the workflow succeeds, you've successfully:
- Generated an OIDC token in GitHub Actions
- Exchanged it with Octo STS
- Received a short-lived GitHub token
- Used that token to access the GitHub API

## Step 5 — Verify Trust Policy Enforcement

To understand how trust policies protect your repositories, try modifying the trust policy to see enforcement in action.

1. Edit `.github/chainguard/example.sts.yaml` and change the subject to a different branch:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/develop

permissions:
  contents: read
  issues: write
```

2. Commit and push the change to the `main` branch.

3. Run the test workflow again from the **Actions** tab.

This time, the workflow should fail at the token exchange step because the workflow is running on `main` but the trust policy now requires the `develop` branch.

This demonstrates that Octo STS validates the OIDC token claims against your trust policy before issuing GitHub tokens.

## Understanding Token Permissions

The permissions in your trust policy determine what operations the generated GitHub token can perform. Common permissions include:

- **contents: read** - Read repository contents
- **contents: write** - Modify files, push commits
- **issues: read/write** - Manage issues
- **pull_requests: read/write** - Manage pull requests
- **checks: write** - Create check runs
- **workflows: write** - Modify workflow files

For a complete list of available permissions, see the [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/).

## Best Practices

**Start with minimal permissions**: Begin with `contents: read` and add permissions only as needed. It's easier to expand access than to audit overly broad permissions.

**Use specific subject matching**: Prefer exact subject matches over patterns when possible. For example, `repo:org/repo:ref:refs/heads/main` is better than `repo:org/repo:.*`.

**Enable branch protection**: Configure branch protection rules on your main branch to prevent octo-sts clients from bypassing pull request reviews.

**Create separate policies for different workflows**: Don't use a single policy for all automation. Create specific policies for different use cases (CI, releases, dependency updates, etc.).

**Review policies regularly**: Periodically audit your trust policies to ensure they still match your security requirements.

## Troubleshooting

**Token exchange fails with 403 Forbidden**

This typically means:
- The OIDC token doesn't match the trust policy (check issuer and subject)
- The trust policy file is missing or has syntax errors
- The octo-sts app doesn't have access to the repository

**Cannot read trust policy file**

Ensure:
- The file is at `.github/chainguard/{name}.sts.yaml`
- The file is committed to the repository
- The octo-sts app has `contents: read` permission

**Token works but has wrong permissions**

Verify:
- The permissions in your trust policy are correct
- You're using the token from octo-sts, not another token
- The repository hasn't changed branch protection rules that restrict the operation

## Next Steps

Now that you have octo-sts working, explore specific use cases:

- [Using Octo STS with GitHub Actions](/open-source/octo-sts/how-to-use-octo-sts-with-github-actions/) - Integrate octo-sts into common GitHub Actions workflows including Renovate
- [Using Octo STS with Kubernetes](/open-source/octo-sts/how-to-use-octo-sts-with-kubernetes/) - Federate Kubernetes service accounts with GitHub
- [Using Octo STS with Cloud Providers](/open-source/octo-sts/how-to-use-octo-sts-with-cloud-providers/) - Connect AWS, GCP, or Azure workloads
- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/) - Learn advanced trust policy features including pattern matching and custom claims
