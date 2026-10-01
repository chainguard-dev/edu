---
date: 2026-09-30T19:15:34Z
title: "chainctl images overlays"
slug: chainctl_images_overlays
url: /platform/chainctl/chainctl-docs/chainctl_images_overlays/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images overlays

Manage Custom Assembly overlays and the repos they are attached to.

### Synopsis

Manage tag-based Custom Assembly overlays.

An overlay is a reusable image customization (packages, environment
variables, annotations, accounts, and certificates) owned by an
organization or folder. Attaching an overlay to a repo creates a binding
that selects which of the repo's tags the overlay applies to:

- --all: every tag.
- --variant: a tag variant, such as dev.
- --tag: specific tags.

When bindings of different kinds match the same tag, they layer in the
order ALL, then VARIANT, then EXACT, with later layers taking
precedence. Bindings of the same kind may coexist on a repo only when
their overlays do not conflict.

Chainguard rebuilds the matching images after an overlay or binding
changes. These rebuilds run only for organizations enrolled in tag-based
Custom Assembly. Contact your Chainguard account team to enroll.

### Examples

```
  # Create an overlay that adds packages
  chainctl images overlays create my-overlay --parent my-org --package curl --package jq

  # Attach it to every tag of a repo
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --all

  # List overlays and their bindings
  chainctl images overlays list --parent my-org
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
* [chainctl images overlays attach](/platform/chainctl/chainctl-docs/chainctl_images_overlays_attach/)	 - Attach a Custom Assembly overlay to a repo.
* [chainctl images overlays create](/platform/chainctl/chainctl-docs/chainctl_images_overlays_create/)	 - Create a Custom Assembly overlay.
* [chainctl images overlays delete](/platform/chainctl/chainctl-docs/chainctl_images_overlays_delete/)	 - Delete a Custom Assembly overlay.
* [chainctl images overlays detach](/platform/chainctl/chainctl-docs/chainctl_images_overlays_detach/)	 - Detach a Custom Assembly overlay from a repo.
* [chainctl images overlays list](/platform/chainctl/chainctl-docs/chainctl_images_overlays_list/)	 - List Custom Assembly overlays and their bindings.
* [chainctl images overlays update](/platform/chainctl/chainctl-docs/chainctl_images_overlays_update/)	 - Update a Custom Assembly overlay's name or configuration.
* [chainctl images overlays update-binding](/platform/chainctl/chainctl-docs/chainctl_images_overlays_update-binding/)	 - Change which tags a Custom Assembly overlay binding applies to.

