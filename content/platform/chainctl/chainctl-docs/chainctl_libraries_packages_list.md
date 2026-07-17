---
date: 2026-07-01T03:32:22Z
title: "chainctl libraries packages list"
slug: chainctl_libraries_packages_list
url: /platform/chainctl/chainctl-docs/chainctl_libraries_packages_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries packages list

List Libraries packages.

### Synopsis

List packages in the Chainguard Libraries catalog for an ecosystem, optionally filtered by a search query.

```
chainctl libraries packages list --ecosystem ECOSYSTEM [--query QUERY] [--output=json|table] [flags]
```

### Options

```
      --ecosystem string   The ecosystem to list packages for (JAVA, PYTHON, JAVASCRIPT).
      --limit int32        The maximum number of packages to return; results are paginated automatically up to this limit. (default 50)
      --query string       A search string to filter packages by name. If empty, all packages in the ecosystem are returned.
      --remediated         Only return remediated packages.
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

* [chainctl libraries packages](/chainguard/chainctl/chainctl-docs/chainctl_libraries_packages/)	 - Inspect Libraries packages.

