---
date: 2026-10-30T14:11:50Z
title: "chainctl checks attempts"
slug: chainctl_checks_attempts
url: /platform/chainctl/chainctl-docs/chainctl_checks_attempts/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks attempts

List every attempt at a check.

### Synopsis

List every time the platform tried to produce a check's result, oldest first: why it was tried (the first attempt, a retry past an environmental failure, a policy retry, a requested rerun), how it ended, whether the action cache answered it and from which run, the trust class it ran in, and where its time went.

REF is a directory (its HEAD), a pull request URL or owner/repo#N, a full 40-character commit SHA, or a Run or WorkflowRun id; the current directory by default. "checks logs --attempt N" and "checks events --attempt N" read one attempt.

With -o json the attempts are printed as the API returns them.

```
chainctl checks attempts [REF] --check CHECK [--workflow WORKFLOW] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Was this check retried, or served from the cache?
  chainctl checks attempts acme/app#123 --check test
```

### Options

```
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

