---
date: 2024-02-20T22:23:18Z
title: "chainctl config set"
slug: chainctl_config_set
url: /chainguard/chainctl/chainctl-docs/chainctl_config_set/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl config set

Set an individual configuration value property.

### Synopsis

Set an individual configuration value property. Property names are dot delimited and lowercase (for example, output.color.pass).

```
chainctl config set PROPERTY_NAME PROPERTY_VALUE
```

### Examples

```
  # Set the api URL
  chainctl config set platform.api https://console-api.enforce.dev
```

### Options

```
  -h, --help   help for set
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

