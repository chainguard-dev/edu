---
date: 2023-11-20T14:40:12Z
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
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

