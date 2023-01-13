---
date: 2022-12-15T19:03:53-05:00
title: "chainctl clusters open"
slug: chainctl_clusters_open
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_open/
draft: false
images: []
type: "article"
toc: true
---
## chainctl clusters open

Open the console for a cluster.

```
chainctl clusters open [CLUSTER_ID] [--output table|json]
```

### Options

```
  -h, --help   help for open
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp_authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
```

### SEE ALSO

* [chainctl clusters](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

