---
date: 2026-09-02T22:28:18Z
title: "chainctl config"
slug: chainctl_config
url: /platform/chainctl/chainctl-docs/chainctl_config/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl config

Local config file commands for chainctl.

### Synopsis

Local config file commands for chainctl.

Every config property can also be set with an environment variable, which is
useful for scripts and CI. Take the property name, uppercase it, replace dots
with underscores, and add a `CHAINGUARD_` prefix:

  - `default.group` becomes `CHAINGUARD_DEFAULT_GROUP`
  - `platform.api` becomes `CHAINGUARD_PLATFORM_API`
  - `output.silent` becomes `CHAINGUARD_OUTPUT_SILENT`

Environment variables take precedence over the config file, and command line
flags take precedence over both.

Setting `default.group` supplies the default for --parent, so exporting
`CHAINGUARD_DEFAULT_GROUP` avoids passing --parent to every command.

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl config edit](/platform/chainctl/chainctl-docs/chainctl_config_edit/)	 - Edit the current chainctl config file.
* [chainctl config reset](/platform/chainctl/chainctl-docs/chainctl_config_reset/)	 - Remove local chainctl config files and restore defaults.
* [chainctl config save](/platform/chainctl/chainctl-docs/chainctl_config_save/)	 - Save the current chainctl config to a config file.
* [chainctl config set](/platform/chainctl/chainctl-docs/chainctl_config_set/)	 - Set an individual configuration value property.
* [chainctl config unset](/platform/chainctl/chainctl-docs/chainctl_config_unset/)	 - Unset a configuration property and return it to default.
* [chainctl config validate](/platform/chainctl/chainctl-docs/chainctl_config_validate/)	 - Run diagnostics on local config.
* [chainctl config view](/platform/chainctl/chainctl-docs/chainctl_config_view/)	 - View the current chainctl config.

