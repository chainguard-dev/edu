---
date: 2022-08-29T10:58:14-04:00
title: "chainctl clusters uninstall"
slug: chainctl_clusters_uninstall
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_uninstall/
draft: false
images: []
type: "article"
toc: true
---
## chainctl clusters uninstall

Uninstalls Chainguard from the current kubernetes context.

```
chainctl clusters uninstall [--context CONTEXT_NAME | --inactive DURATION | --inactive DURATION --group GROUP_NAME|GROUP_ID] [flags]
```

### Examples

```
  chainctl cluster uninstall
  
  # Uninstall all clusters not seen in 7 days
  chainctl cluster uninstall --inactive 168h
```

### Options

```
      --context string      Indicates the name of the context (in kubectl) to disconnect from Chainguard.
      --group string        Name or ID of a group to filter clusters not seen within the given duration.
  -h, --help                help for uninstall
      --inactive duration   Delete all clusters that have not been seen within the given duration. (default 168h0m0s)
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

