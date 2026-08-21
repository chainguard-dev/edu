---
date: 2026-08-20T20:16:23Z
title: "chainctl guardener github migrate create"
slug: chainctl_guardener_github_migrate_create
url: /platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener github migrate create

Enqueue a GitHub Actions migration for a repository.

### Synopsis

Enqueue a GitHub Actions migration for a repository.

The migration opens (or updates) a single pull request replacing upstream GitHub
Actions with their Chainguard equivalents at version-equivalent tags. It returns
a long-running operation; by default this command waits for it to complete and
prints the resulting pull request. Pass --wait=false to return immediately with
the operation name, which you can pass to "migrate get" later.

REPOSITORY may be a full URL (https://github.com/owner/repo) or the "owner/repo"
shorthand; only github.com is supported today.

Requires the guardener.actions.migrate capability on the group, which must own
the repository's GitHub App installation.

```
chainctl guardener github migrate create REPOSITORY [flags]
```

### Options

```
      --parent string      Name or UIDP of the Chainguard group that owns the installation. Prompts interactively if omitted.
      --timeout duration   How long to wait for the migration when --wait is set. (default 10m0s)
      --wait               Wait for the migration operation to complete before returning. (default true)
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

* [chainctl guardener github migrate](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate/)	 - Migrate a repository's GitHub Actions to their Chainguard equivalents.

