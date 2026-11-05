---
title: "Get started with Chainguard Workspaces"
linktitle: "Getting started"
description: "Sign up for Chainguard Workspaces, open your first development session, and learn how to detach from it and return."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-11-05T15:56:15+00:00
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

A Chainguard Workspaces *session* is a VM on Chainguard's infrastructure, not on your laptop, for one of your GitHub repositories. When you run `chainctl develop` in your repository's directory, `chainctl` creates a session, syncs your checkout into it, and opens a shell in it. There you can build, test, and run Claude Code as you would on your laptop. When you detach and come back later, your files and running processes are as you left them. To learn how sessions work, including how your directory gets into one and how a session isolates your code, refer to the [Chainguard Workspaces overview](/chainguard/workspaces/overview/) and [How Chainguard Checks and Chainguard Workspaces isolate your code](/get-started/checks-and-workspaces/how-it-works/).

This guide shows you how to open your first session. To open a session with the fewest steps, use the [quick start](#quick-start). To learn how each part works, including how to detach from a session, return to it, and delete it, follow the [step-by-step guide](#step-by-step-guide), which takes about 15 minutes.

{{< beta feature="Chainguard Workspaces" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly allowance, or that arrange access with their Chainguard account team" >}}

{{% quickstart %}}

## Quick start {#quick-start}

You need `chainctl` 0.2.386 or later and a local clone of a GitHub repository. To install or update `chainctl`, refer to [Install or update chainctl](/get-started/checks-and-workspaces/set-up/#install-or-update-chainctl). Claude Code is the only coding agent that sessions supply a credential for, and you can install others yourself. To use Claude Code in a session, [log in to Claude Code on your laptop](/chainguard/workspaces/coding-agents/#before-you-begin) first, or let Chainguard hold a Claude login for you when you open the session.

1. **Sign up**

    ```shell
    chainctl develop init
    ```

    The command creates your Chainguard organization, if you don't have one, and turns on Chainguard Workspaces. When it asks which GitHub account to link, choose the one that owns your repository: press `Enter` for your own user, or enter the organization's name.

1. **Install the Chainguard App**

    If the app isn't on that account yet, `chainctl develop init` offers to open its installation page, and finishes linking the account after you install it. You can also [install the app](https://github.com/apps/chainguard/installations/new) before you sign up.

1. **Open a session**

    In your repository's directory, run:

    ```shell
    chainctl develop
    ```

    The command creates a session, syncs your checkout into it, and opens a shell in it. To start Claude Code, run `claude` in the session. If Chainguard doesn't hold a Claude login for you yet, the command first asks whether it should, as described in [Step 2](#step-2-open-a-session).

Your session is open. To learn what's in it, and how to detach, return, and delete it when you're done, go to [Step 3: Work in the session](#step-3-work-in-the-session).
{.quick-start-done}
{{% /quickstart %}}

## Step-by-step guide {#step-by-step-guide}

The following steps open a session one step at a time and explain what `chainctl` does at each one. If you followed the quick start, your session is already open, so skip to Step 3.

### Step 1: Sign up {#step-1-sign-up}

<span id="step-1-install-or-update-chainctl"></span><span id="step-2-install-the-chainguard-app"></span><span id="step-3-sign-up-and-turn-on-checks-and-workspaces"></span>

Sign up as described in [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/). You install or update `chainctl`, install the Chainguard App on the account that owns your repository, and run `chainctl develop init`, which turns on Chainguard Workspaces and Chainguard Checks together. You also need a local clone of a repository on github.com that you can push to. Claude Code is the only coding agent that sessions supply a credential for, and you can install others yourself. Optionally, install and log in to [Claude Code](https://code.claude.com/docs/en/overview) on your laptop, so you can use it in the session. Alternatively, run `chainctl develop claude login` to let Chainguard hold a Claude login for your sessions, so that Claude Code keeps working while you're detached, as described in [Let Chainguard hold your Claude login](/chainguard/workspaces/coding-agents/#let-chainguard-hold-your-claude-login).

### Step 2: Open a session

Change to your repository's directory, then run `chainctl develop`. Replace `$REPO_DIR` with the path to your local clone, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
cd $REPO_DIR
chainctl develop --parent $ORGANIZATION
```

If you belong to only one Chainguard organization, you can omit `--parent`.

The first time you run the command in a directory, `chainctl` creates a session, syncs your directory into it, and attaches your terminal to a shell in the session. The session gets a name made of the repository name and two generated words, such as `app/quiet-harbor`, and a short ID, such as `3f9a2c1e`.

The session's tools come from its *environment*. If your repository has neither a `.chainguard/develop.yaml` file nor a `.chainguard/ci.yaml` file, the session opens on the default environment, which includes Claude Code, `vim`, and `apk` for installing more packages. If your repository has a `.chainguard/ci.yaml` file, for example because you tried [Chainguard Checks](/chainguard/checks/overview/), the session gets only the packages that the file lists, so tools such as `vim`, `apk`, and `claude` might be missing. To use the default environment instead, open the session with `chainctl develop --env default`. The `--env` flag always opens a new session, so if you're at your session limit, such as the one session that the free monthly allowance gives you, delete your current session first, as described in [Step 5](#step-5-delete-the-session). Refer to [How a session chooses its environment](/chainguard/workspaces/session-environment/#how-a-session-chooses-its-environment).

If Chainguard doesn't hold a Claude login for you, `chainctl` asks whether it should. A login that Chainguard holds sends the session short-lived tokens, so Claude Code keeps working while you're detached. To log in, answer `y`. `chainctl` opens your browser to sign in to Claude, and after you sign in, the page shows a code. Paste the code into your terminal within 5 minutes. If you answer `n`, the session uses the Claude credential on your laptop, if it has one, and `chainctl` doesn't ask again on that laptop. You can log in later with `chainctl develop claude login`, as described in [Let Chainguard hold your Claude login](/chainguard/workspaces/coding-agents/#let-chainguard-hold-your-claude-login).

Each time you attach, `chainctl` prints a line that starts with `claude:` and says which Claude credential the session uses, such as `claude: using your laptop's Claude login`.

While you're attached, `chainctl` keeps a status row at the bottom of your terminal. The row lists the session's terminals and shows messages from `chainctl`. To open more terminals in the session, refer to [Use several terminals in a session](/chainguard/workspaces/manage-sessions/#use-several-terminals-in-a-session). The first time you attach to a session from your laptop, `chainctl` also prints a short guide to the status row and the session menu's keys above the shell's prompt.

### Step 3: Work in the session

Your shell runs as `root` in `/work`, which holds your repository. Try a few commands to look around:

```shell
git status
cat /etc/chainguard/session.yaml
```

The `git status` output matches your laptop's checkout at the moment you opened the session, including uncommitted changes. The `/etc/chainguard/session.yaml` file records the session's ID, repository, and commit, and the environment it was built from.

From here, you can work as you would on your laptop. For example:

- Run `claude` to start Claude Code. It uses your laptop's Claude Code login, or the Claude login Chainguard holds for you if you ran `chainctl develop claude login`. Refer to [Use Claude Code in a session](/chainguard/workspaces/coding-agents/).
- Run `run-ci` to run your repository's checks against the working tree, if your repository uses [Chainguard Checks](/chainguard/checks/overview/), Chainguard's CI for pull requests, and its `.chainguard/ci.yaml` file defines checks.
- Install more tools with `apk`, such as `apk add vim`, if the session uses the default environment. If the session uses your repository's file and has no `apk`, add the packages to the file instead, as described in [Configure a session's environment](/chainguard/workspaces/session-environment/).
- Commit and run `git push`. Your laptop's git `user.name` and `user.email` are already set in the session, and the Chainguard App adds the credential for the push. If you connected your GitHub account with `chainctl develop github login`, the Chainguard Develop app adds it instead, as described in [Let sessions act on GitHub as you](/chainguard/workspaces/github-as-you/). To check whether you connected it, run `chainctl develop github status`.

Commits you make in a session aren't signed, because the session gets your git `user.name` and `user.email` but not your signing key or settings. If a branch requires signed commits, GitHub rejects your push to it. To get your work onto that branch, refer to [The branch requires signed commits](/chainguard/workspaces/troubleshooting/#the-branch-requires-signed-commits).

### Step 4: Detach and return to the session

To detach, press `Ctrl+]` to open the session menu, then press `Enter` or `d` to choose **Detach — keep running while busy**. Your terminal returns to your laptop's shell. The session keeps running while it's busy, such as during a build or a Claude Code turn. After it's been idle for 10 minutes, and no later than 24 hours after you last detach, it parks to a snapshot and stops using compute.

To return, run `chainctl develop` again from the same directory:

```shell
chainctl develop --parent $ORGANIZATION
```

Because the directory has exactly one session, `chainctl` reattaches to it, resuming it first if it parked. Your files, running processes, and shell are as you left them.

Your directory syncs into the session only the first time you attach. Changes you make on your laptop after that don't reach the session, and changes in the session don't reach your laptop. To move work between them, push from one and pull on the other.

### Step 5: Delete the session

A parked session expires 5 days after it parks, and until then it counts toward your session limit. With the free monthly allowance, you can have one session at a time, so delete it when you're done. First, list your sessions to find its name:

```shell
chainctl develop list --parent $ORGANIZATION
```

Then delete the session by name. This example deletes `app/quiet-harbor`:

```shell
chainctl develop delete app/quiet-harbor --parent $ORGANIZATION
```

The `delete` command asks you to confirm, then destroys the session's VM and its snapshot. Anything you didn't push is gone.

## Give teammates access {#give-teammates-access}

<span id="add-a-teammate"></span><span id="add-a-teammate-to-a-starter-organization"></span>

Each teammate opens and manages their own sessions, which count toward your organization's [limits](/chainguard/workspaces/overview/#availability-and-limits). To open sessions, a teammate needs the `owner` or `limited_owner` role, or the `sandbox.user` role. To give them one, refer to [Give teammates access](/get-started/checks-and-workspaces/set-up/#give-teammates-access).

## Next steps

- [Manage sessions](/chainguard/workspaces/manage-sessions/) covers using several terminals or sessions, keeping a session running while you're away, and the session menu.
- [Configure a session's environment](/chainguard/workspaces/session-environment/) explains how to choose the packages and network access a session gets.
- [Manage session credentials](/chainguard/workspaces/credentials/) explains what a session can reach and how to change it.
- Ask questions in the #workspaces-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
