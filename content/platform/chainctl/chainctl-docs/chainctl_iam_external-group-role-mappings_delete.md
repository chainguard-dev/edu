---
date: 2026-07-01T03:32:22Z
title: "chainctl iam external-group-role-mappings delete"
slug: chainctl_iam_external-group-role-mappings_delete
url: /platform/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam external-group-role-mappings delete

Delete IdP group-to-role mappings.

```
chainctl iam external-group-role-mappings delete {MAPPING_ID | --all --idp IDP} [--yes] [flags]
```

### Examples

```
  # Delete a single group mapping by ID
  chainctl iam external-group-role-mappings delete MAPPING_UIDP

  # Delete all group mappings for an identity provider
  chainctl iam external-group-role-mappings delete --all --idp IDP_UIDP
```

### Options

```
      --all          Delete all mappings for the identity provider given by --idp
      --idp string   Identity provider UIDP whose mappings to delete (with --all)
  -y, --yes          Skip confirmation prompt
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

* [chainctl iam external-group-role-mappings](/chainguard/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings/)	 - Manage IdP group-to-role mappings.

