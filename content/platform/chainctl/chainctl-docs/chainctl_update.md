---
date: 2026-07-23T16:28:18Z
title: "chainctl update"
slug: chainctl_update
url: /platform/chainctl/chainctl-docs/chainctl_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl update

Update chainctl.

### Synopsis

Update chainctl to the latest release.

When signature verification is enabled (currently opt-in via
CHAINCTL_EXPERIMENTAL_UPDATE_VERIFY=true), the downloaded binary's signature is
verified before it is installed; a binary that fails verification is never
installed. Verification requires network access to the download host
(dl.enforce.dev) and, at least on first use, to the Sigstore TUF CDN
(tuf-repo-cdn.sigstore.dev). If those hosts are unreachable (for example,
behind a restrictive proxy), the update fails and the current binary is left in
place; as a fallback, download the latest release directly from
https://dl.enforce.dev/chainctl/latest/.

```
chainctl update [--yes] [--force]
```

### Options

```
      --force   Skip the version check and update chainctl regardless of the current version.
  -y, --yes     Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control

