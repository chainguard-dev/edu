---
date: 2026-07-23T16:28:18Z
title: "chainctl policies override create"
slug: chainctl_policies_override_create
url: /platform/chainctl/chainctl-docs/chainctl_policies_override_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies override create

Create a policy override.

### Synopsis

Create an override that waives a policy for one specific image.

The override flips the policy's result to ALLOWED for the image
identified by --digest (a manifest digest), under the policy named by
--policy. A --reason is required to record why the waiver was granted.

Creating an override requires the policies.override.create capability,
a separate capability typically held by organization owners.

```
chainctl policies override create --policy POLICY --digest DIGEST --reason REASON [--parent ORG] [--output=json|table] [flags]
```

### Examples

```
  # Waive the no-eol policy for a specific image digest
  chainctl policies override create --policy=no-eol --parent=engineering \
  --digest=sha256:abc123... --reason="approved exception, ticket OPS-42"
```

### Options

```
      --digest string   The image manifest digest to waive (e.g. sha256:abc...).
      --parent string   The name or id of the organization to scope the override to.
      --policy string   The name or UIDP of the policy to override.
      --reason string   The justification for the override.
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

* [chainctl policies override](/platform/chainctl/chainctl-docs/chainctl_policies_override/)	 - Manage policy overrides.

