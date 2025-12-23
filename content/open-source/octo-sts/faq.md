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

Octo STS is a GitHub App developer by Chainguard that acts as a Security Token Service for GitHub. It allows workloads with OIDC tokens from various identity providers (GitHub Actions, cloud providers, Kubernetes, etc.) to exchange those tokens for short-lived GitHub access tokens. The primary goal is to eliminate the need for long-lived Personal Access Tokens (PATs).

### Why should I use Octo STS instead of Personal Access Tokens?

Personal Access Tokens are long-lived credentials that pose security risks:
- They don't expire automatically
- They're often stored in multiple places
- If leaked, they provide persistent access
- They're difficult to rotate across many systems

Octo STS provides:
- Short-lived tokens that expire automatically
- No credentials to store in your automation
- Audit trail of token usage
- Fine-grained permission control per workload

### How does Octo STS compare to GitHub's built-in GITHUB_TOKEN?

GitHub Actions provides a `GITHUB_TOKEN` automatically, but it has limitations:
- Cannot update workflow files
- Cannot trigger other workflows
- Limited to a fixed set of permissions

Octo STS tokens can:
- Update workflow files (useful for Renovate)
- Have any permissions defined in your trust policy
- Work consistently across all automation platforms, not just GitHub Actions

### Is Octo STS free to use?

Yes, octo-sts is open source and the hosted service at octo-sts.dev is free to use. You can also self-host Octo STS if you prefer.

### Can I self-host Octo STS?

Yes, octo-sts is open source and can be self-hosted. See the [Octo STS repository](https://github.com/octo-sts/app) for deployment instructions.

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

Octo STS requests a superset of permissions to support all possible use cases. However, it only creates tokens with the specific permissions defined in your trust policies. The app needs `contents: read` to read trust policy files, but all other permissions are only granted based on your policies.

### What happens if I don't create any trust policies?

If you install Octo STS but don't create trust policies, the app cannot issue any tokens. Trust policies are required to specify which identities are trusted and what permissions to grant them.

### Can I use octo-sts with private repositories?

Yes, octo-sts works with both public and private repositories. The app needs access to read the repository's trust policy files.

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

Octo STS tokens are as safe as the trust policies you create. They're short-lived (typically 1-8 hours), reducing the window of opportunity if compromised. Follow security best practices:
- Use specific subject matching
- Grant minimum required permissions
- Enable branch protection
- Regularly audit trust policies

### What if someone steals an octo-sts token?

Short-lived tokens minimize risk:
- Tokens expire automatically (default: 1 hour)
- Branch protection prevents unauthorized changes even with write permissions
- Audit logs show token usage
- Revoking the trust policy immediately prevents new token issuance

This is significantly better than stolen PATs, which are valid indefinitely until manually revoked.

### Can Octo STS tokens bypass branch protection?

No. Branch protection rules are enforced by GitHub regardless of the token type. Even with `contents: write` permission, Octo STS tokens must follow branch protection requirements like pull request reviews and status checks.

### How do I revoke access immediately?

To revoke access immediately:
1. Delete or modify the trust policy file
2. Commit and push the changes
3. New token exchanges will fail immediately
4. Existing tokens will expire based on their lifetime (typically within an hour)

For faster revocation, you can temporarily uninstall the octo-sts app from the repository, though this affects all trust policies in that repository.

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

### Can I restrict token usage by time of day?

Octo STS doesn't natively support time-based restrictions, but you can implement this in your workload by only requesting tokens during specific time windows. The workload can check the current time before calling octo-sts.

## Integration

### Can I use octo-sts with Dependabot?

Dependabot uses its own built-in token mechanism and cannot currently use octo-sts. Use octo-sts with Renovate instead for dependency updates with custom token management.

### Does octo-sts work with GitHub Enterprise?

Octo STS can work with GitHub Enterprise Server (GHES) and GitHub Enterprise Cloud (GHEC). For GHES, you may need to self-host Octo STS and configure it to work with your enterprise instance.

### Can I use octo-sts from a CI/CD system other than GitHub Actions?

Yes, octo-sts works with any system that can:
1. Obtain OIDC tokens (Jenkins, GitLab CI, CircleCI, etc.)
2. Make HTTP requests to exchange tokens
3. Use the resulting GitHub token

The key is having an OIDC identity provider that Octo STS can validate.

### How do I use octo-sts with Terraform?

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

### Can I use octo-sts to access multiple repositories?

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

### Token exchange fails with 403 Forbidden

Common causes:
- **Trust policy doesn't exist**: Verify the file exists at `.github/chainguard/{identity}.sts.yaml`
- **OIDC token doesn't match policy**: Check that issuer and subject match your OIDC token
- **App not installed**: Ensure octo-sts is installed and has access to the repository
- **Wrong branch**: Trust policies are typically read from the default branch (main/master)

Debug by examining the OIDC token claims:
```shell
echo $OIDC_TOKEN | cut -d'.' -f2 | base64 -d | jq
```

### Token exchange fails with 401 Unauthorized

This typically means the OIDC token itself is invalid:
- Token has expired
- Token signature verification failed
- Token issuer is not trusted by octo-sts

Verify your OIDC token is valid and properly signed.

### Token works but GitHub operations fail

Possible issues:
- **Insufficient permissions**: The trust policy doesn't grant the required permission (e.g., trying to push commits with only `contents: read`)
- **Branch protection**: The operation is blocked by branch protection rules (this is intentional)
- **Rate limiting**: Too many API requests are being made
- **Resource doesn't exist**: Trying to access a repository or resource that doesn't exist

Check the GitHub API error message for specific details.

### Renovate cannot update GitHub Actions

Ensure the trust policy includes `workflows: write`:

```yaml
permissions:
  contents: write
  workflows: write  # Required for updating .github/workflows/
  pull_requests: write
```

Without `workflows: write`, Renovate cannot modify workflow files.

### Token exchange succeeds but token is empty

This usually indicates a problem with the response parsing. The octo-sts API returns:

```json
{
  "access_token": "ghs_...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

Ensure you're extracting `.access_token` from the response.

### OIDC issuer cannot be reached

If octo-sts reports it cannot reach the OIDC issuer:
- Ensure the issuer URL is publicly accessible
- For private Kubernetes clusters, expose the OIDC discovery endpoint publicly
- Check that the issuer provides a `.well-known/openid-configuration` endpoint
- Verify there are no firewall rules blocking access

### Pattern matching isn't working

Common regex issues:
- **Missing anchors**: Use `^` and `$` if you need exact boundaries
- **Special characters**: Escape special regex characters in YAML (use quotes)
- **Greedy matching**: Use `.*?` for non-greedy matching instead of `.*`

Test patterns separately:
```shell
echo "repo:org/repo:ref:refs/heads/main" | grep -E "repo:org/repo:ref:refs/heads/.*"
```

## Operational Questions

### How long do Octo STS tokens last?

By default, tokens expire after 1 hour. The exact lifetime depends on the GitHub App's maximum token duration, which is currently 8 hours but typically shorter.

### Can I refresh Octo STS tokens?

No, Octo STS tokens cannot be refreshed. When a token expires, exchange a new OIDC token with Octo STS to obtain a new GitHub token. This is intentional - short-lived tokens should be regularly renewed.

### What happens when octo-sts permissions are updated?

Octo STS periodically adds or removes GitHub permissions to support new use cases. When this happens:
- An issue is created in the Octo STS repository explaining the changes
- You'll receive a notification to approve the updated permissions in your GitHub App installation
- Updates are applied quarterly, with exceptions for critical changes

### How many token exchanges can I make?

There are no hard limits imposed by octo-sts itself. However:
- GitHub API rate limits apply to the resulting tokens (5000 requests/hour for authenticated requests)
- Be considerate of the shared Octo STS service
- For high-volume use cases, consider self-hosting

### Can I see which tokens were issued?

Octo STS logs token exchanges for security auditing. Access to these logs depends on whether you're using the hosted service or self-hosting. Individual users cannot directly access exchange logs from the hosted service, but GitHub's audit logs will show API actions taken with the tokens.

### What if octo-sts.dev is down?

If the hosted Octo STS service is unavailable:
- Your automation will fail to obtain tokens
- Consider implementing retry logic with exponential backoff
- For critical services, consider self-hosting octo-sts for increased availability
- Monitor [octo-sts status](https://github.com/octo-sts/app/issues) for service updates

## Migration

### How do I migrate from PATs to octo-sts?

1. Identify where PATs are currently used
2. Determine if those systems can provide OIDC tokens
3. Create appropriate trust policies for each use case
4. Update automation to exchange OIDC tokens instead of using PATs
5. Test thoroughly in a non-production environment
6. Revoke PATs once octo-sts is working

### Can I use both PATs and octo-sts during migration?

Yes, you can use both during a transition period. This allows gradual migration and rollback capability if issues arise.

### What if my system cannot provide OIDC tokens?

If a system cannot provide OIDC tokens:
- Check if the system can be configured to use an external OIDC provider
- Consider proxying through a system that does support OIDC
- For legacy systems, PATs may still be necessary
- Contact the system vendor about OIDC support

## Getting Help

### Where can I report bugs?

Report bugs in the [octo-sts GitHub repository](https://github.com/octo-sts/app/issues).

### Where can I ask questions?

- GitHub Discussions in the [Octo STS repository](https://github.com/octo-sts/app/discussions)
- Open an issue for specific problems
- Review existing FAQ and documentation

### How can I contribute to octo-sts?

Octo STS is open source. Contributions are welcome:
- Report bugs and request features
- Improve documentation
- Submit pull requests for code changes
- Share your use cases and integration patterns

See the [repository](https://github.com/octo-sts/app) for contribution guidelines.

## Next Steps

- [Getting Started with Octo STS](/open-source/octo-sts/getting-started-with-octo-sts/) - Set up octo-sts for the first time
- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/) - Detailed trust policy documentation
- [GitHub Actions Integration](/open-source/octo-sts/how-to-use-octo-sts-with-github-actions/) - Use octo-sts with GitHub Actions
