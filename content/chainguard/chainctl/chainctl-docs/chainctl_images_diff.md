---
date: 2023-08-15T09:26:23Z
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
      --group string     The name or id of the parent group to list image repos.
  -h, --help             help for diff
      --show-dates       Whether to show date tags of the form latest-{date}.
      --show-epochs      Whether to show epoch tags of the form 1.2.3-r4.
      --show-referrers   Whether to show referrer tags of the form sha256-deadbeef.{sig,sbom,att}.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.

