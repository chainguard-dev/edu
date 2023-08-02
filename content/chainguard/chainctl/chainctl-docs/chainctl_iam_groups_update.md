---
date: 2023-08-01T23:41:56Z
title: "chainctl iam groups update"
slug: chainctl_iam_groups_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_groups_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam groups update

Update a group.

```
chainctl iam groups update GROUP_NAME | GROUP_ID [--name GROUP_NAME] [--description GROUP_DESCRIPTION] [flags]
```

### Examples

```

# Update a group's name
chainctl iam groups update my-group --name new-group-name

# Update a group's description
chainctl iam groups update 19d3a64f20c64ba3ccf1bc86ce59d03e705959ad/efb53f2857d567f2 --description "A description of the group."

# Remove a group's description
chainctl iam groups update my-group --description ""
```

### Options

```
  -d, --description string   The updated description for the group.
  -h, --help                 help for update
  -n, --name string          The updated name for the group.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

