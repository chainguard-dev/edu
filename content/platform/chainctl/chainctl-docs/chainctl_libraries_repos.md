---
date: 2026-11-18T15:28:55Z
title: "chainctl libraries repos"
slug: chainctl_libraries_repos
url: /platform/chainctl/chainctl-docs/chainctl_libraries_repos/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries repos

Manage Libraries repositories.

### Synopsis

A repository is a named endpoint for pulling libraries. Each repository has
its own URL for each ecosystem, in the form
https://libraries.cgr.dev/ECOSYSTEM/~/ORG/REPO/, and its own upstream
fallback setting. Your organization's existing URLs, such as
https://libraries.cgr.dev/javascript/, are its default repository, named
default. Creating, changing or deleting a named repository does not change
the default repository.

Repository URLs serve JavaScript packages. Repository URLs for other
ecosystems are listed as "(not serving yet)" and are not served.

Your plan sets how many repositories you can have: Starter has the default
repository only, Team has the default repository and one named repository,
and Enterprise has as many named repositories as you need.

Name the organization with --parent and the repository as the argument, for
example "chainctl libraries repos create prod --parent=example.com".

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

* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.
* [chainctl libraries repos create](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_create/)	 - Create a Libraries repository.
* [chainctl libraries repos delete](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_delete/)	 - Delete a Libraries repository.
* [chainctl libraries repos describe](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_describe/)	 - Describe a Libraries repository.
* [chainctl libraries repos list](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_list/)	 - List Libraries repositories.
* [chainctl libraries repos upstreams](/platform/chainctl/chainctl-docs/chainctl_libraries_repos_upstreams/)	 - Manage the upstream registries of a Libraries repository.

