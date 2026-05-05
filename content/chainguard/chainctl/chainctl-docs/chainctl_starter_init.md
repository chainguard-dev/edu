---
date: 2026-05-04T16:59:58Z
title: "chainctl starter init"
slug: chainctl_starter_init
url: /chainguard/chainctl/chainctl-docs/chainctl_starter_init/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl starter init

Initialize a new catalog starter organization.

### Synopsis

Initialize a new catalog starter organization.

A catalog starter organization gives a team free access to a small set of
Chainguard images for evaluation. Each starter org is entitled to a
limited number of images of your choice (base or application); the
exact quota is shown by 'chainctl starter status'. Other Chainguard
platform features may be unavailable to starter organizations; refer
to the documentation for the current scope.

This command is interactive. It will:

    1. Prompt you to authenticate with a supported identity provider.
    2. Register a new Chainguard identity for your email address.
    3. Create a new starter organization tied to your email domain.

Once your organization exists, the Chainguard platform will automatically
entitle it to choose images to be added. It should be ready within a
few minutes.

Authentication requirements:

    * You must use a business email address. Personal email providers (Gmail,
      Yahoo, etc.) are not eligible.
    * Authentication must use one of:
        - Email and password; or
        - Google, only if your business uses a Google Workspace account
          registered to your business domain.

If this command fails and you think the organization already exists,
you may follow up by running 'chainctl starter request-access'
to request access.

```
chainctl starter init [flags]
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

* [chainctl starter](/chainguard/chainctl/chainctl-docs/chainctl_starter/)	 - Manage catalog starter organizations

