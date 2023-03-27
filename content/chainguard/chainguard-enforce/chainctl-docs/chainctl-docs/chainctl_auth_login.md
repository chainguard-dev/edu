---
date: 2023-03-23T19:47:43Z
title: "chainctl auth login"
slug: chainctl_auth_login
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_login/
draft: false
images: []
type: "article"
toc: true
---
## chainctl auth login

Login to the Chainguard platform.

```
chainctl auth login [--identity-token TOKEN] [--invite-code INVITE_CODE | --register] [--cluster CLUSTER_ID] [--refresh]
```

### Examples

```
  # Default auth login flow:
  chainctl auth login
  
  # Refreshing a token within a Kubernetes context:
  chainctl auth login --identity-token=PATH_TO_TOKEN --refresh
  
  # Register and create a new root group
  chainctl auth login --register
  
  # Register by accepting an invite to an existing group
  chainctl auth login --invite-code eyJncnAiOiI5MzA...
```

### Options

```
      --cluster string          UID of the Cluster.
      --headless                Skip browser authentication and use device flow.
  -h, --help                    help for login
      --identity string         The unique ID of the identity to assume when logging in.
      --identity-token string   Use an explicit passed identity token or token path.
      --invite-code string      Registration invite code.
      --refresh                 Enable auto refresh of the Chainguard token (for workloads).
      --register                Register a new account if needed. Will create a new root group when an invite code is not specified.
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

* [chainctl auth](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.

