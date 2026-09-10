---
title: "Reproducibility and Chainguard Containers"
linktitle: "Reproducibility"
description: "What makes a build reproducible, and how to rebuild any Chainguard Container from its signed apko configuration and confirm the result matches bit for bit"
type: "article"
date: 2024-05-20T12:21:01+00:00
lastmod: 2026-09-09T00:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 030
toc: true
aliases:
- /chainguard/chainguard-images/videos/repro/
- /chainguard/chainguard-images/staying-secure/repro/
- /chainguard/containers/videos/repro/
- /chainguard/containers/staying-secure/repro/
---

A build is reproducible when the same inputs produce the same output, bit for bit, regardless of who runs it and when they run it. Chainguard builds its containers with [apko](https://github.com/chainguard-dev/apko) from a declarative configuration, and publishes that configuration as a signed attestation on every build. You can retrieve the configuration, rebuild the container yourself, and check the digest you get against the one Chainguard published.

## What reproducibility requires

Reproducibility requires more than a build that succeeds twice. Binary identical means every byte matches, so a reproducible build has to control three things:

- **The versions of its inputs.** Not only source code, but every dependency, each pinned to an exact version.
- **The version of the build tooling.** The same inputs run through two versions of a build tool can produce two different results.
- **Anything that varies from run to run.** Timestamps and generated unique IDs are the most common causes. They change on every build, and they change the output along with them.

When a build meets those conditions, anyone can verify its output independently: rather than trusting that a container was built from the configuration it claims, you can rebuild it and compare the digests.

## Reproduce a Chainguard Container

You need [cosign](https://github.com/sigstore/cosign), [apko](https://github.com/chainguard-dev/apko), [crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane), `jq`, and a registry you can push to. cosign and apko are both distributed as signed binaries on their GitHub releases pages, and apko can also run from a container if you would rather not install it. The examples use `cgr.dev/chainguard/nginx`, one of Chainguard's [Free containers](/chainguard/containers/concepts/container-categories/#free-containers), so they run as written.

### Record the digest you want to match

```sh
crane digest cgr.dev/chainguard/nginx:latest
```

```output
sha256:<digest>
```

Chainguard moves the `latest` tag as it publishes rebuilds, so start by pinning down which build you're reproducing. The `<digest>` you get back is the value to match at the end; it differs from the one anyone else gets unless you both pull the same build. [Inspecting Chainguard Containers](/chainguard/containers/troubleshooting/inspecting-containers/) covers digests in more detail.

### Retrieve the build configuration

Every build carries its apko configuration as an attestation. The following command verifies that attestation and writes the configuration to a file:

```shell
cosign verify-attestation \
  --type https://apko.dev/image-configuration \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/nginx:latest | jq -r .payload | base64 -d | jq .predicate > latest.apko.json
```

The two certificate flags are what make that a verification. They tell cosign to accept the attestation only if it was signed by the GitHub Actions workflow that builds Chainguard's containers, using a certificate from that workflow's OIDC issuer. Without them you would be reading an attestation that is present, rather than one that is genuine. The rest of the pipeline unwraps the result: `jq -r .payload` takes the in-toto payload, `base64 -d` decodes it, and `jq .predicate` keeps the apko configuration itself.

Read the configuration back from the file that the configuration was piped into:

```shell
jq . latest.apko.json
```

The following shows this command's abridged output, highlighting a few fields worth calling out:

```json
{
  "contents": {
    "packages": [
      "ca-certificates-bundle=20260611-r1",
      "glibc-2.44-locale-posix=2.44-r6",
      "glibc-2.44=2.44-r6",
      "ld-linux-2.44=2.44-r6",
      "..."
    ],
    "repositories": [
      "https://apk.cgr.dev/chainguard"
    ]
  },
  "accounts": {
    "run-as": "65532",
    "users": [
      { "gid": 65532, "homedir": "/home/nginx", "uid": 65532, "username": "nginx" }
    ]
  },
  "archs": [ "amd64", "arm64" ],
  "entrypoint": { "command": "/usr/sbin/nginx" },
  "stop-signal": "SIGQUIT"
}
```

apko builds are declarative: the configuration names a list of APK packages and some metadata, and nothing more. Two details in it matter. Each package is pinned to an exact version, and the list is complete — `glibc` does not quietly pull in a dependency that the file doesn't name. Everything else in the file is metadata that the build applies to the finished container: the user account to run as, the architectures to build, the entrypoint, the stop signal.

### Rebuild and compare

Point apko at the configuration and give it somewhere to push:

```sh
apko publish latest.apko.json ttl.sh/nginx-repro
```

apko builds one image per architecture in the `archs` list, assembles them into an index, pushes the result, and prints the digest of what it pushed as its final line:

```output
ttl.sh/nginx-repro@sha256:<digest>
```

That digest is the same `<digest>` the first step recorded, which means the rebuild is byte-for-byte identical to the container Chainguard published. The registry it was pushed to has no bearing on the value: a digest covers the content, not where it lives.

To run apko from its container instead of installing it, mount the directory holding the configuration and pass the same arguments:

```shell
docker run --rm -v "$PWD":/work -w /work cgr.dev/chainguard/apko:latest publish latest.apko.json ttl.sh/nginx-repro
```

`apko publish` needs a registry to push to. These examples use [ttl.sh](https://ttl.sh), a free registry whose images expire after a short time, which suits a throwaway comparison. Any registry you can write to works.

### Compare images that don't match

When two digests differ, [diffoci](https://github.com/reproducible-containers/diffoci) reports the specific differences between the images rather than leaving you to compare two hashes:

```sh
diffoci diff cgr.dev/chainguard/nginx:latest ttl.sh/nginx-repro
```

When the images match, the command exits without reporting anything. When they differ, it lists the differing files and where they differ. Add `--ignore-timestamps` to set aside timestamp differences, or `--semantic` to ignore everything diffoci treats as non-substantive, including file ordering and redundant file mode bits.

## What limits reproducibility

Three factors can prevent an exact match, and each is worth understanding before concluding that a rebuild has failed.

- **The version of apko matters.** A change in how a build tool handles something as small as a symbolic link is enough to change a digest. Every Chainguard Container records the version that built it in its SLSA provenance attestation:

  ```shell
  cosign verify-attestation \
    --type https://slsa.dev/provenance/v1 \
    --certificate-oidc-issuer https://token.actions.githubusercontent.com \
    --certificate-identity https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
    cgr.dev/chainguard/nginx:latest | jq -r .payload | base64 -d | jq .predicate.runDetails.builder
  ```

  ```output
  {
    "id": "https://github.com/chainguard-dev/terraform-provider-apko",
    "version": {
      "apko": "v1.2.43",
      "terraform-provider-apko": "v1.2.20"
    }
  }
  ```

  If a rebuild produces a different digest, check that version first.

- **APKs cannot be rebuilt bit for bit from source.** You can build the packages themselves from source, and their contents match, but each APK embeds a signature made with Chainguard's private signing key. Without that key you cannot produce an identical package file.

- **The pinned package versions have to be available.** apko installs the exact versions the configuration names, so reproducing an old container depends on those versions still being served from the repository it points at.

## Correction to the video

The following video says that Chainguard keeps older package versions only for a short time, and that reproducing an older container therefore means holding your own copies of the APKs. That statement is not accurate. Chainguard retains every package version it has issued, so you can rebuild containers from months ago without arranging your own storage. Chainguard may age older versions out in the future to keep the package index manageable, and only the latest versions are serviced with fixes, but retention today is indefinite.

{{< youtube 0Qn2J89UEvI >}}

## Related reading

- [How to retrieve SBOMs and attestations for Chainguard Containers](/chainguard/containers/security-and-compliance/retrieve-image-sboms/) — the other attestation types published alongside the apko configuration, and how to fetch them.
- [Inspecting Chainguard Containers](/chainguard/containers/troubleshooting/inspecting-containers/) — identifying a build by digest, and reading the software versions inside it.
- [Verifying Chainguard Containers and metadata signatures with Cosign](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/) — verifying signatures and provenance more generally.
- [How Chainguard Containers are tested](/chainguard/containers/concepts/how-we-build-and-test/images-testing/) — what happens to a container before it's published.
