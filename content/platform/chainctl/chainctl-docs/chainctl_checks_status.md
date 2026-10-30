---
date: 2026-10-28T16:22:54Z
title: "chainctl checks status"
slug: chainctl_checks_status
url: /platform/chainctl/chainctl-docs/chainctl_checks_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks status

Show whether a commit's or pull request's checks pass.

### Synopsis

Show the checks of the newest Run for REF and whether they pass.

REF is a directory (its HEAD), a pull request URL or owner/repo#N, a full 40-character commit SHA, or a Run or WorkflowRun id; the current directory by default.

The Run's verdict is its fold: every blocking check's outcome. status exits 1
only when the fold is done and did not pass, so a failing advisory check is
shown as "(advisory)" and does not fail it. A Run still executing exits 0;
pass --watch to wait for it to finish. A commit or pull request the platform
created no Run for has no platform verdict, and status says so and exits 2: a
Run a client created without an event is never its verdict. A check that runs only on request is
shown with the pull request label that requests it, and the weakenings of
base checks the change defers until after merge are listed under the table.
When the Run's GitHub check completed with no Run in place of its result (a
rerun or change whose merge onto the base branch failed, or whose Run's
creation was refused), the check's reason is shown above the table; the exit
code still follows the Run's fold.

```
chainctl checks status [REF] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--watch] [--output=json|table]
```

### Examples

```
  # This checkout's HEAD
  chainctl checks status

  # A pull request, until its checks finish
  chainctl checks status acme/app#123 --watch

  # For scripts and agents
  chainctl checks status . -o json

  # The repository ID to trust in a workload identity's subject
  chainctl checks status . -o json | jq -r .repository_id
```

### Options

```
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
      --watch                Wait until the Run finishes, printing its checks whenever they change.
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

