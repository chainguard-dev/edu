---
title: "Getting Started with The Guardener"
linktitle: "Getting Started"
description: "Install The Guardener GitHub App and link your Chainguard organization to your GitHub organization to start using The Guardener."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
draft: false
tags: ["GitHub", "Getting Started"]
images: []
menu:
  docs:
    parent: "guardener"
weight: 010
toc: true
---

This guide walks you through everything you need to start using The Guardener on your GitHub repositories:

1. [Install The Guardener GitHub App](#step-1-install-the-guardener-github-app) on your GitHub organization.
2. [Link your Chainguard organization to your GitHub organization](#step-2-link-your-chainguard-organization-to-github).
3. [Verify the link](#step-3-verify-the-link) and enable your first feature.

Linking your Chainguard organization to your GitHub organization is what entitles you to use The Guardener — there is no separate entitlement step.

{{< beta feature="The Guardener" access="organizations that have installed and linked The Guardener GitHub App" >}}

## Prerequisites

Before you begin, make sure you have the following:

- **`chainctl` installed and authenticated.** If you haven't installed it yet, follow the [chainctl installation guide](/chainguard/chainctl-usage/how-to-install-chainctl/), then run `chainctl auth login`.
- **A Chainguard organization** where you are an owner, or where you otherwise hold the `guardener.association.manage` capability. This capability is required to link a GitHub organization to your Chainguard group. See the [Built-in Roles and Capabilities Reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for more information on roles.
- **Owner (admin) access to the GitHub organization** you want to link. Installing the app and authorizing the link both require GitHub organization ownership.

The `chainctl guardener` commands identify your Chainguard organization by its group name — you don't need to look up a group ID. Pass the name with `--group`, or omit the flag entirely and `chainctl` will prompt you to select from the organizations you have access to.

## Step 1: Install The Guardener GitHub App

Install The Guardener GitHub App on the GitHub organization whose repositories you want The Guardener to manage.

1. Go to the [Guardener GitHub App page](https://github.com/apps/chainguard-guardener).
2. Select **Install** (or **Configure** if it is already installed on another account).
3. Choose the GitHub organization to install it on.
4. Choose which repositories The Guardener can access. You can grant access to **All repositories** or select specific repositories. You can change this selection later in your GitHub organization settings.
5. Review the requested permissions and confirm the installation.

### Permissions The Guardener requests

The Guardener requests the minimum GitHub permissions needed to operate:

| Permission | Access | Why it's needed |
| ---------- | ------ | --------------- |
| Contents | Read & write | Read repository files (workflows, signatures, configuration) and push migration pull request branches. |
| Pull requests | Read & write | Receive pull request events, read diffs, and post review comments and pull requests. |
| Workflows | Read & write | Read and update GitHub Actions workflow files during Actions migration. |
| Checks | Write | Publish check runs that report The Guardener's results. |

Installing the app does **not** change any repository on its own. Each feature stays disabled until you opt in with a configuration file, as described in [Configuration](/chainguard/guardener/configuration/).

## Step 2: Link your Chainguard organization to GitHub

Linking associates your GitHub organization with a Chainguard group so The Guardener knows which Chainguard organization your GitHub activity belongs to.

Run `chainctl guardener github link`, passing your GitHub organization login and your Chainguard group name:

```shell
chainctl guardener github link \
  --github-org <github-org-login> \
  --group <group-name>
```

If you omit `--group`, `chainctl` prompts you to select the Chainguard organization to link.

A browser window opens to authorize with GitHub. This step proves that you own the GitHub organization. The Guardener GitHub App must already be installed on the organization (see [Step 1](#step-1-install-the-guardener-github-app)) for the link to succeed.

> **Note**: Linking requires that you are an owner of the Chainguard group (specifically, that you hold the `guardener.association.manage` capability) **and** an owner of the GitHub organization.

If you need to link your own user account rather than an organization, pass your GitHub username to `--github-org`.

## Step 3: Verify the link

After linking, confirm that The Guardener is active on your repositories:

- Open a repository that The Guardener can access and confirm The Guardener GitHub App appears under the repository's or organization's installed GitHub Apps.
- Add your first configuration file (for example, `.chainguard/actions.yaml`) as described in [Configuration](/chainguard/guardener/configuration/), then open a pull request to see The Guardener respond.

## Unlinking a GitHub organization

To remove the association between a GitHub organization and a Chainguard group, use `chainctl guardener github unlink`:

```shell
chainctl guardener github unlink \
  --github-org <github-org-login> \
  --group <group-name>
```

When you pass `--group` and hold the `guardener.association.manage` capability on that group, the organization is unlinked using your Chainguard credentials with no browser involved. Otherwise, `chainctl` falls back to the GitHub authorization flow to prove you own the organization. Either way, you must be logged in to Chainguard.

Unlinking stops The Guardener from acting on the organization's repositories. To fully remove The Guardener, also uninstall the GitHub App from your GitHub organization settings.

## Command reference

For the complete set of flags and options, see the `chainctl` reference:

- [`chainctl guardener`](/chainguard/chainctl/chainctl-docs/chainctl_guardener/)
- [`chainctl guardener github`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github/)
- [`chainctl guardener github link`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_link/)
- [`chainctl guardener github unlink`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_unlink/)

## Next steps

- **[Configuration](/chainguard/guardener/configuration/)** — Learn the `.chainguard/` configuration model and how to enable features per repository.
- **[Actions Security](/chainguard/guardener/actions-security/)** — Recommend and migrate GitHub Actions to hardened, SHA-pinned equivalents.
- **[Commit Verification](/chainguard/guardener/commit-verification/)** — Require cryptographically signed commits in pull requests.
