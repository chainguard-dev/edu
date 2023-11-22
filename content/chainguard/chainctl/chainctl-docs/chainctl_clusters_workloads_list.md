---
date: 2023-11-21T23:15:25Z
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
chainctl clusters workloads list CLUSTER_NAME|CLUSTER_ID [--active-within=DURATION] [--namespace=NAMESPACE] [--output tree|table|json|wide]
```

### Options

```
      --active-within duration   How recently a workload must have been active to be listed. Zero will return all workloads. (default 24h0m0s)
  -h, --help                     help for list
  -n, --namespace string         The namespace whose workloads to list (default: all).
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

* [chainctl clusters workloads](/chainguard/chainctl/chainctl-docs/chainctl_clusters_workloads/)	 - Interact with cluster workloads.

