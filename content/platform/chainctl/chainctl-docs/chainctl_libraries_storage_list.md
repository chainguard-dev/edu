---
date: 2026-10-06T09:26:34Z
title: "chainctl libraries storage list"
slug: chainctl_libraries_storage_list
url: /platform/chainctl/chainctl-docs/chainctl_libraries_storage_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries storage list

List storage usage per ecosystem.

```
chainctl libraries storage list [--ecosystem ECOSYSTEM] [--parent ORG] [--output=json|table] [flags]
```

### Options

```
      --ecosystem string   Only list storage usage for this ecosystem (GO). Omit for every ecosystem that reports usage.
      --parent string      The name or id of the organization whose storage usage to list.
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

* [chainctl libraries storage](/platform/chainctl/chainctl-docs/chainctl_libraries_storage/)	 - Show the storage your organization's uploads use in Libraries.

