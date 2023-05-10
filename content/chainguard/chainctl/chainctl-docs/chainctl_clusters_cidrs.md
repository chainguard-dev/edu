---
date: 2023-05-09T16:54:34Z
title: "chainctl clusters cidrs"
slug: chainctl_clusters_cidrs
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_cidrs/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters cidrs

Enforce Egress CIDR related commands.

### Options

```
  -h, --help   help for cidrs
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

* [chainctl clusters](/chainguard/chainctl/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.
* [chainctl clusters cidrs list](/chainguard/chainctl/chainctl-docs/chainctl_clusters_cidrs_list/)	 - List Enforce Egress CIDR ranges.

