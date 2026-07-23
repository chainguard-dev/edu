---
date: 2026-07-22T19:49:10Z
title: "chainctl policies override"
slug: chainctl_policies_override
url: /platform/chainctl/chainctl-docs/chainctl_policies_override/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies override

Manage policy overrides.

### Synopsis

A policy override is an admin-granted waiver that flips a DENIED
policy result to ALLOWED for one specific artifact. It does not change
the policy or its binding; it records a deliberate, attributable
exception that the engine applies after evaluation.

Each override names exactly one policy and one artifact. Creating an
override requires the policies.override.create capability, which is
typically held by organization owners.

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

* [chainctl policies](/platform/chainctl/chainctl-docs/chainctl_policies/)	 - Manage policies.
* [chainctl policies override create](/platform/chainctl/chainctl-docs/chainctl_policies_override_create/)	 - Create a policy override.
* [chainctl policies override delete](/platform/chainctl/chainctl-docs/chainctl_policies_override_delete/)	 - Delete a policy override.
* [chainctl policies override list](/platform/chainctl/chainctl-docs/chainctl_policies_override_list/)	 - List policy overrides.

