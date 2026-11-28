---
date: 2026-11-27T13:55:02Z
title: "chainctl iam identities describe"
slug: chainctl_iam_identities_describe
url: /platform/chainctl/chainctl-docs/chainctl_iam_identities_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities describe

View the details of an identity.

### Synopsis

View the details of an identity: where it lives, the roles it holds, and
what it trusts.

For an identity assumed from CI, the output shows the token claims it
accepts (issuer, subject, audience, and any extra claims) as exact values
or patterns. Compare them with the claims in the failing job's OIDC token.
"Last seen at" is the last successful token exchange; 0001-01-01 means no
exchange has ever matched. An identity with no role bindings has no Roles
section.

Example output for a GitHub Actions identity:

```
Identity "github-ci"
Last seen at: 2026-11-12 18:04:11.512 +0000 UTC

ID: 0123.../abcd...
Location: my-org [0123...]

Roles:
  - my-org: registry.pull

Type: Claim match
  Issuer: https://token.actions.githubusercontent.com
  Subject Pattern: repo:my-org/my-repo:ref:refs/heads/main
```

```
chainctl iam identities describe {IDENTITY_NAME | IDENTITY_ID} [flags]
```

### Examples

```
  # Show what an identity trusts and which roles it holds
  chainctl iam identities describe github-ci
  
  # Emit JSON for scripting
  chainctl iam identities describe github-ci -o json
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

* [chainctl iam identities](/platform/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.

