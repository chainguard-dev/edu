---
date: 2023-06-13T23:28:25Z
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
chainctl iam roles capabilities list [--actions=ACTION,...] [--resources=RESOURCE,...] [--output tree|table|json]
```

### Examples

```
  # List all capabilities
  chainctl iam roles capabilities list
  
  # List all capabilities for groups and clusters
  chainctl iam roles capabilities list --resources=groups,clusters
  
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
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam roles capabilities](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles_capabilities/)	 - IAM role capabilities

