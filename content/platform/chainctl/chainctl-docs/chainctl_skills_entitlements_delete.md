---
date: 2026-07-01T03:32:22Z
title: "chainctl skills entitlements delete"
slug: chainctl_skills_entitlements_delete
url: /platform/chainctl/chainctl-docs/chainctl_skills_entitlements_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills entitlements delete

Delete the skills entitlement from an organization.

### Synopsis

Delete the skills entitlement from an organization.

WARNING: This removes the skills folder and entitlement record for the org.
All skill repos under the org become inaccessible. There is no recovery path.

```
chainctl skills entitlements delete --parent=PARENT [flags]
```

### Options

```
      --parent string   The name or id of the org to delete the skills entitlement from.
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

* [chainctl skills entitlements](/chainguard/chainctl/chainctl-docs/chainctl_skills_entitlements/)	 - Manage skills entitlements for an organization.

