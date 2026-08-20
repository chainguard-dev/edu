---
date: 2026-08-19T18:15:14Z
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
identified by --digest — a sha256 digest written as sha256: followed by
exactly 64 lowercase hex characters — under the policy named by --policy.
A tag or a non-sha256 value is rejected locally before any API call. A
--reason is required to record why the waiver was granted.

An override matches exactly one manifest digest. For a multi-arch image,
pulls are enforced against the per-platform child manifest, not the index
digest, so override the child digest that "chainctl policies check"
reports as enforced; overriding the index digest alone may not unblock
the pull.

Creating an override requires the policies.override.create capability,
a separate capability typically held by organization owners.

```
chainctl policies override create --policy POLICY --digest DIGEST --reason REASON [--parent ORG] [--output=json|table] [flags]
```

### Examples

```
  # Waive the no-eol policy for a specific image digest
  chainctl policies override create --policy=no-eol --parent=engineering \
  --digest=sha256:<64-hex-digest> --reason="approved exception, ticket OPS-42"
```

### Options

```
      --digest string          The sha256 image digest to waive, as sha256: followed by exactly 64 lowercase hex characters (tags and other algorithms are rejected before any API call). For a multi-arch image use the per-platform child digest that "chainctl policies check" reports, not the index digest.
      --parent string          The name or id of the organization to scope the override to.
      --policy string          The name or UIDP of the policy to override.
      --reason string          The justification for the override.
      --resource-type string   Resource type used to disambiguate a policy referenced by name (shorthand: Repo, Python, Java, Javascript; or a full type). Ignored when the policy is given by UIDP.
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

