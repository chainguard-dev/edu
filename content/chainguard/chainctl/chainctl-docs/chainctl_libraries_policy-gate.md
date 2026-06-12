---
date: 2026-06-11T20:09:07Z
title: "chainctl libraries policy-gate"
slug: chainctl_libraries_policy-gate
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy-gate

Manage Libraries policy gates.

### Synopsis

Libraries policy gates control which upstream packages your organization can
pull. A policy configures automatic gates (cooldown, malware) and explicit
block/allow lists; a binding activates a policy for an (organization,
ecosystem) pair in either ENFORCED or LOG mode.

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

* [chainctl libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.
* [chainctl libraries policy-gate binding](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_binding/)	 - Manage Libraries policy gate bindings.
* [chainctl libraries policy-gate create](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_create/)	 - Create a custom Libraries policy.
* [chainctl libraries policy-gate delete](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_delete/)	 - Delete a custom Libraries policy.
* [chainctl libraries policy-gate describe](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_describe/)	 - Describe a Libraries policy.
* [chainctl libraries policy-gate disable](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_disable/)	 - Disable a Libraries policy for an organization.
* [chainctl libraries policy-gate enable](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_enable/)	 - Enable a Libraries policy for an organization.
* [chainctl libraries policy-gate list](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_list/)	 - List Libraries policies.
* [chainctl libraries policy-gate update](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_update/)	 - Update a custom Libraries policy.

