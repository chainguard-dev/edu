---
date: 2026-10-30T14:11:50Z
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

By continuing, you agree that your use of Chainguard Workspaces is subject to the Secured Platform Terms (https://www.chainguard.dev/legal/secure-platform-terms) as a Secured Platform Offering.

Chainguard Workspaces is a Technology Preview as described in the Chainguard Master Service and License Agreement (chainguard.dev/legal/master-service-and-license-agreement). Technology Previews are pre-release features, are provided "AS IS" without warranty of any kind, and are not recommended for production use. Do not use a Technology Preview to process Personal Data or any data subject to legal or regulatory compliance requirements unless specifically authorized. Chainguard may modify, suspend, or discontinue a Technology Preview at any time without notice. If you are accepting on behalf of an organization, you represent that you have authority to bind that organization to the Secured Platform Terms and the Master Service and License Agreement.

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

