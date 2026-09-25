---
title: "Chainguard Libraries for Go overview"
linktitle: "Go overview"
description: "Go modules for your application development"
type: "article"
date: 2026-09-25T00:00:00+00:00
lastmod: 2026-09-25T00:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Go", "Overview"]
menu:
  docs:
    parent: "go"
weight: 051
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

- Your organization’s private Go modules, when private module uploads are enabled
- Chainguard-remediated module versions
- Eligible versions from the upstream Go module proxy, when upstream fallback is enabled

The `/go` endpoint is the endpoint you configure in `GOPROXY`. It uses the standard Go module proxy paths for version lists, metadata, `go.mod` files, and module source archives.
Go builds from source on the customer side. Unlike ecosystems that distribute prebuilt language artifacts, Chainguard Libraries for Go distributes module source archives. A CVE-remediated module is published as a distinct Go version rather than replacing the upstream bytes for the same version.

## CVE remediation

Chainguard Libraries for Go can provide backported fixes for high and critical CVEs in older module versions when upgrading to a newer upstream release is not practical.
Remediated Go versions use the `-cgr.N` prerelease suffix. For example: `v1.2.5-cgr.1`.

The suffix identifies a Chainguard-remediated source archive. Because `-cgr.N` versions are prereleases, Go’s minimal version selection and `@latest` do not select them automatically. Adopt a remediated version explicitly in `go.mod` or with a version-specific command such as:

```bash
go get example.com/module@v1.2.5-cgr.1
go mod tidy
go mod verify
```

Replace the module path and version with the remediated version available for your dependency.

## Private Go modules

Organizations with private module upload enabled can publish tagged module versions to an organization-scoped Go registry. Uploaded modules are resolved before remediated and upstream versions for that organization, while still subject to Chainguard security controls and organization policies.

Private uploads must use a canonical semantic version. The `-cgr.N` namespace is reserved for Chainguard-remediated versions and cannot be used for customer-uploaded versions.

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
