---
date: 2026-10-30T14:11:50Z
title: "chainctl starter init"
slug: chainctl_starter_init
url: /platform/chainctl/chainctl-docs/chainctl_starter_init/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl starter init

Initialize a new Chainguard Starter organization.

### Synopsis

Initialize a new Chainguard Starter organization.

A Chainguard Starter organization gives a team free access to a small set of
Chainguard images for evaluation. Each starter org is entitled to a
limited number of images of your choice (base or application); the
exact quota is shown by 'chainctl starter status'. Other Chainguard
platform features may be unavailable to starter organizations; refer
to the documentation for the current scope.

By default this command is interactive. It will:

    1. Prompt you to authenticate with a supported identity provider, or
       use the one --social-login names.
    2. Register a new Chainguard identity for your email address.
    3. Create a new starter organization. With a business email address it
       is named after your email domain. With a personal email address you
       name it yourself, at a prompt or with --name, and its registry and
       package paths use its ID instead of the name.
    4. With --images, wait for the organization to be ready and add those
       images to it, as 'chainctl starter add-images' does.

Before it creates the organization, it asks your name, company, job title,
and whether you want updates from Chainguard. --given-name, --family-name,
--company, --job-title and --email-updates answer those questions instead.
The terms line is printed either way. With --non-interactive, it never
prompts: it leaves the identity provider to the browser, treats a missing
--email-updates as no, and fails naming the missing flags instead of asking.
It checks them before you sign in, except --name: whether your organization
needs one is known only after you sign in.

Once your organization exists, the Chainguard platform will automatically
entitle it to choose images to be added. It should be ready within a
few minutes.

With --output json, the questions and progress go to stderr, and stdout
carries one JSON object: the outcome, the organization's ID and name, the
images added, the next command to run, and the error, if any. An
already-in-org outcome also carries "organizations", the organizations
the identity belongs to, "identity", the email it signed in with, and
"hint", what to do instead. Its next command is 'chainctl starter status'
when one of those organizations is a Starter organization, and none
otherwise.

Exit codes:

    0  The organization was created, with the --images added.
    1  Any other failure, such as an invalid or missing flag, or a network
       error.
    3  This identity already belongs to an organization. The browser may
       have reused an earlier sign-in; sign out in the browser to use
       another identity.
    4  This identity isn't eligible for a Starter organization.
    5  The organization couldn't be created. One may already exist for
       your email domain; run 'chainctl starter request-access'.
    6  Authentication failed.
    7  The organization was created, but a later step failed: signing in
       again to pick it up, or adding the --images. The JSON's next
       field names the command to run next. A Ctrl-C after the
       organization was created also exits 7.
    8  The browser sign-in wasn't finished within 5 minutes. Run the same
       command again; the JSON's next field names it.

Authentication requirements:

    * Use a business email address to get an organization named after your
      company's domain. Where personal email providers (Gmail, Yahoo, etc.)
      are accepted, the organization isn't tied to any domain.
    * Authenticate with a verified email address using GitHub, Google,
      email and password, or GitLab where available. For GitHub and GitLab,
      this must be your primary email.

If this command fails and you think the organization already exists,
you may follow up by running 'chainctl starter request-access'
to request access.

```
chainctl starter init [--output=json] [flags]
```

### Examples

```
  # Sign up, answering the prompts
  chainctl starter init

  # Sign in with GitHub, add two images, and print the result as JSON
  chainctl starter init --social-login github --images nginx,redis --output json

  # Sign up without prompts; you still sign in in the browser
  chainctl starter init --non-interactive --social-login google \
    --given-name Ada --family-name Lovelace --company Acme --job-title Engineer
```

### Options

```
      --company string        Your company's name, instead of answering its question.
      --email-updates         Whether to receive updates from Chainguard, instead of answering its question.
      --family-name string    Your last or family name, instead of answering its question.
      --given-name string     Your first or given name, instead of answering its question.
      --images strings        Catalog images to add once the organization is ready, as 'chainctl starter add-images' does. Comma-separated or repeated.
      --job-title string      Your job title, instead of answering its question.
      --name string           Name of the organization, when you sign up with a personal email address. It can't look like a domain name. Ignored for an organization named after your email domain.
      --non-interactive       Never prompt: skip the provider menu, and fail naming the flags still needed instead of asking a question.
      --social-login string   Identity provider to sign in with, instead of choosing from a menu. Must be one of: email, google, github, gitlab
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

* [chainctl starter](/platform/chainctl/chainctl-docs/chainctl_starter/)	 - Manage Chainguard Starter organizations

