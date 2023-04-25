---
date: 2023-04-24T22:08:04Z
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

