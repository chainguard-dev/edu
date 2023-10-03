---
date: 2023-10-03T20:15:50Z
title: "chainctl clusters profiles list"
slug: chainctl_clusters_profiles_list
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_profiles_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters profiles list

List cluster profiles.

```
chainctl clusters profiles list [--output table|json|wide]
```

### Options

```
  -h, --help   help for list
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

* [chainctl clusters profiles](/chainguard/chainctl/chainctl-docs/chainctl_clusters_profiles/)	 - Profile related commands.

