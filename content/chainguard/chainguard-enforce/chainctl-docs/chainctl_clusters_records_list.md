---
date: 2022-08-29T10:58:14-04:00
title: "chainctl clusters records list"
slug: chainctl_clusters_records_list
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_records_list/
draft: false
images: []
type: "article"
toc: true
---
## chainctl clusters records list

List cluster records.

```
chainctl clusters records list [CLUSTER_ID] [--active-within DURATION] [--output table|json|wide] [flags]
```

### Options

```
      --active-within duration   How recently a record must have been created to be listed (zero will return all records). (default 168h0m0s)
  -h, --help                     help for list
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

* [chainctl clusters records](/chainguard/chainguard-enforce/chainctl-docs/chainctl_clusters_records/)	 - Interact with cluster records.

