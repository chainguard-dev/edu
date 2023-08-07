---
date: 2023-08-07T16:21:27Z
title: "chainctl iam roles create"
slug: chainctl_iam_roles_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_roles_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam roles create

Create an IAM role.

```
chainctl iam roles create ROLE_NAME --group=GROUP_NAME|GROUP_ID --capabilities=CAPABILITY,... [--description=DESCRIPTION] [--yes] [--output table|json|id]
```

### Examples

```
  # Create a role
  chainctl iam roles create my-role --group=engineering --capabilities=policy.list,groups.list
  
  # Create a role and choose parameters interactively
  chainctl iam roles create my-role
```

### Options

```
      --capabilities strings   A comma separated list of capabilities to grant this role.
      --description string     A description of the role.
      --group string           Group to create this role under.
  -h, --help                   help for create
  -y, --yes                    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

