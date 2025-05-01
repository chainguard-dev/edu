---
date: 2025-04-25T17:55:09Z
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
chainctl iam roles create ROLE_NAME --parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID --capabilities=CAPABILITY,... [--description=DESCRIPTION] [--yes] [--output=id|json|table]
```

### Examples

```
  # Create a role
  chainctl iam roles create my-role --parent=engineering --capabilities=policy.list,groups.list
  
  # Create a role and choose parameters interactively
  chainctl iam roles create my-role
```

### Options

```
      --capabilities strings   A comma separated list of capabilities to grant this role.
      --description string     A description of the role.
  -h, --help                   help for create
      --parent string          Location to create this role under.
  -y, --yes                    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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
  -o, --output string      Output format. One of: [csv, env, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

