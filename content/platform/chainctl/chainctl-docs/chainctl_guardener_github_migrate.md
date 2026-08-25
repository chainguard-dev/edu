---
date: 2026-08-24T17:35:47Z
title: "chainctl guardener github migrate"
slug: chainctl_guardener_github_migrate
url: /platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener github migrate

Migrate a repository's GitHub Actions to their Chainguard equivalents.

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

* [chainctl guardener github](/platform/chainctl/chainctl-docs/chainctl_guardener_github/)	 - Link and unlink a GitHub organization to a Chainguard group.
* [chainctl guardener github migrate create](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_create/)	 - Enqueue a GitHub Actions migration for a repository.
* [chainctl guardener github migrate get](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_get/)	 - Show the state of a migration operation.

