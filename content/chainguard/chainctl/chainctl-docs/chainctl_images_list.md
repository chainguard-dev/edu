---
date: 2025-09-02T09:39:16Z
title: "chainctl images list"
slug: chainctl_images_list
url: /chainguard/chainctl/chainctl-docs/chainctl_images_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images list

List tagged images from Chainguard registries.

```
chainctl images list [--repo=REPO_NAME] [--public | --parent=PARENT_NAME|PARENT_ID] [--updated-within=DURATION] [--show-dates] [--show-epochs] [--show-referrers] [--output=csv|id|json|table|terse|tree|wide]
```

### Options

```
  -h, --help                      help for list
      --parent string             The name or id of the parent location to list image repos.
      --public                    List repos from the public Chainguard registry.
      --recursive                 Search repositories recursively through all descendants instead of just children
      --repo string               Search for a specific repo by name.
      --show-dates                Whether to show date tags of the form latest-{date}.
      --show-epochs               Whether to show epoch tags of the form 1.2.3-r4.
      --show-referrers            Whether to show referrer tags of the form sha256-deadbeef.{sig,sbom,att}.
      --updated-within duration   The duration within which an image must have been updated (0 disables the filter).
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

