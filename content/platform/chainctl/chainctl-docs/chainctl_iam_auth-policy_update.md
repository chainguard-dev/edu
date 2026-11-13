---
date: 2026-11-12T21:48:09Z
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

Update how long a sign-in to an organization lasts.

### Synopsis

Update how long a sign-in to an organization lasts.

--session-duration sets how long a sign-in to the organization lasts before
its members must sign in again: from 1h to 90d, as a number of days (30d) or
hours (12h). --session-duration=default returns to Chainguard's default,
currently 20h.

The length runs from sign-in. At 30d or less, a session lasts that long from
sign-in, and using it does not extend it. Above 30d, a session lasts while it
is used at least once every 30 days, up to the length. A session whose client
does not rotate its refresh tokens lasts at most 20h.

A member of several organizations gets the shortest length among the verified
ones; an unverified organization, which cannot hold a policy, does not count.

A shorter length reaches an existing session at its next token refresh only
when a length over 20h has already extended that session past 20h from
sign-in. It does not cut any other existing session, such as one signed in
under a length of 20h or less: that session keeps the expiry it was issued
with, at most 20h from sign-in.

```
chainctl iam auth-policy update --parent ORGANIZATION_NAME | ORGANIZATION_ID --session-duration=DURATION [--output=json|table]
```

### Examples

```
  # Sign members out 7 days after they sign in
  chainctl iam auth-policy update --parent my-org --session-duration=7d
  
  # Sessions last up to 90 days if used at least every 30 days
  chainctl iam auth-policy update --parent my-org --session-duration=90d
  
  # Return to Chainguard's default session length
  chainctl iam auth-policy update --parent my-org --session-duration=default
```

### Options

```
      --parent string             The organization (name or UIDP) whose authentication policy to update. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --session-duration string   How long a sign-in to the organization lasts, from 1h to 90d (for example 30d or 12h), or "default" for Chainguard's default.
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

