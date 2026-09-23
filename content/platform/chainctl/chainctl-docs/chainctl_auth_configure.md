---
date: 2026-09-22T16:17:57Z
title: "chainctl auth configure"
slug: chainctl_auth_configure
url: /platform/chainctl/chainctl-docs/chainctl_auth_configure/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure

Configure a local tool to authenticate to Chainguard.

### Synopsis

Configure a local tool to authenticate to Chainguard.

Each subcommand writes credentials where its tool looks for them, using
your current Chainguard session. With --pull-token it writes a
longer-lived credential instead, for environments that cannot run an
interactive login (CI systems, build servers, etc.).

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

* [chainctl auth](/platform/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl auth configure docker](/platform/chainctl/chainctl-docs/chainctl_auth_configure_docker/)	 - Configure a Docker credential helper
* [chainctl auth configure npm](/platform/chainctl/chainctl-docs/chainctl_auth_configure_npm/)	 - Configure npm credentials for Chainguard Libraries for JavaScript

