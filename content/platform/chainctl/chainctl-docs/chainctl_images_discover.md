---
date: 2026-09-21T22:21:18Z
title: "chainctl images discover"
slug: chainctl_images_discover
url: /platform/chainctl/chainctl-docs/chainctl_images_discover/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images discover

Find Chainguard replacements for the images your project uses.

### Synopsis

Find Chainguard replacements for the images your project uses.

Reads every image reference under DIR (default: the current directory).
For each upstream image, it reports whether Chainguard publishes a hardened
replacement and whether your organization can pull it today.

Resolve references directly with repeatable --image flags. This skips the
directory scan.

Private-registry references are supported. An exact catalog alias is
preferred. Otherwise, repository suffixes are tried from most to least
specific. Thus registry.example/cache/dotnet/sdk retains dotnet/sdk, while
a reference ending in nginx can still suggest Chainguard's nginx. Namesake
matching identifies a catalog offering, not identical image contents.
Both what you build and what you run are covered: Dockerfile FROM
instructions, Kubernetes manifests, Compose files, Helm values, Terraform,
shell scripts and Makefiles.

Helm values are read as written, not rendered. An image assembled from
registry, repository, tag and digest keys is resolved. This includes a
chart-wide imageRegistry or imageNamespace and an empty tag standing for
the chart's appVersion. A reference computed inside templates is beyond
what reading values can see, so treat the result as what values declare.

Your immutability choice stays as written: a digest-pinned reference comes
back digest-pinned. A maintained tag is kept. A variant or older patch
resolves to the same version without the source-image variant suffix when
possible. An untagged reference is made explicit as latest, which is what Docker
already uses. When a requested version is not maintained, the suggestion uses
the newest concrete stable version on the same minor line, then the newest in
the same major, never an older line than the one you asked for. Symbolic
latest is the fallback when that major is not maintained. The resolved tag is
part of the suggested image reference. An image not yet entitled is named with
a tag because its digest cannot be resolved until it is in your catalog.

Up to three candidates are shown for each reference. Pass one image reference
to --all-candidates to show every matching variant and all of its maintained
tags. FIPS variants rank first by default; pass --fips=false to rank standard
variants first instead. Both variants remain visible when Chainguard publishes
them.

Every reference is listed with what you can do: pull the replacement today,
ask for entitlement, nothing (already on Chainguard), or nothing to move to.
What has no replacement is as much of the answer as what does.

```
chainctl images discover [DIR]
```

### Examples

```
chainctl images discover
chainctl images discover ./services
chainctl images discover --parent my-org
chainctl images discover --image nginx:1.29
chainctl images discover --all-candidates nginx:1.29
chainctl images discover --image nginx:1.29 --fips=false
chainctl images discover -o json
```

### Options

```
      --all-candidates string   Show every variant and maintained tag for one image reference.
      --fips                    Prefer FIPS variants when both FIPS and standard images are available. (default true)
      --image stringArray       Resolve an image reference directly instead of scanning a directory; may be repeated.
      --parent string           Name or UIDP of the organization whose entitlements to check. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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

