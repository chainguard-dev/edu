---
date: 2026-11-23T15:46:28Z
title: "chainctl libraries repos create"
slug: chainctl_libraries_repos_create
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos create

Create a Libraries repository.

### Synopsis

Create a repository in an organization and print its URL for each ecosystem
the organization is entitled to. The repository starts with the upstream
registries Chainguard provides for each ecosystem.

The name cannot be the name of a folder that already exists in the
organization. Starter plans cannot create a repository, Team plans can create
one, and Enterprise plans can create as many as you need.

```
chainctl libraries repos create NAME --parent ORG [--output=id|json|table] [flags]
```

### Examples

```
  # Create the repository prod in example.com
  chainctl libraries repos create prod --parent=example.com
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

