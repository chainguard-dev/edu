---
title: "Manage Chainguard Workspaces sessions"
linktitle: "Manage sessions"
description: "Open, detach from, return to, list, rename, and delete Chainguard Workspaces sessions, and keep a session running while you're away."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "chainctl", "Procedural"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 30
---

A Chainguard Workspaces session lasts beyond a single terminal. You can detach from it and return later, keep it running while an agent works, or open several sessions on the same repository. This page explains how to do each of these with `chainctl develop`.

The examples on this page use `$ORGANIZATION` for the name of your Chainguard organization. If you belong to only one organization, you can omit `--parent`.

## How chainctl develop chooses a session

The `chainctl develop` command takes one optional argument, which tells it what to open:

| Argument | What `chainctl develop` does |
| -------- | ---------------------------- |
| None, or a directory | Reattaches to the directory's session if it has exactly one, and creates one if it has none. If the directory has several sessions, it asks which one you want. |
| A subdirectory of a checkout | Opens the whole repository with its history, and starts the shell in the subdirectory. |
| A repository URL, such as `github.com/acme/app` | Opens the repository at its default branch, without syncing a local directory. |
| A session name, such as `app/quiet-harbor`, or a short ID, such as `3f9a2c1e` | Returns to that session. |

Sessions you open from a directory and sessions you open from a repository URL are separate. Running `chainctl develop github.com/acme/app` doesn't return to a session you opened from your local clone of that repository.

## Detach from a session

While you're attached to a session, press `Ctrl+]` to open the session menu. You can also type `~.` at the start of a line. The menu has the following options:

| Option | What it does |
| ------ | ------------ |
| **Detach — let it park** | Returns you to your laptop's shell. The session keeps running for about 10 minutes, then parks. |
| **Detach — keep running 4h** | Returns you to your laptop's shell and keeps the session running for 4 hours. |
| **Detach — keep running for…** | Asks for a duration, such as `90m`, or a time, such as `17:30`, up to 24 hours from now. |
| **Rename…** | Changes the session's name. |
| **Credentials** | Shows what the session can reach. Refer to [Manage session credentials](/chainguard/workspaces/credentials/). |
| **Status** | Shows the session's state. |
| **Back** | Closes the menu and returns to the session. |

To send `Ctrl+]` to a program in the session, press it twice. To list the other escape sequences, type `~?` at the start of a line.

If you exit the session's shell, for example with `exit`, `chainctl` asks whether to keep the session running while you're away. Press `Esc` to let it park.

## Return to a session

To return to a session, run `chainctl develop` from the directory you opened it on, or pass the session's name or short ID from anywhere:

```shell
chainctl develop app/quiet-harbor --parent $ORGANIZATION
```

If the session is parked, `chainctl` resumes it first, which usually takes a few seconds. The session's memory is restored along with its disk, so running processes, such as a build or an agent, continue where they stopped.

Returning to a session doesn't sync your directory again. Your directory syncs only the first time you attach, so move later changes between your laptop and the session with git.

## Keep a session running while you're away

A session that keeps running uses compute while you're away, but an agent in it can keep working. To keep a session running, choose one of the **Detach — keep running** options in the session menu.

To decide ahead of time that a session keeps running when you detach, pass `--keep` with a duration of up to 24 hours when you open or return to it:

```shell
chainctl develop --keep 8h --parent $ORGANIZATION
```

With `--keep 8h`, the menu's first option becomes **Detach — keep running 8h**, and exiting the shell keeps the session running without asking.

For a long-running task, create a new session with `--keep always`. That session keeps running instead of parking when you detach, until 7 days after you last detach from it:

```shell
chainctl develop --keep always --name migration --parent $ORGANIZATION
```

Some credentials, including the one Claude Code uses, come from your laptop. If your terminal served one of them while you were attached, it keeps serving after you detach and keep the session running, through sleep and network interruptions, until you press `Ctrl+C`. If you close the terminal or press `Ctrl+C`, Claude Code stops working in the session until you return to it. Refer to [Use Claude Code in a session](/chainguard/workspaces/coding-agents/) for details.

## Open more than one session

During a free trial, each user can have one session at a time, including a parked one. To open another, delete the one you have first.

Outside the trial limit, you can run several sessions on the same repository, for example to give each of several agents its own copy of the code. To open another session on a directory that already has one, pass `--new`, and optionally `--name` to choose the second part of its name:

```shell
chainctl develop --new --name scratch --parent $ORGANIZATION
```

This command creates a session named `app/scratch`. Without `--name`, `chainctl` generates a name. Once a directory has several sessions, return to one by its name or short ID.

The `--name`, `--env`, `--check`, and `--keep always` flags each open a new session, so you don't need `--new` with them.

## List sessions

To list your sessions, most recently used first, run `chainctl develop list`:

```shell
chainctl develop list --parent $ORGANIZATION
```

The output shows each session's name, the branch checked out in it, its state, and when you last used it:

```
         NAME          |  BRANCH   |         STATE          | LAST USED
-----------------------|-----------|------------------------|-----------
 acme/app/quiet-harbor | main      | running, parks in 6m   | 4m ago
 acme/app/scratch      | fix-tests | parked, expires Oct 13 | 2d ago
```

The `STATE` column tells you whether a session is running, when it parks or stops running, and when a parked session expires. To add each session's commit, environment, and directory, pass `-o wide`. To include expired sessions, pass `--expired`.

## Rename a session

To rename a session, pass its current name or short ID and the new second part of its name. The repository part stays the same:

```shell
chainctl develop rename app/quiet-harbor tests --parent $ORGANIZATION
```

This command renames the session to `app/tests`.

## Delete a session

A parked session expires 5 days after it parks. Chainguard then discards its VM and snapshot, but the session stays in `chainctl develop list --expired`, and its name stays in use until you delete it. To delete a session, run `chainctl develop delete` with its name or short ID:

```shell
chainctl develop delete app/scratch --parent $ORGANIZATION
```

The command asks you to confirm, then destroys the session's VM and its snapshot. Anything in the session that you didn't push is lost. To skip the confirmation, for example in a script, pass `--yes`.

## Use sessions from scripts

To use `chainctl develop` without a terminal, for example from a script or a coding agent on your laptop, pass `--non-interactive`. With it, `chainctl` never prompts: an ambiguous session reference, or a repository with no `.chainguard/ci.yaml`, is an error instead of a question.

To create a session and print its details as JSON without attaching to it, pass `--output json`:

```shell
chainctl develop --new --non-interactive --output json --parent $ORGANIZATION
```

The session's `/work` directory stays empty until you attach with `chainctl develop` from the same directory, which uploads it. Without a terminal, a session can't ask you to approve requests beyond its defaults, so it refuses them. To allow them ahead of time, pass `--with`, as described in [Manage session credentials](/chainguard/workspaces/credentials/).
