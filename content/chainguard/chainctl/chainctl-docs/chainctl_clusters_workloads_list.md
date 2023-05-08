---
date: 2023-05-08T20:57:19Z
title: "chainctl clusters workloads list"
slug: chainctl_clusters_workloads_list
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_workloads_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters workloads list

List cluster workloads.

```
chainctl clusters workloads list [CLUSTER_ID] [--active-within DURATION] [--output tree|table|json|wide]
```

### Options

```
      --active-within duration   How recently a workload must have been active to be listed. Zero will return all workloads. (default 24h0m0s)
  -h, --help                     help for list
  -n, --namespace string         The namespace whose workloads to list (default: all).
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

* [chainctl clusters workloads](/chainguard/chainctl/chainctl-docs/chainctl_clusters_workloads/)	 - Interact with cluster workloads.

