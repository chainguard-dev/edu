---
date: 2023-08-01T23:41:56Z
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
chainctl iam groups list [--output tree|table|json|id] [flags]
```

### Examples

```

chainctl iam group list

```

### Options

```
  -h, --help   help for list
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

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

