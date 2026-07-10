---
date: 2026-07-01T03:32:22Z
title: "chainctl libraries policy"
slug: chainctl_libraries_policy
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy

Manage Libraries policies.

### Synopsis

Libraries policies control which upstream packages your organization can
pull. A policy configures automatic gates (cooldown, malware) and explicit
block/allow lists; a binding activates a policy for an (organization,
ecosystem) pair in either ENFORCE or PREVIEW mode.

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
* [chainctl libraries policy binding](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_binding/)	 - Manage Libraries policy bindings.
* [chainctl libraries policy create](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_create/)	 - Create a custom Libraries policy.
* [chainctl libraries policy delete](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_delete/)	 - Delete a custom Libraries policy.
* [chainctl libraries policy describe](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_describe/)	 - Describe a Libraries policy.
* [chainctl libraries policy disable](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_disable/)	 - Disable a Libraries policy for an organization.
* [chainctl libraries policy enable](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_enable/)	 - Enable a Libraries policy for an organization.
* [chainctl libraries policy list](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_list/)	 - List Libraries policies.
* [chainctl libraries policy update](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_update/)	 - Update a custom Libraries policy.

