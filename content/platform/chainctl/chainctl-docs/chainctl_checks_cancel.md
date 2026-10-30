---
date: 2026-10-28T16:22:54Z
title: "chainctl checks cancel"
slug: chainctl_checks_cancel
url: /platform/chainctl/chainctl-docs/chainctl_checks_cancel/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks cancel

Cancel a Run.

### Synopsis

Cancel a Run and every workflow of it still queued or running. RUN is a Run's resource name, its id, or a prefix of its id unique among the instance's recent Runs.

A Run GitHub started (for a pull request, or as a postsubmit) is GitHub's: cancelling it reports its checks on GitHub as cancelled, and only a new push, GitHub's Re-run or `chainctl checks rerun` starts them again. It is refused unless --force is given.

Cancelling a Run whose cancellation was already requested is harmless; a Run that has finished cannot be cancelled. With --output json the Run is printed as the API returns it.

```
chainctl checks cancel RUN [--force] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Cancel a Run you started, by id prefix
  chainctl checks cancel 3f9a1c2e

  # Cancel a Run GitHub started for a pull request
  chainctl checks cancel 3f9a1c2e --force
```

### Options

```
      --force                Cancel the Run even when GitHub started it.
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

