---
date: 2026-11-17T20:29:50Z
title: "chainctl libraries repos upstreams"
slug: chainctl_libraries_repos_upstreams
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos upstreams

Manage the upstream registries of a Libraries repository.

### Synopsis

A repository has a list of upstream registries for each ecosystem. When
Chainguard has not built a package, the repository tries its enabled upstream
registries in order. Upstream fallback is on only when the organization's
Libraries entitlement includes upstream packages and at least one upstream
registry in the list is enabled.

You can enable, disable and reorder the upstream registries Chainguard
provides; you cannot add your own. On the Starter plan you can disable an
upstream registry but not enable or reorder one. Only JavaScript repository
URLs are served now, so only the JavaScript list affects requests.

Name the repository with --parent ORG/REPO, for example
--parent=example.com/prod. The default repository has no upstream list: its
upstream fallback follows the organization's entitlement.

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

* [chainctl libraries repos](/platform/chainctl/chainctl-docs/chainctl_libraries_repos/)	 - Manage Libraries repositories.
* [chainctl libraries repos upstreams disable](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams_disable/)	 - Disable an upstream registry of a Libraries repository.
* [chainctl libraries repos upstreams enable](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams_enable/)	 - Enable an upstream registry of a Libraries repository.
* [chainctl libraries repos upstreams list](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams_list/)	 - List the upstream registries of a Libraries repository.
* [chainctl libraries repos upstreams reorder](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams_reorder/)	 - Set the order of the upstream registries of a Libraries repository.

