---
date: 2026-11-05T20:53:08Z
title: "chainctl iam identity-providers reset-correlation-rule"
slug: chainctl_iam_identity-providers_reset-correlation-rule
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_reset-correlation-rule/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers reset-correlation-rule

Change an identity provider's correlation rule, unlinking its SCIM-provisioned users.

### Synopsis

Change how an identity provider's OIDC sign-ins are matched to the users it provisions through SCIM. Every SCIM-provisioned user of the identity provider is unlinked from their Chainguard identity and loses the roles SCIM granted them. Each user links again, and gets those roles back, at their next sign-in that matches under the new rule. Deactivated users stay deactivated, and role bindings not managed by SCIM are untouched. A rule change also retires the organization's SSO-only validation of the identity provider, so it must be validated again before SSO-only can be turned on.

Running it with the rule the identity provider already has changes nothing and finishes an unlink an earlier reset left incomplete.

```
chainctl iam identity-providers reset-correlation-rule IDENTITY_PROVIDER --oidc-correlation-rule=RULE [--yes] [--output=json] [flags]
```

### Options

```
      --oidc-correlation-rule string   The new correlation rule: sub_equals_external_id (stock Okta) or oid_equals_external_id (Microsoft Entra ID; requires the profile scope).
  -y, --yes                            Skip confirmation prompt
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

* [chainctl iam identity-providers](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

