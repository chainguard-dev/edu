---
date: 2026-06-26T20:33:43Z
title: "chainctl policies binding"
slug: chainctl_policies_binding
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_binding/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies binding

Manage policy bindings.

### Synopsis

A policy binding is a link between a policy and a group of image
resources. When a binding exists, the linked policy is active for image
pulls within that group; without a binding the policy has no effect.

Currently, bindings support linking a policy to an organization ID,
which applies the policy to all images under that organization.

Use these commands to create or delete bindings.

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
* [chainctl policies binding create](/chainguard/chainctl/chainctl-docs/chainctl_policies_binding_create/)	 - Create a policy binding.
* [chainctl policies binding delete](/chainguard/chainctl/chainctl-docs/chainctl_policies_binding_delete/)	 - Delete a policy binding.
* [chainctl policies binding list](/chainguard/chainctl/chainctl-docs/chainctl_policies_binding_list/)	 - List policy bindings.

