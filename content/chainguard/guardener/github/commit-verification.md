---
title: "Chainguard Guardener Commit Verification"
linktitle: "Commit Verification"
description: "Configure Chainguard Guardener to verify that every commit in a pull request is cryptographically signed by an authorized signer."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
draft: false
tags: ["GitHub", "Security"]
images: []
aliases:
- /chainguard/guardener/commit-verification/
menu:
  docs:
    parent: "guardener-github"
weight: 040
toc: true
---

The Commit Verification feature verifies that every commit in a pull request is cryptographically signed by an authorized signer, according to a policy you control. This ensures that changes to your codebase come from identities you trust, and it supports both keyless (Sigstore) signatures and static keys such as GPG.

Keyless commit signatures are verified using [gitsign](https://github.com/sigstore/gitsign) and [Sigstore](/open-source/sigstore/). Static key authorities (such as GPG) are verified directly against the key material you supply, without gitsign.

## Enable Commit Verification

Add a `.chainguard/source.yaml` file to your repository that defines one or more **authorities**. A commit is accepted if it satisfies **any** of the listed authorities.

```yaml
spec:
  authorities:
    - keyless:
        url: https://fulcio.sigstore.dev
        identities:
          - subjectRegExp: .+@example.com$
            issuer: https://accounts.google.com
      ctlog:
        url: https://rekor.sigstore.dev
```

The example above accepts commits signed with keyless Sigstore signatures where the signer's identity is an `@example.com` address authenticated through Google.

## Keyless (Sigstore) authorities

A `keyless` authority verifies short-lived certificates issued by a Sigstore certificate authority (Fulcio) and logged in a transparency log (Rekor). Use `identities` to constrain which signer identities are trusted. The fields in the example above are:

- `keyless.url` — the Fulcio instance that issued the signing certificate.
- `keyless.identities` — one or more identity constraints. Each entry matches the certificate's subject and issuer.
    - `subjectRegExp` — a regular expression the signer's subject (for example, an email address) must match. Use `subject` for an exact match instead.
    - `issuer` — the OIDC issuer that authenticated the signer (for example, `https://accounts.google.com`). Use `issuerRegExp` for a pattern match.
- `ctlog.url` — the transparency log (Rekor) instance used to verify the signature was logged.

## Static key authorities

A `key` authority verifies signatures made with a static key, such as GPG. This is useful for accepting commits signed by well-known keys — for example, GitHub's own `web-flow` key used when merging in the web UI:

```yaml
spec:
  authorities:
    - key:
        kms: https://github.com/web-flow.gpg
```

<!-- TODO: Confirm the full set of static-key source options (inline key material, file paths, KMS references) and document them here. -->

## Combining authorities

Because a commit is accepted if it satisfies any authority, you can allow several trusted sources at once. The following policy accepts commits signed either by an `@example.com` Sigstore identity or by GitHub's `web-flow` key:

```yaml
spec:
  authorities:
    - keyless:
        url: https://fulcio.sigstore.dev
        identities:
          - subjectRegExp: .+@example.com$
            issuer: https://accounts.google.com
      ctlog:
        url: https://rekor.sigstore.dev
    - key:
        kms: https://github.com/web-flow.gpg
```

## Configuration reference

| Field                                                   | Purpose                                                                    |
| ------------------------------------------------------- | -------------------------------------------------------------------------- |
| `spec.authorities`                                      | List of authorities. A commit is accepted if it satisfies any one of them. |
| `spec.authorities[].keyless.url`                        | Fulcio instance that issued the signing certificate.                       |
| `spec.authorities[].keyless.identities[].subjectRegExp` | Regular expression the signer's subject must match.                        |
| `spec.authorities[].keyless.identities[].issuer`        | OIDC issuer that authenticated the signer.                                 |
| `spec.authorities[].ctlog.url`                          | Transparency log (Rekor) instance used to verify the signature.            |
| `spec.authorities[].key.kms`                            | Reference to a static key (for example, GPG) used to verify signatures.    |

<!-- TODO: Confirm whether verification is reported as a non-blocking check or a required/blocking check, and how failures surface on the pull request. Document the behavior here. -->

## Next steps

- **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommend and migrate GitHub Actions to hardened, SHA-pinned equivalents.
- **[Configuration](/chainguard/guardener/configuration/)** — Review the shared `.chainguard/` configuration model.
- Learn more about the signing technology behind this feature in the [Sigstore documentation](/open-source/sigstore/).
