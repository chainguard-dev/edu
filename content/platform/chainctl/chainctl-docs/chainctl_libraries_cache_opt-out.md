---
date: 2026-08-20T20:16:23Z
title: "chainctl libraries cache opt-out"
slug: chainctl_libraries_cache_opt-out
url: /platform/chainctl/chainctl-docs/chainctl_libraries_cache_opt-out/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries cache opt-out

Opt the org out of the resolution cache.

### Synopsis

Opt the org out of the resolution cache: it stops recording resolutions and
recorded ones stop being enforced, so every fetch resolves to the current
best tier. Recorded entries are retained; opting back in resumes from them.

```
chainctl libraries cache opt-out [--ecosystem ECOSYSTEM] [--parent ORG] [flags]
```

### Options

```
      --ecosystem string   Change one ecosystem (JAVA, PYTHON, JAVASCRIPT). Omit for all ecosystems.
      --parent string      The name or id of the organization whose opt-out to change.
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

