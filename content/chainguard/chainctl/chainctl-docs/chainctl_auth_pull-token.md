---
date: 2025-08-19T19:52:13Z
title: "chainctl auth pull-token"
slug: chainctl_auth_pull-token
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth pull-token

Create a pull token.

```
chainctl auth pull-token [flags]
```

### Options

```
  -h, --help                       help for pull-token
      --library-ecosystem python   The language ecosystem to access with the pull token. Valid values are python and `java`.
      --name string                Pull token name. (default "pull-token")
      --parent string              The IAM organization or folder with which the pull token identity is associated.
      --save                       If true with --pull-token, save the pull token to the Docker configuration.
      --ttl ns                     Time To Live for the validity of the pull token. Valid unit strings range from nanoseconds to hours and are ns, `us`, `ms`, `s`, `m`, and `h`. Maxiumum value is 8760h or one year. (default 720h0m0s)
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

* [chainctl auth](/chainguard/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl auth pull-token create](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token_create/)	 - Create a pull token.
* [chainctl auth pull-token list](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token_list/)	 - List all pull-tokens

