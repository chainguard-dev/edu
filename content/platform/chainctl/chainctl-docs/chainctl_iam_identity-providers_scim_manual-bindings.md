---
date: 2026-11-12T21:48:09Z
title: "chainctl iam identity-providers scim manual-bindings"
slug: chainctl_iam_identity-providers_scim_manual-bindings
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_manual-bindings/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim manual-bindings

Find and remove manual role bindings that SCIM now supersedes.

### Synopsis

After an organization moves to SCIM, the role bindings assigned directly before the move stay in place beside the ones SCIM grants, so a person's access is the union of both. These commands show which manual bindings SCIM has made redundant and remove them in bulk, always from a plan you have reviewed.

Each manual role binding held by a person SCIM provisions is sorted into one class.

A, duplicate: a SCIM-managed binding already grants the same role at the same scope. Removing it changes nothing.

B, covered: SCIM-managed bindings at the same scope or a parent scope already include every capability of the role. Removing it changes nothing in practice.

C, not covered: anything else. Removing it takes access away.

Never classified, and never removed: the owner and support roles, and people with no current SCIM link (including links made under a replaced correlation rule). They are listed only with --include-excluded.

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

* [chainctl iam identity-providers scim](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim/)	 - Manage SCIM provisioning for an identity provider.
* [chainctl iam identity-providers scim manual-bindings list](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_manual-bindings_list/)	 - List the manual role bindings that SCIM supersedes, by class.
* [chainctl iam identity-providers scim manual-bindings remove](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_manual-bindings_remove/)	 - Remove the manual role bindings that SCIM supersedes, after a reviewed plan.

