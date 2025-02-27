---
date: 2025-02-26T10:02:49Z
title: "chainctl iam roles capabilities list"
slug: chainctl_iam_roles_capabilities_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_roles_capabilities_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam roles capabilities list

List IAM role capabilities.

```
chainctl iam roles capabilities list [--actions=ACTION,...] [--resources=RESOURCE,...] [--output=json|table|tree]
```

### Examples

```
  # List all capabilities
  chainctl iam roles capabilities list
  
  # List all capabilities for groups and repos
  chainctl iam roles capabilities list --resources=groups,repos
  
  # List all capabilities that include list
  chainctl iam roles capabilities list --actions=list
```

### Options

```
      --actions strings     Capability actions to list.
  -h, --help                help for list
      --resources strings   Capability resources to list.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam roles capabilities](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles_capabilities/)	 - IAM role capabilities

