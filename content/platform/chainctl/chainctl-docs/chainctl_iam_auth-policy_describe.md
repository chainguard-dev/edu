---
date: 2026-10-26T19:49:34Z
title: "chainctl iam auth-policy describe"
slug: chainctl_iam_auth-policy_describe
url: /platform/chainctl/chainctl-docs/chainctl_iam_auth-policy_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam auth-policy describe

Describe an organization's authentication policy.

### Synopsis

Describe an organization's authentication policy.

The SSO Only column reports one of:
  true   only the organization's own identity provider can sign members in.
  false  every sign-in method is allowed.
  unset  the organization has never configured a policy. Sign-in is
         unrestricted, as with false, but nothing has been chosen yet.

In JSON output the same states are {"sso_only":true}, {"sso_only":false}, and
the sso_only key omitted entirely, so a scripted check should treat a missing
key as unset rather than as off (with jq, ".sso_only // false" is the
effective value).

```
chainctl iam auth-policy describe --parent ORGANIZATION_NAME | ORGANIZATION_ID [--output=json|table]
```

### Examples

```
  # Show whether my-org requires its identity provider for every sign-in
  chainctl iam auth-policy describe --parent my-org
  
  # Emit JSON for scripting
  chainctl iam auth-policy describe --parent my-org -o json
```

### Options

```
      --parent string   The organization (name or UIDP) whose authentication policy to show. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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

* [chainctl iam auth-policy](/platform/chainctl/chainctl-docs/chainctl_iam_auth-policy/)	 - Manage an organization's authentication policy (which sign-in methods its members may use).

