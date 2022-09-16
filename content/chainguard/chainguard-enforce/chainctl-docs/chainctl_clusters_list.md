---
date: 2022-08-29T10:58:14-04:00
title: "chainctl clusters list"
slug: chainctl_clusters_list
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_list/
draft: false
images: []
type: "article"
toc: true
---
## chainctl clusters list

List clusters.

```
chainctl clusters list [--name NAME] [--active-within DURATION] [--group GROUP_ID|GROUP_NAME] [--output table|json] [flags]
```

### Examples

```
  chainctl cluster list
```

### Options

```
      --active-within duration   How recently a cluster must have been active to be listed (zero will return all clusters). (default 168h0m0s)
      --group string             The name or id of the parent group to list clusters from.
  -h, --help                     help for list
  -n, --name string              The given name of the resource.
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string   The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string     A specific chainctl config file.
      --console string    The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string     The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string     Output format. One of: ["", "table", "tree", "json", "id", "wide"]
```

### SEE ALSO

* [chainctl clusters](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

