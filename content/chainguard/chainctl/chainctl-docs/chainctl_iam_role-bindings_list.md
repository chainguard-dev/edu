---
date: 2023-08-10T17:12:48Z
title: "chainctl iam role-bindings list"
slug: chainctl_iam_role-bindings_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam role-bindings list

List role-bindings.

```
chainctl iam role-bindings list --group=GROUP_NAME|GROUP_ID [--output table|tree|json]
```

### Examples

```
  # List role-bindings
  chainctl iam role-bindings list
  
  # Filter role-bindings by group
  chainctl iam role-bindings list --group=my-group
```

### Options

```
      --group string   List role-bindings from this group. (optional)
  -h, --help           help for list
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

* [chainctl iam role-bindings](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role-bindings resource interactions.

