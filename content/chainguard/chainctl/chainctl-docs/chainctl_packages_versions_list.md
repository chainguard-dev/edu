---
date: 2025-04-08T07:31:17Z
title: "chainctl packages versions list"
slug: chainctl_packages_versions_list
url: /chainguard/chainctl/chainctl-docs/chainctl_packages_versions_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl packages versions list

List package version data from Chainguard repositories.

```
chainctl packages versions list PACKAGE_NAME [--show-eol] [--show-active] [--show-fips] [--output=csv|json|table|wide]
```

### Options

```
  -h, --help          help for list
      --show-active   Show only active versions.
      --show-eol      Show only EOL versions.
      --show-fips     Show only FIPS versions.
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
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl packages versions](/chainguard/chainctl/chainctl-docs/chainctl_packages_versions/)	 - Package version related commands for the Chainguard platform.

