---
date: 2026-10-30T14:11:50Z
title: "chainctl"
slug: chainctl
url: /platform/chainctl/chainctl-docs/chainctl/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl

Chainguard Control

### Synopsis

Chainguard Control (chainctl) manages Chainguard resources from the command line.

Exit codes:

- 0: the command succeeded, or a confirmation prompt was declined and nothing was changed.
- 1: the command failed. This covers every error, including invalid arguments and flags, and commands that act as a gate: a check that failed, a policy that denied, a --check or --exit-code gate that matched, or "chainctl images repos build apply --dry-run" finding changes to apply.
- 2: "chainctl checks status" only. The platform created no Run for the commit or pull request, so there is no verdict.
- 3-8: "chainctl starter init" only. Each names a way the signup ended; "chainctl starter init --help" lists them.
- 130: the command was interrupted with SIGINT (Ctrl-C) and did not finish. A command that unwinds after the first Ctrl-C may exit 1, or 0 if it treats the cancellation as a clean stop; "chainctl starter init" exits 7 once it has created the organization. A second Ctrl-C forces 130.
- 143: the command was terminated with SIGTERM.

"chainctl develop" and "chainctl develop attach" exit with the session shell's exit code when the shell exits. "chainctl develop exec" exits with the command's exit code, 124 when --timeout killed it, and 255 when the command's outcome is unknown. "chainctl develop check" exits 0 when the checks pass and 1 when a step fails.

The number in brackets in some error messages, such as "[4] ...", is chainctl's internal error code, also shown as "code" with --output json. It is not the process exit code.

```
chainctl [flags]
```

### Options

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

* [chainctl actions](/platform/chainctl/chainctl-docs/chainctl_actions/)	 - Interact with the Chainguard Actions product.
* [chainctl agent](/platform/chainctl/chainctl-docs/chainctl_agent/)	 - Agent-powered commands.
* [chainctl auth](/platform/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl checks](/platform/chainctl/chainctl-docs/chainctl_checks/)	 - Inspect and manage a repository's Checks on the Chainguard sandbox plane.
* [chainctl config](/platform/chainctl/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.
* [chainctl develop](/platform/chainctl/chainctl-docs/chainctl_develop/)	 - Open or resume a cloud development session.
* [chainctl events](/platform/chainctl/chainctl-docs/chainctl_events/)	 - Events related commands for the Chainguard platform.
* [chainctl guardener](/platform/chainctl/chainctl-docs/chainctl_guardener/)	 - Manage guardener integrations.
* [chainctl iam](/platform/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl images](/platform/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.
* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.
* [chainctl packages](/platform/chainctl/chainctl-docs/chainctl_packages/)	 - Interact with Chainguard packages
* [chainctl policy](/platform/chainctl/chainctl-docs/chainctl_policy/)	 - Manage policies.
* [chainctl skills](/platform/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.
* [chainctl starter](/platform/chainctl/chainctl-docs/chainctl_starter/)	 - Manage Chainguard Starter organizations
* [chainctl update](/platform/chainctl/chainctl-docs/chainctl_update/)	 - Update chainctl.
* [chainctl version](/platform/chainctl/chainctl-docs/chainctl_version/)	 - Prints the version

