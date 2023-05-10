---
date: 2023-05-09T16:54:34Z
title: "chainctl auth"
slug: chainctl_auth
url: /chainguard/chainctl/chainctl-docs/chainctl_auth/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth

Auth related commands for the Chainguard platform.

### Options

```
  -h, --help   help for auth
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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl auth login](/chainguard/chainctl/chainctl-docs/chainctl_auth_login/)	 - Login to the Chainguard platform.
* [chainctl auth logout](/chainguard/chainctl/chainctl-docs/chainctl_auth_logout/)	 - Logout from the Chainguard platform.
* [chainctl auth status](/chainguard/chainctl/chainctl-docs/chainctl_auth_status/)	 - Inspect the local Chainguard Token.

