---
date: 2024-01-23T09:30:47Z
title: "chainctl iam groups delete"
slug: chainctl_iam_groups_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_groups_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam groups delete

Delete group

```
chainctl iam groups delete [GROUP_NAME | GROUP_ID] [--yes] [--skip-refresh] [flags]
```

### Examples

```

# Delete a group by ID
chainctl iam group delete e533448ca9770c46f99f2d86d60fc7101494e4a3

# Delete a group by name
chainctl iam group delete my-group

# Delete a group to be selected interactively
chainctl iam group delete

```

### Options

```
  -h, --help           help for delete
      --skip-refresh   Skips attempting to reauthenticate and refresh the Chainguard auth token if it becomes out of date.
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

