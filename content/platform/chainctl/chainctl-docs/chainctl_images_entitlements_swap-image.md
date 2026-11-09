---
date: 2026-11-06T22:09:37Z
title: "chainctl images entitlements swap-image"
slug: chainctl_images_entitlements_swap-image
url: /platform/chainctl/chainctl-docs/chainctl_images_entitlements_swap-image/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images entitlements swap-image

Atomically swap catalog images on an organization's registry entitlement.

### Synopsis

Atomically remove and add catalog images on an organization's registry entitlement in a single request.

Either the whole swap applies or nothing does, so a swap never leaves an image removed without its replacement. Each image you swap out counts against the organization's rolling 30-day swap quota. Unless the swap quota is unlimited, an image you swap out cannot be added back to the same entitlement until 30 days after its removal. Swaps made by Chainguard staff count against neither. Both --remove and --add are required and may be repeated; an image may not appear in both.

```
chainctl images entitlements swap-image (--parent=PARENT | --entitlement-id=ENTITLEMENT_ID) --remove=IMAGE --add=IMAGE [flags]
```

### Options

```
      --add strings             Catalog image name to add. Repeatable.
      --entitlement-id string   The id of the entitlement to swap images on directly.
      --parent string           The name or id of the org to swap entitlement images on.
      --remove strings          Catalog image name to remove. Repeatable.
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

* [chainctl images entitlements](/platform/chainctl/chainctl-docs/chainctl_images_entitlements/)	 - Manage entitlements to registry repositories.

