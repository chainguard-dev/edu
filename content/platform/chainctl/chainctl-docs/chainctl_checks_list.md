---
date: 2026-10-30T14:11:50Z
title: "chainctl checks list"
slug: chainctl_checks_list
url: /platform/chainctl/chainctl-docs/chainctl_checks_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks list

List Runs.

### Synopsis

List the instance's Runs, newest first.

--repo, --ref and --trigger are filtered by the server. A Run's outcome is
folded from its workflows when it is read, so --outcome is filtered here,
over at most the 500 newest Runs the other filters match; a Run that
has not finished matches no outcome.

```
chainctl checks list [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--repo REPO] [--ref REF] [--trigger presubmit|postsubmit] [--outcome OUTCOME] [--limit N] [--output=json|table]
```

### Examples

```
  # What's broken on main?
  chainctl checks list --repo acme/app --ref refs/heads/main --outcome failed

  # The newest postsubmit Runs, as JSON
  chainctl checks list --trigger postsubmit -o json
```

### Options

```
      --limit int            The most Runs to list. (default 20)
      --outcome string       Only finished Runs with this outcome: passed, failed, errored, dependency_failed or cancelled.
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --ref string           Only Runs of this git ref, e.g. refs/heads/main; a bare branch name means refs/heads/NAME.
      --repo string          Only Runs of this repository: owner/repo for GitHub, or host/path.
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
      --trigger string       Only Runs of this trigger: presubmit or postsubmit.
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

