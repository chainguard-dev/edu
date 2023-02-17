---
date: 2023-02-17T21:22:59Z
title: "chainctl iam"
slug: chainctl_iam
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_iam/
draft: false
images: []
type: "article"
toc: true
---
## chainctl iam

IAM related commands for the Chainguard platform.

### Options

```
  -h, --help   help for iam
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

* [chainctl](/chainguard/chainguard-enforce/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl iam groups](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.
* [chainctl iam invites](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_invites/)	 - Manage invite codes that register identities or clusters with Chainguard.
* [chainctl iam role-bindings](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role bindings resource interactions.
* [chainctl iam roles](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

