---
date: 2023-07-27T14:41:01Z
title: "chainctl clusters discover"
slug: chainctl_clusters_discover
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_discover/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters discover

Discover eligible clusters.

```
chainctl clusters discover --provider=PROVIDER1,PROVIDER2,... [--states=STATE1,STATE2,...] [--profiles=PROFILE1,PROFILE2,...] [--opt=KEY=VALUE,KEY=VALUE...] --group=GROUP_NAME|GROUP_ID [--output table|json]
```

### Examples

```
  # Discover GCP clusters
  chainctl cluster discover --provider=gcp
  
  # Discover eligible ECS and App Runner instances
  chainctl cluster discover --provider=ecs,app_runner --states=ELIGIBLE
```

### Options

```
      --group string           The name or id of the parent group to discover clusters for.
  -h, --help                   help for discover
      --opt strings            extra key=value pairs to define enforcer profile options
      --profiles stringArray   The names of Chainguard profiles to install into the cluster.
      --provider strings       The list of cluster providers over which to perform discovery, e.g. gke
      --states strings         The list of cluster states to return, e.g. UNSUPPORTED, NEEDS_WORK, ELIGIBLE, ENROLLED
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

