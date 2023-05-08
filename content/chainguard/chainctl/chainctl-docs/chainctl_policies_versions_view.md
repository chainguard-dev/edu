---
date: 2023-05-08T20:57:19Z
title: "chainctl policies versions view"
slug: chainctl_policies_versions_view
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_versions_view/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies versions view

View the details of a policy version.

```
chainctl policies versions view {VERSION_ID | --policy=POLICY} [--output json] [flags]
```

### Examples

```
  # View a policy version by ID
  chainctl policies versions view 617ec5ae...
  
  # Interactively select a policy version for a given policy
  chainctl policies versions view --policy=my-policy
```

### Options

```
  -h, --help            help for view
  -p, --policy string   The policy to view a version of. This flag is ignored if VERSION_ID is given.
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

* [chainctl policies versions](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions/)	 - Commands for interacting with policy versions on the Chainguard platform.

