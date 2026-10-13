---
title: "Use Claude Code in a Chainguard Workspaces session"
linktitle: "Use Claude Code"
description: "Run Claude Code in a Chainguard Workspaces session with your own Claude credential, keep it working while you're away, and run several agents in parallel."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T15:17:49+00:00
draft: false
tags: ["Chainguard Workspaces", "AI", "Procedural"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 60
---

A Chainguard Workspaces session is a place for a coding agent to work with less risk to your laptop. The agent runs in the session's VM, which holds no long-lived credentials, and it reaches Claude with your own Claude credential, which stays outside the VM. This page explains how to run Claude Code in a session.

Claude Code is the only coding agent that sessions supply a model credential for. You can install other coding agents in a session, but sessions don't send them a credential.

## Before you begin

Claude Code in a session uses the Claude credential from your laptop, so set it up there first:

1. Update `chainctl` to the [minimum version](/get-started/checks-and-workspaces/#install-or-update-chainctl) or later, as described in [Updating chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl). Earlier versions don't send Claude's credential to a session.
2. Install Claude Code on your laptop, as described in the [Claude Code documentation](https://code.claude.com/docs/en/overview).
3. Run `claude` on your laptop and log in.

When you attach to a session, `chainctl` sends the session's host the first credential it finds on your laptop, in this order: a `chainctl-credential-claude` credential helper on your `PATH`, the `ANTHROPIC_API_KEY` environment variable, an `apiKeyHelper` from your Claude Code settings, the `CLAUDE_CODE_OAUTH_TOKEN` environment variable, and your stored Claude login. Apart from the credential helper, this is the order Claude Code uses on your laptop. Both an API key and a Claude subscription login work.

Claude Code must also be installed in the session. The default environment includes it. If your session uses your repository's `.chainguard/develop.yaml` or `.chainguard/ci.yaml` file, add `claude` to that file's packages, as described in [Configure a session's environment](/chainguard/workspaces/session-environment/).

## Start Claude Code

Open a session, then run `claude` in it:

```shell
claude
```

Claude Code starts without asking you to log in. When you attach, `chainctl` sends your Claude credential to the session's host, outside the VM. Claude Code's requests go to `http://claude/` in the session, and the host sends them on with your credential. The host passes on only requests to the Claude API's messages and models endpoints, not its account or organization endpoints. For a stored Claude login, `chainctl` sends only the short-lived access token, never the refresh token.

If Claude Code in the session reports that the token sent to the session expired, attach to the session again so that `chainctl` sends a fresh one. If `chainctl` says that the Claude login on your laptop expired, run `claude` on your laptop once to refresh it. To keep a long task from stopping when a login expires, use a token from `claude setup-token`, as described in [Keep Claude Code working while you're away](#keep-claude-code-working-while-youre-away). For other errors, refer to [Claude Code reports an error in the session](/chainguard/workspaces/troubleshooting/#claude-code-reports-an-error-in-the-session).

## Use Claude through Vertex AI {#use-claude-through-vertex-ai}

To use Vertex AI, set your Google Cloud project in `chainctl`. You don't need to change your Claude Code settings. Replace `$GCP_PROJECT` with your Google Cloud project ID:

```shell
chainctl config set develop.vertex.project $GCP_PROJECT
```

New sessions then use Vertex AI in that project, as described in [How a session chooses its provider](#how-a-session-chooses-its-provider). The region defaults to `global`. To use another region, set `develop.vertex.region` the same way.

With Vertex AI, `chainctl` sends the session's host a Google credential from your laptop's application default credentials, which `gcloud auth application-default login` sets up. It sends the credential the same way it sends the `gcp` credential, as described in [Use your Google Cloud credentials in a session](/chainguard/workspaces/credentials/#use-your-google-cloud-credentials-in-a-session). Claude Code in the session holds no Google credential.

### How a session chooses its provider

When you create a session, `chainctl` chooses how Claude Code in it reaches Claude, in this order:

1. If Claude Code on your laptop is set to use Vertex AI with `CLAUDE_CODE_USE_VERTEX`, the session uses Vertex AI with the project in `ANTHROPIC_VERTEX_PROJECT_ID` and the region in `CLOUD_ML_REGION`.
2. If you set `develop.vertex.project` in your `chainctl` configuration, the session uses Vertex AI in that project.
3. If Claude Code on your laptop has a Claude login or an API key, the session uses the Anthropic API.
4. If your Google Cloud application default credentials name a project, the session uses Vertex AI in that project.

If none of these applies, the session uses the Anthropic API, and Claude Code works once you log in to Claude on your laptop and attach again.

`chainctl` reads `CLAUDE_CODE_USE_VERTEX` and the other Claude Code variables from the `env` of your Claude Code settings, then from your environment. If Claude Code uses Vertex AI but names no project, `chainctl` uses `develop.vertex.project`, then the project your Google Cloud credentials name, and refuses to create the session if it finds none. When a new session uses Vertex AI, `chainctl` says so and names where the project came from.

### Switch a session to another provider {#switch-a-session-to-another-provider}

A session keeps its provider when it parks and resumes. To switch a running session between the Anthropic API and Vertex AI:

1. Press `Ctrl+]` to open the session menu, and choose **Credentials**.
2. Choose `claude`, then choose **Use Vertex AI…**, or **Use Anthropic…** on a session that uses Vertex AI. To use Vertex AI, your laptop needs Google Cloud application default credentials.
3. Choose whether the change applies to this session only or to new sessions too. For Vertex AI, check the project and region first. For new sessions, `chainctl` saves the project and region in `develop.vertex.project` and `develop.vertex.region`, or clears them when you switch to the Anthropic API.
4. In the session, exit Claude Code with `/exit`, then run `claude --continue` to resume the conversation with the new provider.

Claude Code that's already running keeps the old provider, so its next request fails with a message that tells you to restart it. If `chainctl` tells you to start a new session to use the new provider, the session is too old to switch, so create a new one.

## Configure Claude Code in a session

From your laptop, a session takes only your Claude credential and the Vertex AI settings described in [Use Claude through Vertex AI](#use-claude-through-vertex-ai). The rest of your Claude Code setup stays on your laptop: `chainctl` doesn't copy `~/.claude/settings.json`, `~/.claude/CLAUDE.md`, your MCP servers, plugins, skills, subagents, slash commands, or model choice.

Instead, Claude Code in a session uses the following:

- The session's managed settings, which include a short brief that describes the session and its tools, including how to run your repository's checks with `run-ci`.
- Your repository's own `CLAUDE.md`, `.claude/` directory, and `.mcp.json` file, within the limits described in [MCP servers in a session](#mcp-servers-in-a-session).

To give every session the same setup, commit it to your repository's `CLAUDE.md` and `.claude/` directory.

### Choose a model

A session doesn't set a model, so Claude Code starts with its default model unless your repository's `.claude/settings.json` sets one. To use another model, start Claude Code with `claude --model`, or run `/model` in Claude Code.

With Vertex AI, Claude Code's default model might not be enabled in your Google Cloud project. If Claude Code's requests fail with an error about the model, choose a model that your project has enabled.

### MCP servers in a session {#mcp-servers-in-a-session}

Every session configures two Chainguard MCP servers for Claude Code: [`cg-apk`](/platform/mcp-servers/cg-apk/) and [`cg-versions`](/platform/mcp-servers/cg-versions/). They act as you through your Chainguard identity in the session, so they need no browser sign-in. They work only while that identity does, as described in [Your Chainguard identity in a session](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session), and only if you hold the `mcp.tool.call` capability in the session's organization, as the `owner` and `mcp.tool_user` roles do. The `limited_owner` role that `chainctl develop init` gives you doesn't include it, and neither do the `viewer` and `sandbox.user` roles. An MCP server with the same name in your repository's `.mcp.json` replaces either one.

Claude Code also loads the `https://` MCP servers in your repository's `.mcp.json` without asking you to approve each one. The session adds no credential to their requests.

The session's managed settings allow only MCP servers reached over `https://`, and settings in your repository can't allow others. MCP servers that run as local commands, and servers reached over `http://`, don't start, including ones you add in the session with `claude mcp add`.

The [`cg-oci`](/platform/mcp-servers/cg-oci/) MCP server doesn't work in a session, because the session's requests to `cgr.dev` reach only the container registry.

## Choose a permission mode

Claude Code in a session starts in its default permission mode, so it asks you before it runs commands or edits files.

Because the session is a separate VM that holds no long-lived credentials, you might choose to let Claude Code work without asking. Claude Code normally refuses `--dangerously-skip-permissions` when it runs as `root`, as it does in a session. The session sets `IS_SANDBOX=1` so that Claude Code allows it:

```shell
claude --dangerously-skip-permissions
```

Before you let an agent work unattended, consider what the session can still reach. By default, it can reach the open internet and push to its own repository. To narrow that, give the session an `egress` list, as described in [Network access](/chainguard/workspaces/session-environment/#network-access), and review its credentials, as described in [Manage session credentials](/chainguard/workspaces/credentials/). Requests beyond the session's defaults still need your approval on your terminal.

If you connected your GitHub account before you created the session, and your organization allows it, the session acts on GitHub as you, without asking you first. It can push, approve other people's pull requests, and merge as you, and neither an `egress` list nor `chainctl develop creds` limits it. Before you let an agent work unattended in such a session, protect your branches, as described in [Protect your branches](/chainguard/workspaces/github-as-you/#protect-your-branches).

A session has no credentials for services such as AWS, Azure, or a private package registry. Don't paste one into the session for the agent to use: any agent or command in the session can read it, and it stays in the session's snapshot when the session parks. Do that work on your laptop instead, as described in [Credentials a session can't supply](/chainguard/workspaces/credentials/#credentials-a-session-cant-supply).

## Keep Claude Code working while you're away {#keep-claude-code-working-while-youre-away}

To leave Claude Code working in a session, detach and keep the session running, rather than letting it park:

1. Press `Ctrl+]` to open the session menu.
2. Choose **Detach — keep running 4h**, or **Detach — keep running for…** to set a duration of up to 24 hours.

The session's host keeps the Claude credential that `chainctl` sent, so Claude Code keeps working after you close the terminal. How long it keeps working without a terminal depends on the credential:

| Credential | How long Claude Code keeps working |
| ---------- | ---------------------------------- |
| An API key, the output of an `apiKeyHelper`, or `CLAUDE_CODE_OAUTH_TOKEN` | Until the session parks. |
| Your stored Claude login | Until the access token that `chainctl` sent expires. |
| A Google credential, for Vertex AI | Until the access token that `chainctl` sent expires, or until the session parks if `chainctl` sent your refresh token. |

When you attach, `chainctl` says which credential it sent and how long the session keeps it. The **Credentials** screen in the session menu shows the same.

The terminal you detached from keeps serving the session, through sleep and network interruptions, until the session stops running, you press `Ctrl+C`, or you close the terminal. While it serves, it keeps the session's Claude credential current: it sends new Google access tokens, reruns your `apiKeyHelper`, and sends your stored login again each time Claude Code on your laptop refreshes it. If your stored login is about to expire without being refreshed, `chainctl` tells you to run `claude` on your laptop.

For long unattended work with a Claude subscription, run `claude setup-token` on your laptop. In the shell where you run `chainctl develop`, set `CLAUDE_CODE_OAUTH_TOKEN` to the token it prints, and then attach. The session keeps that token until it parks.

When the session parks, its host discards the credential. When you return, `chainctl` sends it again, and Claude Code is still running in the session, with its conversation intact.

While the terminal serves a detached session, it refuses new approval requests, so allow anything the agent will need ahead of time with `--with`.

For a task that runs longer than a day, create a session with `--keep always`. Refer to [Keep a session running while you're away](/chainguard/workspaces/manage-sessions/#keep-a-session-running-while-youre-away).

## Run several agents in parallel {#run-several-agents-in-parallel}

You can run several agents in one session, each in its own terminal, or give each agent its own session.

### Run agents in one session

To start another agent in a session you're attached to, press `Ctrl+]` to open the session menu, press `c` to start a terminal, and run `claude` in the new terminal. To switch between terminals, press `Ctrl+]`, then the terminal's number. A session runs up to nine terminals. Refer to [Use several terminals in a session](/chainguard/workspaces/manage-sessions/#use-several-terminals-in-a-session) for the other keys and the status row.

Open each terminal from the session menu, not by running `chainctl develop` in another terminal window on your laptop. Only one `chainctl` can be attached to a session at a time, so a second one takes over and detaches the first, as described in [Return to a session](/chainguard/workspaces/manage-sessions/#return-to-a-session).

The terminals share the session's VM, including its CPUs, memory, and `/work` directory. When two agents work in `/work`, each one's edits and branch switches change the files the other is working on. To keep their work apart, give each agent after the first its own branch in a git worktree outside `/work`. For example, in the new terminal, run:

```shell
git -C /work worktree add -b fix-cache /root/fix-cache
cd /root/fix-cache
claude
```

The `run-ci` command checks only `/work`, so an agent in another worktree can't check its work with it before it pushes. Only one `run-ci` or `chainctl develop check` can run in a session at a time, so one started while another runs fails and tells you to wait for the first to finish.

### Run agents in separate sessions

With the [free monthly allowance](/chainguard/workspaces/overview/#availability-and-limits), each user can have one session at a time, so this section applies only if your organization's allowance includes more sessions, such as one arranged with your Chainguard account team.

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

If you detached from the session and kept it running, `chainctl develop check` might fail with a message that says `the guest is held by another controller`. Run the command again, or attach to the session and run `run-ci` in it.

Both commands run the checks in the session's own environment, against its working tree as it is now. They skip checks that only a pull request can run, and print a line for each, as described in [How run-ci differs from a pull request run](/chainguard/checks/run-checks/#how-run-ci-differs-from-a-pull-request-run). A pass in the session doesn't cover those checks, so have the agent report any skipped checks along with its result.

A pass predicts that the pull request's checks will pass, but only [Chainguard Checks](/chainguard/checks/overview/), which runs each check in a fresh VM, decides what GitHub shows.
