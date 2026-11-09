---
date: 2026-11-06T22:09:37Z
title: "chainctl develop accept-terms"
slug: chainctl_develop_accept-terms
url: /platform/chainctl/chainctl-docs/chainctl_develop_accept-terms/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop accept-terms

Accept the terms Workspaces is offered under.

### Synopsis

Accept the legal documents an organization must accept to use Workspaces: the
Secured Platform Terms and the Master Service and License Agreement (MSLA).

An organization owner runs this once per organization. Re-running after
acceptance is a no-op. --parent names the organization; without it, the
default.group config value is used, or you pick one.

For a Starter organization, it prints what the Starter plan includes before
the terms, even with --yes.

By purchasing or subscribing to any products, services or other offerings ("Selected Offerings") that Chainguard, Inc. ("Chainguard") sells through its self-service purchase functionality ("Chainguard Self-Service"), you agree:

(a) to be bound by Chainguard's Master Service and License Agreement (https://www.chainguard.dev/legal/master-service-and-license-agreement), unless a separate and binding agreement between you and Chainguard is in effect and governs the Selected Offerings, in which case that agreement applies, (in either case, the "Agreement");
(b) the applicable descriptions and related terms for the Selected Offerings available at Product and Services Offerings (https://www.chainguard.dev/legal/offerings-overview);
(c) Selected Offerings made by you via Chainguard Self-Service constitutes an Order under the Agreement, the payment for which will be processed by our third party payment processor in accordance with Chainguard's Privacy Notice (https://www.chainguard.dev/legal/privacy-notice). Chainguard does not store your financial account information on our systems; however, we may have access to, and retain, subscriber information we receive from through our third-party payment processors.

If Customer does not agree to these terms, Customer may not access or use any Product, Service, or Technology Preview.

Where an interactive terminal isn't available, pass --yes.

```
chainctl develop accept-terms [flags]
```

### Examples

```
  # Pick an organization and accept its terms
  chainctl develop accept-terms

  # Accept for a named organization without prompting
  chainctl develop accept-terms --parent acme.com --yes
```

### Options

```
      --yes   Accept the terms non-interactively. By using this flag you agree to the statement in this command's help, which it also prints.
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
      --non-interactive    Disable prompts; fail if a session or group choice is ambiguous.
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
      --parent string      Organization or folder name/ID (defaults to $CHAINCTL_SANDBOX_GROUP, then default.group).
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl develop](/platform/chainctl/chainctl-docs/chainctl_develop/)	 - Open or resume a cloud development session.

