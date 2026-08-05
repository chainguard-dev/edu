---
date: 2026-08-04T12:12:40Z
title: "chainctl libraries cache list"
slug: chainctl_libraries_cache_list
url: /platform/chainctl/chainctl-docs/chainctl_libraries_cache_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries cache list

List resolution cache entries.

### Synopsis

List the org's recorded resolutions: which tier each package version was
served from. Live entries govern serving; retired entries were superseded by
a zap and are kept until cleaned up.

```
chainctl libraries cache list [--ecosystem ECOSYSTEM] [--group G | --scope S | --package P] [--tier TIER] [--live] [--limit N] [--parent ORG] [--output=json|table] [flags]
```

### Options

```
      --ecosystem string   Only list entries for this ecosystem (JAVA, PYTHON, JAVASCRIPT).
      --group string       Only list entries under a Maven group prefix. Requires --ecosystem.
      --limit int32        Maximum number of entries to show. (default 100)
      --live               Only list live entries (the ones that govern serving).
      --package string     Only list entries for one package. Requires --ecosystem.
      --parent string      The name or id of the organization whose resolution cache to list.
      --registry string    Only list entries for one registry.
      --scope string       Only list entries under an npm scope prefix. Requires --ecosystem.
      --tier string        Only list entries recording this tier (CHAINGUARD or UPSTREAM).
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

