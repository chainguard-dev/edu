---
date: 2026-07-22T19:49:10Z
title: "chainctl auth"
slug: chainctl_auth
url: /platform/chainctl/chainctl-docs/chainctl_auth/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth

Auth related commands for the Chainguard platform.

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

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl auth configure-docker](/platform/chainctl/chainctl-docs/chainctl_auth_configure-docker/)	 - Configure a Docker credential helper
* [chainctl auth configure-npm](/platform/chainctl/chainctl-docs/chainctl_auth_configure-npm/)	 - Configure npm credentials for Chainguard Libraries for JavaScript
* [chainctl auth delete-account](/platform/chainctl/chainctl-docs/chainctl_auth_delete-account/)	 - Permanently delete your user account.
* [chainctl auth login](/platform/chainctl/chainctl-docs/chainctl_auth_login/)	 - Login to the Chainguard platform.
* [chainctl auth logout](/platform/chainctl/chainctl-docs/chainctl_auth_logout/)	 - Logout from the Chainguard platform.
* [chainctl auth pull-token](/platform/chainctl/chainctl-docs/chainctl_auth_pull-token/)	 - Create a pull token.
* [chainctl auth status](/platform/chainctl/chainctl-docs/chainctl_auth_status/)	 - Inspect the local Chainguard Token.
* [chainctl auth token](/platform/chainctl/chainctl-docs/chainctl_auth_token/)	 - Print the local Chainguard Token.

