---
date: 2026-06-16T22:17:50Z
title: "chainctl iam external-group-role-mappings create"
slug: chainctl_iam_external-group-role-mappings_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam external-group-role-mappings create

Create an IdP group-to-role mapping.

```
chainctl iam external-group-role-mappings create --external-group-id GROUP --role ROLE --scope SCOPE --idp IDP [flags]
```

### Examples

```
  # Map IdP group "Platform-SRE" to the owner role at the org root
  chainctl iam external-group-role-mappings create --external-group-id "Platform-SRE" --role owner --scope ORG_UIDP --idp IDP_UIDP
```

### Options

```
      --external-group-id string   IdP group identifier (the claim value from the IdP token)
      --idp string                 Identity provider UIDP that owns this mapping
      --role string                Role UIDP or name to grant
      --scope string               Group UIDP where the role applies (the organization root)
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

