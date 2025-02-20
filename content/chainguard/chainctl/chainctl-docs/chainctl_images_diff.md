---
date: 2025-02-19T23:30:24Z
title: "chainctl images diff"
slug: chainctl_images_diff
url: /chainguard/chainctl/chainctl-docs/chainctl_images_diff/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images diff

Diff images.

```
chainctl images diff FROM_IMAGE TO_IMAGE [flags]
```

### Options

```
  -h, --help              help for diff
      --platform string   Specifies the platform in the form os/arch (e.g. linux/amd64, linux/arm64) (default "linux/amd64")
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

* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.

