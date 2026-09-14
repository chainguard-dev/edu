---
date: 2026-09-11T15:58:59Z
title: "chainctl iam identity-providers scim users list"
slug: chainctl_iam_identity-providers_scim_users_list
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_users_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim users list

List the SCIM-provisioned users of an identity provider.

### Synopsis

List the users a SCIM connector has provisioned for an identity provider, including users provisioned but not yet logged in — their linked identity is empty until first login. If the identity provider is omitted, the single identity provider in your organization is used, or you are prompted to choose.

```
chainctl iam identity-providers scim users list [IDENTITY_PROVIDER] [--output=json|table] [flags]
```

### Examples

```
  # List SCIM users for your organization's identity provider
  chainctl iam identity-providers scim users list
  
  # List for a specific identity provider, showing only active users
  chainctl iam identity-providers scim users list my-idp --active
  
  # Find a provisioned user by their SCIM userName
  chainctl iam identity-providers scim users list --user-name=alice@example.com
```

### Options

```
      --active               Show only active users.
      --external-id string   Filter by exact IdP-assigned externalId.
      --inactive             Show only inactive (deprovisioned) users.
      --user-name string     Filter by exact SCIM userName (case-insensitive).
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

* [chainctl iam identity-providers scim users](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_users/)	 - Inspect the SCIM-provisioned users of an identity provider.

