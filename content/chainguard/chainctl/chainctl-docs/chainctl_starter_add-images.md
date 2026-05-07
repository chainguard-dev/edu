---
date: 2026-05-06T12:14:02Z
title: "chainctl starter add-images"
slug: chainctl_starter_add-images
url: /chainguard/chainctl/chainctl-docs/chainctl_starter_add-images/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl starter add-images

Add catalog images to your catalog starter organization.

### Synopsis

Add catalog images to your catalog starter organization.

The target organization is the single verified kind=starter org the
caller's identity is bound to — auto-discovered, no flags needed.

Images are resolved against the catalog by exact name match. The server
picks the active starter entitlement that has remaining capacity. The
total cap across all starter images is enforced by the server.

```
chainctl starter add-images IMAGE_NAME [IMAGE_NAME ...] [flags]
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl starter](/chainguard/chainctl/chainctl-docs/chainctl_starter/)	 - Manage catalog starter organizations

