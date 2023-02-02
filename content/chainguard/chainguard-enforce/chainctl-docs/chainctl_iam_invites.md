---
date: 2023-01-31T17:36:40-05:00
title: "chainctl iam invites"
slug: chainctl_iam_invites
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_invites/
draft: false
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
```

### SEE ALSO

* [chainctl iam](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam invites create](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_invites_create/)	 - Generate an invite code to identities or register clusters with Chainguard.
* [chainctl iam invites delete](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_invites_delete/)	 - Delete invite codes
* [chainctl iam invites list](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_invites_list/)	 - Show invites that are active.

