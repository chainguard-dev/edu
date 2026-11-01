---
date: 2026-10-30T14:11:50Z
title: "chainctl checks failures"
slug: chainctl_checks_failures
url: /platform/chainctl/chainctl-docs/chainctl_checks_failures/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks failures

Show why a Run's checks failed.

### Synopsis

Show each failed check of a Run: the step that failed, with its exit code and command, and the end of the output of what failed it, quoted from the check's log.

What is quoted is the executor's inference from facts it recorded when the step ended: the failing Go tests, decoded from go test -json events on the step's output; else the processes the step's exec tree says exited non-zero and wrote output, the last to write among them last; else the end of the step's output, with a note saying why. A note is the executor's, but can quote the guest agent's own account of what the exec tree lacks. Process names, test names and quoted text are the guest's (guest-attested). A check with no such record (it errored on the platform, or ran before the executor kept one) shows its error and the "checks logs" command that reads its last lines.

Checks that did not run are counted; --not-run lists them with the reason.

REF is a directory (its HEAD), a pull request URL or owner/repo#N, a full 40-character commit SHA, or a Run or WorkflowRun id; the current directory by default. With --check, only that check.

The whole answer is held to --budget bytes: as many failed checks in full as fit, then one line each, then the names of the rest. A budget too small for the header and the count of the checks left out is refused. With -o json each quote carries the log byte ranges it came from and the log's digest, and a "more" command reads the output before it. Guest text is escaped there; on a terminal it is sanitized unless --raw.

```
chainctl checks failures [REF] [--check CHECK [--workflow WORKFLOW]] [--budget BYTES] [--not-run] [--raw] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Why did this pull request's checks fail?
  chainctl checks failures acme/app#123

  # One check, with more of its output
  chainctl checks failures acme/app#123 --check test --budget 32768

  # For an agent
  chainctl checks failures . -o json
```

### Options

```
      --budget int           The most bytes the answer takes, header and every check included. (default 8192)
      --check string         The check, by name.
      --not-run              Also list the checks that did not run, with the reason, outside the budget.
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --raw                  Write the repository's and the guest's text as raw bytes, escape sequences included, even to a terminal. Output that is not a terminal is always raw.
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

