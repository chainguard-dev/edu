---
date: 2024-02-08T19:39:21Z
title: "chainctl iam invites"
slug: chainctl_iam_invites
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_invites/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam invites

Manage invite codes that register identities or clusters with Chainguard.

### Options

```
  -h, --help   help for invites
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

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam invites create](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_create/)	 - Generate an invite code to identities or register clusters with Chainguard.
* [chainctl iam invites delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_delete/)	 - Delete invite codes
* [chainctl iam invites list](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_list/)	 - List group invites.

