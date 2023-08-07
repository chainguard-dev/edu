---
date: 2023-08-07T16:21:27Z
title: "chainctl iam role-bindings update"
slug: chainctl_iam_role-bindings_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam role-bindings update

Update a role-binding.

```
chainctl iam role-bindings update BINDING_ID [--role=ROLE] [--identity=IDENTITY] [--output table|json|id]
```

### Examples

```
  # Update the role an identity is bound to
  chainctl iam role-bindings update fb694596eb1678321f94eec283e1e0be690f655c/a2973bac66ebfde3 --role=editor
  
  # Update the identity bound to a role
  chainctl iam role-bindings update fb694596eb1678321f94eec283e1e0be690f655c/a2973bac66ebfde3 --identity=support-identity
```

### Options

```
  -h, --help              help for update
      --identity string   The name or ID of the identity to bind.
      --role string       The name or ID of the role to bind to the identity.
  -y, --yes               Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

