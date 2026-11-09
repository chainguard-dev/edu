---
date: 2026-11-06T22:09:37Z
title: "chainctl auth sessions list"
slug: chainctl_auth_sessions_list
url: /platform/chainctl/chainctl-docs/chainctl_auth_sessions_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth sessions list

List your sign-in sessions, marking the one this chainctl holds with *.

```
chainctl auth sessions list [--output=json|table] [flags]
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
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl auth sessions](/platform/chainctl/chainctl-docs/chainctl_auth_sessions/)	 - List and revoke your sign-in sessions.

