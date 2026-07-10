---
date: 2026-07-01T03:32:22Z
title: "chainctl actions catalog list"
slug: chainctl_actions_catalog_list
url: /platform/chainctl/chainctl-docs/chainctl_actions_catalog_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl actions catalog list

List Chainguard Actions in the public catalog.

```
chainctl actions catalog list [--upstream-owner=OWNER [--upstream-repo=REPO]] [--output=json|table] [flags]
```

### Options

```
      --page-size int32         Maximum number of actions to fetch per page (0 uses the server default).
      --upstream-owner string   Filter to actions mirroring this upstream owner (e.g. "actions").
      --upstream-repo string    Filter to actions mirroring this upstream repo (requires --upstream-owner).
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

* [chainctl actions catalog](/platform/chainctl/chainctl-docs/chainctl_actions_catalog/)	 - Browse the public Chainguard Actions catalog.

