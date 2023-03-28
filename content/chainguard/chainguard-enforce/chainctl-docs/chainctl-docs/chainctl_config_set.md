---
date: 2023-03-28T14:50:08Z
title: "chainctl config set"
slug: chainctl_config_set
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_config_set/
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

