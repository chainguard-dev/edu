---
date: 2026-05-04T16:59:58Z
title: "chainctl starter status"
slug: chainctl_starter_status
url: /chainguard/chainctl/chainctl-docs/chainctl_starter_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl starter status

Show catalog starter organization status, quota, and image readiness.

### Synopsis

Show the status of your catalog starter organization.

Reports the registry path, account provisioning status, image quota
usage, and per-image readiness — INITIALIZING until the catalog
syncer has both created the repo and mirrored at least one tag, READY
afterwards.

Use this command to check whether a newly-added image is pullable yet,
or to confirm your starter org has finished provisioning before
running 'chainctl starter add-images'.

```
chainctl starter status [flags]
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

* [chainctl starter](/chainguard/chainctl/chainctl-docs/chainctl_starter/)	 - Manage catalog starter organizations

