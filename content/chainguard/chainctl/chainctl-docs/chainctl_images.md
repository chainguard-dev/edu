---
date: 2025-05-12T21:16:51Z
title: "chainctl images"
slug: chainctl_images
url: /chainguard/chainctl/chainctl-docs/chainctl_images/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images

Images related commands for the Chainguard platform.

### Options

```
  -h, --help   help for images
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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl images diff](/chainguard/chainctl/chainctl-docs/chainctl_images_diff/)	 - Diff images.
* [chainctl images history](/chainguard/chainctl/chainctl-docs/chainctl_images_history/)	 - Show history for a specific image tag.
* [chainctl images list](/chainguard/chainctl/chainctl-docs/chainctl_images_list/)	 - List tagged images from Chainguard registries.
* [chainctl images repos](/chainguard/chainctl/chainctl-docs/chainctl_images_repos/)	 - Image repo related commands for the Chainguard platform.

