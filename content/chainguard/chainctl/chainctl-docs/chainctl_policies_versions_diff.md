---
date: 2024-02-20T22:23:18Z
title: "chainctl policies versions diff"
slug: chainctl_policies_versions_diff
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_versions_diff/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies versions diff

View the differences between two versions of a policy.

```
chainctl policies versions diff VERSION_ID VERSION_ID [flags]
```

### Options

```
  -h, --help   help for diff
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

* [chainctl policies versions](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions/)	 - Commands for interacting with policy versions on the Chainguard platform.

