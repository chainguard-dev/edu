---
title: "Octo STS"
linktitle: "Octo STS"
type: "article"
lead: "A security token service that eliminates the need for GitHub Personal Access Tokens by enabling OIDC-based federation for GitHub API access"
description: "Learn about Octo STS, an open source security token service for GitHub that uses OIDC federation to eliminate long-lived Personal Access Tokens"
date: 2025-12-23T15:04:05+01:00
lastmod: 2025-12-23T15:04:05+01:00
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

Octo STS operates through a trust policy model. The steps to install and use Octo STS are:

1. **Install the GitHub App**: Add the [octo-sts](https://github.com/apps/octo-sts) GitHub App to your organization or repositories
2. **Define trust policies**: Create policy files (`.github/chainguard/{name}.sts.yaml`) that specify which identities can access which resources
3. **Exchange tokens**: Workloads present OIDC tokens to Octo STS
4. **Receive GitHub tokens**: If the identity matches the trust policy, Octo STS issues a short-lived GitHub token with specified permissions

The Octo STS app needs to request a large number of permissions. This set of permissions is reviewed on a quarterly basis to ensure it meets common use cases without being overly broad.

### The Token Exchange Process

This sequence diagram outlines the token exchange process in Octo STS:

<center><img src="oct-arch.webp" alt="Octo STS sequence diagram showing order of network requests" style="width:950px;"></center>

## Common Use Cases

 - Developing Actions that create Pull Requests (a PAT is required to trigger presubmit GitHub Actions)

 - Developing Actions that interact across repositories (unsupported by built-in permissions)

 - Developing Actions that interact with the GitHub organization level

 - Providing external services (e.g. clouds) with access to repositories

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
