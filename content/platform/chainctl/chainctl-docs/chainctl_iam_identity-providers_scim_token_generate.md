---
date: 2026-07-23T16:28:17Z
title: "chainctl iam identity-providers scim token generate"
slug: chainctl_iam_identity-providers_scim_token_generate
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_token_generate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim token generate

Generate the first SCIM bearer token for an identity provider.

### Synopsis

Generate the first SCIM bearer token for an identity provider. Provisioning stays off until SCIM is explicitly enabled for the identity provider. The plaintext token is shown exactly once; only its SHA-256 digest is stored. If a token already exists (even expired or revoked), regenerate it instead.

```
chainctl iam identity-providers scim token generate IDENTITY_PROVIDER [--output=json] [flags]
```

### Examples

```
  # Generate a SCIM token that expires in a year
  chainctl iam identity-providers scim token generate my-idp --expires-in 8760h
```

### Options

```
      --expires-in duration   How long until the token expires (maximum two years). Unset defaults to one year.
      --never-expires         Explicitly issue a token without a planned expiry.
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

