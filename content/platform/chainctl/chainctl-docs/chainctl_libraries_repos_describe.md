---
date: 2026-11-24T18:17:18Z
title: "chainctl libraries repos describe"
slug: chainctl_libraries_repos_describe
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos describe

Describe a Libraries repository.

### Synopsis

Show a repository's URL for each ecosystem and whether upstream fallback is on.

Upstream fallback is on only when the organization's Libraries entitlement
includes upstream packages and at least one of the repository's upstream
registries is enabled. Leave out NAME, or pass default, to describe the default
repository, whose upstream fallback follows the organization's entitlement.

A URL marked "(not serving yet)" belongs to an ecosystem whose repository URLs
are not served: requests to it are refused. Only JavaScript and Java
repository URLs are served.

```
chainctl libraries repos describe [NAME] --parent ORG [--output=id|json|table] [flags]
```

### Examples

```
  # Describe the repository prod in example.com
  chainctl libraries repos describe prod --parent=example.com
  
  # Describe the default repository of example.com
  chainctl libraries repos describe --parent=example.com
```

### Options

```
      --parent string   Name or UIDP of the organization.
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

* [chainctl libraries repos](/platform/chainctl/chainctl-docs/chainctl_libraries_repos/)	 - Manage Libraries repositories.

