---
date: 2025-05-22T21:15:18Z
title: "chainctl images history"
slug: chainctl_images_history
url: /chainguard/chainctl/chainctl-docs/chainctl_images_history/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images history

Show history for a specific image tag.

### Synopsis

Show history for a specific image tag.

If a digest does not represent a multi-arch image, only a single digest without architecture information will be displayed.
Architecture information may not be available for all digests.

Examples:
  # Show history for a specific tag (selected interactively)
  chainctl images history nginx

  # Show history for a specific tag (specified in the command)
  chainctl images history nginx:1.21.0

  # Show history for a tag in a specific organization
  chainctl images history nginx:1.21.0 --parent=my-org

```
chainctl images history IMAGE[:TAG] [flags]
```

### Options

```
  -h, --help            help for history
      --parent string   Organization to view image history from
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
  -o, --output string      Output format. One of: [csv, env, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.

