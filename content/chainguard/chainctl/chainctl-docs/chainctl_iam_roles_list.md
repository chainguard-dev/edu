---
date: 2025-04-09T07:41:46Z
title: "chainctl iam roles list"
slug: chainctl_iam_roles_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_roles_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam roles list

List IAM roles.

```
chainctl iam roles list [--name=NAME] [--capabilities=CAPABILITY,...] [--parent=PARENT | --managed] [--output=id|json|table]
```

### Examples

```
  # List all accessible roles
  chainctl iam roles list
  
  # List all managed (built-in) roles
  chainctl iam roles list --managed
  
  # List all roles that can create groups
  chainctl iam roles list --capabilities=groups.create
```

### Options

```
      --capabilities strings   A comma separated list of capabilities to grant this role.
  -h, --help                   help for list
      --managed                Only list managed (built-in) roles.
      --name string            The exact name of roles to list.
      --parent string          Location to list roles from.
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

* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

