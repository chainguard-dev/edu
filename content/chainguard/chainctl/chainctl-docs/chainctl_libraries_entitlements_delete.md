---
date: 2026-04-13T16:24:49Z
title: "chainctl libraries entitlements delete"
slug: chainctl_libraries_entitlements_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries entitlements delete

Delete an ecosystem library entitlement from an organization.

```
chainctl libraries entitlements delete --parent=PARENT --ecosystem=LANGUAGE [flags]
```

### Options

```
      --ecosystem string   The language ecosystem to remove the entitlement for.
      --parent string      The name or id of the org to delete an entitlement from.
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

* [chainctl libraries entitlements](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements/)	 - Manage entitlements to language ecosystem libraries.

