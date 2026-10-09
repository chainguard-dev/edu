---
title: "Use Claude Code in a Chainguard Workspaces session"
linktitle: "Use Claude Code"
description: "Run Claude Code in a Chainguard Workspaces session with your own Claude login, keep it working while you're away, and run several agents in parallel."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "AI", "Procedural"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 60
---

A Chainguard Workspaces session is a place for a coding agent to work with less risk to your laptop. The agent runs in the session's VM, which holds no long-lived credentials, and it reaches Claude through your own login on your laptop. This page explains how to run Claude Code in a session.

Claude Code is the only coding agent that sessions supply credentials for. You can install other tools in a session, but they don't get a credential from your laptop.

## Before you begin

Claude Code in a session uses the Claude login on your laptop, so set it up there first:

1. Install Claude Code on your laptop, as described in the [Claude Code documentation](https://code.claude.com/docs/en/overview).
2. Run `claude` on your laptop and log in.

The session uses the same credential Claude Code on your laptop would use, in the same order: the `ANTHROPIC_API_KEY` environment variable, an `apiKeyHelper` from your Claude Code settings, the `CLAUDE_CODE_OAUTH_TOKEN` environment variable, and then your stored Claude login. Both an API key and a Claude subscription login work.

Claude Code must also be installed in the session. The default environment includes it. If your session uses your repository's `.chainguard/ci.yaml` file, add `claude` to the file's packages, as described in [Configure a session's environment](/chainguard/workspaces/session-environment/).

## Start Claude Code

Open a session, then run `claude` in it:

```shell
claude
```

Claude Code starts without asking you to log in. Its requests go to `http://claude/` in the session, and `chainctl` on your laptop answers them with your credential. The session forwards only the Claude API's messages and models endpoints, not its account or organization endpoints.

Each session's Claude Code managed settings include a short brief that describes the session and its tools, including how to run your repository's checks with `run-ci`. Your repository's own `CLAUDE.md` and `.claude/` settings also apply, except that the managed settings allow only MCP servers reached over HTTPS, so MCP servers that your repository starts as local commands don't run.

If your laptop's Claude login has expired, Claude Code in the session reports an error from the `claude` endpoint, and `chainctl` prints a message on your laptop. Run `claude` on your laptop, log in again, and retry.

## Use Claude through Vertex AI

If your organization uses Claude through Google Cloud Vertex AI, tell `chainctl` your Google Cloud project before you create the session. Replace `$GCP_PROJECT` with your Google Cloud project ID:

```shell
chainctl config set develop.vertex.project $GCP_PROJECT
```

The region defaults to `global`. To use a different one, set `develop.vertex.region` the same way.

With these settings, `chainctl` on your laptop sends the session's Claude requests to Vertex AI with your laptop's Google Cloud application default credentials, and Chainguard configures Claude Code in the session for Vertex AI. A session keeps the route it was created with.

## Choose a permission mode

Claude Code in a session starts in its default permission mode, so it asks you before it runs commands or edits files.

Because the session is a separate VM that holds no long-lived credentials, you might choose to let Claude Code work without asking. Claude Code normally refuses `--dangerously-skip-permissions` when it runs as `root`, as it does in a session. The session sets `IS_SANDBOX=1` so that Claude Code allows it:

```shell
claude --dangerously-skip-permissions
```

Before you let an agent work unattended, consider what the session can still reach. By default, it can reach the open internet and push to its own repository. If you connected your GitHub account before you created the session, the session can also push to any repository you can access where the Chainguard App is installed, and use the `gh` CLI and the GitHub API as you, without asking you first. To narrow that, give the session an `egress` list, as described in [Network access](/chainguard/workspaces/session-environment/#network-access), and review its credentials, as described in [Manage session credentials](/chainguard/workspaces/credentials/). Requests beyond the session's defaults still need your approval on your terminal.

## Keep Claude Code working while you're away

To leave Claude Code working in a session, detach and keep the session running, rather than letting it park:

1. Press `Ctrl+]` to open the session menu.
2. Choose **Detach — keep running 4h**, or **Detach — keep running for…** to set a duration of up to 24 hours.
3. Leave the terminal open.

Claude's credential comes from your laptop, so the terminal you detached from keeps serving it, through sleep and network interruptions, until you press `Ctrl+C`. If you close that terminal or press `Ctrl+C`, Claude Code's requests fail until you return to the session. When you return, Claude Code is still running in the session, with its conversation intact.

While the terminal serves a detached session, it refuses new approval requests, so allow anything the agent will need ahead of time with `--with`.

For a task that runs longer than a day, create a session with `--keep always`. Refer to [Keep a session running while you're away](/chainguard/workspaces/manage-sessions/#keep-a-session-running-while-youre-away).

## Run several agents in parallel

During a free trial, each user can have one session at a time, so this section applies to organizations with more sessions.

Each session is its own VM with its own copy of your repository, so you can give each agent its own session. To open more sessions on the same repository, pass `--new` and a name for each one:

```shell
chainctl develop --new --name fix-auth --parent $ORGANIZATION
chainctl develop --new --name fix-cache --parent $ORGANIZATION
```

Run each command in its own terminal. Each agent works on its own branch in its own session, and pushes its work when it's done.

## Check the agent's work before it pushes

If your repository has a `.chainguard/ci.yaml` file with checks, Claude Code can run them in the session with `run-ci`, and the session's brief tells it how. You can also ask it to run `run-ci` before it pushes. The `run-ci` command exits with `0` when every check passes, `1` when a check fails, and `2` when the checks couldn't run.

To run the same checks from your laptop without attaching, use `chainctl develop check`:

```shell
chainctl develop check app/fix-auth --parent $ORGANIZATION
```

Both commands run the checks in the session's own environment, against its working tree as it is now. A pass predicts that the pull request's checks will pass, but only [Chainguard Checks](/chainguard/checks/overview/), which runs each check in a fresh VM, decides what GitHub shows.
