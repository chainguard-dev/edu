---
date: 2022-08-29T10:58:14-04:00
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
chainctl clusters open [CLUSTER_ID] [--output table|json] [flags]
```

### Options

```
  -h, --help   help for open
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string   The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string     A specific chainctl config file.
      --console string    The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string     The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string     Output format. One of: ["", "table", "tree", "json", "id", "wide"]
```

### SEE ALSO

* [chainctl clusters](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

