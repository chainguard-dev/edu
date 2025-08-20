---
date: 2025-08-19T19:52:13Z
title: "chainctl auth configure-docker"
slug: chainctl_auth_configure-docker
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_configure-docker/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure-docker

Configure a Docker credential helper

```
chainctl auth configure-docker [flags]
```

### Options

```
      --headless                   Skip browser authentication and use device flow.
  -h, --help                       help for configure-docker
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with
      --identity-token string      Use an explicit passed identity token or token path.
      --name string                Optional name for the pull token (default "pull-token")
      --org-name string            Organization to use for authentication. If configured the organization's custom identity provider will be used
      --parent string              The IAM organization or folder with which the pull-token identity is associated.
      --pull-token                 Whether to register a pull token that can pull images
      --save                       If true with --pull-token, save the pull token to the Docker config
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

