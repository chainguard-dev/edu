---
date: 2026-10-26T19:49:34Z
title: "chainctl develop list"
slug: chainctl_develop_list
url: /platform/chainctl/chainctl-docs/chainctl_develop_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop list

List your live development sessions in the group.

### Synopsis

List your live sessions in the group, most recently used first, with the branch checked out in each, its state (running, until when it keeps running, when it parks, or when a parked session expires), and when it was last used. -o wide adds HEAD, the environment, and the directory a directory session was opened on. --expired also lists your expired sessions. --all lists every user's sessions with an OWNER column; it requires the permission to list other users' sessions in the group.

```
chainctl develop list [--all] [--expired] [--output=json|table|wide]
```

### Options

```
  -a, --all       List all users' sessions in the group (requires permission).
      --expired   Also list your expired sessions.
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

* [chainctl develop](/platform/chainctl/chainctl-docs/chainctl_develop/)	 - Open or resume a cloud development session.

