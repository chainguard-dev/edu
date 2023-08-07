---
date: 2023-08-07T16:21:27Z
title: "chainctl clusters"
slug: chainctl_clusters
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters

Cluster related commands for the Chainguard platform.

### Options

```
  -h, --help   help for clusters
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl clusters cidrs](/chainguard/chainctl/chainctl-docs/chainctl_clusters_cidrs/)	 - Enforce Egress CIDR related commands.
* [chainctl clusters describe](/chainguard/chainctl/chainctl-docs/chainctl_clusters_describe/)	 - Describe a cluster.
* [chainctl clusters discover](/chainguard/chainctl/chainctl-docs/chainctl_clusters_discover/)	 - Discover eligible clusters.
* [chainctl clusters install](/chainguard/chainctl/chainctl-docs/chainctl_clusters_install/)	 - Install Chainguard into the current kubernetes context.
* [chainctl clusters list](/chainguard/chainctl/chainctl-docs/chainctl_clusters_list/)	 - List clusters.
* [chainctl clusters open](/chainguard/chainctl/chainctl-docs/chainctl_clusters_open/)	 - Open the console for a cluster.
* [chainctl clusters print-config](/chainguard/chainctl/chainctl-docs/chainctl_clusters_print-config/)	 - Print the tenant configuration in YAML.
* [chainctl clusters profiles](/chainguard/chainctl/chainctl-docs/chainctl_clusters_profiles/)	 - Profile related commands.
* [chainctl clusters records](/chainguard/chainctl/chainctl-docs/chainctl_clusters_records/)	 - Interact with cluster records.
* [chainctl clusters search](/chainguard/chainctl/chainctl-docs/chainctl_clusters_search/)	 - Search a cluster or group of clusters.
* [chainctl clusters uninstall](/chainguard/chainctl/chainctl-docs/chainctl_clusters_uninstall/)	 - Uninstalls Chainguard from the current kubernetes context.
* [chainctl clusters update](/chainguard/chainctl/chainctl-docs/chainctl_clusters_update/)	 - Update the name or description of a cluster.
* [chainctl clusters workloads](/chainguard/chainctl/chainctl-docs/chainctl_clusters_workloads/)	 - Interact with cluster workloads.

