---
date: 2024-02-08T18:29:07Z
title: "chainctl iam organizations list"
slug: chainctl_iam_organizations_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_organizations_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam organizations list

List organizations and folders.

```
chainctl iam organizations list [--organization=ORGANIZATION_NAME|ORGANIZATION_NAME] [--output tree|table|json|id]
```

### Examples

```
  # List all organizations and folders user is authorized to view.
  chainctl iam organizations list
  
  # Restrict list to my-org and its folders
  chainctl iam organizations list --organization=my-org
```

### Options

```
  -h, --help                  help for list
      --organization string   Organization to list folders from.
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

* [chainctl iam organizations](/chainguard/chainctl/chainctl-docs/chainctl_iam_organizations/)	 - IAM organization interactions.

