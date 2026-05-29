---
date: 2026-05-28T17:13:42Z
title: "chainctl policy-gate binding create"
slug: chainctl_policy-gate_binding_create
url: /chainguard/chainctl/chainctl-docs/chainctl_policy-gate_binding_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy-gate binding create

Create a policy gate binding.

### Synopsis

Create a binding to activate a policy for an organization.
If the policy is already enabled with the same mode, this is a no-op. To
change the mode of an existing binding, pass --mode explicitly.

The --mode flag controls enforcement behavior:
  ENFORCE  Blocks image pulls that violate the policy.
  DRY_RUN  Records violations without blocking pulls.

The default mode is DRY_RUN. Binding to an organization applies the policy to
all repos within it.

```
chainctl policy-gate binding create --policy POLICY [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--mode MODE] [--output=json|table] [flags]
```

### Examples

```

# Enforce a policy on all repos in an organization
chainctl policy-gate binding create --policy=no-critical-cves --parent=engineering --mode=ENFORCE

# Enable a policy in dry-run mode
chainctl policy-gate binding create --policy=no-critical-cves --parent=engineering --mode=DRY_RUN

# Create a binding with interactive organization selection
chainctl policy-gate binding create --policy=no-critical-cves

```

### Options

```
      --mode string         The policy mode (ENFORCE or LOG).
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

* [chainctl policy-gate binding](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_binding/)	 - Manage policy gate bindings.

