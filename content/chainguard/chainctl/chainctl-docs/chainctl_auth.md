---
date: 2024-03-14T15:41:40Z
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
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl auth configure-docker](/chainguard/chainctl/chainctl-docs/chainctl_auth_configure-docker/)	 - Configure a Docker credential helper
* [chainctl auth login](/chainguard/chainctl/chainctl-docs/chainctl_auth_login/)	 - Login to the Chainguard platform.
* [chainctl auth logout](/chainguard/chainctl/chainctl-docs/chainctl_auth_logout/)	 - Logout from the Chainguard platform.
* [chainctl auth status](/chainguard/chainctl/chainctl-docs/chainctl_auth_status/)	 - Inspect the local Chainguard Token.

