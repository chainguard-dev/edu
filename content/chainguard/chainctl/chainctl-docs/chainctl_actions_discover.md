---
date: 2026-05-28T17:13:42Z
title: "chainctl actions discover"
slug: chainctl_actions_discover
url: /chainguard/chainctl/chainctl-docs/chainctl_actions_discover/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl actions discover

Discover GitHub Actions dependencies used by your workflows.

### Synopsis

Discover GitHub Actions dependencies.

Walks the target's workflows and composite-action definitions and resolves
every action and container image they (transitively) use.

TARGET may be:
  - a local directory (default: current directory) — scans .github/workflows/
    and action.{yml,yaml}
  - a repo "owner/repo" — scans the repo's workflows and action.{yml,yaml}
  - a single action ref "owner/repo[/subpath]@version"

Requires a GitHub token via $GITHUB_TOKEN or 'gh auth token'.

```
chainctl actions discover [TARGET] [flags]
```

### Examples

```
  chainctl actions discover
  chainctl actions discover .
  chainctl actions discover actions/checkout@v4
  chainctl actions discover chainguard-dev/mono
```

### Options

```
      --cache-dir string   Directory for caching GitHub API responses (default: $TMPDIR/chainctl-discover-cache)
      --clear-cache        Clear the cache directory before running
      --timeout duration   Maximum time to spend resolving dependencies (default 5m0s)
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

* [chainctl actions](/chainguard/chainctl/chainctl-docs/chainctl_actions/)	 - Interact with the Chainguard Actions product.

