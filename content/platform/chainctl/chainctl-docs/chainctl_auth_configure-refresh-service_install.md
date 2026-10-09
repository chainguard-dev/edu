---
date: 2026-10-08T18:22:10Z
title: "chainctl auth configure-refresh-service install"
slug: chainctl_auth_configure-refresh-service_install
url: /platform/chainctl/chainctl-docs/chainctl_auth_configure-refresh-service_install/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure-refresh-service install

Install a background service for automatic token refresh

### Synopsis

Install (or update) a user-level service that refreshes Chainguard tokens
in the background.

By default the service refreshes every cached token: the audiences to refresh
are discovered by scanning the local token cache on each refresh cycle, so
tokens created later are picked up without restarting the service.

With --audience, the service refreshes only the given audiences instead.

Rerunning install updates the existing service in place.

```
chainctl auth configure-refresh-service install [flags]
```

### Examples

```
  # Install (or update) the token refresh service.
  chainctl auth configure-refresh-service install
  
  # Refresh only specific audiences.
  chainctl auth configure-refresh-service install --audience=libraries.cgr.dev --audience=apk.cgr.dev
```

### Options

```
      --audience stringArray   Audience to refresh (can be specified multiple times). Defaults to refreshing every cached token.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
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

