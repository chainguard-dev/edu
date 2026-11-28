---
date: 2026-11-27T13:55:02Z
title: "chainctl libraries repos upstreams disable"
slug: chainctl_libraries_repos_upstreams_disable
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams_disable/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos upstreams disable

Disable an upstream registry of a Libraries repository.

### Synopsis

Disable an upstream registry in a repository's list for an ecosystem, so the
repository no longer tries it. Disabling the last enabled upstream registry
turns upstream fallback off for that ecosystem. The change takes effect within
about a minute.

```
chainctl libraries repos upstreams disable NAME --parent ORG/REPO --ecosystem ECOSYSTEM [flags]
```

### Examples

```
  # Disable npmjs for the repository prod in example.com
  chainctl libraries repos upstreams disable npmjs --parent=example.com/prod --ecosystem=javascript
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

