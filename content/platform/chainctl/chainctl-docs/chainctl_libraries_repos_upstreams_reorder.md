---
date: 2026-11-27T13:55:02Z
title: "chainctl libraries repos upstreams reorder"
slug: chainctl_libraries_repos_upstreams_reorder
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams_reorder/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos upstreams reorder

Set the order of the upstream registries of a Libraries repository.

### Synopsis

Set the order in which a repository tries its upstream registries for an
ecosystem. List every upstream registry in the ecosystem's list once, first
tried first.

Only JavaScript and Java repository URLs are served now, so only the
JavaScript and Java lists affect requests.

```
chainctl libraries repos upstreams reorder NAME... --parent ORG/REPO --ecosystem ECOSYSTEM [--output=json|table] [flags]
```

### Examples

```
  # Set the order of the JavaScript upstream registries of the repository prod.
  # JavaScript has one upstream registry, npmjs, so this keeps its order.
  chainctl libraries repos upstreams reorder npmjs --parent=example.com/prod --ecosystem=javascript
```

### Options

```
      --ecosystem string   The ecosystem of the upstream list (dotnet, go, java, javascript, python).
      --parent string      The repository, as ORG/REPO: the name or UIDP of the organization, then the repository name.
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

* [chainctl libraries repos upstreams](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams/)	 - Manage the upstream registries of a Libraries repository.

