---
date: 2026-10-26T19:49:34Z
title: "chainctl checks describe"
slug: chainctl_checks_describe
url: /platform/chainctl/chainctl-docs/chainctl_checks_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks describe

Describe a Run: its workflows, checks and steps.

### Synopsis

Describe a Run: where it came from, its status, and the tree of its
workflows and their checks.

RUN is a Run's resource name, its id, or a prefix of its id unique among the
instance's recent Runs; "checks list" and "checks status -o json" print them.
It may also be a WorkflowRun outside a Run, by resource name or full id, as a
repository the platform creates no Runs for has; a WorkflowRun inside a Run
describes its Run.

--steps adds each check's steps. --events adds the Run's recorded events and
each attempt's timings (queued, waiting for a slot, booting, provisioning,
running steps), which say where its time went.

With -o json the Run, its WorkflowRuns and, under --events, the event streams
are printed as the API returns them.

```
chainctl checks describe RUN [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--steps] [--events] [--output=json|table]
```

### Examples

```
  # A Run's checks and their steps
  chainctl checks describe 0f3a --steps

  # Why was it slow?
  chainctl checks describe 0f3a --events
```

### Options

```
      --events               Show the Run's recorded events and each attempt's timings.
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --steps                Show each check's steps.
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
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

