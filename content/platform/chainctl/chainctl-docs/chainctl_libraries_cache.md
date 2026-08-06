---
date: 2026-08-05T11:11:55Z
title: "chainctl libraries cache"
slug: chainctl_libraries_cache
url: /platform/chainctl/chainctl-docs/chainctl_libraries_cache/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries cache

Manage the Libraries resolution cache.

### Synopsis

Manage your organization's Libraries resolution cache. Once your org is
served a package version from a tier (Chainguard-built or upstream), that
resolution is recorded and held stable so lockfile hashes keep verifying.
Zapping retires recorded resolutions so the next fetch re-resolves to the
current best tier; clients that hold lockfiles must regenerate them to pick
up new hashes.

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

* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.
* [chainctl libraries cache list](/platform/chainctl/chainctl-docs/chainctl_libraries_cache_list/)	 - List resolution cache entries.
* [chainctl libraries cache opt-in](/platform/chainctl/chainctl-docs/chainctl_libraries_cache_opt-in/)	 - Opt the org back into the resolution cache.
* [chainctl libraries cache opt-out](/platform/chainctl/chainctl-docs/chainctl_libraries_cache_opt-out/)	 - Opt the org out of the resolution cache.
* [chainctl libraries cache status](/platform/chainctl/chainctl-docs/chainctl_libraries_cache_status/)	 - Show resolution cache status.
* [chainctl libraries cache zap](/platform/chainctl/chainctl-docs/chainctl_libraries_cache_zap/)	 - Zap resolution cache entries.

