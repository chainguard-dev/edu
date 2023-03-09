---
date: 2023-03-09T00:41:03Z
title: "chainctl config edit"
slug: chainctl_config_edit
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_config_edit/
draft: false
images: []
type: "article"
toc: true
---
## chainctl config edit

Edit the current chainctl config file.

### Synopsis

Edit the current chainctl config file. Use the environment variable EDITOR to set the path to your preferred editor (default: nano).

```
chainctl config edit [--config FILE] [--yes] [--output ] [flags]
```

### Options

```
  -h, --help   help for edit
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

