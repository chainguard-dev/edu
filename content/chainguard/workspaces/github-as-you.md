---
title: "Let Chainguard Workspaces sessions act on GitHub as you"
linktitle: "Act on GitHub as you"
description: "Connect your GitHub account so that the Chainguard Workspaces sessions you create act on GitHub as you through the Chainguard Develop GitHub App, and learn how to limit what those sessions can do."
type: "article"
date: 2026-10-12T00:00:00+00:00
lastmod: 2026-10-20T14:50:35+00:00
draft: false
tags: ["Chainguard Workspaces", "Security", "Procedural"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 55
---

By default, a Chainguard Workspaces session reaches GitHub through the Chainguard App with access to specific repositories, as described in [Manage session credentials](/chainguard/workspaces/credentials/). If you connect your GitHub account, the sessions you create afterward act on GitHub as you instead, unless your organization's `user_github` policy bans it. They act through the Chainguard Develop GitHub App (`chainguard-develop`), which is separate from the Chainguard App that runs Chainguard Checks. A session that acts as you can do the following:

- Fetch and push with `git` for any repository you can access where the Chainguard Develop app is installed.
- Use the `gh` CLI and the GitHub API, within the app's permissions and your own access.

This page explains how to connect your account, where to install the app, and how to limit what these sessions can do.

## Connect your GitHub account

Your organization's policy allows this by default, so an organization owner doesn't need to turn anything on. To have the sessions you create act on GitHub as you, connect your GitHub account once. If a GitHub organization you work in requires SAML single sign-on, sign in to it in your browser first. `chainctl` opens your browser so you can authorize the connection:

```shell
chainctl develop github login
```

`chainctl develop init` offers the same step when you sign up, as described in [Get started with Chainguard Workspaces](/chainguard/workspaces/getting-started/).

The connection applies to the sessions you create in every organization that doesn't ban it, and renews itself until you disconnect it. No GitHub token is written to your laptop. If your organization allows it and you haven't connected an account, or your connection expired or was revoked, `chainctl develop` prints a one-line reminder when it creates a session, and creates the session anyway. To disconnect, run `chainctl develop github logout`.

Each session keeps the GitHub identity it was created with, so connecting your account doesn't change the sessions you already have. After you disconnect, a session that acts as you refuses `git` and `gh` requests until you connect again, and `chainctl` offers to connect your account when you attach to it.

## Install the Chainguard Develop app {#install-the-chainguard-develop-app}

A session that acts as you reaches only the repositories where the Chainguard Develop app is installed. Install it from the [Chainguard Develop installation page](https://github.com/apps/chainguard-develop/installations/new) on the following accounts:

- Every GitHub organization or account that owns a private repository your sessions fetch. Sessions read public repositories without the app.
- Every organization or account that owns a repository your sessions push to.
- Your own GitHub account, for your own repositories and forks.

An organization owner installs the app on an organization, and a member can request it. The app asks for read and write access to contents, pull requests, and workflows, and read-only access to checks, commit statuses, and actions.

On a terminal, `chainctl develop github login` and `chainctl develop init` check which accounts the checkout in your current directory needs, and walk you through each installation that's missing. To check again later, run `chainctl develop github status` in your checkout. It shows your GitHub account, the app it's connected through, whether the connection works, whether your organization's policy allows sessions to act as you, and which accounts still need the app.

If the app can't reach a repository that a session needs, `chainctl develop` or the failed `git` command says why and where to fix it. Refer to [A session that acts as you can't reach a repository](/chainguard/workspaces/troubleshooting/#a-session-that-acts-as-you-cant-reach-a-repository).

## What a session that acts as you can do

A session that acts as you can do anything your GitHub account can, within the Chainguard Develop app's permissions, and GitHub attributes everything it does to you:

- It can approve other people's pull requests, and its approvals count toward required reviews and code owner reviews as yours would. GitHub doesn't let it approve pull requests you opened.
- It can merge any pull request you can merge, including with auto-merge or a merge queue.
- It can push changes to files in `.github/workflows`. A workflow that the session pushes can run on GitHub Actions with a `GITHUB_TOKEN` whose permissions the workflow file sets, so the workflow can create check runs and commit statuses and rerun workflows. If the repository allows GitHub Actions to create and approve pull requests, the workflow can also approve pull requests as `github-actions[bot]`, including ones you opened, and those approvals count toward required reviews. To limit this, refer to [Protect your branches](#protect-your-branches).
- It can't directly create or update check runs or commit statuses, or rerun GitHub Actions workflows, because the app can only read them. To rerun Chainguard Checks from a session, use `chainctl checks rerun`, as described in [Your Chainguard identity in a session](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session).

## Protect your branches {#protect-your-branches}

Because an agent in a session that acts as you can approve and merge as you, protect the branches it shouldn't change on its own with a branch protection rule or ruleset. Require pull request reviews, and turn on **Require approval of the most recent reviewable push**, so that someone other than the account that pushed last must approve each pull request.

Required reviews take effect only when a pull request merges. A session that acts as you can push a workflow to a new branch, and GitHub can run that workflow, with access to the repository's secrets and a `GITHUB_TOKEN`, before anyone reviews it. To keep a session from pushing workflow changes, and to keep workflows from approving pull requests, also do the following:

- Add a [push ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#creating-a-push-ruleset) with a **Restrict file paths** rule for `.github/workflows/**/*`. It blocks pushes that change workflow files on every branch, except from the actors on the ruleset's bypass list. Push rulesets are available for private and internal repositories on GitHub Team and GitHub Enterprise Cloud plans.
- In your repository or organization settings, go to **Actions > General**, and under **Workflow permissions**, clear **Allow GitHub Actions to create and approve pull requests**. A workflow then can't use its `GITHUB_TOKEN` to approve a pull request, or to open one.

## Controls that don't apply to a session that acts as you {#controls-that-dont-apply-to-a-session-that-acts-as-you}

For a session that acts as you, `chainctl` doesn't ask you to approve GitHub requests, and the session's `github` source and bindings aren't used. The following have no effect on its GitHub access:

- `github:` entries of `--with`, and `--with all`
- The GitHub part of `--with none`, which still turns off `claude`, `cgr.dev`, `chainguard`, and `gcp`
- `chainctl develop creds --revoke github:...` and `--source github=...`
- Your organization's `--org-github` and `--org-github-push-beyond-session` settings

`chainctl develop creds` shows that the session acts as you on GitHub, and tells you when a change to its `github` credential has no effect. To keep a new session off your GitHub account, run `chainctl develop github logout` before you create the session, or have an organization owner ban sessions from acting as their owner.

## Ban sessions from acting as their owner

To ban sessions in an organization from acting as their owner, run the following command with the permissions described in [Set your organization's GitHub policy](/chainguard/workspaces/credentials/#set-your-organizations-github-policy):

```shell
chainctl develop policy set --user-github=false --parent $ORGANIZATION
```

Replace `$ORGANIZATION` with the name of your Chainguard organization. New sessions in the organization then reach GitHub through their `github` source, as sessions do by default. Sessions that already act as their owner refuse GitHub requests while the ban is on. To lift the ban, set `--user-github=true`. Sessions created during the ban keep reaching GitHub through their `github` source after you lift it.
