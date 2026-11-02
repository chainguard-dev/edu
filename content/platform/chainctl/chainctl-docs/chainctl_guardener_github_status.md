---
date: 2026-10-30T14:11:50Z
title: "chainctl guardener github status"
slug: chainctl_guardener_github_status
url: /platform/chainctl/chainctl-docs/chainctl_guardener_github_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener github status

List the GitHub organizations linked to your Chainguard groups.

### Synopsis

List the GitHub organizations linked to your Chainguard groups.

By default every group you can see is checked and each group with a linked
GitHub organization is listed. Pass --parent to list only one group.

Which repositories guardener acts on is controlled by the guardener GitHub App's
repository selection on GitHub — follow the SETTINGS link in the output to review
or change it.

Requires the guardener.association.list capability on a group to list its
organizations (read-only; no GitHub authorization or browser flow is involved).
Groups you lack it on are left out.

```
chainctl guardener github status [flags]
```

### Options

```
      --parent string   Name or UIDP of the Chainguard group to list. Lists every group with a linked organization if omitted.
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

