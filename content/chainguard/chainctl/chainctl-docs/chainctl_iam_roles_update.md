---
date: 2025-09-02T09:39:16Z
title: "chainctl iam roles update"
slug: chainctl_iam_roles_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_roles_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam roles update

Update an IAM role.

```
chainctl iam roles update ROLE_NAME|ROLE_ID [--capabilities=CAPABILITY,...] [--add-capabilities=CAPABILITY,...] [--remove-capabilities=CAPABILITY,...] [--description=DESCRIPTION] [--yes] [--output=id|json|table]
```

### Examples

```
  # Update a role with a complete set of capabilities
  chainctl iam roles update my-role --capabilities=policy.list,groups.list,identity.list
  
  # Add new capabilities to a role
  chainctl iam roles update my-role --add-capabilities=policy.create
  
  # Remove an existing capabilities from a role
  chainctl iam roles update my-role --remove-capabilities=identity.list
  
  # Interactively choose capabilities to add to a role
  chainctl iam roles update my-role --add-capabilities=
```

### Options

```
      --add-capabilities strings      A comma separated list of capabilities to add to this role (can't be used with --capabilities).
      --capabilities strings          A comma separated list of capabilities to grant this role.
      --description string            A description of the role.
  -h, --help                          help for update
      --remove-capabilities strings   A comma separated list of capabilities to remove from this role (can't be used with --capabilities).
  -y, --yes                           Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

