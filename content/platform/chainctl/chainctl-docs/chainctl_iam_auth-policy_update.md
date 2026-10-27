---
date: 2026-10-26T19:49:34Z
title: "chainctl iam auth-policy update"
slug: chainctl_iam_auth-policy_update
url: /platform/chainctl/chainctl-docs/chainctl_iam_auth-policy_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam auth-policy update

Update an organization's authentication policy.

### Synopsis

Update an organization's authentication policy.

--sso-only=true makes the organization's own identity provider the only way
to sign in to it. Members who sign in any other way (a social login such as
Google or GitHub, for example) are shut out of the organization as soon as
the change is saved, so enabling it prints a warning and asks for
confirmation; pass --yes to skip the prompt. When the organization already
requires SSO, enabling it again changes nothing and asks nothing.
--sso-only=false lifts the restriction and asks nothing.

--sso-only must be given explicitly as true or false. An update that names
no control is refused rather than sent as a no-op.

```
chainctl iam auth-policy update --parent ORGANIZATION_NAME | ORGANIZATION_ID --sso-only={true|false} [--yes] [--output=json|table]
```

### Examples

```
  # Require my-org's identity provider for every sign-in (asks for confirmation)
  chainctl iam auth-policy update --parent my-org --sso-only=true
  
  # The same, non-interactively
  chainctl iam auth-policy update --parent my-org --sso-only=true --yes
  
  # Allow every sign-in method again
  chainctl iam auth-policy update --parent my-org --sso-only=false
```

### Options

```
      --parent string   The organization (name or UIDP) whose authentication policy to update. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sso-only        Whether the organization's own identity provider is the only way to sign in to it. Must be given explicitly as --sso-only=true or --sso-only=false.
  -y, --yes             Skip the confirmation prompt when enabling --sso-only.
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

