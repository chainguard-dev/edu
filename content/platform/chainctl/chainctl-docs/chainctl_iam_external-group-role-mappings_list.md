---
date: 2026-08-27T20:49:25Z
title: "chainctl iam external-group-role-mappings list"
slug: chainctl_iam_external-group-role-mappings_list
url: /platform/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam external-group-role-mappings list

List IdP group-to-role mappings.

```
chainctl iam external-group-role-mappings list --parent PARENT [--idp IDP] [flags]
```

### Examples

```
  # List all group mappings in an organization
  chainctl iam external-group-role-mappings list --parent my-org

  # List mappings for a specific identity provider
  chainctl iam external-group-role-mappings list --parent my-org --idp my-idp
```

### Options

```
      --idp string      Narrow results to a specific identity provider (name or UIDP)
      --parent string   Organization or folder (name or UIDP) to list mappings under
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

* [chainctl iam external-group-role-mappings](/platform/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings/)	 - Manage IdP group-to-role mappings (also available under 'iam identity-providers group-mappings').

