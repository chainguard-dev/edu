---
date: 2023-04-19T23:22:15Z
title: "chainctl iam groups create"
slug: chainctl_iam_groups_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_groups_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam groups create

Create a new group or add a group under an existing group.

```
chainctl iam groups create GROUP_NAME [--parent GROUP_NAME | GROUP_ID | --no-parent] [--description DESCRIPTION] [--yes] [--skip-refresh] [flags]
```

### Options

```
  -d, --description string   The description of the group.
  -h, --help                 help for create
      --no-parent            The new group should be a new root group.
      --parent string        The id, suffix, or name of the parent group for the new group.
      --skip-refresh         Skips attempting to reauthenticate and refresh the Chainguard auth token if it becomes out of date.
  -y, --yes                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

