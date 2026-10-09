---
date: 2026-10-08T18:22:10Z
title: "chainctl skills status"
slug: chainctl_skills_status
url: /platform/chainctl/chainctl-docs/chainctl_skills_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills status

Check a harden job or wait for it to finish.

### Synopsis

Check the job ID printed by skills harden without uploading or submitting
the skill again. Progress names the pipeline stage once the job is running.
--wait tracks the job to completion and downloads the hardened skill and report
to ./hardened/NAME, with .hardened-artifact.json recording the published
reference and digest. A timeout or interrupt leaves the job running. A skill the
post-hardening scan rejected downloads unmodified to ./unhardened/NAME and exits
nonzero, naming the scanner and rule that rejected it. Other failures exit
nonzero and name the stage the job failed in.

```
chainctl skills status --group <org> --id <job-id> [flags]
```

### Examples

```
  chainctl skills status --group my-org --id <job-id>
  chainctl skills status --group my-org --id <job-id> --wait --timeout 30m
```

### Options

```
  -g, --group string       Target organization name or UIDP (required).
      --id string          Harden job ID (required).
      --timeout duration   Maximum command duration with --wait (0 means no timeout).
      --wait               Wait for hardening to finish and download the result.
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

* [chainctl skills](/platform/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

