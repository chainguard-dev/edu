---
date: 2026-05-26T19:38:09Z
title: "chainctl skills entitlements create"
slug: chainctl_skills_entitlements_create
url: /chainguard/chainctl/chainctl-docs/chainctl_skills_entitlements_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills entitlements create

Create a skills entitlement for an organization.

### Synopsis

Create a skills entitlement for an organization.

This enables the org to push and pull skill artifacts via skills.cgr.dev.
The command is idempotent: re-running it on an already-entitled org
converges to the correct state without returning an error.

```
chainctl skills entitlements create --parent=PARENT [--output=json|table] [flags]
```

### Options

```
      --parent string   The name or id of the org to create a skills entitlement for.
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

* [chainctl skills entitlements](/chainguard/chainctl/chainctl-docs/chainctl_skills_entitlements/)	 - Manage skills entitlements for an organization.

