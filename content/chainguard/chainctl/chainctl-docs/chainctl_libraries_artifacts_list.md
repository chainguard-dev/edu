---
date: 2026-06-25T19:50:48Z
title: "chainctl libraries artifacts list"
slug: chainctl_libraries_artifacts_list
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_artifacts_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries artifacts list

List Libraries artifacts.

### Synopsis

List artifacts in the Chainguard Libraries catalog for an ecosystem, optionally filtered by a search query.

```
chainctl libraries artifacts list --ecosystem ECOSYSTEM [--query QUERY] [--output=json|table] [flags]
```

### Options

```
      --ecosystem string   The ecosystem to list artifacts for (JAVA, PYTHON, JAVASCRIPT).
      --limit int32        The maximum number of artifacts to return; results are paginated automatically up to this limit. (default 50)
      --query string       A search string to filter artifacts by name. If empty, all artifacts in the ecosystem are returned.
      --remediated         Only return remediated artifacts.
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

* [chainctl libraries artifacts](/chainguard/chainctl/chainctl-docs/chainctl_libraries_artifacts/)	 - Inspect Libraries artifacts.

