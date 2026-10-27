---
date: 2026-10-26T19:49:34Z
title: "chainctl checks accept-terms"
slug: chainctl_checks_accept-terms
url: /platform/chainctl/chainctl-docs/chainctl_checks_accept-terms/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks accept-terms

Accept the terms Checks is offered under.

### Synopsis

Accept the legal documents an organization must accept to use Checks: the
Code Analysis Terms and the Master Service and License Agreement (MSLA).

An organization owner runs this once per organization; an organization must
have accepted them to run Checks. Re-running after acceptance is a no-op.
--parent names the organization; without it, the default.group config value
is used, or you pick one.

By continuing, you agree that your use of Chainguard Checks is subject to the Code Analysis Terms (https://www.chainguard.dev/legal/code-analysis-terms) as a Code Analysis Offering.

Chainguard Checks is a Technology Preview as described in the Chainguard Master Service and License Agreement (chainguard.dev/legal/master-service-and-license-agreement). Technology Previews are pre-release features, are provided "AS IS" without warranty of any kind, and are not recommended for production use. Do not use a Technology Preview to process Personal Data or any data subject to legal or regulatory compliance requirements unless specifically authorized. Chainguard may modify, suspend, or discontinue a Technology Preview at any time without notice. If you are accepting on behalf of an organization, you represent that you have authority to bind that organization to the Code Analysis Terms and the Master Service and License Agreement.

Where an interactive terminal isn't available, pass --yes. By using --yes you
agree to the statement above.

```
chainctl checks accept-terms [flags]
```

### Examples

```
  # Pick an organization and accept its terms
  chainctl checks accept-terms

  # Accept for a named organization without prompting
  chainctl checks accept-terms --parent acme.com --yes
```

### Options

```
      --parent string   The organization (name or ID) to accept the terms for. Defaults to the default.group config value.
      --yes             Accept the terms non-interactively. By using this flag you agree to the statement in this command's help, which it also prints.
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

* [chainctl checks](/platform/chainctl/chainctl-docs/chainctl_checks/)	 - Inspect and manage a repository's Checks on the Chainguard sandbox plane.

