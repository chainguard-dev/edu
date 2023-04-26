---
date: 2023-04-25T23:36:21Z
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
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam role-bindings](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role-bindings resource interactions.

