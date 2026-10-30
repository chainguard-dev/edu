---
date: 2026-10-28T16:22:54Z
title: "chainctl checks events"
slug: chainctl_checks_events
url: /platform/chainctl/chainctl-docs/chainctl_checks_events/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks events

Print the events one attempt at a check recorded.

### Synopsis

Print the structured events one attempt at a check recorded, in the order they were recorded: when each activity (provisioning, a step, a process the step ran) started and finished, its progress, and the diagnostics attached to it. "checks describe --events" prints every check's events of a Run at once; this reads one attempt, all of it.

REF is a directory (its HEAD), a pull request URL or owner/repo#N, a full 40-character commit SHA, or a Run or WorkflowRun id; the current directory by default. --attempt reads that attempt instead of the current one; "checks attempts" lists them.

Event messages and attributes are producer observations, some from the guest, so each line is sanitized. With -o json the events are printed as the API returns them.

```
chainctl checks events [REF] --check CHECK [--workflow WORKFLOW] [--attempt N] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # What did the check spend its time on?
  chainctl checks events acme/app#123 --check test

  # The first attempt of a retried check
  chainctl checks events acme/app#123 --check test --attempt 1 -o json
```

### Options

```
      --attempt int32        Read this attempt of the check instead of its current one.
      --check string         The check, by name.
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
      --workflow string      The workflow the check is in, when two workflows have a check of that name.
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

