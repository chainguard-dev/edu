---
date: 2026-11-24T18:17:18Z
title: "chainctl libraries repos delete"
slug: chainctl_libraries_repos_delete
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos delete

Delete a Libraries repository.

### Synopsis

Delete a repository from an organization. Its URLs stop serving packages.

Delete refuses while the repository still has pull tokens, Libraries policy
bindings or Libraries policies, and names them. Pass --force to delete those,
and the pull tokens' role bindings, with the repository. Delete always refuses
while the repository has image repositories, folders, identities that are not
pull tokens or their role bindings, or identity providers, or while a binding
outside the repository uses one of its Libraries policies; delete those first.

```
chainctl libraries repos delete NAME --parent ORG [--force] [--yes] [flags]
```

### Examples

```
  # Delete the repository dev from example.com
  chainctl libraries repos delete dev --parent=example.com
  
  # Delete it with its pull tokens, without asking to confirm
  chainctl libraries repos delete dev --parent=example.com --force --yes
```

### Options

```
      --force           Also delete the repository's pull tokens, role bindings, Libraries policy bindings and Libraries policies.
      --parent string   Name or UIDP of the organization.
  -y, --yes             Delete without asking to confirm.
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

