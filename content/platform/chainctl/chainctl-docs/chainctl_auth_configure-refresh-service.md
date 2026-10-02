---
date: 2026-10-01T22:22:49Z
title: "chainctl auth configure-refresh-service"
slug: chainctl_auth_configure-refresh-service
url: /platform/chainctl/chainctl-docs/chainctl_auth_configure-refresh-service/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure-refresh-service

Manage a background service that keeps Chainguard tokens refreshed

### Synopsis

Manage a user-level background service that keeps Chainguard tokens refreshed
by periodically running 'chainctl auth login --refresh-only'.

The service manager is selected automatically for your operating system:
systemd (Linux) or launchd (macOS). By default every cached token is
refreshed; specific audiences can be selected at install time instead.

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
* [chainctl auth configure-refresh-service install](/platform/chainctl/chainctl-docs/chainctl_auth_configure-refresh-service_install/)	 - Install a background service for automatic token refresh
* [chainctl auth configure-refresh-service uninstall](/platform/chainctl/chainctl-docs/chainctl_auth_configure-refresh-service_uninstall/)	 - Uninstall the background token-refresh service

