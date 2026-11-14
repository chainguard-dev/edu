---
date: 2026-11-13T20:36:51Z
title: "chainctl images entitlements add-image"
slug: chainctl_images_entitlements_add-image
url: /platform/chainctl/chainctl-docs/chainctl_images_entitlements_add-image/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images entitlements add-image

Add a catalog image to an organization's registry entitlement.

```
chainctl images entitlements add-image (--parent=PARENT | --entitlement-id=ENTITLEMENT_ID) IMAGE_NAME [flags]
```

### Options

```
      --entitlement-id string   The id of the entitlement to add the image to directly.
      --parent string           The name or id of the org to add an entitlement image to.
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

