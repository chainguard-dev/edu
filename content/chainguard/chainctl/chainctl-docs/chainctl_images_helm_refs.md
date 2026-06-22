---
date: 2026-06-19T17:44:19Z
title: "chainctl images helm refs"
slug: chainctl_images_helm_refs
url: /chainguard/chainctl/chainctl-docs/chainctl_images_helm_refs/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images helm refs

List image references pinned in a Chainguard Helm chart

### Synopsis

List every distinct image reference pinned in a Chainguard Helm
chart's chart-lock attestation, including images from subcharts.

By default each ref is printed on its own line as
{registry}/{repoName}:{tag}@{digest}, with the {registry}/{org} prefix derived
from the chart-lock's chart reference. Use --repository to override that
prefix when emitting refs for a relocated copy of the chart's images.

With -o json, each ref is emitted as a JSON object containing the repoName,
tag and digest fields recorded in the chart-lock; the repository override
does not affect the JSON output.

```
chainctl images helm refs CHART_REFERENCE [flags]
```

### Examples

```

# Print pinned image refs for a chart
chainctl images helm refs cgr.dev/my-org/charts/flux:v2.18.4

# Emit as JSON
chainctl images helm refs cgr.dev/my-org/charts/flux:v2.18.4 -o json

# Override the prefix to describe a relocated mirror of the images
chainctl images helm refs cgr.dev/my-org/charts/flux:v2.18.4 \
  --repository myregistry.internal/images/chainguard
```

### Options

```
      --repository string   Override the {registry}/{org} prefix for image references (e.g., myregistry.internal/images/chainguard)
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

* [chainctl images helm](/chainguard/chainctl/chainctl-docs/chainctl_images_helm/)	 - Helm chart related commands

