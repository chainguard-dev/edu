---
date: 2023-04-14T15:52:13Z
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

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam invites create](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_create/)	 - Generate an invite code to identities or register clusters with Chainguard.
* [chainctl iam invites delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_delete/)	 - Delete invite codes
* [chainctl iam invites list](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_list/)	 - Show invites that are active.

