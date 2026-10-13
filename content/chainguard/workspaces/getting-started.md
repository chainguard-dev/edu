---
title: "Get started with Chainguard Workspaces"
linktitle: "Getting started"
description: "Sign up for Chainguard Workspaces, open your first development session, and learn how to detach from it and return."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "Getting Started", "Procedural"]
images: []
menu:
  docs:
    parent: "workspaces"
    identifier: "Workspaces Getting Started"
toc: true
weight: 20
---

This guide walks you through signing up for Chainguard Workspaces, opening a session on one of your repositories, detaching from the session, and returning to it. It takes about 15 minutes.

{{< beta feature="Chainguard Workspaces" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly allowance, or that arrange access with their Chainguard account team" >}}

## Prerequisites

Before you begin, make sure you have the following:

- A GitHub account that can install GitHub Apps on the personal account or organization that owns your repository. To install the app on an organization and link it, you need the owner role on that organization.
- A local clone of a repository on github.com that you can push to.
- Optional: [Claude Code](https://code.claude.com/docs/en/overview) installed and logged in on your laptop.

## Step 1: Install or update chainctl

Workspaces uses the `chainctl develop` command. If you don't have `chainctl` yet, follow the [chainctl installation guide](/platform/chainctl-usage/how-to-install-chainctl/).

This guide needs `chainctl` 0.2.380 or later. Earlier releases can't sign you up as this guide describes or run Claude Code in a session. If you already have `chainctl`, update it to the latest release, because Workspaces changes often during the beta:

```shell
sudo chainctl update
```

If you installed `chainctl` with Homebrew, run `brew upgrade chainctl` instead. Refer to [Updating chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl) for details.

## Step 2: Install the Chainguard App

By default, sessions fetch and push your repository through the Chainguard App, a GitHub App that also backs [Chainguard Checks](/chainguard/checks/overview/) and [Guardener](/chainguard/guardener/). The sign-up in the next step links your Chainguard organization to a GitHub account.

1. Go to the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new).
2. Choose the personal account or organization that owns your repository.
3. Choose **All repositories**, or select the repositories you want to use with Workspaces.
4. Review the requested permissions and select **Install**.

## Step 3: Sign up and turn on Checks and Workspaces

The `chainctl develop init` command signs you in, creates a free [Chainguard Starter](/chainguard/containers/reference/catalog-starter/) organization if you don't have one, and turns on Chainguard Checks and Chainguard Workspaces with a free monthly allowance that resets on the first day of each month (UTC). Run it in an interactive terminal, because it opens your browser and asks questions as it goes:

```shell
chainctl develop init
```

To create an organization, sign in with an email address and password or with Google. Other sign-in methods, such as GitHub, can't create one.

The command does the following:

1. Signs you in through your browser, and registers a new Chainguard identity if you don't have one.
2. Picks the Chainguard organization to use:
   - If you don't belong to one, it asks your name, company, job title, and whether you want updates from Chainguard, then creates one. With a work email address, the organization is named after your email domain. With a personal email address, you name it, and its registry paths use its ID instead of its name.
   - If you belong to exactly one organization on the Starter or Team plan, it uses that one.
   - Otherwise, it stops and asks you to name an organization with `--parent`.
3. Asks you to accept the terms that Checks and Workspaces are offered under, if your organization hasn't accepted them yet: the Code Analysis Terms, the Secured Platform Terms, the Master Service and License Agreement (MSLA), and the Terms of Service and Data Privacy Agreement that cover linking the Chainguard App.
4. If your organization isn't linked to a GitHub account yet, asks which one to link. Link the account that owns your repository: press `Enter` for your own GitHub user, or enter the name of a GitHub organization you own, such as `acme`, not a URL. It then opens your browser so you can authorize the link. If the Chainguard App isn't installed on the account, it offers to open the page that installs it, then authorizes and links again.
5. Turns on Checks and Workspaces with the monthly allowance, and prints each product's limits, which [Availability and limits](/chainguard/workspaces/overview/#availability-and-limits) describes. If Chainguard already granted your organization an allowance, it keeps that one.
6. Offers to connect your GitHub account, if you haven't yet and your organization allows it, so that the sessions you create act on GitHub as you. The connection uses Chainguard Develop, a GitHub App separate from the Chainguard App. If you agree, it opens your browser again. If you run the command in your repository's directory, it also offers to install Chainguard Develop on the GitHub accounts your repository needs. You can decline and connect later with `chainctl develop github login`, as described in [Let sessions act on GitHub as you](/chainguard/workspaces/github-as-you/).

A GitHub account can be linked to only one Chainguard organization at a time. When you authorize the link, GitHub might ask you to authorize single sign-on for your GitHub organizations. Linking your own GitHub user doesn't need it, so you can select **Continue**. To link an organization that requires SAML single sign-on, authorize single sign-on for that organization.

You can answer some of the questions ahead of time with flags. For example, to link the `acme` GitHub organization instead of your own GitHub user:

```shell
chainctl develop init --github-org acme
```

For every flag, refer to the [`chainctl develop init` reference](/chainguard/workspaces/chainctl-develop-reference/#chainctl-develop-init).

If your company already has a Chainguard organization, `chainctl develop init` can't create another one for your email domain, so ask an owner of that organization to add you, as described in [Give teammates access](#give-teammates-access). If the command stops with an error, refer to [`chainctl develop init` fails](/chainguard/workspaces/troubleshooting/#chainctl-develop-init-fails).

If your organization already has Workspaces through your Chainguard account team, someone with the `owner` role must accept the terms before anyone can open sessions in it, as described in [`chainctl develop accept-terms`](/chainguard/workspaces/chainctl-develop-reference/#chainctl-develop-accept-terms).

## Step 4: Open a session

Change to your repository's directory, then run `chainctl develop`. Replace `$REPO_DIR` with the path to your local clone, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
cd $REPO_DIR
chainctl develop --parent $ORGANIZATION
```

If you belong to only one Chainguard organization, you can omit `--parent`.

The first time you run the command in a directory, `chainctl` creates a session, syncs your directory into it, and attaches your terminal to a shell in the session. The session gets a name made of the repository name and two generated words, such as `app/quiet-harbor`, and a short ID, such as `3f9a2c1e`. If your repository has neither a `.chainguard/develop.yaml` file nor a `.chainguard/ci.yaml` file, the session opens on the default environment.

While you're attached, `chainctl` keeps a status row at the bottom of your terminal. The row lists the session's terminals and shows messages from `chainctl`. To open more terminals in the session, refer to [Use several terminals in a session](/chainguard/workspaces/manage-sessions/#use-several-terminals-in-a-session). The first time you attach to a session from your laptop, `chainctl` also prints a short guide to the status row and the session menu's keys above the shell's prompt.

## Step 5: Work in the session

Your shell runs as `root` in `/work`, which holds your repository. Try a few commands to look around:

```shell
git status
cat /etc/chainguard/session.yaml
```

The `git status` output matches your laptop's checkout at the moment you opened the session, including uncommitted changes. The `/etc/chainguard/session.yaml` file records the session's ID, repository, and commit, and the environment it was built from.

From here, you can work as you would on your laptop. For example:

- Run `claude` to start Claude Code. It uses your laptop's Claude Code login. Refer to [Use Claude Code in a session](/chainguard/workspaces/coding-agents/).
- Run `run-ci` to run your repository's checks against the working tree, if your `.chainguard/ci.yaml` defines checks.
- Commit and run `git push`. Your laptop's git `user.name` and `user.email` are already set in the session, and the Chainguard App, or Chainguard Develop if you connected your GitHub account, adds the credential for the push.

Commits you make in a session aren't signed, because the session gets your git `user.name` and `user.email` but not your signing key or settings. If a branch requires signed commits, GitHub rejects your push to it. To get your work onto that branch, refer to [The branch requires signed commits](/chainguard/workspaces/troubleshooting/#the-branch-requires-signed-commits).

## Step 6: Detach and return to the session

To detach, press `Ctrl+]` to open the session menu, then press `Enter` or `d` to choose **Detach — let it park**. Your terminal returns to your laptop's shell. The session keeps running for about 10 minutes, then parks to a snapshot and stops using compute.

To return, run `chainctl develop` again from the same directory:

```shell
chainctl develop --parent $ORGANIZATION
```

Because the directory has exactly one session, `chainctl` reattaches to it, resuming it first if it parked. Your files, running processes, and shell are as you left them.

Your directory syncs into the session only the first time you attach. Changes you make on your laptop after that don't reach the session, and changes in the session don't reach your laptop. To move work between them, push from one and pull on the other.

## Step 7: Delete the session

A parked session expires 5 days after it parks, and until then it counts toward your session limit. With the free monthly allowance, you can have one session at a time, so delete it when you're done. First, list your sessions to find its name:

```shell
chainctl develop list --parent $ORGANIZATION
```

Then delete the session by name. This example deletes `app/quiet-harbor`:

```shell
chainctl develop delete app/quiet-harbor --parent $ORGANIZATION
```

The `delete` command asks you to confirm, then destroys the session's VM and its snapshot. Anything you didn't push is gone.

## Give teammates access

Each teammate opens and manages their own sessions, which count toward your organization's [limits](/chainguard/workspaces/overview/#availability-and-limits). To open sessions, a teammate needs the `owner` or `limited_owner` role, or the `sandbox.user` role together with `viewer`. Refer to [Roles](/chainguard/workspaces/chainctl-develop-reference/#roles).

### Add a teammate

In a Starter organization, the steps differ, as described in [Add a teammate to a Starter organization](#add-a-teammate-to-a-starter-organization). If you have the `owner` role in your organization, invite your teammate and grant them the `sandbox.user` role as follows:

1. Create an invite for your teammate with the `viewer` role. Your teammate needs it as well as `sandbox.user`, because `sandbox.user` alone doesn't let `chainctl develop` find your organization. Replace `$EMAIL` with your teammate's email address:

   ```shell
   chainctl iam invite create $ORGANIZATION --role viewer --email $EMAIL
   ```

2. Send your teammate the invite code that the command prints. Your teammate accepts the invite by logging in with it, replacing `$INVITE_CODE` with the code:

   ```shell
   chainctl auth login --invite-code $INVITE_CODE
   ```

3. After your teammate accepts, list your organization's role-bindings. The output shows each member's identity ID next to their email address:

   ```shell
   chainctl iam role-bindings list --parent $ORGANIZATION
   ```

4. Grant your teammate the `sandbox.user` role, replacing `$IDENTITY_ID` with their identity ID:

   ```shell
   chainctl iam role-bindings create --identity $IDENTITY_ID --role sandbox.user --parent $ORGANIZATION
   ```

Your teammate can then install `chainctl`, as described in [Step 1](#step-1-install-or-update-chainctl), and open a session, as described in [Step 4](#step-4-open-a-session). For more about roles, refer to [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

### Add a teammate to a Starter organization

If you created your organization with `chainctl develop init`, it's a Starter organization, and you have the `limited_owner` role rather than `owner`. You can't create role-bindings for other users, so you can't grant the `sandbox.user` role. An invite can give only a role whose permissions you also have, and of those roles, only `limited_owner` can open sessions.

To let your teammate open sessions, run step 1 of [Add a teammate](#add-a-teammate) with `--role limited_owner` instead of `--role viewer`, replacing `$EMAIL` with your teammate's email address:

```shell
chainctl iam invite create $ORGANIZATION --role limited_owner --email $EMAIL
```

The `limited_owner` role also lets its holder manage your organization's billing and invite or remove members. Your teammate accepts the invite as described in step 2 of [Add a teammate](#add-a-teammate).

Invites in a Starter organization have the following limits:

- Each invite must name your teammate's email address with `--email`, and the address must be in your organization's domain or one of its subdomains.
- If you signed up with a personal email address, you can't invite anyone.

A coworker whose email address is in your organization's domain can also ask to join by running `chainctl starter request-access`, which emails you the request.

## Next steps

- [Manage sessions](/chainguard/workspaces/manage-sessions/) covers using several terminals or sessions, keeping a session running while you're away, and the session menu.
- [Configure a session's environment](/chainguard/workspaces/session-environment/) explains how to choose the packages and network access a session gets.
- [Manage session credentials](/chainguard/workspaces/credentials/) explains what a session can reach and how to change it.
- Ask questions in the #workspaces-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
