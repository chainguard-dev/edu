---
title: "Octo STS FAQ"
linktitle: "FAQ"
type: "article"
lead: "Frequently asked questions about Octo STS, including troubleshooting, security considerations, and common use cases"
description: "Learn about Octo STS for GitHub token federation, including setup issues, security best practices, and integration patterns"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "FAQ"]
draft: false
images: []
menu:
  docs:
    parent: "octo-sts"
weight: 60
toc: true
---

This page answers frequently asked questions about Octo STS, including setup, security, troubleshooting, and common use cases.

## General Questions

### What is Octo STS?

Octo STS is a GitHub App developed by Chainguard that acts as a Security Token Service for GitHub. It allows workloads with OIDC tokens from various identity providers (GitHub Actions, cloud providers, Kubernetes, etc.) to exchange those tokens for short-lived GitHub access tokens. The primary goal is to eliminate the need for long-lived Personal Access Tokens (PATs).

### Why should I use Octo STS instead of Personal Access Tokens?

Personal Access Tokens pose security risks as they allow provide persistent access to resources and are not tied to a given workload. Attackers regularly abuse leaked PATs to gain access to systems and resources.

By comparison, Octo STS tokens are short-lived (1 hour) and typically tightly scoped to the workload in question. This vastly reduces the scope for abuse.

### How does Octo STS compare to GitHub's built-in GITHUB\_TOKEN?

GitHub Actions provides a `GITHUB_TOKEN` automatically, but it has limitations:
- Cannot update workflow files
- Cannot trigger other workflows
- Limited to a fixed set of permissions

Octo STS tokens can:
- Update workflow files (useful for Renovate)
- Have any permissions defined in your trust policy
- Work consistently across all automation platforms, not just GitHub Actions

### Is Octo STS free to use?

Yes, Octo STS is open source and the hosted service at octo-sts.dev is free to use. You can also self-host Octo STS if you prefer.

### Can I self-host Octo STS?

Yes, Octo STS is open source and can be self-hosted. See the [Octo STS repository](https://github.com/octo-sts/app) for deployment instructions.

## Setup and Configuration

### How do I install Octo STS?

Install the GitHub App:
1. Visit [https://github.com/apps/octo-sts](https://github.com/apps/octo-sts)
2. Click **Install**
3. Select the organization or user account
4. Choose which repositories to grant access
5. Approve the permissions

Then create trust policies in your repositories at `.github/chainguard/{name}.sts.yaml`.

### Why does Octo STS request so many permissions?

Octo STS requests a superset of permissions to support a large range of use cases. However, it only creates tokens with the specific permissions defined in your trust policies. The app needs `contents: read` to read trust policy files, but all other permissions are only granted based on your policies.

### What happens if I don't create any trust policies?

If you install Octo STS but don't create trust policies, the app cannot issue any tokens. Trust policies are required to specify which identities are trusted and what permissions to grant them.

### Can I use Octo STS with private repositories?

Yes, Octo STS works with both public and private repositories. The app needs access to read the repository's trust policy files.

### How do I update trust policy permissions?

Edit the trust policy file in your repository, commit, and push the changes. The new permissions take effect immediately for subsequent token exchanges. Existing tokens retain their original permissions until they expire.

### Can I have multiple trust policies in one repository?

Yes, you can create multiple policy files with different names:
- `.github/chainguard/renovate.sts.yaml`
- `.github/chainguard/deploy.sts.yaml`
- `.github/chainguard/ci.sts.yaml`

Each policy can have different identity requirements and permissions. Specify which policy to use via the `identity` parameter when exchanging tokens.

## Security

### Are Octo STS tokens safe?

Octo STS tokens are as safe as the trust policies you create. They're short-lived (1 hour), reducing the window of opportunity if compromised.

### Can Octo STS tokens bypass branch protection?

No. Branch protection rules are enforced by GitHub regardless of the token type. Even with `contents: write` permission, Octo STS tokens must follow branch protection requirements like pull request reviews and status checks.

### Should I use pattern matching or exact subjects?

Prefer exact subject matching when possible:

```yaml
# Better: Exact match
subject: repo:org/repo:ref:refs/heads/main
```

Use pattern matching only when you need flexibility:

```yaml
# When necessary: Pattern match
subject_pattern: "repo:org/repo:ref:refs/heads/.*"
```

Exact matching is more secure because it's harder to accidentally grant broader access than intended.

## Integration

### Can I use Octo STS from a CI/CD system other than GitHub Actions?

Yes, Octo STS works with any system that can:
1. Obtain OIDC tokens (Jenkins, GitLab CI, CircleCI, etc.)
2. Make HTTP requests to exchange tokens
3. Use the resulting GitHub token

The key is having an OIDC identity provider that Octo STS can validate.

### How do I use Octo STS with Terraform?

Use Terraform's `external` data source to exchange tokens:

```hcl
data "external" "github_token" {
  program = ["bash", "-c", <<-EOT
    OIDC_TOKEN=$(get_oidc_token)
    RESPONSE=$(curl -s -H "Authorization: Bearer $OIDC_TOKEN" \
      "https://octo-sts.dev/sts/exchange?scope=org/repo&identity=terraform")
    echo $RESPONSE | jq '{token: .access_token}'
  EOT
  ]
}

provider "github" {
  token = data.external.github_token.result.token
}
```

### Can I use Octo STS to access multiple repositories?

Yes, use organization trust policies with a `repositories` field:

```yaml
issuer: https://token.actions.githubusercontent.com
subject: repo:org/automation-repo:ref:refs/heads/main

permissions:
  contents: read

repositories:
  - org/repo-one
  - org/repo-two
  - org/repo-three
```

The resulting token can access all listed repositories.

## Troubleshooting

### Token exchange fails

Common causes:
- **Trust policy doesn't exist**: Verify the file exists at `.github/chainguard/{identity}.sts.yaml`
- **OIDC token doesn't match policy**: Check that issuer and subject match your OIDC token
- **App not installed**: Ensure Octo STS is installed and has access to the repository
- **Wrong branch**: Trust policies are typically read from the default branch (main/master)
- **Invalid permissions**: The policy requests permissions that don't exist or can't be granted by the app

## Operational Questions

### How long do Octo STS tokens last?

By default, tokens expire after 1 hour. 

### Can I refresh Octo STS tokens?

No, Octo STS tokens cannot be refreshed. When a token expires, exchange a new OIDC token with Octo STS to obtain a new GitHub token. This is intentional - short-lived tokens should be regularly renewed.

### What happens when Octo STS permissions are updated?

Octo STS periodically adds or removes GitHub permissions to support new use cases. When this happens:
- An issue is created in the Octo STS repository explaining the changes
- You'll receive a notification to approve the updated permissions in your GitHub App installation
- Updates are applied quarterly, with exceptions for critical changes

## Migration

### How do I migrate from PATs to Octo STS?

1. Identify where PATs are currently used
2. Determine if those systems can provide OIDC tokens
3. Create appropriate trust policies for each use case
4. Update automation to exchange OIDC tokens instead of using PATs
5. Test thoroughly in a non-production environment
6. Revoke PATs once Octo STS is working

### Can I use both PATs and Octo STS during migration?

Yes, you can use both during a transition period. This allows gradual migration and rollback capability if issues arise.

## Getting Help

### Where can I report bugs?

Report bugs in the [Octo STS GitHub repository](https://github.com/octo-sts/app/issues).

### Where can I ask questions?

- GitHub Discussions in the [Octo STS repository](https://github.com/octo-sts/app/)
- Open an issue for specific problems
- Review existing FAQ and documentation

### How can I contribute to Octo STS?

Octo STS is open source. Contributions are welcome:
- Report bugs and request features
- Improve documentation
- Submit pull requests for code changes
- Share your use cases and integration patterns

See the [repository](https://github.com/octo-sts/app) for contribution guidelines.

