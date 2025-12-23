---
title: "Octo STS"
linktitle: "Octo STS"
type: "article"
lead: "A security token service that eliminates the need for GitHub Personal Access Tokens by enabling OIDC-based federation for GitHub API access"
description: "Learn about Octo STS, an open source security token service for GitHub that uses OIDC federation to eliminate long-lived Personal Access Tokens"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "Overview", "OIDC", "Security"]
draft: false
images: []
menu:
  docs:
    parent: "open-source"
weight: 100
toc: true
---

Octo STS is a GitHub App developed by Chainguard that acts as a Security Token Service (STS) for the GitHub API. It enables workloads running anywhere that can produce OIDC tokens to federate with GitHub, exchanging those tokens for short-lived GitHub access tokens. The primary goal is to eliminate the need for GitHub Personal Access Tokens (PATs), which are long-lived credentials that pose significant security risks.

## Why Octo STS Matters

Long-lived access tokens are a common target in security incidents. When attackers gain access to a PAT, they can exploit it to access repositories, make changes, and pivot to other resources. These tokens often have broad permissions and no expiration date, making them particularly dangerous if compromised.

Octo STS addresses this problem by:

- **Eliminating long-lived credentials**: No more PATs that sit around indefinitely
- **Enabling OIDC federation**: Leverage existing identity providers to authenticate workloads
- **Providing short-lived tokens**: Generated tokens expire automatically
- **Implementing fine-grained access control**: Grant only the permissions needed for specific tasks
- **Supporting multiple identity providers**: Works with GitHub Actions, cloud providers (AWS, GCP, Azure), Kubernetes, and any OIDC-compliant system

## How Octo STS Works

Octo STS operates through a trust policy model:

1. **Install the GitHub App**: Add the [octo-sts](https://github.com/apps/octo-sts) GitHub App to your organization or repositories
2. **Define trust policies**: Create policy files that specify which identities can access which resources
3. **Exchange tokens**: Workloads present OIDC tokens to Octo STS
4. **Receive GitHub tokens**: If the identity matches the trust policy, Octo STS issues a short-lived GitHub token with specified permissions

### The Token Exchange Process

```
[Workload] → OIDC Token → [Octo STS] → Validates → Trust Policy
                                          ↓
                            Short-lived GitHub Token ← Returns
```

The workload can then use this GitHub token to interact with the GitHub API, open pull requests, push commits, or perform other operations as defined by the trust policy.

## Key Features

**OIDC-Based Federation**
Octo STS validates OIDC tokens from various identity providers, including GitHub Actions, cloud provider identity services, and Kubernetes service accounts.

**Fine-Grained Access Control**
Trust policies specify exactly which permissions to grant, following the principle of least privilege. You can create different policies for different workloads.

**Pattern Matching**
Trust policies support both exact matching and regular expressions for flexible identity validation, including custom claim matching.

**Repository and Organization Scope**
Policies can be scoped to individual repositories or shared across an organization, providing flexibility in how you manage access.

**Automatic Token Expiration**
All tokens issued by Octo STS are short-lived, reducing the window of opportunity if a token is compromised.

## Common Use Cases

**Automated Dependency Updates**
Run tools like Renovate as GitHub Actions without storing PATs, automatically opening pull requests to update dependencies.

**CI/CD Pipelines**
Enable continuous integration and deployment workflows from cloud environments or Kubernetes clusters to interact with GitHub securely.

**GitOps Workflows**
Allow Kubernetes operators and controllers to update repository contents without long-lived credentials.

**Cloud-to-GitHub Integration**
Connect cloud workloads running in AWS, GCP, or Azure to GitHub repositories using native cloud identity.

**Multi-Repository Automation**
Create organization-level policies that allow automation tools to work across multiple repositories with appropriate permissions.

## Security Model

Octo STS implements several security best practices:

- **Branch protection enforcement**: Policies cannot bypass repository branch protection rules
- **Audit trail**: All token exchanges are logged for security monitoring
- **Minimal permissions**: The app requests a superset of permissions but only grants what's specified in trust policies
- **Regular permission reviews**: The Octo STS team updates permissions quarterly with community notification

## Getting Started

To begin using Octo STS:

1. [Install the octo-sts GitHub App](https://github.com/apps/octo-sts)
2. Create your first trust policy in `.github/chainguard/{name}.sts.yaml`
3. Configure your workload to exchange its OIDC token
4. Test the token exchange and verify permissions

For detailed instructions, see the [Getting Started with Octo STS](/open-source/octo-sts/getting-started-with-octo-sts/) guide.

## Learn More

- [Getting Started with Octo STS](/open-source/octo-sts/getting-started-with-octo-sts/) - Set up Octo STS and create your first trust policy
- [Using Octo STS with GitHub Actions](/open-source/octo-sts/how-to-use-octo-sts-with-github-actions/) - Integrate Octo STS into GitHub Actions workflows
- [Using Octo STS with Kubernetes](/open-source/octo-sts/how-to-use-octo-sts-with-kubernetes/) - Federate Kubernetes workload identities with GitHub
- [Using Octo STS with Cloud Providers](/open-source/octo-sts/how-to-use-octo-sts-with-cloud-providers/) - Connect AWS, GCP, and Azure workloads to GitHub
- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/) - Complete trust policy syntax and options
- [FAQ](/open-source/octo-sts/faq/) - Frequently asked questions and troubleshooting

## Resources

- [Octo STS GitHub Repository](https://github.com/octo-sts/app)
- [Original Blog Post](https://www.chainguard.dev/unchained/the-end-of-github-pats-you-cant-leak-what-you-dont-have)
- [Trust Policy JSON Schema](https://raw.githubusercontent.com/octo-sts/app/refs/heads/main/pkg/octosts/octosts.TrustPolicy.json)
