---
date: 2026-09-03T18:18:22Z
title: "chainctl libraries cache zap"
slug: chainctl_libraries_cache_zap
url: /platform/chainctl/chainctl-docs/chainctl_libraries_cache_zap/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries cache zap

Zap resolution cache entries.

### Synopsis

Retire resolution cache entries at the chosen scope: a Maven group or npm
scope prefix, a single package or version, one ecosystem, or the whole org.
Zapped coordinates re-resolve to the current best tier on their next fetch,
which changes artifact hashes for them — regenerate lockfiles afterwards.
Use --dry-run first to see how many entries a zap would retire. Real zaps
prompt for confirmation; pass --yes to skip the prompt in scripts.

```
chainctl libraries cache zap [--ecosystem ECOSYSTEM] [--group G | --scope S | --package P [--version V]] [--registry R] [--dry-run] [--yes] [--parent ORG] [flags]
```

### Options

```
      --dry-run            Report how many entries the zap would retire without changing anything.
      --ecosystem string   Scope the zap to one ecosystem (JAVA, PYTHON, JAVASCRIPT). Omit for an org-wide zap.
      --group string       Zap a Maven group prefix (e.g. com.fasterxml.jackson). Requires --ecosystem.
      --package string     Zap a single package (java: group:artifact). Requires --ecosystem.
      --parent string      The name or id of the organization whose resolution cache to zap.
      --registry string    Narrow a package or prefix zap to one registry.
      --scope string       Zap an npm scope prefix (e.g. @angular). Requires --ecosystem.
      --version string     Zap a single version. Requires --package.
  -y, --yes                Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

