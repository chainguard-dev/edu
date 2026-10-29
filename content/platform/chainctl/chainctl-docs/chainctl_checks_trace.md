---
date: 2026-10-28T16:22:54Z
title: "chainctl checks trace"
slug: chainctl_checks_trace
url: /platform/chainctl/chainctl-docs/chainctl_checks_trace/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks trace

Show the commands a check ran.

### Synopsis

Print what ran under each step of a check: the step's exec tree, every process the step started as the guest kernel observed it, with each program's name, wall time and how it ended.

REF names the Run as for "checks logs": "." or a directory (the default), a pull request, a full commit SHA, a Run id or a prefix of one, or a WorkflowRun outside a Run by full id.

With --check, that check's steps; without it, every check with a recorded tree, each introduced by a line naming it. A tree names programs, never command lines, and identical sibling processes share one line ("cc ×312  41s total  exit 0"). A tree marked INCOMPLETE lost events or was cut to fit, and its shape may be wrong where spans are missing.

For a failed step the output names a likely failing command. It is INFERRED from the tree, never recorded: shells and build tools routinely absorb non-zero exits, so the candidate can be wrong. --failed prints only failed steps, each as the path from the step's command down to that candidate.

Program names and step labels come from the repository and the guest, so any that could move the cursor are printed quoted. With -o json each step's document is one JSON object per line.

```
chainctl checks trace [REF] [--check CHECK [--workflow WORKFLOW]] [--failed] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Every step's tree for this checkout's "test" check
  chainctl checks trace --check test

  # Only the path to each failed step's likely failing command
  chainctl checks trace acme/app#123 --check test --failed

  # Each step's document as JSON
  chainctl checks trace --check test -o json | jq .
```

### Options

```
      --check string         The check, by name.
      --failed               Print only failed steps, each as the path from the step's command down to its inferred failing command.
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

