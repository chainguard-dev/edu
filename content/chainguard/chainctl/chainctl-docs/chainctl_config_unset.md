---
date: 2023-06-30T16:00:39Z
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
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl config](/chainguard/chainctl/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.

