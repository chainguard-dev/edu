---
date: 2026-06-12T17:28:47Z
title: "chainctl policies enable"
slug: chainctl_policies_enable
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_enable/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies enable

Enable a policy for an organization.

### Synopsis

Enable a policy by creating a binding for an organization.
If the policy is already enabled, its mode (or parameter values) is updated.

This is a shortcut for "policies binding create".

The default mode is DRY_RUN. Pass --param=KEY=VALUE (repeatable) to supply
values for policies that declare a parameter schema; omitted parameters
fall back to the schema's declared default.

```
chainctl policies enable --policy POLICY [--parent ORG] [--mode MODE] [--param KEY=VALUE] [--output=json|table] [flags]
```

### Examples

```

# Enable a policy in DRY_RUN mode
chainctl policies enable --policy=no-eol --parent=example.com --mode=DRY_RUN

# Enable a policy in enforce mode
chainctl policies enable --policy=no-eol --parent=example.com --mode=ENFORCE

# Enable a policy with a parameter value
chainctl policies enable --policy=cooldown --parent=example.com --mode=ENFORCE --param=days=14

```

### Options

```
      --mode string         The policy mode (ENFORCE or LOG).
      --param stringArray   Parameter value as key=value. Repeatable.
      --parent string       The name or id of the organization to scope the binding to.
      --policy string       The name or UIDP of the policy to bind.
      --resources strings   The resource types this binding applies to. (default [registry.chainguard.dev/Repo])
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

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Manage policies.

