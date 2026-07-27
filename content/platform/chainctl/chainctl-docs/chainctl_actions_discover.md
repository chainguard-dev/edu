---
date: 2026-07-23T16:28:17Z
title: "chainctl actions discover"
slug: chainctl_actions_discover
url: /platform/chainctl/chainctl-docs/chainctl_actions_discover/
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

Walks the target's workflows and composite-action definitions and lists every
action and container image they reference.

TARGET may be:
  - a local directory (default: current directory) — scans .github/workflows/
    and action.{yml,yaml}
  - a repo "owner/repo" — scans the repo's workflows and action.{yml,yaml}
  - a single action ref "owner/repo[/subpath]@version"

By default only the directly-referenced actions are listed. Pass --recursive to
follow each referenced action into its own definition on GitHub and resolve the
full transitive dependency graph.

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
      --recursive          Recurse into referenced actions' definitions on GitHub to resolve transitive dependencies
      --skip-catalog       Skip matching discovered actions against the Chainguard Actions catalog
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

* [chainctl actions](/platform/chainctl/chainctl-docs/chainctl_actions/)	 - Interact with the Chainguard Actions product.

