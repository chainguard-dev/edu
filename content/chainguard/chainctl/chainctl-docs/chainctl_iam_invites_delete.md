---
date: 2023-07-20T09:07:04Z
title: "chainctl iam invites delete"
slug: chainctl_iam_invites_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_invites_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam invites delete

Delete invite codes

```
chainctl iam invites delete {INVITE_ID... | --expired} [--yes] [flags]
```

### Options

```
      --expired   When true, delete all expired invite codes.
  -h, --help      help for delete
  -y, --yes       Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam invites](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites/)	 - Manage invite codes that register identities or clusters with Chainguard.

