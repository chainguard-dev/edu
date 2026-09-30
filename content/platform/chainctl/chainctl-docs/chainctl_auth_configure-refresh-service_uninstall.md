---
date: 2026-09-29T17:51:01Z
title: "chainctl auth configure-refresh-service uninstall"
slug: chainctl_auth_configure-refresh-service_uninstall
url: /platform/chainctl/chainctl-docs/chainctl_auth_configure-refresh-service_uninstall/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure-refresh-service uninstall

Uninstall the background token-refresh service

### Synopsis

Uninstall the background token-refresh service.

This stops the service and removes its files.

```
chainctl auth configure-refresh-service uninstall [flags]
```

### Examples

```
  # Uninstall the token refresh service.
  chainctl auth configure-refresh-service uninstall
```

### Options

```
  -y, --yes   Skip confirmation prompt
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

* [chainctl auth configure-refresh-service](/platform/chainctl/chainctl-docs/chainctl_auth_configure-refresh-service/)	 - Manage a background service that keeps Chainguard tokens refreshed

