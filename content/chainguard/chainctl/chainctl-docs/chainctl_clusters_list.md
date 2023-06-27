---
date: 2023-06-27T18:22:50Z
title: "chainctl clusters list"
slug: chainctl_clusters_list
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters list

List clusters.

```
chainctl clusters list [--name=NAME] [--active-within=DURATION] [--group=GROUP_NAME|GROUP_ID] [--output table|json]
```

### Examples

```
  # List all clusters visible to the current user.
  chainctl cluster list
  
  # List all clusters in the group "my-group"
  chainctl cluster list --group my-group
  
  # List all clusters that have some recorded activity within the last 6 hours
  chainctl cluster list --active-within 6h
```

### Options

```
      --active-within duration   How recently a cluster must have been active to be listed. Zero will return all clusters. (default 24h0m0s)
      --group string             The name or id of the parent group to list clusters for.
  -h, --help                     help for list
  -n, --name string              The given name of the resource.
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

* [chainctl clusters](/chainguard/chainctl/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

