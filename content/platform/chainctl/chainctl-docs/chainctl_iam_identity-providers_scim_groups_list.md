---
date: 2026-10-22T17:36:19Z
title: "chainctl iam identity-providers scim groups list"
slug: chainctl_iam_identity-providers_scim_groups_list
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_groups_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim groups list

List the SCIM-provisioned groups of an identity provider.

### Synopsis

List the groups a SCIM connector has pushed for an identity provider, with each group's member count. The External Id is the value an external group role mapping matches on. If the identity provider is omitted, the single identity provider in your organization is used, or you are prompted to choose.

```
chainctl iam identity-providers scim groups list [IDENTITY_PROVIDER] [--output=json|table] [flags]
```

### Examples

```
  # List SCIM groups for your organization's identity provider
  chainctl iam identity-providers scim groups list
  
  # List for a specific identity provider
  chainctl iam identity-providers scim groups list my-idp
  
  # Find a group by its display name
  chainctl iam identity-providers scim groups list --display-name=Engineering
```

### Options

```
      --display-name string   Filter by display name (case-insensitive).
      --external-id string    Filter by external id (case-sensitive). This is the value a role mapping uses.
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

* [chainctl iam identity-providers scim groups](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_groups/)	 - Inspect the SCIM-provisioned groups of an identity provider.

