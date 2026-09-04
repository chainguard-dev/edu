---
date: 2026-09-03T18:18:22Z
title: "chainctl guardener scans"
slug: chainctl_guardener_scans
url: /platform/chainctl/chainctl-docs/chainctl_guardener_scans/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener scans

View guardener dependency scans.

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

* [chainctl guardener](/platform/chainctl/chainctl-docs/chainctl_guardener/)	 - Manage guardener integrations.
* [chainctl guardener scans get](/platform/chainctl/chainctl-docs/chainctl_guardener_scans_get/)	 - Show one dependency scan.
* [chainctl guardener scans list](/platform/chainctl/chainctl-docs/chainctl_guardener_scans_list/)	 - List a group's dependency scans.

