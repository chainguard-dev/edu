---
date: 2026-07-23T16:28:18Z
title: "chainctl iam identity-providers scim token regenerate"
slug: chainctl_iam_identity-providers_scim_token_regenerate
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_token_regenerate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim token regenerate

Regenerate the SCIM bearer token for an identity provider.

### Synopsis

Regenerate the SCIM bearer token, whether the current one is live, expired, or revoked. A live token keeps authenticating for the overlap window (at most 24h) while the IdP connector is reconfigured with the new one. The new plaintext token is shown exactly once. If the current token may be exposed, do not rely on the overlap: revoke it, or regenerate with --overlap 0 for an immediate cutover.

```
chainctl iam identity-providers scim token regenerate IDENTITY_PROVIDER [--output=json] [flags]
```

### Examples

```
  # Regenerate with a one-hour overlap for reconfiguring the IdP
  chainctl iam identity-providers scim token regenerate my-idp --overlap 1h

  # Regenerate with a one-year expiry and an immediate cutover
  chainctl iam identity-providers scim token regenerate my-idp --overlap 0 --expires-in 8760h
```

### Options

```
      --expires-in duration   How long until the new token expires (maximum two years). Unset defaults to one year.
      --never-expires         Explicitly issue a token without a planned expiry.
      --overlap duration      How long a live previous token keeps authenticating (at most 24h). 0 cuts over immediately; unset defaults to one hour.
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

* [chainctl iam identity-providers scim token](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_token/)	 - Manage the SCIM provisioning bearer token for an identity provider.

