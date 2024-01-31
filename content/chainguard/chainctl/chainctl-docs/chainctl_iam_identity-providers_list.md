---
date: 2024-01-30T18:15:44Z
title: "chainctl iam identity-providers list"
slug: chainctl_iam_identity-providers_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers list

List identity providers.

```
chainctl iam identity-providers list --group=GROUP_NAME|GROUP_ID [--output table|tree|json]
```

### Examples

```
  # List identity providers
  chainctl iam identity-providers list
  
  # Filter list by group
  chainctl iam identity-providers list --group=my-group
```

### Options

```
      --group string   List identity providers in this group and its descendents. (optional)
  -h, --help           help for list
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

