---
date: 2023-04-11T16:56:59Z
title: "chainctl config reset"
slug: chainctl_config_reset
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_config_reset/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl config reset

Remove local chainctl config files and restore defaults.

```
chainctl config reset [--yes]
```

### Options

```
  -h, --help   help for reset
  -y, --yes    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl config](/chainguard/chainguard-enforce/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.

