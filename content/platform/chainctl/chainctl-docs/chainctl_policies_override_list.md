---
date: 2026-07-23T16:28:18Z
title: "chainctl policies override list"
slug: chainctl_policies_override_list
url: /platform/chainctl/chainctl-docs/chainctl_policies_override_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies override list

List policy overrides.

### Synopsis

List active policy overrides to see which artifacts have been
waived and for which policy.

Filter by --parent to scope the list to a specific organization.
Without --parent, the list is scoped to your configured default group;
if no default is set, all accessible overrides are listed. Each
override shows its ID, the policy it waives, the targeted artifact, and
the reason.

```
chainctl policies override list [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json|table] [flags]
```

### Examples

```
  # List overrides for an organization
  chainctl policies override list --parent=engineering
  
  # List overrides for your default group (all accessible if no default is set)
  chainctl policies override list
```

### Options

```
      --parent string   The name or id of the organization to list overrides for.
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

* [chainctl policies override](/platform/chainctl/chainctl-docs/chainctl_policies_override/)	 - Manage policy overrides.

