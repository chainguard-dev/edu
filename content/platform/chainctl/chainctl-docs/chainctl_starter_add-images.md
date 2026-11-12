---
date: 2026-11-11T10:22:55Z
title: "chainctl starter add-images"
slug: chainctl_starter_add-images
url: /platform/chainctl/chainctl-docs/chainctl_starter_add-images/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl starter add-images

Add catalog images to your Chainguard Starter organization.

### Synopsis

Add catalog images to your Chainguard Starter organization.

The target organization is the Starter, Team or customer org the
caller's identity is bound to — auto-discovered. An account bound to
more than one names it with --parent; otherwise its Starter org is used,
else its Team org, else its customer org.

Images are resolved against the catalog by exact name match. The server
picks the active starter entitlement that has remaining capacity. The
total cap across all starter images is enforced by the server.

```
chainctl starter add-images IMAGE_NAME [IMAGE_NAME ...] [flags]
```

### Options

```
      --parent string   The name, path or ID of the Starter, Team or customer organization, when your account is bound to more than one.
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

* [chainctl starter](/platform/chainctl/chainctl-docs/chainctl_starter/)	 - Manage Chainguard Starter organizations

