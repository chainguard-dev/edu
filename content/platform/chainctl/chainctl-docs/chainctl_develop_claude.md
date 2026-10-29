---
date: 2026-10-28T16:22:54Z
title: "chainctl develop claude"
slug: chainctl_develop_claude
url: /platform/chainctl/chainctl-docs/chainctl_develop_claude/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop claude

Let the sandbox plane hold a Claude login for your development sessions.

### Synopsis

Log in to Claude once with login, and the sandbox plane serves claude in your sessions from that login, whether or not you are attached: claude keeps working after you detach a session you keep running, across its renewal parks and the plane's restarts. Sessions you create from then on use it, and an existing session switches to it at its next attach unless you chose its claude source yourself. It uses Claude Code's own login, asks only for inference, and serves only Claude Code in your sessions.

No token is written to this machine: the plane keeps the login sealed, refreshes it itself, and hands the guest a placeholder. The login lasts about four weeks; the attach says when it is about to end, and login again renews it. logout revokes it at Anthropic, which ends it in every session at once.

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
      --non-interactive    Disable prompts; fail if a session or group choice is ambiguous.
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
      --parent string      Organization or folder name/ID (defaults to $CHAINCTL_SANDBOX_GROUP, then default.group).
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl develop](/platform/chainctl/chainctl-docs/chainctl_develop/)	 - Open or resume a cloud development session.
* [chainctl develop claude login](/platform/chainctl/chainctl-docs/chainctl_develop_claude_login/)	 - Log in to Claude for your development sessions.
* [chainctl develop claude logout](/platform/chainctl/chainctl-docs/chainctl_develop_claude_logout/)	 - Revoke the Claude login your development sessions use.
* [chainctl develop claude status](/platform/chainctl/chainctl-docs/chainctl_develop_claude_status/)	 - Show the Claude login your development sessions use.

