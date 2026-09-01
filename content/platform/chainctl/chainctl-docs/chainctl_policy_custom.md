---
date: 2026-08-31T17:17:40Z
title: "chainctl policy custom"
slug: chainctl_policy_custom
url: /platform/chainctl/chainctl-docs/chainctl_policy_custom/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy custom

Manage your custom policies.

### Synopsis

Manage the lifecycle of your organization's custom policies:
validate a manifest before submitting, create a new policy, update an
existing one, and delete when it's no longer needed.

A custom policy is a Rego expression paired with a single supported
resource type and an optional parameter schema. Each policy is
identified by (name, resource type) within an organization.

The supported resource type is set at create time and cannot be changed
afterwards.

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

* [chainctl policy](/platform/chainctl/chainctl-docs/chainctl_policy/)	 - Manage policies.
* [chainctl policy custom create](/platform/chainctl/chainctl-docs/chainctl_policy_custom_create/)	 - Create a custom policy.
* [chainctl policy custom delete](/platform/chainctl/chainctl-docs/chainctl_policy_custom_delete/)	 - Delete a custom policy.
* [chainctl policy custom update](/platform/chainctl/chainctl-docs/chainctl_policy_custom_update/)	 - Update a custom policy.
* [chainctl policy custom validate](/platform/chainctl/chainctl-docs/chainctl_policy_custom_validate/)	 - Validate a custom policy manifest or expression without persisting it.

