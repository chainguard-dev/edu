---
date: 2026-10-30T14:11:50Z
title: "chainctl checks rerun"
slug: chainctl_checks_rerun
url: /platform/chainctl/chainctl-docs/chainctl_checks_rerun/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks rerun

Rerun a pull request's checks, or a finished postsubmit Run.

### Synopsis

Rerun the checks of a Run the platform started, once it has finished. REF is a pull request URL or owner/repo#N, `.` or a directory (its HEAD), a full 40-character commit SHA, or a Run id (its resource name, its id, or a prefix of its id unique among the instance's recent Runs).

For a pull request, the checks of its newest Run are rerun at the head that Run ran, exactly as GitHub's Re-run does: the platform builds a fresh Run of that head from the pull request itself, keeping its requested checks and skipping cached results, and reports it on the pull request as before. It does so only while the pull request is open at that head; a Run of a head the pull request has moved past is refused. The platform can also answer the rerun with no Run, on the pull request's check: when the head no longer merges cleanly onto the base branch, the merge cannot be made, or the Run's creation is refused. --watch then stops and prints the check's reason, and checks status shows it beside the earlier Run. In a repository whose pull requests' checks are still a single WorkflowRun rather than a Run, the same rerun is asked for, named by the pull request; --watch cannot follow it there.

For a postsubmit Run the platform started for a pushed branch, a fresh Run of the same commit, ref, changed paths and checks starts at once, with cached results skipped, and names the Run it reruns.

A Run created with `chainctl checks run` is run again with that command.

With --output json the API's answer is printed: the new Run for a postsubmit Run, and for a pull request the Run whose checks are rerun. Under --watch the fresh Run is followed to its final status instead.

With --watch the command exits 1 when the Run is done and its verdict did not pass, or when the command fails (including when it is interrupted); 0 when it passed. For a pull request whose checks are a single WorkflowRun, --watch cannot follow them and the command exits 0 once the rerun is asked for.

```
chainctl checks rerun REF [--watch] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Rerun a flaky check on a pull request, and wait for the result
  chainctl checks rerun acme/app#123 --watch

  # Rerun this checkout's HEAD
  chainctl checks rerun .

  # Rerun a flaky postsubmit Run, by id prefix
  chainctl checks rerun 3f9a1c2e
```

### Options

```
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
      --watch                Wait until the fresh Run finishes, printing its checks whenever they change.
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

