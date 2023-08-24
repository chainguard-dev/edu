---
date: 2023-08-23T22:23:54Z
title: "chainctl clusters uninstall"
slug: chainctl_clusters_uninstall
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_uninstall/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters uninstall

Uninstalls Chainguard from the current kubernetes context.

```
chainctl clusters uninstall [--group={GROUP_NAME|GROUP_ID}] [--context=CONTEXT_NAME | --cluster={CLUSTER_NAME|CLUSTER_ID} | --inactive=DURATION] [--active-within=DURATION] [--yes]
```

### Examples

```
  # Uninstall a cluster and choose the context interactively
  chainctl cluster uninstall
  
  # Uninstall all clusters not seen in 7 days
  chainctl cluster uninstall --inactive=168h
  
  # Uninstall a cluster in a given group by context
  chainctl cluster uninstall --group=my-group --context=my-context
  
  # Uninstall a cluster in a given group by name
  chainctl cluster uninstall --group=my-group --cluster=my-cluster
  
  # Uninstall a cluster by ID
  chainctl cluster uninstall --cluster=ef127a7c0...
```

### Options

```
      --active-within duration   How recently a cluster must have been active to be listed. Zero will return all clusters. (default 24h0m0s)
      --cluster string           Indicates the name or ID of the cluster to disconnect from Chainguard.
      --context string           Indicates the name of the context (in kubectl) to disconnect from Chainguard.
      --group string             Name or ID of a group to filter clusters by for uninstallation.
  -h, --help                     help for uninstall
      --inactive duration        Delete all clusters that have not been seen within the given duration. (default 168h0m0s)
  -y, --yes                      Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl clusters](/chainguard/chainctl/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

