---
date: 2025-03-27T19:16:41Z
title: "chainctl config unset"
slug: chainctl_config_unset
url: /chainguard/chainctl/chainctl-docs/chainctl_config_unset/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl config unset

Unset a configuration property and return it to default.

### Synopsis

Unset a configuration property and return it to default. Property names are dot delimited and lowercase (for example, output.color.pass).

```
chainctl config unset PROPERTY_NAME
```

### Examples

```
  # Return the pass color to its default
  chainctl config unset output.color.pass
```

### Options

```
  -h, --help   help for unset
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

* [chainctl config](/chainguard/chainctl/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.

