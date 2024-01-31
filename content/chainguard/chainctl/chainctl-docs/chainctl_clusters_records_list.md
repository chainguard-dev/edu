---
date: 2024-01-30T18:15:44Z
title: "chainctl clusters records list"
slug: chainctl_clusters_records_list
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_records_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters records list

List cluster records.

```
chainctl clusters records list [CLUSTER_NAME | CLUSTER_ID] [--active-within DURATION] [--image IMAGE] [--output table|json|wide]
```

### Options

```
      --active-within duration   How recently a record must have been active to be listed. Zero will return all records. (default 24h0m0s)
  -h, --help                     help for list
      --image string             The name of an image or regular expression to filter the results.
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl clusters records](/chainguard/chainctl/chainctl-docs/chainctl_clusters_records/)	 - Interact with cluster records.

