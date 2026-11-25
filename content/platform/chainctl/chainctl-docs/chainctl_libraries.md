---
date: 2026-11-24T18:17:18Z
title: "chainctl libraries"
slug: chainctl_libraries
url: /platform/chainctl/chainctl-docs/chainctl_libraries/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries

Ecosystem library related commands.

### Synopsis

Ecosystem library related commands.

Your organization pulls libraries from its default repository: one URL per
ecosystem, such as https://libraries.cgr.dev/javascript/. Creating named
repositories does not change those URLs. A named repository has its own URL
for each ecosystem and its own upstream fallback setting; see
"chainctl libraries repos --help".

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

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl libraries cache](/platform/chainctl/chainctl-docs/chainctl_libraries_cache/)	 - Manage the Libraries resolution cache.
* [chainctl libraries entitlements](/platform/chainctl/chainctl-docs/chainctl_libraries_entitlements/)	 - Manage entitlements to language ecosystem libraries.
* [chainctl libraries go](/platform/chainctl/chainctl-docs/chainctl_libraries_go/)	 - Go module registry commands.
* [chainctl libraries packages](/platform/chainctl/chainctl-docs/chainctl_libraries_packages/)	 - Inspect Libraries packages.
* [chainctl libraries policy](/platform/chainctl/chainctl-docs/chainctl_libraries_policy/)	 - Manage Libraries policies.
* [chainctl libraries remediate](/platform/chainctl/chainctl-docs/chainctl_libraries_remediate/)	 - Discover and apply Chainguard -cgr.N CVE remediations for a JavaScript project
* [chainctl libraries repos](/platform/chainctl/chainctl-docs/chainctl_libraries_repos/)	 - Manage Libraries repositories.
* [chainctl libraries storage](/platform/chainctl/chainctl-docs/chainctl_libraries_storage/)	 - Show and delete your organization's uploads in Libraries.
* [chainctl libraries update-hashes](/platform/chainctl/chainctl-docs/chainctl_libraries_update-hashes/)	 - Update lockfile integrity hashes with Chainguard Libraries checksums
* [chainctl libraries verify](/platform/chainctl/chainctl-docs/chainctl_libraries_verify/)	 - A tool to analyze the use of Chainguard Libraries in various artifacts

