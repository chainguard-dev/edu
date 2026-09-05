---
date: 2026-09-04T19:05:48Z
title: "chainctl guardener scans get"
slug: chainctl_guardener_scans_get
url: /platform/chainctl/chainctl-docs/chainctl_guardener_scans_get/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener scans get

Show one dependency scan.

### Synopsis

Show one dependency scan by the ID a "scans list" summary carried: every
declared artifact (its package URL and the files that declared it) and the
relationships between artifacts.

Requires the guardener.scan.get capability on the group that owns the scan.

```
chainctl guardener scans get SCAN_ID [flags]
```

### Options

```
  -o, --output string   Output format: table or json. (default "table")
      --parent string   Name or UIDP of the Chainguard group that owns the scan. Prompts interactively if omitted.
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
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl guardener scans](/platform/chainctl/chainctl-docs/chainctl_guardener_scans/)	 - View guardener dependency scans.

