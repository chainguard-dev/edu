---
date: 2026-10-30T14:11:50Z
title: "chainctl develop"
slug: chainctl_develop
url: /platform/chainctl/chainctl-docs/chainctl_develop/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop

Open or resume a cloud development session.

### Synopsis

Open a cloud development session for your code.

Run without an argument to open or resume a session for the current directory.
You can also pass a local directory, GitHub repository URL, or session name or ID.
Use --new for a fresh session; use "chainctl develop ls" to find existing ones.

Local files and Git history sync on the first attach only. Later attaches resume
where you left off; they do not upload new local edits. Send later edits with
"chainctl develop exec". Opening a subdirectory includes the whole repository
and starts the shell in that subdirectory.

The environment comes from .chainguard/develop.yaml, then .chainguard/ci.yaml.
Use --env or --check to choose another. Without either file, interactive sessions
use the default environment; scripts must choose one with --env.

Press Ctrl+] to open the session menu and detach. Detached sessions keep running
while busy, pause after 10 minutes idle, and pause at most 24 hours after your
last attach.
Paused sessions resume when you reconnect and expire after 5 days.

Claude, cgr.dev, scoped Chainguard access, and GitHub remotes are available by
default. Use --with for more access or "chainctl develop creds" to manage it.
Connect your GitHub account with "chainctl develop github login".

--output json prints session details without attaching or syncing local files.

```
chainctl develop [DIR|REPO|SESSION] [flags]
```

### Examples

```
  # Open or resume a session for your code
  chainctl develop
  chainctl develop ~/src/my-project
  chainctl develop github.com/org/repo

  # Resume a session by name
  chainctl develop repo/quiet-harbor

  # Start a separate session with a name
  chainctl develop --name scratch

  # Choose a CI check's environment or a local environment file
  chainctl develop --check lint
  chainctl develop --env ./dev.yaml

  # Grant access to Google Cloud or another GitHub repository
  chainctl develop --with gcp
  chainctl develop --with github:org/other+push

  # Keep running for 8 hours after detaching
  chainctl develop --keep 8h

  # Create and sync a session from a script, then detach
  # Add --env default if the repository has no .chainguard environment
  echo exit | chainctl develop --new --non-interactive
```

### Options

```
      --cache               Mount read-only build caches. --cache=true implies --new; defaults to $CHAINCTL_DEVELOP_CACHE for new sessions.
      --check string        Use this CI check's environment. Implies --new.
      --env string          Environment: YAML file, default, or generate (generate requires a local directory). Implies --new.
      --git-remote string   Git remote to use for a local directory; '-' uploads without a repository.
      --keep string         After detach: keep running for a duration (e.g. 8h, max 24h), always (never pause), or park (pause after the idle window, even if busy). always/park imply --new.
      --name string         Name for a new session, shown as <repo>/<name>. Implies --new.
      --new                 Create a new session instead of resuming one.
      --non-interactive     Disable prompts; fail if a session or group choice is ambiguous.
      --parent string       Organization or folder name/ID (defaults to $CHAINCTL_SANDBOX_GROUP, then default.group).
      --with stringArray    Grant access (repeatable, comma-separated): claude, cgr.dev, chainguard, gcp, aws, azure, github:OWNER/REPO[+push], github:OWNER/*, github:*, all (excludes cloud providers), or none (own repository only).
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl develop accept-terms](/platform/chainctl/chainctl-docs/chainctl_develop_accept-terms/)	 - Accept the terms Workspaces is offered under.
* [chainctl develop check](/platform/chainctl/chainctl-docs/chainctl_develop_check/)	 - Run the repository's checks inside a development session.
* [chainctl develop claude](/platform/chainctl/chainctl-docs/chainctl_develop_claude/)	 - Let the sandbox plane hold a Claude login for your development sessions.
* [chainctl develop creds](/platform/chainctl/chainctl-docs/chainctl_develop_creds/)	 - Show or change a development session's credentials.
* [chainctl develop delete](/platform/chainctl/chainctl-docs/chainctl_develop_delete/)	 - Delete a development session.
* [chainctl develop exec](/platform/chainctl/chainctl-docs/chainctl_develop_exec/)	 - Run a command in a development session.
* [chainctl develop github](/platform/chainctl/chainctl-docs/chainctl_develop_github/)	 - Connect your GitHub account to development sessions.
* [chainctl develop init](/platform/chainctl/chainctl-docs/chainctl_develop_init/)	 - Sign up for Chainguard Starter with Checks and Workspaces.
* [chainctl develop list](/platform/chainctl/chainctl-docs/chainctl_develop_list/)	 - List your live development sessions in the group.
* [chainctl develop mcp](/platform/chainctl/chainctl-docs/chainctl_develop_mcp/)	 - Serve tools for development sessions to an MCP client over stdio.
* [chainctl develop policy](/platform/chainctl/chainctl-docs/chainctl_develop_policy/)	 - Show or change the group's policy for development sessions.
* [chainctl develop rename](/platform/chainctl/chainctl-docs/chainctl_develop_rename/)	 - Rename a development session.

