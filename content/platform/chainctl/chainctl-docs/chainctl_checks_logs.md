---
date: 2026-10-28T16:22:54Z
title: "chainctl checks logs"
slug: chainctl_checks_logs
url: /platform/chainctl/chainctl-docs/chainctl_checks_logs/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks logs

Print a check's log.

### Synopsis

Print the combined stdout and stderr of a Run's checks, followed by each check's annotations: the ::error, ::warning and ::notice lines the check printed, as the control plane reads them back from the log.

REF names the Run: "." or a directory (its checkout's HEAD, the default), a pull request URL or owner/repo#N, a full 40-character commit SHA, or a Run id or a prefix of one. A commit or pull request with several Runs reads the newest.

With --check, that check's log; with --workflow too, the check of that name in that workflow, which is needed only when two workflows share the name. Without --check, every check that has a log, each introduced by a line naming it.

REF may also be a WorkflowRun outside a Run by its full id, and a pull request whose checks are such a WorkflowRun reads its newest one.

The bounded views read a part of one check's log, and need --check:

  --errors       the lines the control plane's log parser names as errors (::error commands, and error-level JSON, logfmt and prefixed lines), with -C lines around each. When it names none, the log's last 30 lines, saying so.
  --grep RE      the lines matching the RE2 expression RE, with -C lines around each, reading at most 64 MiB.
  --tail N       the last N lines. The API reads a log only forward, so this reads the whole log.
  --offset BYTES [--limit-bytes N]
                 exactly the N bytes (64 KiB by default) from byte BYTES.

Each excerpt is introduced by the byte range it covers; pass its start back as --offset with --limit-bytes to read around it. A view that leaves anything out says so after its excerpts, with the --offset it continues at: --errors and --grep start at --offset when it is given. Offsets are GetJobLog's: a part of a long log the store did not retain is marked by a "# [not retained: ...]" line that counts toward no offset. With -o json each excerpt is one JSON object per line, carrying its WorkflowRun, workflow, check, attempt, byte range and log digest, and a last "summary" object says what was left out.

--follow keeps reading a running check's live output until it finishes (and, without --check, until every check of the Run has), waiting for a check that has not started; a check retried while it is followed is followed into its new attempt, introduced by a line naming the attempt. --attempt reads one attempt of a retried check, such as an earlier one.

The log is the repository's and the guest's own output. On a terminal it is printed with escape sequences and other control characters removed; it is written as raw bytes when stdout is not a terminal, or with --raw.

```
chainctl checks logs [REF] [--check CHECK [--workflow WORKFLOW]] [--follow] [--attempt N] [--errors [-C N] [--max N] [--offset BYTES] | --grep RE [-C N] [--max N] [--offset BYTES] | --tail N | --offset BYTES [--limit-bytes N]] [--raw] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # The log of this checkout's "test" check
  chainctl checks logs --check test

  # Follow a pull request's check while it runs
  chainctl checks logs acme/app#123 --check test --workflow go --follow

  # The first attempt of a retried check in a Run
  chainctl checks logs 0f3a --check e2e --attempt 1

  # A failed check's error lines, three lines of context around each
  chainctl checks logs acme/app#123 --check test --errors -C 3

  # Where a test failed, and the 4 KiB after an excerpt that starts at byte 81920
  chainctl checks logs acme/app#123 --check test --grep '^--- FAIL'
  chainctl checks logs acme/app#123 --check test --offset 81920 --limit-bytes 4096
```

### Options

```
      --attempt int32        Read this attempt of the check instead of its current one. Needs --check.
      --check string         The check, by name.
  -C, --context int          With --errors or --grep, show this many lines before and after each one.
      --errors               Show only the lines the control plane's log parser names as errors, with --context lines around each. Needs --check.
  -f, --follow               Keep reading a running check's live output until it finishes, waiting for a check that has not started.
      --grep string          Show only the lines matching this RE2 regular expression, with --context lines around each. Needs --check.
      --limit-bytes int      Read exactly this many bytes of the log from --offset (64 KiB when only --offset is given). Needs --check.
      --max int              With --errors or --grep, show at most this many of them (10 errors or 20 matches by default).
      --offset int           Start --errors or --grep at this byte of the log, or read the window of --limit-bytes bytes from it. Needs --check.
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --raw                  Write the repository's and the guest's text as raw bytes, escape sequences included, even to a terminal. Output that is not a terminal is always raw.
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --tail int             Show only the log's last N lines, as many of them as fit in 16 KiB. Needs --check.
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

