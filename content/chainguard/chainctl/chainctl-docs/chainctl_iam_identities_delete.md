---
date: 2023-11-30T14:25:57Z
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
chainctl iam identities delete {IDENTITY_NAME | IDENTITY_ID | --expired [--group=GROUP]} [--yes] [--output ] [flags]
```

### Examples

```
  # Delete an identity by name
  chainctl iam identities delete my-identity
  
  # Delete all expired static identities in a group
  chainctl iam identities delete --expired --group=my-group
```

### Options

```
      --expired        Delete all expired identities.
      --group string   Name or ID of the parent group to delete expired identities from.
  -h, --help           help for delete
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.

