---
date: 2026-09-25T09:27:27Z
title: "chainctl skills harden"
slug: chainctl_skills_harden
url: /platform/chainctl/chainctl-docs/chainctl_skills_harden/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills harden

Submit a skill for server-side hardening.

### Synopsis

Submit a skill to the Skills API for server-side hardening.
Pass a local path or use --folder to package and upload a directory; SKILL.md
supplies the skill name. An uploads registry reference uses an existing artifact.
--digest uses an artifact already uploaded to uploads.cgr.dev/ORG/NAME and
requires --name. The digest must be sha256:<64-hex>, not a tag or a full reference.
--group is required and accepts an organization name or UIDP.

Prints the job ID and status after submission. With --wait, polls until the
job finishes, downloads the result to ./hardened/NAME, and prints its reference
and digest. HARDENING.md in the download contains the report and scanner findings.
--timeout bounds the command when waiting. A timeout or interrupt leaves the
server-side job running.

Submitting unchanged content to the same organization as the same user returns
the same job ID. Use skills status to check a saved job ID or resume waiting
without uploading again.

```
chainctl skills harden [<path|uploads-ref>] --group <org> [flags]
```

### Examples

```
  chainctl skills harden --group my-org ./my-skill --wait --timeout 30m
  chainctl skills harden --folder ./my-skill --group my-org
  chainctl skills harden uploads.cgr.dev/my-org/my-skill:latest --group my-org --wait
  chainctl skills harden --digest sha256:<64-hex> --name my-skill --group my-org
  chainctl skills status --group my-org --id <job-id> --wait
```

### Options

```
      --digest string      SHA256 digest of an artifact already in the uploads registry.
      --folder string      Local skill directory containing SKILL.md.
  -g, --group string       Target organization name or UIDP (required).
      --name string        Uploaded skill name (required with --digest).
      --timeout duration   Maximum command duration with --wait (0 means no timeout).
      --wait               Wait for hardening to finish.
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

