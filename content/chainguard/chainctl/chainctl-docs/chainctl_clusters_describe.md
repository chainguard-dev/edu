---
date: 2023-11-21T23:15:25Z
title: "chainctl clusters describe"
slug: chainctl_clusters_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters describe

Describe a cluster.

```
chainctl clusters describe [CLUSTER_NAME | CLUSTER_ID] [--active-within DURATION] [--all] [--images] [--packages] [--policies] [--output |json]
```

### Examples

```
  # Describe a cluster
  chainctl cluster describe my-cluster
  
  # Display just the records of images that have been seen in the past 6 hours.
  chainctl cluster describe --active-within 6h
  
  # Display just policy information about a cluster
  chainctl cluster describe my-cluster --policies
  
  # Display package and image information, and include all records
  chainctl cluster describe my-cluster --images --packages --all
  
  # Including all three flags is the same as the default behavior with no flags.
  chainctl cluster describe my-cluster --images --packages --policies
```

### Options

```
      --active-within duration   How recently a cluster must have been active to be listed. Zero will return all clusters. (default 24h0m0s)
      --all                      Whether to include all records in the output, even for large collections.
  -h, --help                     help for describe
      --images                   Include images data in output. Use with --packages and/or --policies to filter output. If all three are omitted, all categories are included by default.
      --packages                 Include package data in output. Use with --images and/or --policies to filter output. If all three are omitted, all categories are included by default.
      --policies                 Include policy data in output. Use with --packages and/or --images to filter output. If all three are omitted, all categories are included by default.
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

