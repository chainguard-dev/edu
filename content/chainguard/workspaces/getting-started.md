---
title: "Get started with Chainguard Workspaces"
linktitle: "Getting started"
description: "Start a free trial of Chainguard Workspaces, open your first development session, and learn how to detach from it and return."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
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

This guide walks you through starting a free trial of Chainguard Workspaces, opening a session on one of your repositories, detaching from the session, and returning to it. It takes about 15 minutes, plus about an hour while Chainguard finishes setting up a new organization.

{{< beta feature="Chainguard Workspaces" access="organizations that start a free trial with `chainctl develop init`, or that arrange access with their Chainguard account team" >}}

## Prerequisites

Before you begin, make sure you have the following:

- A GitHub account that can install GitHub Apps on the personal account or organization that owns your repository. To install the app on an organization and link it, you need the owner role on that organization.
- A local clone of a repository on github.com that you can push to.
- Optional: [Claude Code](https://code.claude.com/docs/en/overview) installed and logged in on your laptop.

## Step 1: Install or update chainctl

Workspaces uses the `chainctl develop` command. If you don't have `chainctl` yet, follow the [chainctl installation guide](/platform/chainctl-usage/how-to-install-chainctl/).

If you already have `chainctl`, update it to the latest release, because Workspaces changes often during the beta:

```shell
sudo chainctl update
```

If you installed `chainctl` with Homebrew, run `brew upgrade chainctl` instead. Refer to [Updating chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl) for details.

## Step 2: Install the Chainguard App

Sessions fetch and push your repository through the Chainguard App, a GitHub App that also backs [Chainguard Checks](/chainguard/checks/overview/) and [Guardener](/chainguard/guardener/). The trial setup in the next step links your Chainguard organization to the GitHub account where you install the app, and fails if the app isn't installed there.

1. Go to the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new).
2. Choose the personal account or organization that owns your repository.
3. Choose **All repositories**, or select the repositories you want to use with Workspaces.
4. Review the requested permissions and select **Install**.

## Step 3: Start a free trial

The `chainctl develop init` command signs you up and starts a free 30-day trial of both Chainguard Workspaces and Chainguard Checks. Run it in an interactive terminal, because it opens your browser and asks questions as it goes:

```shell
chainctl develop init
```

The command does the following:

1. Signs you in through your browser, and registers a new Chainguard identity if you don't have one.
2. Creates a Chainguard organization for you if you don't belong to one. If you belong to several, it asks which one to use.
3. Asks you to accept the terms that Chainguard Checks and Chainguard Workspaces are offered under.
4. Asks for the GitHub organization or user to link, and opens your browser so you can authorize the link. Enter the account name only, such as `acme`, not a URL.
5. Starts the trial and prints what it includes.

You can answer some of the questions ahead of time with flags. If you don't belong to a Chainguard organization yet, name the new one with `--name`. If you already belong to one or more, choose one with `--parent` instead. To name the GitHub account to link, pass `--github-org`. In this example, `acme-trial` is the new Chainguard organization and `acme` is the GitHub organization:

```shell
chainctl develop init --name acme-trial --github-org acme
```

Each organization can start one trial. After the trial starts, Chainguard finishes setting up a new organization within about an hour. Until then, `chainctl develop` refuses to open sessions in it.

If your organization already has Workspaces through your Chainguard account team, skip `chainctl develop init`. Instead, have an organization owner accept the terms once for the organization:

```shell
chainctl develop accept-terms --parent $ORGANIZATION
```

Replace `$ORGANIZATION` with the name of your Chainguard organization. If your GitHub account isn't linked to the organization yet, link it as described in [Getting started with Guardener](/chainguard/guardener/github/getting-started/#step-2-link-your-chainguard-organization-to-github), which uses the same Chainguard App.

## Step 4: Open a session

Change to your repository's directory, then run `chainctl develop`. Replace `$REPO_DIR` with the path to your local clone, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
cd $REPO_DIR
chainctl develop --parent $ORGANIZATION
```

If you belong to only one Chainguard organization, you can omit `--parent`.

The first time you run the command in a directory, `chainctl` creates a session, syncs your directory into it, and attaches your terminal to a shell in the session. The session gets a name made of the repository name and two generated words, such as `app/quiet-harbor`, and a short ID, such as `3f9a2c1e`. If your repository has no `.chainguard/ci.yaml` file, the session opens on the default environment.

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
- Commit and run `git push`. Your laptop's git `user.name` and `user.email` are already set in the session, and the Chainguard App adds the credential for the push.

## Step 6: Detach and return to the session

To detach, press `Ctrl+]` to open the session menu, then choose **Detach — let it park**. Your terminal returns to your laptop's shell. The session keeps running for about 10 minutes, then parks to a snapshot and stops using compute.

To return, run `chainctl develop` again from the same directory:

```shell
chainctl develop --parent $ORGANIZATION
```

Because the directory has exactly one session, `chainctl` reattaches to it, resuming it first if it parked. Your files, running processes, and shell are as you left them.

Your directory syncs into the session only the first time you attach. Changes you make on your laptop after that don't reach the session, and changes in the session don't reach your laptop. To move work between them, push from one and pull on the other.

## Step 7: Delete the session

A parked session expires 5 days after it parks. During a free trial, a parked session still counts as your one session, so delete it when you're done. First, list your sessions to find its name:

```shell
chainctl develop list --parent $ORGANIZATION
```

Then delete the session by name. This example deletes `app/quiet-harbor`:

```shell
chainctl develop delete app/quiet-harbor --parent $ORGANIZATION
```

The `delete` command asks you to confirm, then destroys the session's VM and its snapshot. Anything you didn't push is gone.

## Next steps

- [Manage sessions](/chainguard/workspaces/manage-sessions/) covers multiple sessions, keeping a session running while you're away, and the session menu.
- [Configure a session's environment](/chainguard/workspaces/session-environment/) explains how to choose the packages and network access a session gets.
- [Manage session credentials](/chainguard/workspaces/credentials/) explains what a session can reach and how to change it.
- Ask questions in the #workspaces-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
