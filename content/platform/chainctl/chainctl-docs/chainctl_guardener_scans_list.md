---
date: 2026-09-03T18:18:22Z
title: "chainctl guardener scans list"
slug: chainctl_guardener_scans_list
url: /platform/chainctl/chainctl-docs/chainctl_guardener_scans_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener scans list

List a group's dependency scans.

### Synopsis

List summaries of a group's dependency scans.

Guardener continuously scans the repositories of the group's linked GitHub
installations. The listing shows one summary per repository — its most recent
scan — newest first. Resolve a summary's ID to the full scan with "scans get".

Requires the guardener.scan.list capability on the group.

```
chainctl guardener scans list [flags]
```

### Options

```
  -o, --output string   Output format: table or json. (default "table")
      --parent string   Name or UIDP of the Chainguard group whose scans to list. Prompts interactively if omitted.
      --repo string     Only list scans of this repository (a github.com URL or "owner/repo").
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

