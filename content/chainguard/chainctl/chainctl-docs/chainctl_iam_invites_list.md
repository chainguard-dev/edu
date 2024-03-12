---
date: 2024-03-11T21:48:45Z
title: "chainctl iam invites list"
slug: chainctl_iam_invites_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_invites_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam invites list

List organization and folder invites.

```
chainctl iam invites list [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--output table|json|id]
```

### Examples

```
  # List all accessible invites
  chainctl iam invites list
  
  # Filter invites by location
  chainctl iam invites list --parent=my-org
```

### Options

```
  -h, --help            help for list
      --parent string   List invites from this location.
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

* [chainctl iam invites](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites/)	 - Manage invite codes that register identities or clusters with Chainguard.

