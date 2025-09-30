---
date: 2025-09-29T18:30:00Z
title: "chainctl images tags"
slug: chainctl_images_tags
url: /chainguard/chainctl/chainctl-docs/chainctl_images_tags/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images tags

Tags related commands for images.

### Synopsis

Commands for listing and resolving image tags.

### Options

```
  -h, --help   help for tags
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
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.
* [chainctl images tags list](/chainguard/chainctl/chainctl-docs/chainctl_images_tags_list/)	 - List tags from repositories using --parent, --public, or --repo flags.
* [chainctl images tags resolve](/chainguard/chainctl/chainctl-docs/chainctl_images_tags_resolve/)	 - Resolve tags for a specific image reference.

