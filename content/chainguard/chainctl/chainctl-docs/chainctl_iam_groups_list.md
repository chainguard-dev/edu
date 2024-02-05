---
date: 2024-02-03T00:11:18Z
title: "chainctl iam groups list"
slug: chainctl_iam_groups_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_groups_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam groups list

List groups.

```
chainctl iam groups list [--group=GROUP_NAME|GROUP_ID] [--output tree|table|json|id] [flags]
```

### Examples

```
  # List all groups user is authorized to view.
  chainctl iam group list
  
  # Restrict group list to my-group and its descendants
  chainctl iam group list --group=my-group
```

### Options

```
      --group string   Group to list descendants from (inclusive).
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

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

