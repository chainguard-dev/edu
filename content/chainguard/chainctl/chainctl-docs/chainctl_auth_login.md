---
date: 2025-09-02T09:39:16Z
title: "chainctl auth login"
slug: chainctl_auth_login
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_login/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth login

Login to the Chainguard platform.

```
chainctl auth login [--invite-code=INVITE_CODE] [--identity-token=PATH_TO_TOKEN] [--identity=IDENTITY_ID] [--identity-provider=IDP_ID] [--org-name=ORG_NAME] [--social-login={email|google|github|gitlab}] [--headless] [--prefer-ambient-credentials] [--refresh] [--output=id|json|none|table]
```

### Examples

```
  # Default auth login flow:
  chainctl auth login
  
  # Refreshing a token within a Kubernetes context:
  chainctl auth login --identity-token=PATH_TO_TOKEN --refresh
  
  # Headless login using --org-name
  chainctl auth login --headless --org-name my-org
  
  # Register by accepting an invite to an existing location
  chainctl auth login --invite-code eyJncnAiOiI5MzA...
```

### Options

```
      --headless                     Skip browser authentication and use device flow.
  -h, --help                         help for login
      --identity string              The unique ID of the identity to assume when logging in.
      --identity-provider string     The unique ID of the customer managed identity provider to authenticate with
      --identity-token string        Use an explicit passed identity token or token path.
      --invite-code string           Registration invite code.
      --org-name string              Organization to use for authentication. If configured the organization's custom identity provider will be used
      --prefer-ambient-credentials   Auth with ambient credentials, if present, before using a supplied identity token.
      --refresh                      Enable auto refresh of the Chainguard token (for workloads).
      --social-login string          Which of the default identity providers to use for authentication. Must be one of: email, google, github, gitlab
      --sts-http1-downgrade          Downgrade STS requests to HTTP/1.x
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

