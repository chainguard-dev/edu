---
date: 2024-02-07T18:15:42Z
title: "chainctl iam roles delete"
slug: chainctl_iam_roles_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_roles_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam roles delete

Delete a custom IAM role.

```
chainctl iam roles delete ROLE_NAME|ROLE_ID [--yes] [--output table|json|id]
```

### Examples

```
  # Delete a role by ID
  chainctl iam roles delete 3ed98fc...
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

