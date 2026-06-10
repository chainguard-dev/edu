---
date: 2026-06-09T15:24:57Z
title: "chainctl policies binding create"
slug: chainctl_policies_binding_create
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_binding_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies binding create

Create a policy binding.

### Synopsis

Create a binding to activate a policy for an organization.
If the policy is already enabled with the same mode, this is a no-op. To
change the mode of an existing binding, pass --mode explicitly.

The --mode flag controls enforcement behavior:
  ENFORCE  Blocks image pulls that violate the policy.
  DRY_RUN  Records violations without blocking pulls.

The default mode is DRY_RUN. Binding to an organization applies the policy to
all repos within it.

Use --param=KEY=VALUE (repeatable) to supply parameter values declared by
the policy's schema. For STRING_LIST parameters, items are comma-separated
within a single --param value.

```
chainctl policies binding create --policy POLICY [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--mode MODE] [--param KEY=VALUE] [--output=json|table] [flags]
```

### Examples

```

# Enforce a policy on all repos in an organization
chainctl policies binding create --policy=no-eol --parent=engineering --mode=ENFORCE

# Enable a policy in dry-run mode
chainctl policies binding create --policy=no-eol --parent=engineering --mode=DRY_RUN

# Create a binding with interactive organization selection
chainctl policies binding create --policy=no-eol

# Create a binding with a parameter value
chainctl policies binding create --policy=cooldown --parent=engineering --mode=ENFORCE --param=days=14

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

* [chainctl policies binding](/chainguard/chainctl/chainctl-docs/chainctl_policies_binding/)	 - Manage policy bindings.

