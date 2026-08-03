---
title: "Managing GitHub App Connections"
linktitle: "App Connections"
description: "Set up, inspect, and remove the connections between your Chainguard organization and your GitHub organizations for Chainguard Guardener."
type: "article"
date: 2026-08-03T00:00:00+00:00
lastmod: 2026-08-03T00:00:00+00:00
draft: false
tags: ["GitHub", "Configuration"]
images: []
menu:
  docs:
    parent: "guardener-github"
weight: 015
toc: true
---

Chainguard Guardener acts on your GitHub repositories on behalf of your Chainguard organization. The bridge between the two is a **connection**: a Guardener GitHub App installation on a GitHub organization, linked to a Chainguard organization. This page explains how connections work and how to set up, inspect, change, and remove them.

For a first-time walkthrough, refer to [Getting Started](/chainguard/guardener/github/getting-started/). This page is the fuller reference for managing connections over time.

{{< beta feature="Chainguard Guardener" access="organizations that have installed and linked the Chainguard Guardener GitHub App" >}}

## How connections work

A connection has two halves, one on each side:

1. **A GitHub App installation** — the [Guardener GitHub App](https://github.com/apps/chainguard-guardener) installed on a GitHub organization (or personal account). The installation is what grants the Guardener access to repositories and delivers repository events to it. GitHub assigns each installation a numeric **installation ID**.
2. **A link** — an association, stored on the Chainguard platform, between that installation and a Chainguard organization. The link is what tells the Guardener which Chainguard organization the GitHub activity belongs to, and it is what entitles the organization to use the Guardener.

Both halves are required. Installing the app without linking leaves the Guardener inactive; linking fails if the app is not installed.

A few rules govern connections:

- **A GitHub organization can be linked to exactly one Chainguard organization at a time.** Linking an organization that is already linked elsewhere fails with an "already linked to a different Chainguard group" error; unlink it first (refer to [Moving a GitHub organization](#moving-a-github-organization-to-a-different-chainguard-organization)).
- **A Chainguard organization can link any number of GitHub organizations.** Each linked GitHub organization appears as its own connection.
- **Personal accounts work like organizations.** To connect your own GitHub user account instead of an organization, install the app on your account and pass your GitHub username as the organization.
- **Re-linking is safe.** Linking a GitHub organization that is already linked to the same Chainguard organization succeeds without changing anything.

### Required permissions

The `chainctl guardener github` commands check permissions on both sides of the connection:

| Action | Requires |
| ------ | -------- |
| Link (`link`) | **Both**: the `guardener.association.manage` capability on the Chainguard organization (held by owners), **and** ownership of the GitHub organization. |
| List connections (`status`) | The `guardener.association.list` capability on the Chainguard organization. |
| Unlink (`unlink`) | **Either**: the `guardener.association.manage` capability on the Chainguard organization, **or** ownership of the GitHub organization (refer to [Removing a connection](#removing-a-connection)). |

Refer to the [Built-in Roles and Capabilities Reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for how capabilities map to roles.

Commands that prove GitHub organization ownership (`link`, and the fallback path of `unlink`) open a browser window to authorize with GitHub. Listing connections with `status` is read-only and never involves a browser.

## Setting up a connection

### Step 1: Install the Guardener GitHub App

Install the app on the GitHub organization whose repositories the Guardener should manage:

1. Go to the [Guardener GitHub App page](https://github.com/apps/chainguard-guardener).
2. Select **Install** (or **Configure** if it is already installed on another account).
3. Choose the GitHub organization (or your personal account) to install it on.
4. Choose which repositories the Guardener can access — **All repositories** or a selected subset. You can change this later (refer to [Changing repository access](#changing-which-repositories-are-connected)).
5. Review the requested permissions and confirm.

Installing the app does not change any repository on its own. Every Guardener feature stays disabled until you opt in with a configuration file, as described in [Configuration](/chainguard/guardener/github/configuration/).

### Step 2: Link the GitHub organization to your Chainguard organization

Run `chainctl guardener github link`, passing the GitHub organization login and your Chainguard organization name:

```shell
chainctl guardener github link \
  --github-org <github-org-login> \
  --group <organization-name>
```

If you omit `--group`, `chainctl` prompts you to select from the Chainguard organizations you have access to.

A browser window opens to authorize with GitHub; completing it proves that you own the GitHub organization. On success, `chainctl` prints the linked organization and its installation ID:

```
Linked GitHub organization "example-org" to group example.com (installation 12345678).
```

> **Note:** The first time an organization links a GitHub organization, `chainctl` prompts you to accept the Chainguard Guardener [Terms of Service](https://www.chainguard.dev/legal/guardener) and [Data Privacy Agreement](https://www.chainguard.dev/legal/supplemental-dpa) on behalf of your organization. Acceptance is recorded once per organization and covers subsequent links.

If the browser flow cannot use its default local port (8989), pass a different one with `--port`.

### Step 3: Verify the connection

List the connections for your Chainguard organization:

```shell
chainctl guardener github status --group <organization-name>
```

The linked GitHub organization should appear in the output, as described in the next section.

## Inspecting connections

`chainctl guardener github status` lists every GitHub organization linked to a Chainguard organization:

```
Repository visibility scope: PUBLIC (default; public repositories only)

ORGANIZATION  INSTALLATION ID  SETTINGS
example-org   12345678         https://github.com/settings/installations/12345678
```

- **ORGANIZATION** — the GitHub organization (or user) login for the connection.
- **INSTALLATION ID** — GitHub's identifier for the app installation backing the connection.
- **SETTINGS** — the GitHub settings page for the installation, where a GitHub owner can review its permissions and repository access.

### Repository visibility scope

Above the connection list, `status` prints the organization's **repository visibility scope**, which controls which repositories the Guardener responds to across all of the organization's connections:

- **PUBLIC** (the default) — the Guardener acts on public repositories only, even when the installation grants it access to private repositories.
- **ALL** — the Guardener acts on both public and private repositories.

The visibility scope is managed by Chainguard. If you need the Guardener to cover private repositories, contact Chainguard support to have your organization's scope updated.

> **Note:** Reading the visibility scope requires the `guardener.entitlement.list` capability. Without it, `status` still lists your connections and prints a warning that the scope was skipped.

## Changing which repositories are connected

Repository access is controlled on the GitHub side, by the app installation. To change it:

1. Open the installation's settings page — the **SETTINGS** URL from `chainctl guardener github status`, or your GitHub organization's **Settings → GitHub Apps** page.
2. Under **Repository access**, switch between **All repositories** and **Only select repositories**, or adjust the selected list.

No change on the Chainguard side is needed; the existing link continues to apply to whatever the installation can access. Remember that access alone does nothing — each repository still needs a `.chainguard/` configuration file (or an org-level default) to enable a feature, and the [repository visibility scope](#repository-visibility-scope) still applies.

## Moving a GitHub organization to a different Chainguard organization

Because a GitHub organization can be linked to only one Chainguard organization at a time, moving it is an unlink followed by a link:

```shell
chainctl guardener github unlink \
  --github-org <github-org-login> \
  --group <old-organization>

chainctl guardener github link \
  --github-org <github-org-login> \
  --group <new-organization>
```

The GitHub App installation is untouched by the move; only the Chainguard-side association changes.

## Removing a connection

To remove a connection, unlink the GitHub organization:

```shell
chainctl guardener github unlink \
  --github-org <github-org-login> \
  --group <organization-name>
```

Unlinking accepts either side's authority:

- **Chainguard credentials.** When you pass `--group` and hold the `guardener.association.manage` capability on that organization, the unlink completes with no browser involved.
- **GitHub ownership.** Otherwise — including when you have lost access to the Chainguard organization — `chainctl` falls back to the GitHub authorization flow, and proving that you own the GitHub organization is sufficient. You must still be logged in to Chainguard (`chainctl auth login`), but no access to the linked organization is required.

Unlinking stops the Guardener from acting on the organization's repositories. To fully remove the Guardener, also uninstall the GitHub App from your GitHub organization's **Settings → GitHub Apps** page. Uninstalling only the app (without unlinking) also stops the Guardener, but leaves a dangling association; prefer unlinking first.

## Troubleshooting

**"the guardener GitHub App must be installed on the GitHub account (organization or user) before it can be linked"**
Linking checks for an existing installation. Install the app on the GitHub organization ([Step 1](#step-1-install-the-guardener-github-app)), then run `link` again.

**"that GitHub organization is already linked to a different Chainguard group"**
Each GitHub organization can be linked to only one Chainguard organization. Unlink it from its current organization first — anyone who owns the GitHub organization can do this, even without access to the current Chainguard organization (refer to [Removing a connection](#removing-a-connection)).

**The browser authorization fails or never completes**
The GitHub flow requires that you are an owner of the GitHub organization; membership alone is not enough. If the local callback port is in use, re-run the command with `--port <port>`. The flow times out after a few minutes — re-run the command to try again.

**`status` shows the connection but the Guardener isn't doing anything**
A connection alone changes nothing. Check that the repository is covered by the installation's repository access, that its visibility matches your [repository visibility scope](#repository-visibility-scope), and that the feature you expect is enabled by a `.chainguard/` configuration file (refer to [Configuration](/chainguard/guardener/github/configuration/)).

## Command reference

For the complete set of flags and options, refer to the `chainctl` reference:

- [`chainctl guardener`](/chainguard/chainctl/chainctl-docs/chainctl_guardener/)
- [`chainctl guardener github`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github/)
- [`chainctl guardener github link`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_link/)
- [`chainctl guardener github unlink`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_unlink/)

## Next steps

- **[Configuration](/chainguard/guardener/github/configuration/)** — Enable Guardener features with `.chainguard/` configuration files.
- **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommend and migrate GitHub Actions to hardened, SHA-pinned equivalents.
- **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Require cryptographically signed commits in pull requests.
