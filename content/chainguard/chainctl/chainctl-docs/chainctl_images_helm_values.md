---
date: 2026-02-24T18:33:45Z
title: "chainctl images helm values"
slug: chainctl_images_helm_values
url: /chainguard/chainctl/chainctl-docs/chainctl_images_helm_values/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images helm values

Generate relocation overrides for a Chainguard Helm chart

### Synopsis

Generate minimal Helm value overrides to relocate a chart's images to a
different registry and/or organization. The output contains only the values
that differ from the chart defaults and can be passed directly to helm install -f.

Use --registry to point images at a different registry host, and --org to
change the organization prefix. If neither flag is set the output is empty.

```
chainctl images helm values CHART_REFERENCE [flags]
```

### Examples

```

# Point images at a registry mirror
chainctl images helm values cgr.dev/my-org/charts/nginx:latest --registry myregistry.example.com

# Change the organization prefix (my-org -> other-org)
chainctl images helm values cgr.dev/my-org/charts/nginx:latest --org other-org

# Both registry and organization
chainctl images helm values cgr.dev/my-org/charts/nginx:latest \
  --registry myregistry.example.com --org other-org

# Install with relocated images
helm install my-release oci://cgr.dev/my-org/charts/nginx \
  -f <(chainctl images helm values cgr.dev/my-org/charts/nginx:latest --registry myregistry.example.com)

# Output as JSON
chainctl images helm values cgr.dev/my-org/charts/nginx:latest --registry myregistry.example.com -o json
```

### Options

```
      --org string        Override the organization prefix for image repositories (e.g., other-org)
      --registry string   Override the registry host for all image references
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

