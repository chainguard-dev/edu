---
date: 2026-10-28T16:22:54Z
title: "chainctl checks run"
slug: chainctl_checks_run
url: /platform/chainctl/chainctl-docs/chainctl_checks_run/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks run

Run a commit's checks on the sandbox plane, advisory.

### Synopsis

Plan the committed tree at the HEAD of the checkout DIR (the current directory by default) as a presubmit, and run it on the sandbox plane.

The plane reads the repository's .chainguard/ configuration at that commit from GitHub, under your organization's own GitHub link, so the commit must be pushed; uncommitted changes are not planned (`chainctl develop check` runs a working tree). The repository is the checkout's origin, or the github.com remote --git-remote names.

The plan has no event context: no trigger, labels or pull request. A check whose when.expr reads them cannot be planned, and the command says which. A `when.changed` gate is measured from --base, by default HEAD's merge base with the remote's default branch, or HEAD's parent when HEAD is on it.

--check restricts the Run to one check and what it needs, and runs it even when it runs only on request; --workflow names its workflow when two have a check of that name. --request satisfies a check's `when: {requested: true}` gate, as a `ci/run:` label does on a pull request; it may be repeated.

The Run is advisory: it is never a pull request's checks or a commit's verdict, so `chainctl checks status` on the commit still reports what the platform ran. Follow the Run by its name, or pass --watch to wait for it. With --output json the Run is printed as the API returns it, or under --watch its final status.

With --watch the command exits 1 when the Run is done and its verdict did not pass, or when the command fails (including when it is interrupted); 0 when it passed.

```
chainctl checks run [DIR] [--check CHECK [--workflow WORKFLOW]] [--request CHECK]... [--git-remote NAME] [--base REV] [--watch] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Run this checkout's HEAD
  chainctl checks run .

  # Just one check, and wait for it
  chainctl checks run . --check test --workflow go --watch

  # A fork checkout: plan upstream, with an on-request check
  chainctl checks run . --request e2e-full --git-remote upstream
```

### Options

```
      --base string           The commit when.changed gates are measured from. Defaults to HEAD's merge base with the remote's default branch, or HEAD's parent on that branch.
      --check string          Run only this check and the checks it needs.
      --git-remote string     The checkout's remote whose github.com repository to plan. Defaults to origin.
      --parent string         The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --request stringArray   Satisfy this check's when: {requested: true} gate, as a ci/run: label does on a pull request. Repeatable.
      --sandbox-url string    URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string          Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
      --watch                 Wait until the Run finishes, printing its checks whenever they change.
      --workflow string       The workflow --check is in, when two workflows have a check of that name.
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

