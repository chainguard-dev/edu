---
date: 2023-03-29T13:31:37Z
title: "chainctl"
slug: chainctl
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl

Chainguard Control

```
chainctl [flags]
```

### Options

```
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
  -h, --help                         help for chainctl
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl auth](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl clusters](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.
* [chainctl config](/chainguard/chainguard-enforce/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.
* [chainctl events](/chainguard/chainguard-enforce/chainctl-docs/chainctl_events/)	 - Events related commands for the Chainguard platform.
* [chainctl iam](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl policies](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.
* [chainctl sigstore](/chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore/)	 - Sigstore related commands for the Chainguard platform.
* [chainctl update](/chainguard/chainguard-enforce/chainctl-docs/chainctl_update/)	 - Update chainctl.
* [chainctl version](/chainguard/chainguard-enforce/chainctl-docs/chainctl_version/)	 - Prints the version

