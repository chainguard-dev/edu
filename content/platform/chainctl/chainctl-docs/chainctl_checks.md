---
date: 2026-10-30T14:11:50Z
title: "chainctl checks"
slug: chainctl_checks
url: /platform/chainctl/chainctl-docs/chainctl_checks/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks

Inspect and manage a repository's Checks on the Chainguard sandbox plane.

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

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl checks accept-terms](/platform/chainctl/chainctl-docs/chainctl_checks_accept-terms/)	 - Accept the terms Checks is offered under.
* [chainctl checks attempts](/platform/chainctl/chainctl-docs/chainctl_checks_attempts/)	 - List every attempt at a check.
* [chainctl checks cancel](/platform/chainctl/chainctl-docs/chainctl_checks_cancel/)	 - Cancel a Run.
* [chainctl checks describe](/platform/chainctl/chainctl-docs/chainctl_checks_describe/)	 - Describe a Run: its workflows, checks and steps.
* [chainctl checks events](/platform/chainctl/chainctl-docs/chainctl_checks_events/)	 - Print the events one attempt at a check recorded.
* [chainctl checks explain](/platform/chainctl/chainctl-docs/chainctl_checks_explain/)	 - Print a repository's resolved checks configuration offline.
* [chainctl checks failures](/platform/chainctl/chainctl-docs/chainctl_checks_failures/)	 - Show why a Run's checks failed.
* [chainctl checks list](/platform/chainctl/chainctl-docs/chainctl_checks_list/)	 - List Runs.
* [chainctl checks logs](/platform/chainctl/chainctl-docs/chainctl_checks_logs/)	 - Print a check's log.
* [chainctl checks migrate](/platform/chainctl/chainctl-docs/chainctl_checks_migrate/)	 - Draft a .chainguard/ci/migrated.yaml from a repository's GitHub Actions presubmits and prove it on the sandbox plane.
* [chainctl checks rerun](/platform/chainctl/chainctl-docs/chainctl_checks_rerun/)	 - Rerun a pull request's checks, or a finished postsubmit Run.
* [chainctl checks run](/platform/chainctl/chainctl-docs/chainctl_checks_run/)	 - Run a commit's checks on the sandbox plane, advisory.
* [chainctl checks stats](/platform/chainctl/chainctl-docs/chainctl_checks_stats/)	 - Summarize the outcomes of the instance's newest runs and their checks.
* [chainctl checks status](/platform/chainctl/chainctl-docs/chainctl_checks_status/)	 - Show whether a commit's or pull request's checks pass.
* [chainctl checks top](/platform/chainctl/chainctl-docs/chainctl_checks_top/)	 - Rank checks by attempts, runtime or failure rate.
* [chainctl checks trace](/platform/chainctl/chainctl-docs/chainctl_checks_trace/)	 - Show the commands a check ran.
* [chainctl checks trends](/platform/chainctl/chainctl-docs/chainctl_checks_trends/)	 - Show how long the slowest checks take, hour by hour.
* [chainctl checks validate](/platform/chainctl/chainctl-docs/chainctl_checks_validate/)	 - Lint a repository's checks configuration offline.

