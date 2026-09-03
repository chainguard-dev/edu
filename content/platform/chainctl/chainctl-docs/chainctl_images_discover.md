---
date: 2026-09-02T22:28:18Z
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

Reads every image reference under DIR (default: the current directory) and
reports, for each upstream image, whether Chainguard publishes a hardened
replacement and whether your organization can pull it today.

Both what you build and what you run are covered: the FROM instructions of your
Dockerfiles, and the Kubernetes manifests, Compose files, Helm values, Terraform,
shell scripts and Makefiles beside them.

Helm values are read as written, not rendered. An image assembled from registry,
repository, tag and digest keys is resolved, including a chart-wide imageRegistry
or imageNamespace and an empty tag standing for the chart's appVersion. A chart
whose reference is computed inside its templates is beyond what reading values
can see, so treat a chart's result as what its values declare.

Your immutability choice stays as you wrote it: a digest-pinned reference comes
back digest-pinned. A maintained tag is kept, a variant or older patch resolves
to its maintained version line when possible, and an untagged reference is made
explicit as latest, which is what Docker already uses. When no requested version
is maintained, the suggestion falls back to a maintained latest tag. An image
you are not yet entitled to is named with a tag because its digest cannot be
resolved until it is in your catalog.

Every reference is listed, with what you can do about it: pull the replacement
today, ask for entitlement, nothing (you are already on Chainguard), or nothing
to move to. What has no replacement is as much of the answer as what does.

```
chainctl images discover [DIR]
```

### Examples

```
  chainctl images discover
  chainctl images discover ./services
  chainctl images discover --parent my-org
  chainctl images discover -o json
```

### Options

```
      --parent string   Name or UIDP of the organization whose entitlements to check. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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

