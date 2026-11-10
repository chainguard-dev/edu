---
date: 2026-11-09T19:57:31Z
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

The Session Duration column is how long a sign-in to the organization lasts
before its members must sign in again, or "default" when the organization
has not chosen one and Chainguard's default applies. In JSON output it is
session_duration_seconds, omitted for the default. A length of 0s, which
only Chainguard sets, means members get no refresh tokens at all.

"chainctl iam auth-policy update --help" explains how the length applies.

```
chainctl iam auth-policy describe --parent ORGANIZATION_NAME | ORGANIZATION_ID [--output=json|table]
```

### Examples

```
  # Show how long a sign-in to my-org lasts
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

* [chainctl iam auth-policy](/platform/chainctl/chainctl-docs/chainctl_iam_auth-policy/)	 - Manage how long a sign-in to an organization lasts.

