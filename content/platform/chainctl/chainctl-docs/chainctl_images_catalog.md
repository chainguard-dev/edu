---
date: 2026-09-04T19:05:48Z
title: "chainctl images catalog"
slug: chainctl_images_catalog
url: /platform/chainctl/chainctl-docs/chainctl_images_catalog/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images catalog

List the Chainguard Images catalog.

### Synopsis

List the Chainguard Images catalog.

Shows every image Chainguard publishes, along with the upstream images each one
replaces. This is the full catalog, not the images your organization is
entitled to pull: use 'chainctl images repos list' for that.

--name matches any image whose name contains the given text, so --name jdk
finds both "jdk" and "adoptium-jdk".

An image can carry hundreds of active tags, so a long page previews a few per
image and reports how many are left. A page short enough to afford it lists
every tag instead, which is what narrowing down gets you; --all-tags asks for
the full list whatever the page length. JSON always carries every tag.

In a terminal the catalog is shown a page at a time and --limit sets the page
size, so the whole catalog stays reachable. When the output is piped or JSON,
--limit is the maximum number of images returned.

```
chainctl images catalog
```

### Examples

```
  chainctl images catalog
  chainctl images catalog --name postgres
  chainctl images catalog --name go --all-tags
  chainctl images catalog --limit 200 -o json
```

### Options

```
      --all-tags      List every active tag for each image, however long the page. A short page does this anyway.
      --limit int32   The number of images per page in an interactive terminal; otherwise the maximum number to return. (default 50)
      --name string   Show only images whose name contains this substring.
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

* [chainctl images](/platform/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.

