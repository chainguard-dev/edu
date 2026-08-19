---
date: 2026-08-18T17:09:18Z
title: "chainctl libraries cache status"
slug: chainctl_libraries_cache_status
url: /platform/chainctl/chainctl-docs/chainctl_libraries_cache_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries cache status

Show resolution cache status.

### Synopsis

Show the org's per-ecosystem resolution cache state: the current zap
generation, how many zaps have run, opt-out state, and the most recent zap
time. Ecosystems that have never been zapped or opted out are in the default
state and are not listed.

```
chainctl libraries cache status [--parent ORG] [--output=json|table] [flags]
```

### Options

```
      --parent string   The name or id of the organization to report on. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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

* [chainctl libraries cache](/platform/chainctl/chainctl-docs/chainctl_libraries_cache/)	 - Manage the Libraries resolution cache.

