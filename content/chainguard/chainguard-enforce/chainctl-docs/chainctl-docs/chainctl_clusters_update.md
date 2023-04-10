---
date: 2023-04-10T21:58:49Z
title: "chainctl clusters update"
slug: chainctl_clusters_update
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters update

Update the name or description of a cluster.

```
chainctl clusters update CLUSTER_NAME | CLUSTER_ID [--name NAME] [--description DESCRIPTION] [--output table|wide|json]
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

* [chainctl clusters](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

