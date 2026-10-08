---
date: 2026-10-07T14:01:35Z
title: "chainctl images overlays list"
slug: chainctl_images_overlays_list
url: /platform/chainctl/chainctl-docs/chainctl_images_overlays_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images overlays list

List Custom Assembly overlays and their bindings.

### Synopsis

List the Custom Assembly overlays under an organization or folder, with
each overlay's configuration and the repos and tags it is attached to.

Use --output json for the binding and overlay UIDs in machine-readable
form.

```
chainctl images overlays list [flags]
```

### Examples

```
  chainctl images overlays list --parent my-org

  # Print every binding UID
  chainctl images overlays list --parent my-org -o json | jq -r '.overlays[].bindings[].id'
```

### Options

```
  -o, --output string   Output format: text or json. (default "text")
      --parent string   Parent group name or UIDP to list overlays and bindings under. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images overlays](/platform/chainctl/chainctl-docs/chainctl_images_overlays/)	 - Manage Custom Assembly overlays and the repos they are attached to.

