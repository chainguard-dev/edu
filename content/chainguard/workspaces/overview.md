---
title: "Chainguard Workspaces overview"
linktitle: "Overview"
description: "Learn how Chainguard Workspaces runs your repository and your coding agents in a remote microVM session without putting your credentials in the session."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-20T12:09:53+00:00
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

{{< beta feature="Chainguard Workspaces" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly allowance, or that arrange access with their Chainguard account team" >}}

## How a session works

When you run `chainctl develop` in a git checkout, `chainctl` creates a microVM and syncs your directory into it at `/work`. The sync includes tracked files, untracked files that `.gitignore` doesn't exclude, and the repository's history, so the session starts on exactly the tree you have, pushed or not. Symbolic links arrive as links, not as the files that they point to, and `chainctl` skips sockets, devices, and named pipes. Submodules arrive as empty directories, and they're also empty in a session that you open from a repository URL. By default, you get a `bash` shell in the session as `root`.

When your checkout has a github.com remote, the session is on one GitHub repository, as described in [Choose the session's repository](/chainguard/workspaces/manage-sessions/#choose-the-sessions-repository). Other directories sync differently:

- A checkout with no github.com remote syncs with its history, but it has no remotes in the session, and the session gets no GitHub credential.
- A directory that isn't a git checkout syncs every file in it, including dotfiles such as `.env`, and the session gets no GitHub credential.

How much of your `.git` directory the sync sends depends on whether the session can start from a commit that its GitHub repository already has. If it can, `chainctl` sends only the commits that your current branch has beyond that commit, and the files that differ from it. Otherwise, it sends your whole `.git` directory except your `.git/config` file and your `.git/hooks` directory. That includes stashes, reflogs, your other branches and tags, and objects that git hasn't pruned yet from commits that you rewrote or deleted. `chainctl` also sends the whole `.git` directory when it can't send only the differences, such as when the checkout has submodules or unresolved merge conflicts. If a secret was ever committed or stashed in the checkout, or in a repository nested in it, assume that it can reach the session.

The session's packages come from [Chainguard's package repositories](/chainguard/containers/building-and-modifying/packages/package-model/). If your repository has a `.chainguard/develop.yaml` file, the session installs the packages that file declares. Otherwise, it installs the packages your `.chainguard/ci.yaml` file declares. If the repository has neither file, the session opens a default environment with a shell, `git`, `gh`, Claude Code, `chainctl`, and other everyday tools. Refer to [Configure a session's environment](/chainguard/workspaces/session-environment/) for details.

Sessions keep running after you detach, then park:

- When you detach, the session keeps running while it's busy, such as during a build or a Claude Code turn, and until it's been idle for 10 minutes, up to 24 hours after you last detach. You can also keep it running for a time you choose, up to 24 hours, or create it with `--keep always`.
- After that, the session *parks*: Chainguard saves its memory and disk to a snapshot and stops the VM, so it uses no compute.
- When you return, the session resumes from the snapshot in seconds, with your processes, files, and shell as you left them.
- A parked session expires 5 days after it parks.

Each session is its own VM. You can open several sessions on the same repository, for example to give each of several agents its own copy of the code, without worktrees or duplicate dependency directories on your laptop.

## How sessions get credentials

No long-lived credential enters a session. Instead, the session reaches each service through a local hostname, such as `http://github/` or `http://claude/`. Outside the VM, Chainguard or `chainctl` on your laptop adds the credential to each request. Depending on the service, the credential comes from one of three places: your laptop (such as your Claude Code login), your Chainguard organization (such as the Chainguard App's access to your repositories), or a login that Chainguard holds for you (such as your Claude login after you run `chainctl develop claude login`).

By default, a session can reach the following:

- Claude, with the same credential Claude Code uses on your laptop, or with your Claude login held by Chainguard.
- The session's own GitHub repository, for fetch and push, and the other github.com repositories that your checkout's remotes point to, where the Chainguard App is installed. To use those, add them as remotes in the session.
- `cgr.dev`, as the Chainguard platform rather than as you.
- Your Chainguard identity, limited to the read, Chainguard Checks, and Model Context Protocol (MCP) capabilities you hold in the session's organization, while you're attached and for up to an hour after you detach.

When the session asks for anything else, such as fetching another private repository, `chainctl` asks you on your terminal. You can approve requests ahead of time, or take access back, at any point. Refer to [Manage session credentials](/chainguard/workspaces/credentials/) for details.

Claude Code can keep working after you close your terminal, for as long as its credential lasts. With your Claude login held by Chainguard, it works whether or not you're attached, for as long as the session runs, as described in [Keep Claude Code working while you're away](/chainguard/workspaces/coding-agents/#keep-claude-code-working-while-youre-away). A service that you set to use a credential from your laptop, such as `github` or `cgr.dev`, works only while you're attached or while the terminal you detached from keeps serving it.

A session can't read your laptop's clipboard. While you're attached, text that you copy in the session goes to your laptop's clipboard, as described in [Copy text from a session](/chainguard/workspaces/manage-sessions/#copy-text-from-a-session).

## Network access

A session reaches the open internet by default, the same as a laptop, so package managers, `git`, and build tools work without configuration. Chainguard always blocks cloud metadata endpoints, loopback addresses, and private IP ranges.

To restrict a session, open it on a check in your `.chainguard/ci.yaml` file that has a `network.egress` allowlist. A session honors the allowlist the same way a check does, and refuses connections to hosts outside it while it keeps running. Unlike Chainguard Checks, though, a session whose environment has no `network` key reaches the open internet. That includes every session that uses a `.chainguard/develop.yaml` file, which can't have a `network` key. Refer to [Network access](/chainguard/workspaces/session-environment/#network-access) for details.

For the security model of Chainguard Workspaces and Chainguard Checks side by side, including the session lifecycle, refer to [How Chainguard Checks and Chainguard Workspaces isolate your code](/get-started/checks-and-workspaces/how-it-works/).

## Use with Chainguard Checks

Chainguard Workspaces and [Chainguard Checks](/chainguard/checks/overview/) read the same `.chainguard/ci.yaml` file. In a session, the `run-ci` command runs your repository's checks against the working tree in `/work`, uncommitted changes included, so you or an agent can find failures before pushing. Chainguard Checks runs the same checks on each pull request and reports the results to GitHub. After you push, most `chainctl checks` commands, such as `status`, `logs`, and `rerun`, work in the session as you, with the permissions you hold in the organization. In a Starter organization, they don't work for the `limited_owner` role, as described in [Your Chainguard identity in a session](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session).

The `run-ci` command runs each check in the session's own environment, which can have different packages and network access than the check declares. It skips checks that only a pull request can run, such as a check that needs a [workload identity](/chainguard/checks/identity-and-trust/). Refer to [How run-ci differs from a pull request run](/chainguard/checks/run-checks/#how-run-ci-differs-from-a-pull-request-run). For the checks it runs, its result predicts the pull request's result, but only Chainguard Checks, which runs each check in a fresh VM, decides what GitHub shows. You can use Chainguard Workspaces without Chainguard Checks, and the other way around.

## Availability and limits {#availability-and-limits}

{{% blurb/technology-preview product="Chainguard Workspaces" %}}

During the beta, Chainguard Workspaces has the following limits:

- GitHub features, including pushing from a session, work only with repositories on github.com.
- By default, each session has 4 vCPUs, 16 GB of memory, and a 50 GB disk. Unless Chainguard has raised your organization's limit, a session can't have more vCPUs or memory than that, but its disk can be up to 100 GB. Refer to [Resources](/chainguard/workspaces/session-environment/#resources) to change a session's size. The `/tmp` directory is held in memory and is limited to a quarter of the session's memory, 4 GB by default, so put large files under `/var/tmp` instead.
- A session can't forward ports to your laptop.
- `chainctl develop init` turns on a free monthly allowance, which resets on the first day of each month (UTC) and includes 500 vCPU-hours of Workspaces. Chainguard Checks has its own allowance. Each user can have one session at a time, including a parked one, and the organization can have three. An allowance arranged with your Chainguard account team can differ.

A session counts its vCPUs against the allowance for every hour its VM runs, whether it's busy or idle. A session with the default 4 vCPUs uses 4 vCPU-hours an hour, including the time it keeps running while it's busy after you detach and the 10 idle minutes before it parks, and a parked session uses none. A 4-vCPU session created with `--keep always` and left running uses the month's allowance in about 5 days. Chainguard doesn't show your usage during the beta.

When the allowance is used up, you can't create a session or resume a parked one until the allowance resets, and being busy no longer keeps a detached session running, so it parks about 10 minutes after you detach. Sessions you're attached to keep running until you detach. Refer to [Your organization's monthly compute allowance is used up](/chainguard/workspaces/troubleshooting/#your-organizations-monthly-compute-allowance-is-used-up) for details.

## Get help

{{% blurb/checks-workspaces-help channel="workspaces-questions" %}}

## Next steps

- [Get started with Chainguard Workspaces](/chainguard/workspaces/getting-started/) to sign up and open your first session.
- [Manage sessions](/chainguard/workspaces/manage-sessions/) to learn how to detach from, return to, and delete sessions.
- [Use Claude Code in a session](/chainguard/workspaces/coding-agents/) to run an agent in a session.
