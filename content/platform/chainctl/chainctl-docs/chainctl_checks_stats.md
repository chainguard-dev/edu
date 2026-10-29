---
date: 2026-10-28T16:22:54Z
title: "chainctl checks stats"
slug: chainctl_checks_stats
url: /platform/chainctl/chainctl-docs/chainctl_checks_stats/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks stats

Summarize the outcomes of the instance's newest runs and their checks.

### Synopsis

Summarize the outcomes of the instance's newest WorkflowRuns, by repository
and by check name within a repository.

The service aggregates at most --limit runs, newest first (500 by default, at most
2000), and returns only the counts. A repository's row counts runs; a
check's row counts its jobs across those runs.

OPEN counts runs or jobs with no outcome yet, queued or running; RUNNING is
the running part of OPEN and is not added to the total. FAIL% is failed over
passed plus failed, so work that has not decided, was cancelled, errored or
was gated off (NOT_INSTANTIATED) does not move it. A fan-out check's
instances ("CHECK/ENTRY") and its fold ("CHECK") are separate rows. CONFIGS is
how many distinct authored configurations a repository's runs resolved.

```
chainctl checks stats [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--limit N] [--output=json|table]
```

### Examples

```
  # The 500 newest runs
  chainctl checks stats

  # A larger sample, for scripts
  chainctl checks stats --limit 2000 -o json
```

### Options

```
      --limit int            The most runs to summarize, newest first; at most 2000. (default 500)
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
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

