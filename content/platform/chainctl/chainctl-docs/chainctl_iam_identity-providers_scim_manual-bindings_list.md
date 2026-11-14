---
date: 2026-11-13T20:36:51Z
title: "chainctl iam identity-providers scim manual-bindings list"
slug: chainctl_iam_identity-providers_scim_manual-bindings_list
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_manual-bindings_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim manual-bindings list

List the manual role bindings that SCIM supersedes, by class.

### Synopsis

List the SCIM-provisioned people of an identity provider who hold role bindings assigned directly, with each binding's class and the SCIM role and group that supersede it. Nothing is changed. If the identity provider is omitted, the single identity provider in your organization is used, or you are prompted to choose.

Each manual role binding held by a person SCIM provisions is sorted into one class.

A, duplicate: a SCIM-managed binding already grants the same role at the same scope. Removing it changes nothing.

B, covered: SCIM-managed bindings at the same scope or a parent scope already include every capability of the role. Removing it changes nothing in practice.

C, not covered: anything else. Removing it takes access away.

Never classified, and never removed: the owner and support roles, and people with no current SCIM link (including links made under a replaced correlation rule). They are listed only with --include-excluded.

```
chainctl iam identity-providers scim manual-bindings list [IDENTITY_PROVIDER] [--output=json|table] [flags]
```

### Examples

```
  # List every manual binding SCIM supersedes
  chainctl iam identity-providers scim manual-bindings list my-idp
  
  # Show only the bindings whose removal would take access away
  chainctl iam identity-providers scim manual-bindings list my-idp --class C
  
  # Include the bindings that are never removed, and why
  chainctl iam identity-providers scim manual-bindings list my-idp --include-excluded
  
  # Show only the owner and support bindings
  chainctl iam identity-providers scim manual-bindings list my-idp --exclusion privileged
```

### Options

```
      --class strings       Only bindings of these classes: A, B, C (or duplicate, covered, not-covered). Default: all.
      --exclusion strings   Only excluded bindings with these reasons: privileged, no-scim-link. Implies --include-excluded.
      --include-excluded    Also list the bindings that are never classified or removed, with the reason.
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

* [chainctl iam identity-providers scim manual-bindings](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_manual-bindings/)	 - Find and remove manual role bindings that SCIM now supersedes.

