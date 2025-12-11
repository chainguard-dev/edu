---
date: 2025-12-10T21:44:57Z
title: "chainctl auth status"
slug: chainctl_auth_status
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth status

Inspect the local Chainguard Token.

```
chainctl auth status [--output=json|table|terse] [flags]
```

### Options

```
      --headless                   Skip browser authentication and use device flow.
  -h, --help                       help for status
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with
      --identity-token string      Use an explicit passed identity token or token path.
      --org-name string            Organization to use for authentication. If configured the organization's custom identity provider will be used
      --quick                      Whether to perform quick offline token checks (vs. calling the Validate API).
      --social-login string        Which of the default identity providers to use for authentication. Must be one of: email, google, github, gitlab
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

