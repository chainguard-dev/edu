---
date: 2026-10-09T15:36:02Z
title: "chainctl guardener github migrate list"
slug: chainctl_guardener_github_migrate_list
url: /platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener github migrate list

List a group's migration operations.

### Synopsis

List a group's migration operations, newest first.

Each migration started with "migrate create", from the console, or by the
scheduled resync is listed once. Pass its OPERATION to "migrate get" to see
each feature's pull request. Use --repo to list one repository's migrations.

Listing requires guardener.actions.migrate or guardener.images.migrate on the
group. Operations for a feature you lack the permission for are left out.

```
chainctl guardener github migrate list [flags]
```

### Options

```
      --limit int       The most migrations to list. (default 20)
  -o, --output string   Output format: table or json. (default "table")
      --parent string   Name or UIDP of the Chainguard group whose migrations to list. Prompts interactively if omitted.
      --repo string     Only list migrations of this repository (a github.com URL or "owner/repo").
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
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl guardener github migrate](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate/)	 - Migrate the Actions and images enabled by a repository's configuration.

