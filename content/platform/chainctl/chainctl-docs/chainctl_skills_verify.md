---
date: 2026-10-08T18:22:10Z
title: "chainctl skills verify"
slug: chainctl_skills_verify
url: /platform/chainctl/chainctl-docs/chainctl_skills_verify/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills verify

Verify that Chainguard signed a published skill.

### Synopsis

Verify that Chainguard's publishing pipeline signed a published skill for the
organization that owns it.

The reference accepts org/name:tag or org/name@sha256:DIGEST. A tag is resolved
once and the digest is verified; the output prints that digest so you can pin
it.

Verification passes only when a sigstore bundle attached to the digest chains
to the public-good Sigstore trusted root, was issued by
https://issuer.enforce.dev to exactly the owning organization's SKILLS service
principal, and has a verified transparency-log entry and timestamp. The
signing identity of Chainguard's own organizations (public, chainguard) is
built into chainctl; for any other organization, chainctl reads its SKILLS
binding with your credentials, which requires the viewer role (or higher) on
that organization.

The result is one of: verified, unsigned, failed, or skipped. Skills on a
staging or development registry are skipped with a warning; uploads are never
Chainguard-signed and always fail. The command exits 0 for verified and
skipped, and 1 for unsigned and failed (the status field tells them apart);
an error that stops verification from running also exits nonzero.

```
chainctl skills verify <ref> [flags]
```

### Examples

```
  # Verify the latest version of a skill:
  chainctl skills verify chainguard/github/lint

  # Verify a pinned digest and print the result as JSON:
  chainctl skills verify chainguard/github/lint@sha256:<digest> -o json
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

