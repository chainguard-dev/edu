---
title: "Chainguard Workspaces overview"
linktitle: "Overview"
description: "Learn how Chainguard Workspaces runs your repository and your coding agents in a remote microVM session without putting your credentials in the session."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "Overview", "AI"]
images: []
menu:
  docs:
    parent: "workspaces"
    identifier: "Workspaces Overview"
toc: true
weight: 10
---

Chainguard Workspaces moves development, and the coding agents that do it, off your laptop. The `chainctl develop` command opens a *session*: a Linux microVM in Chainguard's cloud with your repository checked out, the tools your repository needs, and, by default, Claude Code. You work in it from your own terminal.

A coding agent that runs on your laptop can read your SSH keys, cloud credentials, and browser sessions, and every package it installs runs with the same access. In a session, the agent works in a separate VM that holds no long-lived credentials. When the agent pushes to GitHub or calls Claude, the request leaves the VM without a credential, and your laptop or Chainguard adds one on the way out.

{{< beta feature="Chainguard Workspaces" access="organizations that start a free trial with `chainctl develop init`, or that arrange access with their Chainguard account team" >}}

## How a session works

When you run `chainctl develop` in a git checkout, `chainctl` creates a microVM and syncs your directory into it at `/work`. The sync includes tracked files, untracked files that `.gitignore` doesn't exclude, and the repository's history, so the session starts on exactly the tree you have, pushed or not. You get a shell in the session as `root`.

The session's packages come from Chainguard OS. If your repository has a `.chainguard/ci.yaml` file, the session installs the packages that file declares. If it doesn't, the session opens a default environment with a shell, `git`, `gh`, Claude Code, `chainctl`, and other everyday tools. Refer to [Configure a session's environment](/chainguard/workspaces/session-environment/) for details.

Sessions keep running after you detach, then park:

- When you detach, the session keeps running for about 10 minutes. You can also ask it to keep running for longer, up to 24 hours at a time.
- After that, the session *parks*: Chainguard saves its memory and disk to a snapshot and stops the VM, so it uses no compute.
- When you return, the session resumes from the snapshot in seconds, with your processes, files, and shell as you left them.
- A parked session expires 5 days after it parks.

Each session is its own VM. You can open several sessions on the same repository, for example to give each of several agents its own copy of the code, without worktrees or duplicate dependency directories on your laptop.

## How sessions get credentials

No long-lived credential enters a session. Instead, the session reaches each service through a local hostname, such as `http://github/` or `http://claude/`. Outside the VM, `chainctl` on your laptop or the Chainguard App adds the credential to each request. Depending on the service, the credential comes from your laptop, such as your Claude Code login, or from your Chainguard organization, such as the Chainguard App's access to your repositories.

By default, a session can reach the following:

- Claude, through your laptop's Claude Code login.
- The session's own GitHub repository, for fetch and push, and your checkout's other github.com remotes where the Chainguard App is installed.
- `cgr.dev`, as the Chainguard platform rather than as you.
- Your Chainguard identity, limited to read and Model Context Protocol (MCP) capabilities in the session's organization, while you're attached and for up to an hour after you detach.

When the session asks for anything else, such as fetching another private repository, `chainctl` asks you on your terminal. You can approve requests ahead of time, or take access back, at any point. Refer to [Manage session credentials](/chainguard/workspaces/credentials/) for details.

Services that use a credential from your laptop, such as Claude, work only while you're attached or while the terminal you detached from keeps serving them.

## Network access

A session reaches the open internet by default, the same as a laptop, so package managers, `git`, and build tools work without configuration. Chainguard always blocks cloud metadata endpoints, loopback addresses, and private IP ranges.

To restrict a session, give it an egress allowlist in a `.chainguard/ci.yaml` file. A session honors a check's `network.egress` allowlist the same way a check does, and refuses connections to hosts outside it while it keeps running. Unlike Chainguard Checks, though, a session whose environment has no `network` key reaches the open internet. Refer to [Network access](/chainguard/workspaces/session-environment/#network-access) for details.

## Use with Chainguard Checks

Chainguard Workspaces and [Chainguard Checks](/chainguard/checks/overview/) read the same `.chainguard/ci.yaml` file. In a session, the `run-ci` command runs your repository's checks against the working tree in `/work`, uncommitted changes included, so you or an agent can find failures before pushing. Chainguard Checks runs the same checks on each pull request and reports the results to GitHub.

The `run-ci` command runs each check in the session's own environment, which can have different packages and network access than the check declares. Its result predicts the pull request's result, but only Chainguard Checks, which runs each check in a fresh VM, decides what GitHub shows. You can use Chainguard Workspaces without Chainguard Checks, and the other way around.

## Availability and limits

Chainguard Workspaces is offered as a Technology Preview, as described in the [Chainguard Master Service and License Agreement](https://www.chainguard.dev/legal/master-service-and-license-agreement). Technology Previews aren't recommended for production use. Don't use a Technology Preview to process personal data, or any data subject to legal or regulatory compliance requirements, unless Chainguard specifically authorizes it.

During the beta, Chainguard Workspaces has the following limits:

- GitHub features, including pushing from a session, work only with repositories on github.com.
- By default, each session has 4 vCPUs, 16 GB of memory, and a 50 GB disk. The `/tmp` directory is held in memory and is limited to 4 GB, so put large files under `/var/tmp` instead.
- A session can't forward ports to your laptop.
- A free trial lasts 30 days and includes 500 vCPU-hours of Workspaces. During the trial, each user can have one session at a time, including a parked one, and the organization can have three. Each organization can start one trial.

## Get help

To ask questions or get support, use the #workspaces-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw). If you aren't a member yet, the link invites you to join.

## Next steps

- [Get started with Chainguard Workspaces](/chainguard/workspaces/getting-started/) to start a trial and open your first session.
- [Manage sessions](/chainguard/workspaces/manage-sessions/) to learn how to detach from, return to, and delete sessions.
- [Use Claude Code in a session](/chainguard/workspaces/coding-agents/) to run an agent in a session.
