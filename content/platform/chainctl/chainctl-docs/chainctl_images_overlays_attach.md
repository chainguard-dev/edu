---
date: 2026-09-29T17:51:01Z
title: "chainctl images overlays attach"
slug: chainctl_images_overlays_attach
url: /platform/chainctl/chainctl-docs/chainctl_images_overlays_attach/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images overlays attach

Attach a Custom Assembly overlay to a repo.

### Synopsis

Attach a Custom Assembly overlay to a repo by creating a binding.

The binding selects which of the repo's tags the overlay applies to.
Pass exactly one of:

- --all: every tag.
- --variant: a tag variant, such as dev.
- --tag: specific tags.

A repo can hold several bindings of the same kind only when their
overlays do not conflict; a conflicting binding is rejected, and the
error names the conflicting binding and fields. An overlay can be
attached to a repo only once.

The command prints the binding UID. Use it with "update-binding" and
"detach", or look it up later with "chainctl images overlays list".

```
chainctl images overlays attach [flags]
```

### Examples

```
  # Apply an overlay to every tag of a repo
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --all

  # Apply an overlay to -dev tags only
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --variant dev

  # Apply an overlay to specific tags
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --tag 3.12 --tag 3.13
```

### Options

```
      --all              Bind to every tag on the repo; multiple --all bindings may coexist when their overlays do not conflict. Mutually exclusive with --tag and --variant.
      --overlay string   Overlay to attach: UIDP or name (resolved within the repo's org).
      --parent string    Org name or UIDP for resolving --repo by name; unused when --repo is a UIDP. If unset, auto-selects when the caller belongs to a single org, otherwise prompts.
      --repo string      Target repo: UIDP, or name resolved within --parent.
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

