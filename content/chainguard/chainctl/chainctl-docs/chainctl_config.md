---
date: 2023-05-22T09:40:20Z
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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl config edit](/chainguard/chainctl/chainctl-docs/chainctl_config_edit/)	 - Edit the current chainctl config file.
* [chainctl config reset](/chainguard/chainctl/chainctl-docs/chainctl_config_reset/)	 - Remove local chainctl config files and restore defaults.
* [chainctl config save](/chainguard/chainctl/chainctl-docs/chainctl_config_save/)	 - Save the current chainctl config to a config file.
* [chainctl config set](/chainguard/chainctl/chainctl-docs/chainctl_config_set/)	 - Set an individual configuration value property.
* [chainctl config unset](/chainguard/chainctl/chainctl-docs/chainctl_config_unset/)	 - Unset a configuration property and return it to default.
* [chainctl config view](/chainguard/chainctl/chainctl-docs/chainctl_config_view/)	 - View the current chainctl config.

