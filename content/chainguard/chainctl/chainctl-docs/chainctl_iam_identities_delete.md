---
date: 2025-04-14T14:32:57Z
title: "chainctl iam identities delete"
slug: chainctl_iam_identities_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities delete

Delete one or more identities.

```
chainctl iam identities delete {IDENTITY_NAME | IDENTITY_ID | --expired [--parent=PARENT]} [--yes]
```

### Examples

```
  # Delete an identity by name
  chainctl iam identities delete my-identity
  
  # Delete all expired static identities in an organization
  chainctl iam identities delete --expired --parent=my-org
```

### Options

```
      --expired         Delete all expired identities.
  -h, --help            help for delete
      --parent string   Name or ID of the parent location to delete expired identities from.
  -y, --yes             Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.

