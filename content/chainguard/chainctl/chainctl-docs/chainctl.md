---
date: 2023-12-11T21:29:01Z
title: "chainctl"
slug: chainctl
url: /chainguard/chainctl/chainctl-docs/chainctl/
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
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
  -h, --help                         help for chainctl
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl auth](/chainguard/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl clusters](/chainguard/chainctl/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.
* [chainctl config](/chainguard/chainctl/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.
* [chainctl events](/chainguard/chainctl/chainctl-docs/chainctl_events/)	 - Events related commands for the Chainguard platform.
* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.
* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.
* [chainctl sigstore](/chainguard/chainctl/chainctl-docs/chainctl_sigstore/)	 - Sigstore related commands for the Chainguard platform.
* [chainctl update](/chainguard/chainctl/chainctl-docs/chainctl_update/)	 - Update chainctl.
* [chainctl version](/chainguard/chainctl/chainctl-docs/chainctl_version/)	 - Prints the version

