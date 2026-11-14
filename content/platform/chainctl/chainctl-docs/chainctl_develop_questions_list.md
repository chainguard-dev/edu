---
date: 2026-11-13T20:36:51Z
title: "chainctl develop questions list"
slug: chainctl_develop_questions_list
url: /platform/chainctl/chainctl-docs/chainctl_develop_questions_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop questions list

List the open questions about your sessions.

### Synopsis

List the questions agents asked in your sessions in the group, newest first: only the open ones, or every one with --all.

```
chainctl develop questions list [--all] [--output=json|table]
```

### Options

```
      --all   Also list answered, dismissed, and expired questions.
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

* [chainctl develop questions](/platform/chainctl/chainctl-docs/chainctl_develop_questions/)	 - List and answer the questions agents in your development sessions ask.

