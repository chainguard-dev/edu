---
date: 2023-06-09T16:20:16Z
title: "chainctl clusters records vulns list"
slug: chainctl_clusters_records_vulns_list
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_records_vulns_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters records vulns list

List cluster records vulnerabilities.

```
chainctl clusters records vulns list [CLUSTER_NAME | CLUSTER_ID] [--active-within DURATION] [--image IMAGE] [--output table|json|wide]
```

### Options

```
      --active-within duration   How recently a vuln must have been active to be listed. Zero will return all vulns. (default 24h0m0s)
  -h, --help                     help for list
      --image string             The name of an image or regular expression to filter the results.
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

* [chainctl clusters records vulns](/chainguard/chainctl/chainctl-docs/chainctl_clusters_records_vulns/)	 - Interact with cluster records vulnerabilities.

