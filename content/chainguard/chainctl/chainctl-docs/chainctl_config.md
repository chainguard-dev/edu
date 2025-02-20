---
date: 2025-02-19T23:30:24Z
title: "chainctl config"
slug: chainctl_config
url: /chainguard/chainctl/chainctl-docs/chainctl_config/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl config

Local config file commands for chainctl.

### Options

```
  -h, --help   help for config
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, , json, id, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl config edit](/chainguard/chainctl/chainctl-docs/chainctl_config_edit/)	 - Edit the current chainctl config file.
* [chainctl config reset](/chainguard/chainctl/chainctl-docs/chainctl_config_reset/)	 - Remove local chainctl config files and restore defaults.
* [chainctl config save](/chainguard/chainctl/chainctl-docs/chainctl_config_save/)	 - Save the current chainctl config to a config file.
* [chainctl config set](/chainguard/chainctl/chainctl-docs/chainctl_config_set/)	 - Set an individual configuration value property.
* [chainctl config unset](/chainguard/chainctl/chainctl-docs/chainctl_config_unset/)	 - Unset a configuration property and return it to default.
* [chainctl config validate](/chainguard/chainctl/chainctl-docs/chainctl_config_validate/)	 - Run diagnostics on local config.
* [chainctl config view](/chainguard/chainctl/chainctl-docs/chainctl_config_view/)	 - View the current chainctl config.

