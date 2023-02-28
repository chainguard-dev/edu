---
date: 2023-02-28T15:11:37Z
title: "chainctl config unset"
slug: chainctl_config_unset
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_config_unset/
draft: false
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

