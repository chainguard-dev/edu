---
date: 2026-10-30T14:11:50Z
title: "chainctl auth configure nuget"
slug: chainctl_auth_configure_nuget
url: /platform/chainctl/chainctl-docs/chainctl_auth_configure_nuget/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth configure nuget

Configure NuGet credentials for Chainguard Libraries for .NET

### Synopsis

Configure NuGet to use Chainguard Libraries for .NET.

By default, this command creates a long-lived pull token (30 days unless
--ttl says otherwise) and writes it to a project-level nuget.config. The
same credentials work in environments that don't support OIDC (CI
systems, build servers, etc.). Each run creates a new pull token. A
Starter organization holds at most 5 unexpired pull tokens, and each run
uses one until it expires; "chainctl auth pull-token list" shows them.

With --pull-token=false, it authenticates using your current Chainguard
session and writes that session's token, which expires within the hour.
This uses no pull token.

A config created from scratch names the Chainguard feed as its only
source, so a restore cannot fall back to nuget.org — including sources
inherited from a parent directory or the user-level config, which a new
file also clears for everything beneath it. An existing config is
amended instead: its own sources and settings are kept, which means the
feed may not be the only one — and directives already in the file can
stop NuGet consulting it at all. Either way the command reports whether a
restore would actually reach the feed.

The file configures restore only: the publish endpoint is not a v3
service index, so a source pointing at it would break restore, and
publishing needs its own config.

Credentials are written in cleartext, because NuGet's encrypted
credential store is Windows-only, and the file is readable by its owner
alone on platforms where that is enforceable.

```
chainctl auth configure nuget [flags]
```

### Examples

```
  # Configure NuGet with a pull token for your organization.
  chainctl auth configure nuget --parent=my-org
  
  # Configure NuGet with a pull token that lasts for 24 hours.
  chainctl auth configure nuget --parent=my-org --ttl=24h
  
  # Configure NuGet with your current Chainguard session's token, which expires within the hour.
  chainctl auth configure nuget --pull-token=false
```

### Options

```
      --headless                   Skip browser authentication and use device flow.
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with. Mutually exclusive with --org-name.
      --identity-token string      Use an explicit passed identity token or token path.
      --name string                Optional name for the pull token. (default "pull-token")
      --org-name string            Organization to use for authentication. If configured the organization's custom identity provider will be used. Mutually exclusive with --identity-provider.
      --parent string              The IAM organization or folder with which the pull-token identity is associated.
      --pull-token                 Whether to create a pull token for NuGet authentication. (default true)
      --social-login string        Which of the default identity providers to use for authentication. Must be one of: email, google, github, gitlab
      --sts-http1-downgrade        Downgrade STS requests to HTTP/1.x
      --ttl ns                     Time To Live for the validity of the pull token. Valid unit strings range from nanoseconds to hours and are ns, `us`, `ms`, `s`, `m`, and `h`. The maximum depends on the organization's plan: 720h (30 days) for Starter, 168h (7 days) for Team and 8760h (one year) for other plans. (default 720h0m0s)
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

* [chainctl auth configure](/platform/chainctl/chainctl-docs/chainctl_auth_configure/)	 - Configure a local tool to authenticate to Chainguard.

