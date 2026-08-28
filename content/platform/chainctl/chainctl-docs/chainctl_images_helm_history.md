---
date: 2026-08-27T20:49:25Z
title: "chainctl images helm history"
slug: chainctl_images_helm_history
url: /platform/chainctl/chainctl-docs/chainctl_images_helm_history/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images helm history

Show digest history for a Chainguard Helm chart tag.

### Synopsis

Show the digest history for a Chainguard Helm chart tag.

Chart tags are mutable. This command lists every digest a chart tag has pointed
at over time, ordered newest first, so you can identify when a regression was
introduced and pin to an earlier digest.

CHART accepts either a bare chart name (with --parent) or a full OCI reference.
If no tag is provided, you will be prompted to select one.

```
chainctl images helm history CHART[:TAG] [flags]
```

### Examples

```

# Bare chart name with an explicit parent group path
chainctl images helm history flux:v2.18.4 --parent my-org/charts

# Bare chart name in the iamguarded-charts folder
chainctl images helm history flux:v2.18.4 --parent my-org/iamguarded-charts

# Interactively pick a tag
chainctl images helm history flux --parent my-org/charts

# Full OCI reference
chainctl images helm history cgr.dev/my-org/charts/flux:v2.18.4

# JSON output
chainctl images helm history flux:v2.18.4 --parent my-org/charts -o json
```

### Options

```
      --parent string   Group path where the chart lives (e.g. my-org/charts or my-org/iamguarded-charts). Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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

