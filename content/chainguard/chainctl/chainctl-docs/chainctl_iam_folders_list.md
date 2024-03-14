---
date: 2024-03-14T15:41:40Z
title: "chainctl iam folders list"
slug: chainctl_iam_folders_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_folders_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam folders list

List folders under an organization.

```
chainctl iam folders list ORGANIZATION_NAME | ORGANIZATION_ID [--output tree|table|json|id]
```

### Options

```
  -h, --help   help for list
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

* [chainctl iam folders](/chainguard/chainctl/chainctl-docs/chainctl_iam_folders/)	 - IAM folders interactions.

