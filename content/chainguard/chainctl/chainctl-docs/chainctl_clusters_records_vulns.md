---
date: 2023-08-21T16:12:10Z
title: "chainctl clusters records vulns"
slug: chainctl_clusters_records_vulns
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_records_vulns/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters records vulns

Interact with cluster records vulnerabilities.

### Options

```
  -h, --help   help for vulns
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

* [chainctl clusters records](/chainguard/chainctl/chainctl-docs/chainctl_clusters_records/)	 - Interact with cluster records.
* [chainctl clusters records vulns describe](/chainguard/chainctl/chainctl-docs/chainctl_clusters_records_vulns_describe/)	 - Describe the CVEs from the cluster vulnerability report.
* [chainctl clusters records vulns list](/chainguard/chainctl/chainctl-docs/chainctl_clusters_records_vulns_list/)	 - List cluster records vulnerabilities.

