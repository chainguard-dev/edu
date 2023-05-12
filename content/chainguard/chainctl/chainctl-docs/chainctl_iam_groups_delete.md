---
date: 2023-05-12T04:24:52Z
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

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

