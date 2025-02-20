---
date: 2025-02-19T23:30:24Z
title: "chainctl iam organizations delete"
slug: chainctl_iam_organizations_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_organizations_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam organizations delete

Delete an organization.

```
chainctl iam organizations delete [ORGANIZATION_NAME | ORGANIZATION_ID] [--skip-refresh] [--yes]
```

### Examples

```

# Delete an organization by ID
chainctl iam organizations delete e533448ca9770c46f99f2d86d60fc7101494e4a3

# Delete an organization by name
chainctl iam organizations delete my-org

# Delete an organization to be selected interactively
chainctl iam organizations delete

```

### Options

```
  -h, --help           help for delete
      --skip-refresh   Skips attempting to reauthenticate and refresh the Chainguard auth token if it becomes out of date.
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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
  -o, --output string      Output format. One of: [csv, , json, id, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam organizations](/chainguard/chainctl/chainctl-docs/chainctl_iam_organizations/)	 - IAM organization interactions.

