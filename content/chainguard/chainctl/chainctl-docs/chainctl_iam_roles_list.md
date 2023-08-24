---
date: 2023-08-23T22:23:54Z
title: "chainctl iam roles list"
slug: chainctl_iam_roles_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_roles_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam roles list

List IAM roles.

```
chainctl iam roles list [--name=NAME] [--capabilities=CAPABILITY,...] [--group=GROUP | --managed] [--output table|json|id]
```

### Examples

```
  # List all accessible roles
  chainctl iam roles list
  
  # List all managed (built-in) roles
  chainctl iam roles list --managed
  
  # List all roles that can create groups
  chainctl iam roles list --capabilities=groups.create
```

### Options

```
      --capabilities strings   A comma separated list of capabilities to grant this role.
      --group string           Group to list roles from.
  -h, --help                   help for list
      --managed                Only list managed (built-in) roles.
      --name string            The exact name of roles to list.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

