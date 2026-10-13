---
title: "Manage Chainguard Workspaces sessions"
linktitle: "Manage sessions"
description: "Open, detach from, return to, list, rename, and delete Chainguard Workspaces sessions, run several terminals in one, and keep a session running while you're away."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "chainctl", "Procedural"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 30
---

A Chainguard Workspaces session lasts beyond a single terminal. You can detach from it and return later, keep it running while an agent works, run more than one terminal in it, or open several sessions on the same repository. This page explains how to do each of these with `chainctl develop`.

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

## Choose the session's repository

A session that you open on a directory is on one GitHub repository, and the session's `github` credential is scoped to it. When the session can start from one of the repository's commits, `chainctl` uploads only what differs from that commit. By default, the session is on the repository that your checkout's `origin` remote points to. If the checkout's remotes point to more than one GitHub repository, such as a fork and its upstream, `chainctl` lists them, starting with the one `origin` points to, and asks which one to use when it creates the session. Without a terminal, or with `--non-interactive`, it uses the repository that `origin` points to.

To choose ahead of time, pass `--git-remote` with the name of a remote. This example opens a session on the repository that the `upstream` remote points to:

```shell
chainctl develop --git-remote upstream --parent $ORGANIZATION
```

If the directory's session is on a different repository than the remote you name, `chainctl develop` fails and tells you to add `--new`, as described in [Open more than one session](#open-more-than-one-session).

To open a session on no repository, pass `--git-remote -`, or choose **Upload this directory on no repository** when `chainctl` asks. The session then has no `github` service, so it gets no GitHub credential, and `chainctl` uploads the whole checkout with its history, instead of only what differs from a commit. Files that `.gitignore` excludes still stay on your laptop.

Whatever the session is on, `chainctl` doesn't upload your checkout's `.git/config` file or its `.git/hooks` directory, because they can contain credentials and commands that git runs. Chainguard adds an `origin` remote that points to the session's repository, so `origin` is the session's only remote, even if you chose another remote. A session on no repository has no remotes. Your other remotes aren't in the session, and neither are hooks that you or a hook manager installed.

To fetch from or push to another of your remotes in the session, add it with its HTTPS URL:

```shell
git remote add upstream https://github.com/acme/app
```

The session's `github` credential already covers your checkout's other github.com remotes where the Chainguard App is installed, as described in [What a session can reach by default](/chainguard/workspaces/credentials/#what-a-session-can-reach-by-default). To run your hooks in the session, install them again there, for example with `pre-commit install`.

## Detach from a session

While you're attached to a session, press `Ctrl+]` to open the session menu. You can also type `~.` at the session's shell prompt, or as the first thing you type after you attach or press `Enter`. In a program that draws its own input line, such as Claude Code, `~.` works only right after `Enter`, so use `Ctrl+]` there. The menu has the following options:

| Option | Key | What it does |
| ------ | --- | ------------ |
| **Detach — let it park** | `d` or `Enter` | Returns you to your laptop's shell. The session keeps running for about 10 minutes, then parks. |
| **Detach — keep running 4h** | | Returns you to your laptop's shell and keeps the session running for 4 hours. |
| **Detach — keep running for…** | | Asks for a duration, such as `90m`, or a time, such as `17:30`, up to 24 hours from now. |
| **Park now** | | Returns you to your laptop's shell and parks the session right away, even one you're keeping running. To resume it, run `chainctl develop`, which waits for the park to finish. |
| **Restart the host** | | Parks the session and resumes it on a new host while you stay attached. Running processes continue unless the snapshot can't be restored. |
| **Rename…** | `n` | Changes the session's name. |
| **Credentials** | | Shows and changes what the session can reach. Refer to [Manage session credentials](/chainguard/workspaces/credentials/). |
| **Status** | | Shows the session's name and state, its repository and commit or its directory, its branch, its credential endpoints, what serves its laptop credentials, and the last clipboard copy. |
| **Logs** | `l` | Shows every message `chainctl` has shown since you attached, newest last. |
| **Help** | `h` or `?` | Lists every key. |
| **Back** | `Esc` | Closes the menu and returns to the session. |

The menu ignores what you type for a moment after it opens, so pause before you press a key.

The first option is what `d` or `Enter` does, and the detach options depend on the session. For a session you're already keeping running, the first option is **Detach — keeps running until** followed by a time. A session created with `--keep always` has one detach option, which shows how long it keeps running. The `--keep` flag also changes the first option, as described in [Keep a session running while you're away](#keep-a-session-running-while-youre-away).

To send `Ctrl+]` to a program in the session, press it twice. To see every key, choose **Help**, or type `~?` wherever `~.` works.

If you exit the session's shell, for example with `exit`, any other terminals you opened in the session close too. If the session isn't already being kept running, `chainctl` asks whether to keep it running while you're away. Press `Esc` to let it park.

## Return to a session

To return to a session, run `chainctl develop` from the directory you opened it on, or pass the session's name or short ID from anywhere:

```shell
chainctl develop app/quiet-harbor --parent $ORGANIZATION
```

If the session is parked, `chainctl` resumes it first, which usually takes a few seconds. The session's memory is restored along with its disk, so running processes, such as a build or an agent, continue where they stopped.

Returning to a session doesn't sync your directory again. Your directory syncs only the first time you attach, so move later changes between your laptop and the session with git.

Only one `chainctl` can be attached to a session at a time. If you attach from another terminal or laptop, the new one takes over, and the first one prints `Detached from acme/app/quiet-harbor: another client attached.` followed by the command that returns to the session.

## Keep a session running while you're away

A session that keeps running uses compute while you're away, but an agent in it can keep working. It counts against your organization's monthly allowance the whole time it runs, as described in [Availability and limits](/chainguard/workspaces/overview/#availability-and-limits).

To keep a session running, choose one of the **Detach — keep running** options in the session menu.

To decide ahead of time that a session keeps running when you detach, pass `--keep` with a duration of up to 24 hours when you open or return to it:

```shell
chainctl develop --keep 8h --parent $ORGANIZATION
```

With `--keep 8h`, the menu's first option becomes **Detach — keep running 8h**, and exiting the shell keeps the session running without asking.

For a long-running task, create a new session with `--keep always`. That session keeps running instead of parking when you detach, until 7 days after you last detach from it:

```shell
chainctl develop --keep always --name migration --parent $ORGANIZATION
```

Because it doesn't park, a `--keep always` session can use up the monthly allowance in a few days. To stop it sooner, choose **Park now** in the session menu, or delete the session.

Claude Code can keep working after you close the terminal, for as long as its credential lasts. Refer to [Keep Claude Code working while you're away](/chainguard/workspaces/coding-agents/#keep-claude-code-working-while-youre-away).

For a credential that your laptop serves, such as a `cgr.dev` login you switched to your laptop, the terminal you detached from keeps serving the session until you press `Ctrl+C` or close the terminal. After that, requests that need your laptop fail until you return to the session. Refer to [How credentials reach a session](/chainguard/workspaces/credentials/#how-credentials-reach-a-session).

## Use several terminals in a session

When you run `chainctl develop` in an interactive terminal, it keeps a status row at the bottom of the window. The row lists the session's terminals and shows each message from `chainctl` for a few seconds. It ends with `^] menu`, or with a count of messages you might have missed, such as `^] menu · 2 new`. To read them, choose **Logs** in the session menu.

A session can run up to nine terminals, for example Claude Code in one and your tests in another. `chainctl` also calls them PTYs. To manage them, press `Ctrl+]` to open the session menu, which lists the session's terminals, and then press one of the following keys:

| Key | What it does |
| --- | ------------ |
| `c` | Starts a terminal and switches to it. The new terminal opens in terminal 1's current directory. |
| `1` to `9` | Switches to that terminal. |
| `r` | Renames the terminal shown. Until you rename it, a terminal shows the title of the program running in it, or `shell`. |
| `x` | Asks you to confirm, then closes the terminal shown and stops what runs in it. |

On the status row, the name of the terminal shown is bold. A terminal you're not looking at is marked when it has new output, or when its program rings the bell or sends a notification. When a terminal's command exits, for example after you type `exit` in it, the terminal closes and the row shows the command's exit status.

Terminal 1 is the session's shell, so you can't close it with `x`. Exiting it closes the other terminals and detaches you, as described in [Detach from a session](#detach-from-a-session). When you detach from the session menu instead, every terminal stays open, and when you return from the same laptop, `chainctl` opens the terminal you were in when you left.

All the terminals share the session's `/work` directory. To run several coding agents in one session, refer to [Run several agents in parallel](/chainguard/workspaces/coding-agents/#run-several-agents-in-parallel).

If the session menu doesn't list the session's terminals, the session was created before Workspaces supported more than one, and it has only its shell.

## Open more than one session

With the free monthly allowance, each user can have one session at a time, including a parked one. To open another, delete the one you have first. To work on more than one thing at a time in a single session, open more terminals in it, as described in [Use several terminals in a session](#use-several-terminals-in-a-session).

If your organization's allowance includes more sessions, such as one arranged with your Chainguard account team, you can run several sessions on the same repository, for example to give each of several agents its own copy of the code. To open another session on a directory that already has one, pass `--new`, and optionally `--name` to choose the second part of its name:

```shell
chainctl develop --new --name scratch --parent $ORGANIZATION
```

This command creates a session named `app/scratch`. Without `--name`, `chainctl` generates a name. Once a directory has several sessions, return to one by its name or short ID.

The `--name`, `--env`, `--check`, `--cache`, and `--keep always` flags each open a new session, so you don't need `--new` with them.

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

To list every user's sessions in the organization, with an `OWNER` column, pass `--all`. Only organization owners can use `--all`, and you can return to, rename, or delete only your own sessions.

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

To use `chainctl develop` without a terminal, for example from a script or a coding agent on your laptop, pass `--non-interactive`. With it, `chainctl` never prompts or guesses. An ambiguous session reference is an error, and so is a repository with neither a `.chainguard/develop.yaml` nor a `.chainguard/ci.yaml` file, which would otherwise open on the default environment. To use the default environment, pass `--env default`.

To create a session and print its details as JSON without attaching to it, pass `--output json`:

```shell
chainctl develop --new --non-interactive --output json --parent $ORGANIZATION
```

The session's `/work` directory stays empty until you attach with `chainctl develop` from the same directory, which uploads it. Without a terminal, a session can't ask you to approve requests beyond its defaults, so it refuses them. To allow them ahead of time, pass `--with`, as described in [Manage session credentials](/chainguard/workspaces/credentials/).
