---
date: 2025-08-19T19:52:13Z
title: "chainctl auth"
slug: chainctl_auth
url: /chainguard/chainctl/chainctl-docs/chainctl_auth/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth

Auth related commands for the Chainguard platform.

### Options

```
  -h, --help   help for auth
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl auth configure-docker](/chainguard/chainctl/chainctl-docs/chainctl_auth_configure-docker/)	 - Configure a Docker credential helper
* [chainctl auth login](/chainguard/chainctl/chainctl-docs/chainctl_auth_login/)	 - Login to the Chainguard platform.
* [chainctl auth logout](/chainguard/chainctl/chainctl-docs/chainctl_auth_logout/)	 - Logout from the Chainguard platform.
* [chainctl auth pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/)	 - Create a pull token.
* [chainctl auth status](/chainguard/chainctl/chainctl-docs/chainctl_auth_status/)	 - Inspect the local Chainguard Token.
* [chainctl auth token](/chainguard/chainctl/chainctl-docs/chainctl_auth_token/)	 - Print the local Chainguard Token.

