---
date: 2026-10-30T14:11:50Z
title: "chainctl develop claude logout"
slug: chainctl_develop_claude_logout
url: /platform/chainctl/chainctl-docs/chainctl_develop_claude_logout/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop claude logout

Revoke the Claude login your development sessions use.

### Synopsis

Revoke the Claude login the sandbox plane holds for your sessions, at Anthropic, which ends it in every session at once, and have the plane forget it. Sessions served from it refuse claude until you log in again. When Anthropic cannot be reached nothing is forgotten, and logout says so: run it again.

```
chainctl develop claude logout
```

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

* [chainctl develop claude](/platform/chainctl/chainctl-docs/chainctl_develop_claude/)	 - Let the sandbox plane hold a Claude login for your development sessions.

