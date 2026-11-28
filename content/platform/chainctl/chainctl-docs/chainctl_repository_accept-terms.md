---
date: 2026-11-27T13:55:02Z
title: "chainctl repository accept-terms"
slug: chainctl_repository_accept-terms
url: /platform/chainctl/chainctl-docs/chainctl_repository_accept-terms/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl repository accept-terms

Accept the terms for uploading your own packages and container images.

### Synopsis

Accept the legal documents an organization must accept before it uploads its
own packages or container images:

  Secured Platform Terms: https://www.chainguard.dev/legal/secure-platform-terms

Any data collected is pursuant to Chainguard's Privacy Notice (https://www.chainguard.dev/legal/privacy-notice).

An organization owner runs this once per organization, and it covers everyone
who uploads for that organization. Re-running after acceptance is a no-op, and
so is running it for an organization that already accepted these documents
for another offering. --parent names the organization; without it, the
default.group config value is used, or you pick one.

Where an interactive terminal isn't available, pass --yes. By using --yes you
accept the documents above on the organization's behalf.

```
chainctl repository accept-terms [flags]
```

### Examples

```
  # Pick an organization and accept its terms
  chainctl repository accept-terms

  # Accept for a named organization without prompting
  chainctl repository accept-terms --parent acme.com --yes
```

### Options

```
      --parent string   The organization (name or ID) to accept the terms for. Defaults to the default.group config value.
      --yes             Accept the terms non-interactively. By using this flag you accept the documents this command's help lists, which it also prints.
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

* [chainctl repository](/platform/chainctl/chainctl-docs/chainctl_repository/)	 - Commands for uploading your organization's own packages and container images.

