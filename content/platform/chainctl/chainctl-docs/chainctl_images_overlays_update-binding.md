---
date: 2026-09-29T17:51:01Z
title: "chainctl images overlays update-binding"
slug: chainctl_images_overlays_update-binding
url: /platform/chainctl/chainctl-docs/chainctl_images_overlays_update-binding/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images overlays update-binding

Change which tags a Custom Assembly overlay binding applies to.

### Synopsis

Change the tag selector of a Custom Assembly overlay binding.

Only the selector can change. To attach the overlay to a different repo,
or a different overlay to the repo, detach the binding and attach again.
Find the binding UID with "chainctl images overlays list".

```
chainctl images overlays update-binding <BINDING_UID> [flags]
```

### Examples

```
  chainctl images overlays update-binding <BINDING_UID> --tag 3.12 --tag 3.13
```

### Options

```
      --all              Bind to every tag on the repo; multiple --all bindings may coexist when their overlays do not conflict. Mutually exclusive with --tag and --variant.
      --tag strings      Exact tag names to bind to (repeatable). Mutually exclusive with --all and --variant.
      --variant string   Bind to a tag variant: currently only "dev" (matches tags ending in -dev). Mutually exclusive with --tag and --all.
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

* [chainctl images overlays](/platform/chainctl/chainctl-docs/chainctl_images_overlays/)	 - Manage Custom Assembly overlays and the repos they are attached to.

