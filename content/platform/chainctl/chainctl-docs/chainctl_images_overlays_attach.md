---
date: 2026-10-08T18:22:10Z
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

Attach Custom Assembly overlays to a repo or to every repo in an organization.

### Synopsis

Attach one or more Custom Assembly overlays by creating a binding per
overlay. A binding attaches an overlay to a single repo (--repo) or to
every repo in an organization (--all-repos), including repos created
after the binding exists.

Every binding selects which tags its overlay applies to. Pass exactly
one of:

- --all: every tag.
- --variant: a tag variant, such as dev.
- --tag: specific tags.

A repo can hold several bindings of the same kind only when their
overlays do not conflict; a conflicting binding is rejected, and the
error names the conflicting binding and fields. An overlay can be
attached to a repo only once. Multiple overlays attach in the order
given, one binding each; on a failure, the bindings already created are
kept and the error names the overlay that failed.

An all-repos binding is owned by the organization and applies its
overlay to each repo's matching tags. An overlay can have at most one
all-repos binding per organization. When an all-repos binding and a
repo's own binding match the same tag, the repo's binding takes
precedence where both overlays set the same field, and their package
lists combine. Repos with a legacy customization keep the legacy
behavior; all-repos bindings do not apply to them.

The command prints each binding UID. Use them with "update-binding" and
"detach", or look them up later with "chainctl images overlays list".

```
chainctl images overlays attach [flags]
```

### Examples

```
  # Apply an overlay to every tag of a repo
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --all

  # Apply an overlay to every tag of every repo in the organization,
  # including repos created later
  chainctl images overlays attach --overlay my-overlay --all-repos --parent my-org --all

  # Apply two overlays to every tag of a repo
  chainctl images overlays attach --overlay my-certs,my-packages --repo python --parent my-org --all

  # Apply an overlay to -dev tags only
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --variant dev

  # Apply an overlay to specific tags
  chainctl images overlays attach --overlay my-overlay --repo python --parent my-org --tag 3.12 --tag 3.13
```

### Options

```
      --all               Bind to every tag on the repo; multiple --all bindings may coexist when their overlays do not conflict. Mutually exclusive with --tag and --variant.
      --all-repos         Attach to every repo in the organization, including repos created later; mutually exclusive with --repo.
      --overlay strings   Overlay to attach: UIDP or name (resolved within the repo's org). Comma separated and repeatable; each overlay gets its own binding with the same tag selector.
      --parent string     Org name or UIDP: the organization the binding is created under with --all-repos, or the org for resolving --repo by name (unused when --repo is a UIDP). If unset, auto-selects when the caller belongs to a single org, otherwise prompts. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --repo string       Target repo: UIDP, or name resolved within --parent. Mutually exclusive with --all-repos.
      --tag strings       Exact tag names to bind to (repeatable). Mutually exclusive with --all and --variant. "all" and "dev" are not tags: use --all or --variant=dev.
      --variant string    Bind to a tag variant: currently only "dev" (matches tags ending in -dev). Mutually exclusive with --tag and --all.
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

