---
date: 2023-06-14T19:51:03Z
title: "chainctl auth configure-docker"
slug: chainctl_auth_configure-docker
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_configure-docker/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure-docker

Configure a Docker credential helper

```
chainctl auth configure-docker [flags]
```

### Options

```
      --group string               The IAM group with which the pull-token identity is associated.
      --headless                   Skip browser authentication and use device flow.
  -h, --help                       help for configure-docker
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with
      --identity-token string      Use an explicit passed identity token or token path.
      --pull-token                 Whether to register a pull token that can pull images
      --save                       If true with --pull-token, save the pull token to the Docker config
      --ttl duration               For how long a generated pull-token will be valid. (default 720h0m0s)
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

* [chainctl auth](/chainguard/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.

