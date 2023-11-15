---
date: 2023-11-15T09:28:36Z
title: "chainctl clusters search"
slug: chainctl_clusters_search
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_search/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters search

Search a cluster or group of clusters.

```
chainctl clusters search [CLUSTER_NAME | CLUSTER_ID | GROUP_NAME | GROUP_ID ] [--packages=PACKAGE_LIST] [--active-within DURATION] [--output tree|table|json|wide]
```

### Examples

```
  # Search a cluster by name for klog v2
  chainctl cluster search my_cluster_name --packages=k8s.io/klog/v2
  
  # Search a cluster by ID for both versions of klog
  chainctl cluster search ef127a7c0909329f04b43d845cf80eea4247a07b/a99cd6e82bca5146/9a778e6db762b750 --packages=k8s.io/klog/v2,k8s.io/klog
  
  # Search all clusters within a group that were active within the past 6 hours for zap
  chainctl cluster search my_group --packages=go.uber.org/zap --active-within=6h
```

### Options

```
      --active-within duration   How recently a cluster must have been active to be listed. Zero will return all clusters. (default 24h0m0s)
  -h, --help                     help for search
      --packages string          A comma-delimited list of packages to search for in the cluster.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl clusters](/chainguard/chainctl/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

