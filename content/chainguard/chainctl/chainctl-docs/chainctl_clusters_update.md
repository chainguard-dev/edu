---
date: 2023-10-30T22:49:10Z
title: "chainctl clusters update"
slug: chainctl_clusters_update
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters update

Update the name or description of a cluster.

```
chainctl clusters update CLUSTER_NAME|CLUSTER_ID [--name NAME] [--description DESCRIPTION] [--output table|wide|json]
```

### Examples

```
  # Update a cluster description by name
  chainctl cluster update my-cluster --description "My development cluster."
  
  # Update a cluster name by name
  chainctl cluster update my-cluster --name my-new-cluster
  
  # Update a cluster name by ID
  chainctl cluster update 19d3a64f20c64ba3ccf1bc86ce59d03e705959ad/efb53f2857d567f2 --name new-cluster-name
  
  # Delete a cluster description by name
  chainctl cluster update my-cluster --description ""
```

### Options

```
  -d, --description string     The description of the resource.
  -h, --help                   help for update
  -n, --name string            Given name of the resource.
      --opt strings            extra key=value pairs to define enforcer profile options
      --profiles stringArray   The names of Chainguard profiles to install into the cluster.
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

