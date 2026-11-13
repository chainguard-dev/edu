---
date: 2026-11-12T21:48:09Z
title: "chainctl auth configure-npm"
slug: chainctl_auth_configure-npm
url: /platform/chainctl/chainctl-docs/chainctl_auth_configure-npm/
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
and writes a project-level .npmrc with that session's bearer token, which
expires within the hour. Re-run the command when it does. In CI, log in
first (for example with --identity) and run the command in the same job.

With --pull-token, it creates a long-lived pull token (30 days unless --ttl
says otherwise) for environments that can't log in to Chainguard (build
servers, CI without OIDC, etc.) and writes a project-level .npmrc with basic
auth credentials. Each run creates a new pull token. A Starter organization
holds at most 5 unexpired pull tokens, and each run with --pull-token uses
one until it expires; "chainctl auth pull-token list" shows them.

```
chainctl auth configure-npm [flags]
```

### Examples

```
  # Configure npm with your current Chainguard session's token, which expires within the hour.
  chainctl auth configure-npm
  
  # Configure npm with a long-lived pull token for your organization.
  chainctl auth configure-npm --pull-token --parent=my-org
  
  # Configure npm with a pull token that lasts for 24 hours.
  chainctl auth configure-npm --pull-token --parent=my-org --ttl=24h
```

### Options

```
      --headless                   Skip browser authentication and use device flow.
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with. Mutually exclusive with --org-name.
      --identity-token string      Use an explicit passed identity token or token path.
      --name string                Optional name for the pull token. (default "pull-token")
      --org-name string            Organization to use for authentication. If configured the organization's custom identity provider will be used. Mutually exclusive with --identity-provider.
      --parent string              The IAM organization or folder with which the pull-token identity is associated.
      --pull-token                 Whether to create a pull token for npm authentication. Setting --parent, --ttl or --name implies it.
      --social-login string        Which of the default identity providers to use for authentication. Must be one of: email, google, github, gitlab
      --sts-http1-downgrade        Downgrade STS requests to HTTP/1.x
      --ttl ns                     Time To Live for the validity of the pull token. Valid unit strings range from nanoseconds to hours and are ns, `us`, `ms`, `s`, `m`, and `h`. The maximum depends on the organization's plan: 720h (30 days) for Starter, 168h (7 days) for Team and 8760h (one year) for other plans. (default 720h0m0s)
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

* [chainctl auth](/platform/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.

