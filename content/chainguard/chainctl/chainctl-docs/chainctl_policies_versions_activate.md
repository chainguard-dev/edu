---
date: 2023-11-20T14:40:12Z
title: "chainctl policies versions activate"
slug: chainctl_policies_versions_activate
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_versions_activate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies versions activate

Select a version of a policy to enforce.

```
chainctl policies versions activate {VERSION_ID | --policy=POLICY} [--output table|json]
```

### Examples

```
  # Activate a version by ID
  chainctl policies versions activate 617ec5ae...
  
  # Interactively select which version to activate from a list of all versions for a policy
  chainctl policies versions activate --policy=my-policy
```

### Options

```
  -h, --help            help for activate
  -p, --policy string   The policy to activate a version of. This flag is ignored if VERSION_ID is given.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl policies versions](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions/)	 - Commands for interacting with policy versions on the Chainguard platform.

