---
date: 2026-07-22T19:49:10Z
title: "chainctl guardener github unlink"
slug: chainctl_guardener_github_unlink
url: /platform/chainctl/chainctl-docs/chainctl_guardener_github_unlink/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener github unlink

Unlink a GitHub organization from its Chainguard group.

### Synopsis

Unlink a GitHub organization from its Chainguard group.

If --group is set, this first tries your Chainguard credentials: if you hold
guardener.association.manage on the group, the org is unlinked with no browser
involved. Otherwise (or if those credentials are insufficient) it falls back to
the GitHub authorization flow, which proves you own the organization. Either way
you must be logged in to Chainguard; the GitHub flow just needs no access to the
group.

```
chainctl guardener github unlink [flags]
```

### Options

```
      --github-org string   GitHub account login to unlink (an organization, or your own user).
      --group string        Name or UIDP of the Chainguard group; enables unlinking with your Chainguard credentials (no browser).
      --port int            Local loopback port for the GitHub OAuth callback. (default 8989)
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

* [chainctl guardener github](/platform/chainctl/chainctl-docs/chainctl_guardener_github/)	 - Link and unlink a GitHub organization to a Chainguard group.

