---
date: 2025-04-08T07:31:17Z
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
chainctl iam role-bindings create [--identity=IDENTITY] [--role=ROLE] [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--output=id|json|table]
```

### Examples

```
  # Bind a user-created identity as viewer to a location
  chainctl iam role-bindings create --identity=guest-identity --role=viewer --parent=engineering
  
  # Create a new role-binding using interactive selection for identity, role, and location
  chainctl iam role-bindings create
```

### Options

```
  -h, --help              help for create
      --identity string   The name or ID of the identity to bind.
      --parent string     The name or ID of the location the role-binding belongs to.
      --role string       The name or ID of the role to bind to the identity.
  -y, --yes               Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam role-bindings](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role-bindings resource interactions.

