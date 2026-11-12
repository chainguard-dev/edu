---
date: 2026-11-11T10:22:55Z
title: "chainctl iam identity-providers scim manual-bindings remove"
slug: chainctl_iam_identity-providers_scim_manual-bindings_remove
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_manual-bindings_remove/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim manual-bindings remove

Remove the manual role bindings that SCIM supersedes, after a reviewed plan.

### Synopsis

Remove the role bindings assigned directly that SCIM now supersedes. The command first asks the API for a plan: exactly the bindings that would be removed for the selected classes. It prints the plan and, only after you confirm (or pass --yes), removes exactly that set; if anything changed since the plan, nothing is removed and the command asks you to run it again. With --dry-run it prints the plan for the first batch and stops; later batches are planned only after this one is removed.

By default classes A and B are removed, which changes no one's access. Class C takes access away and is removed only with --include-uncovered (or --class C); confirming it names how many people lose access. Owner and support bindings and people with no current SCIM link are never touched, and the last owner assigned directly cannot be removed while SCIM is on. A large selection is handled in batches, each planned and confirmed in turn.

Each manual role binding held by a person SCIM provisions is sorted into one class.

A, duplicate: a SCIM-managed binding already grants the same role at the same scope. Removing it changes nothing.

B, covered: SCIM-managed bindings at the same scope or a parent scope already include every capability of the role. Removing it changes nothing in practice.

C, not covered: anything else. Removing it takes access away.

Never classified, and never removed: the owner and support roles, and people with no current SCIM link (including links made under a replaced correlation rule). They are listed only with --include-excluded.

```
chainctl iam identity-providers scim manual-bindings remove [IDENTITY_PROVIDER] [--class A,B] [--include-uncovered] [--dry-run] [--yes] [--output=json|table] [flags]
```

### Examples

```
  # Show what would be removed, changing nothing
  chainctl iam identity-providers scim manual-bindings remove my-idp --dry-run
  
  # Review the plan and remove duplicates and covered bindings
  chainctl iam identity-providers scim manual-bindings remove my-idp
  
  # Remove without prompting, for a script that has reviewed the --dry-run output
  chainctl iam identity-providers scim manual-bindings remove my-idp --yes
  
  # Also remove the bindings SCIM does not cover, taking that access away
  chainctl iam identity-providers scim manual-bindings remove my-idp --include-uncovered
```

### Options

```
      --class strings       Classes to remove: A, B, C (or duplicate, covered, not-covered). Default: A,B.
      --dry-run             Print the plan for the first batch without removing anything.
      --include-uncovered   Also remove class C, the bindings SCIM does not cover (not covered). This takes access away.
  -y, --yes                 Skip confirmation prompts.
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

