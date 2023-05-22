---
date: 2023-05-22T09:40:20Z
title: "chainctl policies list"
slug: chainctl_policies_list
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies list

List policies.

```
chainctl policies list [--group=GROUP_NAME | GROUP_ID] [--image=IMAGE] [--output table|json|id] [flags]
```

### Examples

```
  # List all policies in the "eng" group
  chainctl policy list --group=eng
  
  # List all policies the user has permission to view
  chainctl policy list
```

### Options

```
      --group string   The name or id of the parent group to list policies from.
  -h, --help           help for list
      --image string   The name of an image to filter the results.
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

