---
date: 2025-10-06T17:48:56Z
title: "chainctl images tags resolve"
slug: chainctl_images_tags_resolve
url: /chainguard/chainctl/chainctl-docs/chainctl_images_tags_resolve/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images tags resolve

Resolve tags for a specific image reference.

```
chainctl images tags resolve IMAGE_REF
```

### Options

```
      --all    Return all tags that match the digest of the specified image reference.
  -h, --help   help for resolve
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

* [chainctl images tags](/chainguard/chainctl/chainctl-docs/chainctl_images_tags/)	 - Tags related commands for images.

