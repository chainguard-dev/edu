---
date: 2026-11-13T20:36:51Z
title: "chainctl images helm status"
slug: chainctl_images_helm_status
url: /platform/chainctl/chainctl-docs/chainctl_images_helm_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images helm status

Show the sync status of a Helm chart added to an organization.

### Synopsis

Show the sync status of a Helm chart added to an organization.

The status is one of:

  AWAITING_IMAGES  An image the chart requires has no repository in the
                   organization. The missing images are listed; add them with
                   chainctl images helm add-chart.
  QUEUED           The chart is queued to sync.
  IN_PROGRESS      The chart is syncing.
  FAILED           The chart's sync failed.
  SYNCED           The chart is not queued and holds at least one version.

The required images are read from a single chart version. By default the newest
non-FIPS version is checked; pass --fips to check the newest FIPS version, or
--tag to check a specific version. --fips and --tag can't be combined. Every
other part of the status describes the chart repository, not one version.

CHART accepts either a bare chart name (with --parent) or a full OCI reference
without a tag.

```
chainctl images helm status CHART [flags]
```

### Examples

```

# Status of the flux chart in my-org
chainctl images helm status flux --parent my-org/charts

# Check the images a specific chart version requires
chainctl images helm status flux --parent my-org/charts --tag 2.18.4

# Check the images the newest FIPS version requires
chainctl images helm status cgr.dev/my-org/charts/flux --fips

# JSON output
chainctl images helm status flux --parent my-org/charts -o json
```

### Options

```
      --fips            Check the images the newest FIPS version requires.
      --parent string   Group path where the chart lives (e.g. my-org/charts or my-org/iamguarded-charts). Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --tag string      The chart version whose required images to check. Defaults to the newest non-FIPS version.
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

