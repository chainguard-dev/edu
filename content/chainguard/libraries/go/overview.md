---
title: "Chainguard Libraries for Go overview"
linktitle: "Go overview"
description: "Go modules for your application development"
type: "article"
date: 2026-09-25T00:00:00+00:00
lastmod: 2026-09-30T18:13:00+00:00
draft: false
tags: ["Chainguard Libraries", "Go", "Overview"]
menu:
  docs:
    parent: "go"
weight: 51
toc: true
---

Chainguard Libraries for Go provides enhanced security for the Go module ecosystem through an authenticated, secure-by-default Go module proxy. The proxy applies organization-defined policies, malware and greyware protections, cooldown controls, and CVE remediation to Go dependencies before they reach development and build environments.

Go modules support cloud-native infrastructure, high-volume services, fintech, networking, and security applications. Chainguard Libraries for Go helps reduce the risks of consuming modules from public sources, including malicious modules, typosquats, and vulnerabilities in versions your applications still need to use.

{{< beta feature="Chainguard Libraries for Go" enroll="true" >}}

## Runtime requirements

Go modules retrieved from Chainguard have the same module paths, APIs, and Go toolchain requirements as their corresponding upstream projects unless a remediated release explicitly documents otherwise. Your application’s existing go.mod remains the source of truth for module requirements.

## Technical details

You must use the username and password [retrieved with chainctl](/chainguard/libraries/introduction/access/) to access the Chainguard Libraries for Go repository.

The URL for the repository is: `https://libraries.cgr.dev/go/`.

When a Go command requests a module, Chainguard resolves the request through the sources enabled for your organization:

- Chainguard-remediated module versions
- Eligible versions from the upstream Go module proxy, when upstream fallback is enabled

The `/go` endpoint is the endpoint you configure in `GOPROXY`. It uses the standard Go module proxy paths for version lists, metadata, `go.mod` files, and module source archives.
Go builds from source on the customer side. Unlike ecosystems that distribute prebuilt language artifacts, Chainguard Libraries for Go distributes module source archives. A CVE-remediated module is published as a distinct Go version rather than replacing the upstream bytes for the same version.

## CVE remediation

Chainguard Libraries for Go can provide backported fixes for high and critical CVEs in older module versions when upgrading to a newer upstream release is not practical.

Remediated Go versions use the `-cgr.N` prerelease suffix. For example, a remediated build of upstream `v1.2.5` is `v1.2.5-cgr.1`.

The incremented patch number ensures that vulnerability scanners recognize the remediated version as newer than upstream `v1.2.5`, while the `-cgr1` suffix identifies it as  a Chainguard prerelease. A remediated version is a distinct module source archive; it does not replace the upsream bytes for another version.

The suffix identifies a Chainguard-remediated source archive. Because `-cgr.N` versions are prereleases, Go’s minimal version selection and `@latest` do not select them automatically. Use a [`replace` directive](https://go.dev/ref/mod#go-mod-file-replace) in `go.mod` to pin a dependency to its remediated version:

```bash
require example.com/module v1.2.5
replace example.com/module v1.2.5 => example.com/module v1.2.6-cgr1
```

This version-specific form replaces upstream v1.2.5 wherever it is selected, including as a transitive dependency. To force the remediated version regardless of the selected upstream version, omit the old version from the directive:

```bash
replace example.com/module => example.com/module v1.2.6-cgr1
```

Replace the module path and versions with the remediated version available for your dependency. After adding or updating a replace directive, run:

```bash
go mod tidy
go mod verify
```

You can also select the remediated version directly with `go get`, but use `replace` when you need a stable project-level pin:

```bash
go get example.com/module@v1.2.6-cgr1
go mod tidy
go mod verify
```

## Go checksum verification

Chainguard-remediated versions are not recorded in the public Go checksum database because they are not available from public upstream origins. Configure Go to skip public checksum verification for modules retrieved through Chainguard:

```bash
go env -w GONOSUMDB='*'
```

You can alternatively disable checksum database verification globally:

```bash
go env -w GOSUMDB=off
```

The Go module proxy remains authenticated over TLS, and `go.sum` continues to pin the module bytes after the first successful fetch.

Do not use `GOPRIVATE` for this configuration. `GOPRIVATE` also sets `GONOPROXY`, which causes Go to bypass Chainguard. `GONOSUMCHECK` is not a current Go configuration variable and should not be used.

## Upstream fallback

By default, Chainguard Libraries endpoints serve Chainguard-built modules. When [upstream fallback](/chainguard/libraries/introduction/#upstream-fallback-and-controls) is enabled for your organization, the Go endpoint can also serve eligible versions from the upstream Go module proxy under Chainguard security controls.

Upstream fallback can help you adopt Chainguard without waiting for every module and version to be rebuilt. It does not make Chainguard Libraries a complete mirror of the upstream registry. A module or version may be unavailable because it is not yet supported, is inside the cooldown window, or is blocked by Chainguard or your organization’s policies.

### View packages blocked due to malware

Chainguard’s source code and maintainer behavior scanning identifies and blocks malicious and greyware packages in Chainguard Libraries via the Chainguard Repository. You can get a list of blocked packages via chainctl or the API. Refer to the [Libraries Overview page](/chainguard/libraries/introduction/overview/#malware-and-greyware-detection) for more information.
