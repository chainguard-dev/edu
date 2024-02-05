---
date: 2024-02-03T00:11:18Z
title: "chainctl config edit"
slug: chainctl_config_edit
url: /chainguard/chainctl/chainctl-docs/chainctl_config_edit/
draft: false
tags: ["chainctl", "Reference", "Product"]
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
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl config](/chainguard/chainctl/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.

