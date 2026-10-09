---
title: "Troubleshoot Chainguard Workspaces"
linktitle: "Troubleshooting"
description: "Fix common problems with Chainguard Workspaces sessions, including sessions that won't open, missing changes, Claude Code errors, and failed pushes."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "Troubleshooting"]
images: []
menu:
  docs:
    parent: "workspaces"
    identifier: "Workspaces Troubleshooting"
toc: true
weight: 70
---

This page describes common problems with Chainguard Workspaces sessions and how to fix them. If your problem isn't listed here, contact your Chainguard account team or email [support@chainguard.dev](mailto:support@chainguard.dev).

## chainctl doesn't list the develop command

During the beta, `chainctl develop` doesn't appear in `chainctl --help`. You can still run it, and `chainctl develop --help` shows its full help.

If `chainctl` reports that `develop` is an unknown command, or doesn't recognize a flag or subcommand on this site, your `chainctl` is out of date. Update it with `sudo chainctl update`, or with `brew upgrade chainctl` if you installed it with Homebrew.

## A new organization refuses to open sessions

After a trial starts, Chainguard takes about an hour to finish setting up a new organization. Until then, `chainctl develop` refuses to create sessions in it. Wait, then try again.

## A session won't open on a directory

If `chainctl develop` refuses to open a directory, the error says why. The following sections describe the most common causes.

### Several sessions match the directory

If a directory has more than one session, `chainctl` asks which one you want, or lists them and fails when it can't ask. Pass the session's name or short ID instead of the directory.

### The repository has no environment

With `--non-interactive`, a repository with no `.chainguard/ci.yaml` file is an error. Pass `--env default` to use the default environment.

### The directory is a linked worktree or submodule

`chainctl` can't sync a checkout whose `.git` is a pointer to a git directory elsewhere. Run `chainctl develop` from the main checkout, or pass the repository's URL instead.

### You reached the session limit

During a free trial, each user can have one session at a time, including a parked one, and the organization can have three. At the limit, `chainctl develop` fails with a `ResourceExhausted` error that says you're at your limit of active sessions. Delete a session you no longer need with `chainctl develop delete`, or return to the one you have.

## A session fails to start because of a package

If a session fails to start with an error about a package, such as `nothing provides` followed by a package name, the session's environment lists a package that doesn't exist or that your organization can't access. Check the package names in your `.chainguard/ci.yaml` file or `--env` file. Package names often include a version, such as `go-1.24` or `python-3.13`.

## Changes on your laptop don't appear in the session

This is expected. Your directory syncs into a session only the first time you attach. After that, changes on your laptop don't reach the session, and changes in the session don't reach your laptop. Commit and push from the session, then pull on your laptop, or the other way around.

To start a session from your laptop's current tree, open a new one with `chainctl develop --new`.

## Claude Code reports an error in the session

Claude Code in a session gets its credential from your laptop, so most errors mean your laptop can't serve it. The following sections describe the most common causes.

### No laptop is attached

The error says the request is served from the session owner's laptop and no laptop is attached. Return to the session with `chainctl develop`. To keep Claude Code working while you're away, detach with a **Detach — keep running** option and leave the terminal open.

### Your Claude login expired

`chainctl` prints a message on your laptop that your Claude credential expired. Run `claude` on your laptop, log in again, and retry in the session.

### You aren't logged in to Claude

When you attach, `chainctl` tells you that Claude isn't logged in on your laptop. Run `claude` on your laptop and log in.

### Claude Code isn't installed in the session

If `claude` isn't found in the session, the session's environment doesn't list it. Add `claude` to your environment's packages and open a new session, or open one on the default environment with `--env default`.

### Find the details in the forwarding log

`chainctl` writes every credential request it serves, and every failure, to `develop-forward.log` in its configuration directory on your laptop. On macOS, that's `~/Library/Application Support/chainctl/`. On Linux, it's `$XDG_CONFIG_HOME/chainctl/`, or `~/.config/chainctl/` if `XDG_CONFIG_HOME` isn't set.

## A push or fetch fails in the session

If `git push` or `git fetch` fails with a message that the org GitHub App can't serve the repository because it's not installed or not linked, the Chainguard App isn't installed on the GitHub account that owns the repository, or that account isn't linked to your organization. Install the app from the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new), selecting every account you work in. Then allow the repository, replacing `$OWNER` and `$REPO` with its owner and name:

```shell
chainctl develop --with github:$OWNER/$REPO --parent $ORGANIZATION
```

If the message says the request isn't allowed for the session yet, that the session owner declined it, or that nobody answered within 60 seconds, the session asked for access beyond its defaults and nobody approved it. Approve it on your attached terminal when the prompt appears, or allow it ahead of time with `--with`. Refer to [Manage session credentials](/chainguard/workspaces/credentials/).

Pushing from the session over SSH doesn't work. The session rewrites only `https://github.com/` URLs, so keep your remotes on HTTPS.

## A session runs out of space or memory

The `/tmp` directory in a session is held in memory and limited to 4 GB, a quarter of the session's 16 GB of memory. Writing large files there uses memory that your processes need. Put large files under `/var/tmp` or `/work`, which are on the session's 50 GB disk.

## A session started fresh instead of resuming

Rarely, Chainguard can't restore a parked session's snapshot. The session then starts fresh, and `chainctl` says that the parked snapshot couldn't be restored and that uncommitted work was lost. Push your work regularly so that a lost snapshot doesn't cost you much.

## A session has expired

A parked session expires 5 days after it parks, and an expired session can't be resumed. `chainctl develop list --expired` shows your expired sessions. An expired session keeps its name until you delete it, so to reuse the name, delete the expired session with `chainctl develop delete`. Then open a new session with `chainctl develop`.

## Your trial ended or its compute budget is used up

A free trial includes 500 vCPU-hours of Workspaces over 30 days:

- When your organization uses up its compute budget, Chainguard refuses to start or resume sessions, and sessions that are already running finish.
- When the 30 days end, a 7-day grace period starts, and `chainctl` warns you about it. After the grace period, Chainguard refuses every request for the organization's sessions, including attaching to a running one, with a message that the organization's access to Chainguard Workspaces has ended.

To keep using Workspaces, contact your Chainguard account team.

## chainctl can't find your session

`chainctl develop list` shows only your own sessions, so if you're logged in to `chainctl` with a different account than the one that created a session, `chainctl` reports that no session matches. In some cases, it says instead that you're logged in as one identity but the session belongs to another. Only a session's owner can attach to it. Run `chainctl auth login` and choose the account that owns the session.
