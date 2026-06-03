---
date: 2026-06-02T11:07:19Z
title: "chainctl policy-gate"
slug: chainctl_policy-gate
url: /chainguard/chainctl/chainctl-docs/chainctl_policy-gate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy-gate

Manage policy gates.

### Synopsis

Policy Gates are a registry governance feature that controls which images
your organization can pull. Each policy is a guardrail (for example,
"block end-of-life images") that each image is evaluated against at pull.

## Availability

Policy Gates is an opt-in feature. To enable it for your organization,
contact your Chainguard Customer Success representative. If your
organization is not entitled, `chainctl policy-gate list` will return
an error.

## Concepts

**Policy** — A reusable rule that determines whether an image is allowed.
Each policy has a name, a description, and the resource types it applies
to. Policies apply to registry repositories. `chainctl` currently
manages bindings to system policies that ship with the platform. Use
`chainctl policy-gate list` to see which policies are available to your
organization.

**Binding** — A link between a policy and an organization. While a binding
exists, the policy is active for image pulls under that organization.
Without a binding, the policy has no effect.

**Mode** — A binding's mode controls what happens when the policy denies an
image:

- `ENFORCE` — Block the pull.
- `DRY_RUN` — Allow the pull but record the violation.

The default mode for new bindings is `DRY_RUN`.

**Parameter** — A configurable value declared by a policy's schema (for
example, `days` on the cooldown policy). Supply values when you enable a
policy with `--param=KEY=VALUE` (repeatable). Omitted parameters fall
back to the schema's declared default. Use
`chainctl policy-gate describe --policy NAME` to see which parameters a
policy accepts and what defaults apply.

## What happens at pull time

Each active policy is evaluated for every image pull. Policies are
`enabled and disabled independently`, and multiple policies can be active
at the same time. An image is allowed only when every active policy
allows it.

### Examples

```

# Recommended rollout: start in DRY_RUN mode, review violations, then promote to ENFORCE.

# 1. List the policies available to your organization.
chainctl policy-gate list --parent=example.com

# 2. Inspect a specific policy
chainctl policy-gate describe --policy=cooldown --parent=example.com

# 3. Activate a policy in DRY_RUN mode (records, does not block).
# Note: if a policy declares configurable parameters and --param is omitted,
# the schema's default value is applied.
chainctl policy-gate enable --policy=cooldown --parent=example.com --mode=DRY_RUN

# 4. Review which policies are currently active.
chainctl policy-gate binding list --parent=example.com

# 5. Evaluate a specific image against active policies
chainctl policy-gate check cgr.dev/example.com/python:latest

# 6. Promote the policy to ENFORCE mode.
chainctl policy-gate enable --policy=cooldown --parent=example.com --mode=ENFORCE

# 7. Update the parameters for your binding
chainctl policy-gate enable --policy=cooldown --parent=example.com --mode=ENFORCE --param=days=14

# 8. Disable if no longer needed.
chainctl policy-gate disable --policy=cooldown --parent=example.com

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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl policy-gate binding](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_binding/)	 - Manage policy gate bindings.
* [chainctl policy-gate check](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_check/)	 - Check an image against active policy gates.
* [chainctl policy-gate describe](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_describe/)	 - Describe a policy and its parameter schema.
* [chainctl policy-gate disable](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_disable/)	 - Disable a policy gate.
* [chainctl policy-gate enable](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_enable/)	 - Enable a policy gate for an organization.
* [chainctl policy-gate list](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate_list/)	 - List policy gates.

