---
title: "Verifying Chainguard Agent Skills signatures"
date: 2026-10-09T23:38:36+00:00
lastmod: 2026-10-09T23:38:36+00:00
linktitle: "Verify skills"
description: "Check that Chainguard signed a published agent skill with chainctl skills verify, verify before you pull or install, or verify the signature yourself with Cosign."
type: "article"
draft: false
tags: ["Agent Skills", "Procedural", "Security", "Cosign", "chainctl"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 60
---

Chainguard signs every skill it publishes to `skills.cgr.dev`. The signature lets you confirm that a skill came from Chainguard's publishing pipeline and that nobody changed it after Chainguard signed it.

Chainguard signs each published skill as the SKILLS identity of the organization that owns it, and attaches the signature to the skill's digest as a [Sigstore](https://www.sigstore.dev/) bundle. The signature covers the skill's manifest digest, which covers everything in the artifact: the hardened skill files, the `HARDENING.md` report, and the skill's metadata. Chainguard signs only hardened, published skills. It doesn't sign the skills in your organization's uploads registry (`uploads.cgr.dev`).

`chainctl skills validate` doesn't check signatures. It checks that a local skill directory is formatted correctly, and a passing result says nothing about who published a skill. To check that Chainguard signed a skill, use `chainctl skills verify`, as described in this guide.

{{< beta feature="Chainguard Agent Skills" >}}

## Prerequisites

To follow this guide, you need:

* `chainctl` **v0.2.376** or later. Check your version with `chainctl version`. Refer to [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.
* To verify a skill from your own organization, the `viewer` role or higher on that organization. Skills in the `public` and `chainguard` organizations need no role.
* To verify with Cosign instead of `chainctl`, [Cosign](/open-source/sigstore/cosign/how-to-install-cosign/) **v3.1.1** or later. Earlier versions can't verify the transparency log entries Chainguard uses to sign skills.

## Verify a skill with `chainctl`

Pass a skill reference to the `verify` subcommand:

```shell
chainctl skills verify skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest
```

```output
   FIELD   |                                        VALUE
-----------|--------------------------------------------------------------------------------------
 Status    | verified
 Digest    | sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f
 Identity  | https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a
 Issuer    | https://issuer.enforce.dev
 Log Index | 141100935
```

`verify` accepts a reference by tag or by digest. It resolves a tag to a digest once, verifies that digest, and prints it, so you can pin the exact version you verified. To verify a pinned digest and get the result as JSON, add `-o json`:

```shell
chainctl skills verify skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine@sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f -o json
```

```output
{"status":"verified","digest":"sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f","issuer":"https://issuer.enforce.dev","identity":"https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a","logIndex":141100935}
```

For a skill in your organization's private registry, pass the hardened reference that `chainctl skills harden` or `chainctl skills status` returned:

```shell
chainctl skills verify "$HARDENED_REF"
```

The output has the same fields. The `Identity` is your organization's SKILLS identity rather than the `public` one, as described in [Chainguard's skill signing identities](#chainguards-skill-signing-identities).

### What `verify` checks

A skill is `verified` only when a Sigstore bundle attached to its digest passes all of these checks:

* The signing certificate chains to the public-good Sigstore trusted root.
* `https://issuer.enforce.dev` issued the certificate to exactly the SKILLS identity of the organization that owns the skill. No other identity is accepted, and you can't override the identity with a flag or setting.
* The bundle has a verified transparency log entry and a verified timestamp.
* The bundle signs the exact digest being checked.

`chainctl` has the signing identities of the `public` and `chainguard` organizations built in. For any other organization, it reads the organization's SKILLS identity with your credentials, which is why you need the `viewer` role or higher on that organization.

### Results and exit codes

`verify` reports one of four results in the `Status` field, or the `status` key of the JSON output:

| Status | Meaning | Exit code |
| ----- | ----- | ----- |
| `verified` | A bundle signed by the owning organization's SKILLS identity passed every check. | 0 |
| `unsigned` | The digest has no Sigstore bundle. | 1 |
| `failed` | The digest has a bundle, but none of its bundles passed. The `Reason` field explains why. Skills in `uploads.cgr.dev` always fail, because uploads are not Chainguard-signed. | 1 |
| `skipped` | The skill isn't on the production registry, `skills.cgr.dev`, so `chainctl` can't verify it. `verify` prints a warning. | 0 |

An error that stops verification from running, such as a skill that doesn't exist, also exits with a nonzero code.

## Verify before you pull or install

Add `--verify` to `chainctl skills pull` or `chainctl skills install` to check the signature on the exact digest that `chainctl` fetches before it writes anything to disk:

```shell
chainctl skills install --verify skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest
```

`chainctl` prints the verification result before it installs the skill. The following example output shows the results on a machine where Claude Code is present:

```output
Verified sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f: signed by https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a (log index 141100935)
Recorded skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine@sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f in skills-lock.json
Installing github.com/github/awesome-copilot/game-engine
    AGENT    |                              LOCATION                               |                                        MODE
-------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------
 Claude Code | .claude/skills/public-github.com-github-awesome-copilot-game-engine | symlink → ../../.agents/skills/public-github.com-github-awesome-copilot-game-engine
```

`pull` works the same way:

```shell
chainctl skills pull --verify skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest ./game-engine
```

```output
Verified sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f: signed by https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a (log index 141100935)
Skill written to: /home/linky/game-engine
```

If the skill isn't `verified`, the command exits with a nonzero code and writes no files or symlinks. `--verify` is stricter than `verify`: a `skipped` result fails too. With `-o json`, `pull` and `install` include the result that `chainctl skills verify -o json` prints in a `verification` field of their output.

`chainctl` reads its registry setting from configuration files and environment variables, including a `chainctl/config.yaml` in the current working directory. A project you clone could point `chainctl` at a registry other than `skills.cgr.dev`. Treating `skipped` as a failure keeps such a project from silently turning `--verify` off.

If you deliberately work with a staging or development registry, add `--allow-unverifiable-host` along with `--verify` to accept a skill from that registry unverified, with a warning. `--allow-unverifiable-host` has no effect on skills from `skills.cgr.dev`, and `chainctl` rejects it without `--verify`.

## Chainguard's skill signing identities

Chainguard signs each organization's skills as that organization's SKILLS identity. The certificate issuer is always `https://issuer.enforce.dev`, and the certificate identity is the issuer URL followed by the identity's UIDP:

| Organization | Certificate identity |
| ----- | ----- |
| `public` | `https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a` |
| `chainguard` | `https://issuer.enforce.dev/720909c9f5279097d847ad02a2f24ba8f59de36a/c09dd88a8a73ea84` |

To find the SKILLS identity of your own organization, read its account associations:

```shell
chainctl iam account-associations describe your-organization --chainguard -o json \
  | jq -r '.[0].chainguard.service_bindings.SKILLS'
```

The command prints the UIDP of your organization's SKILLS identity. For the `chainguard` organization, it prints the UIDP from the table above:

```output
720909c9f5279097d847ad02a2f24ba8f59de36a/c09dd88a8a73ea84
```

Prefix the UIDP with `https://issuer.enforce.dev/` to get the certificate identity. Reading account associations needs the `viewer` role or higher on the organization.

## Verify a skill with Cosign

`chainctl skills verify` is the simplest way to check a skill's signature. You can also check it yourself with Cosign, using the signing identities from the previous section.

### Public registry

Verifying a skill from the public registry needs no credentials:

```shell
cosign verify \
  --certificate-oidc-issuer=https://issuer.enforce.dev \
  --certificate-identity=https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a \
  skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine@sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f
```

```output
Verification for skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine@sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The code-signing certificate was verified using trusted certificate authority certificates

[{"critical":{"identity":{"docker-reference":"skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine@sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f"},"image":{"docker-manifest-digest":"sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f"},"type":"https://sigstore.dev/cosign/sign/v1"},"optional":{}}]
```

Get the digest of the version you want from `chainctl skills describe` or `chainctl skills verify`. Cosign also accepts a tag, but verifying by digest makes sure you check the exact version you go on to use.

### Private registry

Cosign needs credentials to pull from your organization's registry. Configure the Chainguard Docker credential helper, which Cosign also uses:

```shell
chainctl auth configure-docker
```

Then verify the skill with your organization's SKILLS identity, from the previous section, in place of `<skills-identity-uidp>`:

```shell
cosign verify \
  --certificate-oidc-issuer=https://issuer.enforce.dev \
  --certificate-identity=https://issuer.enforce.dev/<skills-identity-uidp> \
  "$HARDENED_REF"
```

`$HARDENED_REF` is the full hardened reference, including its digest, that `chainctl skills harden` or `chainctl skills status` returned.

{{< note >}}
Earlier instructions for verifying skills used `--new-bundle-format=false` and a `--certificate-identity-regexp` that matched Google Cloud service accounts. Those flags check an older signature format that Chainguard no longer relies on. Use the SKILLS identities on this page instead.
{{< /note >}}

## Attestations

Chainguard doesn't publish provenance attestations for skills yet. This guide will describe how to download and verify them once they're available.

## Learn more

* [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/)
* [Getting started with the Chainguard Agent Skills public registry](/chainguard/agent-skills/public-registry/)
* [Getting started with skill hardening](/chainguard/agent-skills/skill-hardening/)
* [`chainctl skills verify` reference](/platform/chainctl/chainctl-docs/chainctl_skills_verify/)
* [An introduction to Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/)
* [Verifying signatures in air-gapped environments](/open-source/sigstore/cosign/verifying-in-air-gapped-environments/)
