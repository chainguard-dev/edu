---
date: 2026-11-24T18:17:18Z
title: "chainctl libraries packages blocked"
slug: chainctl_libraries_packages_blocked
url: /platform/chainctl/chainctl-docs/chainctl_libraries_packages_blocked/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries packages blocked

List blocked Libraries packages.

### Synopsis

List packages that were withheld by an active Libraries policy, and the repository that withheld each. Defaults to ENFORCE-mode events from the last 30 days.

COUNT is every time the version was withheld. REQUESTED is how many of those were a client asking for the version by name and being refused; the rest were versions left out of a listing. Rows recorded before the serve layer began stamping the request site show 0.

```
chainctl libraries packages blocked [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--ecosystem ECOSYSTEM] [--package NAME] [--mode ENFORCE|PREVIEW] [--requested-only] [--limit N] [--output=json|table] [flags]
```

### Options

```
      --ecosystem string   Only show events for this ecosystem (DOTNET, GO, JAVA, JAVASCRIPT, PYTHON).
      --limit int32        The number of blocked packages per page in an interactive terminal; otherwise the maximum number to return. (default 50)
      --mode string        Only show events in this mode (ENFORCE or PREVIEW). Defaults to ENFORCE.
      --package string     Only show events whose full package name matches, as shown in the PACKAGE column (exact, case-insensitive; e.g. @nx/web, or group/artifact for java).
      --parent string      The name or id of the organization to scope events to, or <org>/<repository> for one repository.
      --requested-only     Only show versions a client asked for by name and was refused, not versions that were only left out of a listing.
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

* [chainctl libraries packages](/platform/chainctl/chainctl-docs/chainctl_libraries_packages/)	 - Inspect Libraries packages.

