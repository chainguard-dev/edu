---
date: 2026-02-06T15:27:44Z
title: "chainctl images changelog"
slug: chainctl_images_changelog
url: /chainguard/chainctl/chainctl-docs/chainctl_images_changelog/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images changelog

Show changelog for image history

### Synopsis

Show changelog for image history.

This command fetches the tag history for an image, analyzes changes between versions,
and displays human-readable summaries of changes (similar to git log).

```
chainctl images changelog IMAGE_REFERENCE [flags]
```

### Examples

```

# Show changelog for an image (default: last 10 versions)
chainctl images changelog cgr.dev/chainguard/nginx:latest

# Show only last 5 versions
chainctl images changelog cgr.dev/chainguard/nginx:latest --depth 5

# Output as JSON
chainctl images changelog cgr.dev/chainguard/nginx:latest --output json

# Output as table
chainctl images changelog cgr.dev/chainguard/nginx:latest --output table
```

### Options

```
      --depth int         Number of historical versions to show (default 10)
  -h, --help              help for changelog
      --platform string   Platform to use for multi-arch images (e.g., linux/amd64, linux/arm64) (default "linux/amd64")
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

