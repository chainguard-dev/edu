---
date: 2023-02-09T23:08:02Z
title: "chainctl clusters discover"
slug: chainctl_clusters_discover
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_discover/
draft: false
images: []
type: "article"
toc: true
---
## chainctl clusters discover

Discover eligible clusters.

```
chainctl clusters discover [--group GROUP_NAME | GROUP_ID] [--output table|json]
```

### Examples

```
  chainctl cluster discover
```

### Options

```
      --group string           The name or id of the parent group to discover clusters for.
  -h, --help                   help for discover
      --profiles stringArray   The names of Chainguard profiles to install into the cluster.
      --provider strings       The list of cluster providers over which to perform discovery, e.g. gke
      --states strings         The list of cluster states to return, e.g. UNSUPPORTED, NEEDS_WORK, ELIGIBLE, ENROLLED
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
```

### SEE ALSO

* [chainctl clusters](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

