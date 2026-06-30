---
date: 2026-06-30T00:00:55Z
title: "chainctl libraries artifacts count"
slug: chainctl_libraries_artifacts_count
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_artifacts_count/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries artifacts count

Count Libraries artifacts per ecosystem.

### Synopsis

Report the total number of artifacts available in the Chainguard Libraries catalog, optionally scoped to a single ecosystem.

```
chainctl libraries artifacts count [--output=json|table] [flags]
```

### Options

```
      --ecosystem string   The ecosystem to count artifacts for (JAVA, PYTHON, JAVASCRIPT).
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

* [chainctl libraries artifacts](/chainguard/chainctl/chainctl-docs/chainctl_libraries_artifacts/)	 - Inspect Libraries artifacts.

