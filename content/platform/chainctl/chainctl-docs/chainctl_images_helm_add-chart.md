---
date: 2026-09-04T19:05:48Z
title: "chainctl images helm add-chart"
slug: chainctl_images_helm_add-chart
url: /platform/chainctl/chainctl-docs/chainctl_images_helm_add-chart/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images helm add-chart

Add a Chainguard Helm chart and its image dependencies to an organization.

### Synopsis

Add a Chainguard Helm chart and its image dependencies to an organization.

Creates synced image repositories in the destination organization for the given
Helm chart and all image dependencies listed in the chart's metadata. Repositories
that already exist in the destination organization are skipped. All tags are synced.

Charts are looked up by name in the community catalog by default. To add a chart
from the iamguarded catalog, prefix the name with "iamguarded-charts/".

The chart's image dependencies are read from a single chart tag. By default the
newest non-FIPS tag is used; pass --tag to inspect a specific chart version
instead (including a FIPS variant).

Examples:
  # Add the argo-cd community chart and all of its image dependencies to an organization
  chainctl images helm add-chart argo-cd --parent my-org

  # Add a specific version of the argo-cd chart
  chainctl images helm add-chart argo-cd --tag 9.5.20 --parent my-org

  # Add the redis iamguarded chart and all of its image dependencies to an organization
  chainctl images helm add-chart iamguarded-charts/redis --parent my-org

```
chainctl images helm add-chart CHART [flags]
```

### Options

```
      --dry-run         Dry-run mode: don't create repos, only show what would change.
      --parent string   The organization to add the chart and its images to.
      --tag string      The chart tag to inspect for image dependencies. Defaults to the newest non-FIPS tag.
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

* [chainctl images helm](/platform/chainctl/chainctl-docs/chainctl_images_helm/)	 - Helm chart related commands

