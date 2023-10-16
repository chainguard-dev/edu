---
date: 2023-10-16T09:37:03Z
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
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.

