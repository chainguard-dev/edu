---
date: 2026-09-22T16:17:57Z
title: "chainctl iam identity-providers describe"
slug: chainctl_iam_identity-providers_describe
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers describe

Describe an identity provider.

### Synopsis

Describe an identity provider, including its OIDC configuration and SCIM provisioning status.

The SCIM row reports one of:
  enabled       SCIM provisioning is on.
  disabled      SCIM provisioning is off.
  not reported  the API surface did not return SCIM status (for example, a
                v1-negotiated organization). This is not the same as disabled.

When SCIM is reported, describe also shows the credential lifecycle state
(live, not_issued, expired, revoked, or rotating), the SCIM endpoint URL, and
the token expiry, so an enabled-but-expired or tokenless provider is not
mistaken for a healthy one.

In JSON output the same three states are {"scim":{"enabled":true}},
{"scim":{"enabled":false}}, and the scim key omitted entirely. A missing scim
key means "not reported", not "disabled", so a scripted check must treat it as
unknown rather than off (with jq, ".scim == null" is unknown and ".scim.enabled"
is the boolean when present).

To change SCIM state or manage tokens, see:
  chainctl iam identity-providers scim --help

```
chainctl iam identity-providers describe [IDENTITY_PROVIDER_NAME | IDENTITY_PROVIDER_ID] [--output=json|table]
```

### Examples

```
  # Describe an identity provider by name
  chainctl iam identity-providers describe my-idp
  
  # Describe an identity provider by ID
  chainctl iam identity-providers describe 9b6da6e64b45129eb4e9f9f3ce9b69ca2a550c6b/034e4afcda8c0b07
  
  # Emit JSON for scripting (the scim key is omitted when SCIM status is not reported)
  chainctl iam identity-providers describe my-idp -o json
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

