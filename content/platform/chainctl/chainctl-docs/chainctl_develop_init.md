---
date: 2026-10-30T14:11:50Z
title: "chainctl develop init"
slug: chainctl_develop_init
url: /platform/chainctl/chainctl-docs/chainctl_develop_init/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop init

Sign up for Chainguard Starter with Checks and Workspaces.

### Synopsis

Sign up for Chainguard Starter and turn on its monthly allowance of Checks and
Workspaces.

To create an organization, sign in with a verified email address using GitHub,
Google, email and password, or GitLab where available. For GitHub and GitLab,
use your primary email address.

This command is interactive. It will:

    1. Sign you in: with a saved session, after you confirm its account
       (without asking under --non-interactive or with no terminal), or
       else through the browser, registering a new Chainguard identity if
       you have none.
    2. Use your organization that can use Checks and Workspaces (Starter,
       Team, or Enterprise), asking which one when several can, or create
       a Starter organization if you have none that can, after asking your
       name, company, job title, and whether you want updates. With a
       business email address it is named after your email domain. With a
       personal email address you name it yourself, at a prompt or with
       --name, and its registry and package paths use its ID instead of
       the name. Pass --parent to pick the organization yourself.
    3. Ask you to accept the terms Checks and Workspaces are offered under.
    4. Link a GitHub account to your organization: your own GitHub user by
       default, or a GitHub organization you own. When the Chainguard GitHub
       App is not installed on it, offer to open the page that installs it,
       and link again once you have. When it is already linked to another
       Chainguard organization, offer to link a different one.
    5. Turn on Checks and Workspaces, with the Starter plan's monthly
       compute allowance.
    6. If the organization's sessions act on GitHub as their owner, offer to
       connect your own GitHub account (chainctl develop github login).

Every organization's owners can turn on Checks and Workspaces with the
Starter allowance; an allowance Chainguard granted the organization is kept
as it is. The compute allowance resets on the 1st of each month (UTC).

Checks and Workspaces are a Technology Preview, as defined under our online
Master Service and License Agreement (MSLA):
https://www.chainguard.dev/legal/master-service-and-license-agreement

```
chainctl develop init [flags]
```

### Examples

```
  # Sign up, answering the prompts
  chainctl develop init

  # Name the new organization and the GitHub organization to link up front
  chainctl develop init --name acme-dev --github-org acme

  # Turn them on in an organization you already have
  chainctl develop init --parent acme.com
```

### Options

```
      --github-org string   GitHub account login to link: an organization, or your own user. Defaults to the GitHub user you authorize as.
      --name string         Name of the organization to create when you have none and sign up with a personal email address. It can't look like a domain name. Ignored for an organization named after your email domain.
      --port int            Local loopback port for the GitHub OAuth callback. (default 8989)
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

