---
date: 2026-10-02T21:08:35Z
title: "chainctl auth token"
slug: chainctl_auth_token
url: /platform/chainctl/chainctl-docs/chainctl_auth_token/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth token

Print the local Chainguard Token.

### Synopsis

Print the local Chainguard Token.

With --capabilities and/or --scope, print a token narrowed to that access
instead of the cached one.

With --delegate, mint a grant for a delegate (see "chainctl iam identities
create delegate"): a token whose only audience is the delegation audience the
delegate pins, narrowed to --scope (required) and to the capabilities of
--role plus any --capabilities. The delegate exchanges the grant for tokens
carrying a subset of that access and expiring no later than the grant, which
lives at most 60 minutes. No API accepts the grant itself.

A grant cannot carry more than you hold; chainctl warns before minting one
that asks for more. Grants are stateless, so there is no per-grant list or
revoke: deleting the delegate stops every future exchange, and grants already
minted expire within 60 minutes.

The grant is minted from the cached refresh token when there is one,
otherwise from ambient credentials or a fresh login, and it is never cached.

The global --audience flag keeps its meaning here: it selects the API
audience of the cached token, and is unrelated to the grant's audience.

```
chainctl auth token [flags]
```

### Examples

```
  # Mint a grant for a delegate carrying the viewer role's capabilities in an organization.
  chainctl auth token --delegate=my-delegate --role=viewer --scope=ORGANIZATION_ID
  
  # Inspect what a grant carries.
  chainctl auth token --delegate=my-delegate --capabilities=repo.list --scope=ORGANIZATION_ID | chainctl auth token capabilities --token -
```

### Options

```
      --capabilities strings   Request a token narrowed to the given capabilities. With --delegate, capabilities the grant carries in addition to --role's.
      --delegate string        Mint a grant for this delegate (name or ID). Requires --scope and --role or --capabilities.
      --interactive            Allow browser or device login when needed, even when stderr is redirected.
      --role strings           With a grant (--delegate), the roles whose capabilities the grant carries.
      --scope strings          Request a token with scope reduced to the given groups (names or IDs).
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

* [chainctl auth](/platform/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl auth token capabilities](/platform/chainctl/chainctl-docs/chainctl_auth_token_capabilities/)	 - Print the capabilities of the local Chainguard Token.

