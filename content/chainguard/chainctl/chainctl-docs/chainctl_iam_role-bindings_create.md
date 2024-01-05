---
date: 2024-01-05T19:14:17Z
title: "chainctl iam role-bindings create"
slug: chainctl_iam_role-bindings_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam role-bindings create

Create a role-binding

```
chainctl iam role-bindings create [--identity=IDENTITY] [--role=ROLE] [--group=GROUP] [--output table|json|id]
```

### Examples

```
  # Bind a user-created identity as viewer to a group
  chainctl iam role-bindings create --identity=guest-identity --role=viewer --group=engineering
  
  # Create a new role-binding using interactive selection for identity, role, and group
  chainctl iam role-bindings create
```

### Options

```
      --group string      The name or ID of the group the role-binding belongs to.
  -h, --help              help for create
      --identity string   The name or ID of the identity to bind.
      --role string       The name or ID of the role to bind to the identity.
  -y, --yes               Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam role-bindings](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role-bindings resource interactions.

