---
title: "Trust Policy Reference"
linktitle: "Trust Policy Reference"
type: "article"
lead: "Complete reference for octo-sts trust policy syntax, configuration options, and validation patterns"
description: "Learn about Octo STS trust policy configuration including claim matching, permission settings, pattern validation, and advanced use cases"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "Reference", "Configuration"]
draft: false
images: []
menu:
  docs:
    parent: "octo-sts"
weight: 50
toc: true
---

Trust policies are YAML configuration files that control how Octo STS validates OIDC tokens and issues GitHub access tokens. This reference provides documentation of trust policy syntax and options.

## File Location

Trust policies must be stored in your repository at:

```
.github/chainguard/{name}.sts.yaml
```

The `{name}` portion becomes the identity parameter in the token exchange request:

```
https://octo-sts.dev/sts/exchange?scope=org/repo&identity={name}
```

For example, `.github/chainguard/renovate.sts.yaml` would be referenced as `identity=renovate`.

## Policy Types

Octo STS supports two types of trust policies:

**Repository Trust Policy**: Grants access to a single repository. The policy file must be in the repository it grants access to.

**Organization Trust Policy**: Grants access to multiple repositories within an organization. Uses additional `repositories` field to specify scope.

## Basic Structure

### Repository Trust Policy

```yaml
issuer: string
subject: string

permissions:
  permission_name: read | write
```

### Organization Trust Policy

```yaml
issuer: string
subject: string

permissions:
  permission_name: read | write

repositories:
  - org/repo-one
  - org/repo-two
```

## Required Fields

### issuer

The OIDC issuer that issued the token. Must match exactly.

**Type**: `string`

**Examples**:
```yaml
issuer: https://token.actions.githubusercontent.com
```
```yaml
issuer: https://accounts.google.com
```
```yaml
issuer: https://kubernetes.default.svc.cluster.local
```

Common issuers:
- GitHub Actions: `https://token.actions.githubusercontent.com`
- Google Cloud: `https://accounts.google.com`
- Kubernetes: `https://kubernetes.default.svc.cluster.local` (varies by cluster)
- AWS (via GitHub): `https://token.actions.githubusercontent.com`
- Azure AD: `https://login.microsoftonline.com/{tenant-id}/v2.0`

### subject

The exact subject claim from the OIDC token that should be trusted.

**Type**: `string`

**Examples**:

GitHub Actions (specific branch):
```yaml
subject: repo:chainguard-dev/example:ref:refs/heads/main
```

GitHub Actions (specific environment):
```yaml
subject: repo:chainguard-dev/example:environment:production
```

Kubernetes service account:
```yaml
subject: system:serviceaccount:default:automation
```

Google service account (numeric ID):
```yaml
subject: "123456789012345678901"
```

**Mutually exclusive with**: `subject_pattern`

### permissions

GitHub API permissions to grant the resulting token. All permissions are optional except that at least one must be specified.

**Type**: `map[string]string`

**Values**: `read`, `write`, `admin` (where supported)

**Example**:
```yaml
permissions:
  contents: read
  issues: write
  pull_requests: write
```

See [Available Permissions](#available-permissions) for the complete list.

## Optional Fields

### subject_pattern

Regular expression pattern to match against the subject claim. Use this when you need flexible subject matching.

**Type**: `string` (regex)

**Examples**:

Match any branch:
```yaml
subject_pattern: "repo:chainguard-dev/example:ref:refs/heads/.*"
```

Match numeric Google service account IDs:
```yaml
subject_pattern: "[0-9]+"
```

Match any service account in a namespace:
```yaml
subject_pattern: "system:serviceaccount:production:.*"
```

**Mutually exclusive with**: `subject`

**Important**: Use anchors (`^` and `$`) if you need exact boundaries. Without anchors, patterns match anywhere in the subject string.

### claim_pattern

Additional claim validation using regular expressions. Validates custom claims beyond issuer and subject.

**Type**: `map[string]string` (claim name to regex pattern)

**Examples**:

Validate email domain:
```yaml
claim_pattern:
  email: ".*@chainguard.dev"
```

Validate Kubernetes namespace:
```yaml
claim_pattern:
  kubernetes.io/namespace: "production"
```

Multiple claim patterns:
```yaml
claim_pattern:
  email: ".*@example.com"
  email_verified: "true"
```

**Common claims by provider**:

GitHub Actions:
- `repository`: Repository full name
- `repository_owner`: Organization or user name
- `ref`: Git ref that triggered the workflow
- `workflow`: Workflow file name
- `event_name`: Event that triggered the workflow
- `job_workflow_ref`: Reference to the workflow

Google Cloud:
- `email`: Service account email
- `email_verified`: Boolean as string

Kubernetes:
- `kubernetes.io/namespace`: Namespace name
- `kubernetes.io/serviceaccount/name`: Service account name
- `kubernetes.io/pod/name`: Pod name

### repositories

**Organization Trust Policies Only**: List of repositories the token can access.

**Type**: `array[string]`

**Format**: `organization/repository`

**Example**:
```yaml
repositories:
  - chainguard-dev/repo-one
  - chainguard-dev/repo-two
  - chainguard-dev/repo-three
```

Without this field, organization policies grant no repository access. This is a safety mechanism to prevent accidentally creating overly permissive policies.

## Available Permissions

### Repository Permissions

**actions** (`read`, `write`)
- Read: View workflow runs and artifacts
- Write: Cancel workflows, re-run workflows

**checks** (`read`, `write`)
- Read: View check runs
- Write: Create and update check runs

**contents** (`read`, `write`)
- Read: Clone repository, read files
- Write: Push commits, create/delete branches

**deployments** (`read`, `write`)
- Read: View deployments
- Write: Create deployments, update deployment status

**discussions** (`read`, `write`)
- Read: View discussions
- Write: Create and manage discussions

**environments** (`read`, `write`)
- Read: View environment configuration
- Write: Configure environments

**issues** (`read`, `write`)
- Read: View issues
- Write: Create, update, close issues

**packages** (`read`, `write`)
- Read: Download packages
- Write: Publish and delete packages

**pages** (`read`, `write`)
- Read: View GitHub Pages settings
- Write: Configure GitHub Pages

**projects** (`read`, `write`, `admin`)
- Read: View projects
- Write: Edit projects
- Admin: Manage project settings

**pull_requests** (`read`, `write`)
- Read: View pull requests
- Write: Create and manage pull requests

**statuses** (`read`, `write`)
- Read: View commit statuses
- Write: Create commit statuses

**workflows** (`read`, `write`)
- Read: View workflow files
- Write: Update workflow files (critical for tools like Renovate)

### Organization Permissions

**members** (`read`, `write`)
- Read: View organization members
- Write: Manage organization membership

**administration** (`read`, `write`)
- Read: View organization settings
- Write: Manage organization settings

### Additional Permissions

For the complete and current list of permissions, see the [octo-sts README](https://github.com/octo-sts/app#octo-sts-github-permissions).

## Pattern Matching Examples

### Example 1: GitHub Actions on Main or Develop

```yaml
issuer: https://token.actions.githubusercontent.com
subject_pattern: "repo:chainguard-dev/example:ref:refs/heads/(main|develop)"

permissions:
  contents: read
  pull_requests: write
```

### Example 2: Any Google Email in Organization

```yaml
issuer: https://accounts.google.com
subject_pattern: "[0-9]+"
claim_pattern:
  email: ".*@chainguard.dev"
  email_verified: "true"

permissions:
  contents: read
```

### Example 3: Kubernetes Service Account in Production Namespace

```yaml
issuer: https://kubernetes.default.svc.cluster.local
subject_pattern: "system:serviceaccount:production:.*"

permissions:
  contents: write
  deployments: write
```

### Example 4: GitHub Actions from Any Repository in Organization

```yaml
issuer: https://token.actions.githubusercontent.com
subject_pattern: "repo:chainguard-dev/.*:ref:refs/heads/main"
claim_pattern:
  repository_owner: "chainguard-dev"

permissions:
  contents: read
```

## Security Considerations

### Principle of Least Privilege

Grant only the minimum permissions required:

```yaml
# Good: Specific permissions for specific task
permissions:
  contents: read
  pull_requests: write
```

```yaml
# Avoid: Overly broad permissions
permissions:
  contents: write
  issues: write
  pull_requests: write
  workflows: write
  packages: write
```

### Subject Matching

Prefer exact subject matches over patterns:

```yaml
# Better: Exact match
subject: repo:org/repo:ref:refs/heads/main
```

```yaml
# Acceptable but broader: Pattern match
subject_pattern: "repo:org/repo:ref:refs/heads/.*"
```

### Branch Protection

Even with `contents: write`, enable branch protection to require pull requests:

1. Require pull request reviews before merging
2. Require status checks
3. Restrict who can push to matching branches

This ensures Octo STS tokens cannot bypass your review process.

### Claim Validation

Use additional claim validation for defense in depth:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:org/repo:ref:refs/heads/main
claim_pattern:
  repository: "org/repo"
  repository_owner: "org"

permissions:
  contents: write
```

This ensures that even if subject validation is somehow bypassed, the repository and owner claims must still match.

## Advanced Patterns

### Time-Based Access (Not Native)

Octo STS doesn't natively support time-based policies, but you can implement this in your workload:

```python
from datetime import datetime, time

# Only request token during maintenance window
now = datetime.now().time()
maintenance_start = time(2, 0)  # 2 AM
maintenance_end = time(4, 0)    # 4 AM

if maintenance_start <= now <= maintenance_end:
    # Exchange token with Octo STS
    pass
else:
    raise Exception("Outside maintenance window")
```

### Conditional Permissions

Use multiple trust policies with different permission levels:

`.github/chainguard/read-only.sts.yaml`:
```yaml
issuer: https://token.actions.githubusercontent.com
subject_pattern: "repo:org/repo:ref:refs/heads/.*"

permissions:
  contents: read
```

`.github/chainguard/read-write.sts.yaml`:
```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:org/repo:ref:refs/heads/main

permissions:
  contents: write
  pull_requests: write
```

Workflows choose which policy to use based on their needs.

### Multi-Cloud Identity

Support multiple cloud providers with one policy using claim patterns:

```yaml
issuer: https://accounts.google.com
subject_pattern: "[0-9]+"
claim_pattern:
  email: "automation@.*\\.iam\\.gserviceaccount\\.com"

permissions:
  contents: read
```

This trusts any Google service account with "automation" in the name across all your projects.

## JSON Schema

Octo STS provides JSON schemas for IDE autocompletion:

- [TrustPolicy Schema](https://raw.githubusercontent.com/octo-sts/app/refs/heads/main/pkg/octosts/octosts.TrustPolicy.json)
- [OrgTrustPolicy Schema](https://raw.githubusercontent.com/octo-sts/app/refs/heads/main/pkg/octosts/octosts.OrgTrustPolicy.json)

### VSCode Configuration

Add to `.vscode/settings.json`:

```json
{
  "yaml.schemas": {
    "https://raw.githubusercontent.com/octo-sts/app/refs/heads/main/pkg/octosts/octosts.TrustPolicy.json": "/.github/chainguard/*"
  }
}
```

This enables autocompletion and validation in VS Code when editing trust policies.

## Validation and Debugging

### Testing Trust Policies

Use the workflow_dispatch trigger to test trust policies manually:

```yaml
name: Test Trust Policy

on:
  workflow_dispatch:
    inputs:
      identity:
        description: 'Identity to test'
        required: true
        default: 'test'

permissions:
  contents: read
  id-token: write

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Test token exchange
        uses: octo-sts/action@f603d3be9d8dd9871a265776e625a27b00effe05 # v1.1.1
        id: octo-sts
        with:
          scope: ${{ github.repository }}
          identity: ${{ github.event.inputs.identity }}

      - name: Verify token
        env:
          GITHUB_TOKEN: ${{ steps.octo-sts.outputs.token }}
        run: |
          gh repo view ${{ github.repository }}
```

### Common Validation Errors

**issuer mismatch**: The OIDC token's issuer doesn't match the trust policy
- Verify the issuer URL exactly matches
- Check for trailing slashes or URL variations

**subject mismatch**: The OIDC token's subject doesn't match the trust policy
- Print the token subject to verify format: `echo $TOKEN | cut -d'.' -f2 | base64 -d | jq .sub`
- Check for extra claim components

**pattern doesn't match**: The regex pattern doesn't match the claim
- Test regex patterns separately to verify they work
- Remember to escape special characters in YAML strings

**missing permissions**: The trust policy file can't be read
- Verify the file exists at `.github/chainguard/{identity}.sts.yaml`
- Check that octo-sts has repository access
- Ensure the file is on the correct branch (usually main/master)

## Best Practices Summary

1. **Use exact subject matching** when possible, fall back to patterns only when necessary
2. **Grant minimum permissions** required for the specific task
3. **Implement branch protection** to require code review even with write permissions
4. **Add claim validation** for additional security beyond subject matching
5. **Create separate policies** for different workflows rather than one broad policy
6. **Document policy purpose** in commit messages when adding or modifying policies
7. **Regular audits** of all trust policies to ensure they're still necessary and appropriately scoped
8. **Use JSON schema** for validation and autocompletion when editing policies

## Next Steps

- [Using Octo STS with GitHub Actions](/open-source/octo-sts/how-to-use-octo-sts-with-github-actions/) - Apply trust policies in GitHub Actions workflows
- [Using Octo STS with Kubernetes](/open-source/octo-sts/how-to-use-octo-sts-with-kubernetes/) - Configure trust policies for Kubernetes workloads
- [FAQ](/open-source/octo-sts/faq/) - Common questions and troubleshooting
