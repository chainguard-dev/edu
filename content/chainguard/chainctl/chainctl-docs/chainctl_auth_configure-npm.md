---
date: 2026-04-20T19:01:43Z
title: "chainctl auth configure-npm"
slug: chainctl_auth_configure-npm
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_configure-npm/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure-npm

Configure npm credentials for Chainguard Libraries for JavaScript

### Synopsis

Configure npm to use Chainguard Libraries for JavaScript.

By default, this command authenticates using your current Chainguard session
and writes a project-level .npmrc file with a bearer token.

With the --pull-token flag, it creates a longer-lived pull token that can be
used in environments that don't support OIDC (CI systems, build servers, etc.)
and writes a project-level .npmrc with basic auth credentials.

```
chainctl auth configure-npm [flags]
```

### Examples

```
  # Configure npm using your current Chainguard session.
  chainctl auth configure-npm
  
  # Configure npm with a long-lived pull token.
  chainctl auth configure-npm --pull-token
  
  # Configure npm with a pull token for a specific organization.
  chainctl auth configure-npm --pull-token --parent=my-org
  
  # Configure npm with a pull token that lasts for 24 hours.
  chainctl auth configure-npm --pull-token --ttl=24h
```

### Options

```
      --headless                   Skip browser authentication and use device flow.
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with
      --identity-token string      Use an explicit passed identity token or token path.
      --name string                Optional name for the pull token. (default "pull-token")
      --org-name string            Organization to use for authentication. If configured the organization's custom identity provider will be used
      --parent string              The IAM organization or folder with which the pull-token identity is associated.
      --pull-token                 Whether to create a pull token for npm authentication.
      --social-login string        Which of the default identity providers to use for authentication. Must be one of: email, google, github, gitlab
      --ttl ns                     Time To Live for the validity of the pull token. Valid unit strings range from nanoseconds to hours and are ns, `us`, `ms`, `s`, `m`, and `h`. Maximum value is 8760h or one year. (default 720h0m0s)
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

* [chainctl auth](/chainguard/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.

