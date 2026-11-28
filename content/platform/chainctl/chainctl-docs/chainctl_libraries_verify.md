---
date: 2026-11-27T13:55:02Z
title: "chainctl libraries verify"
slug: chainctl_libraries_verify
url: /platform/chainctl/chainctl-docs/chainctl_libraries_verify/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries verify

A tool to analyze the use of Chainguard Libraries in various artifacts

### Synopsis

verify analyzes various artifacts
(directories, archives, packages) to analyze how much was built from source by Chainguard,
based on SBOM data, signatures, and artifact inspection.

You can specify one or more paths to analyze multiple artifacts in a single command.

For container images, you can use:
  - Registry references (e.g., cgr.dev/chainguard/nginx:latest)
  - Local single-part images (e.g., redis:latest, nginx:alpine)
  - Docker archive format (docker-archive:/path/to/image.tar)
  - Local images with prefixes (localhost/myapp:latest)

JavaScript package manager caches (npm, pnpm, Yarn Classic) are auto-detected
in container images and local directories by their structure.

Passing a JavaScript lockfile (package-lock.json, npm-shrinkwrap.json,
pnpm-lock.yaml, yarn.lock, bun.lock) reports which of its registry entries carry
a digest covered by a Chainguard attestation, using the integrity hashes the
lockfile records. No install or package cache is required.

An entry counts as verified only when the attested digest is bound to the
tarball bytes the entry permits — that is, when any install honoring the entry's
integrity constraint must use the attested bytes. A lone integrity hash binds:
the package manager rejects any tarball that does not match it. An entry listing
several hashes does not, since any of them may be satisfied — those are reported
as attested but not bound, unless the resolved URL names the same package on
Chainguard's built route (libraries.cgr.dev/javascript/), which fixes the
source. The upstream proxy route serves upstream bytes and does not bind.

A lockfile rewritten by "libraries update-hashes" in its default append mode
keeps the original registry hash alongside the Chainguard one. Such entries
verify only while resolved points at the Chainguard built route, so behind a
private proxy or custom --registry-url they report as not bound. Use
"libraries update-hashes --replace" to record a single Chainguard hash per
entry, which binds regardless of where the entry resolves from.

No downloaded bytes are examined, and platform, optional dependencies, overrides,
and registry configuration still affect what a package manager selects. Entries
with no usable digest — linked and git dependencies, and Yarn Berry's non-SRI
checksums — are reported at zero coverage.

Entries the registry could not answer for — an outage, or rejected credentials —
are reported as unchecked rather than unverified, since a service problem is not
a provenance finding. Requests are retried before an entry is called unchecked.

This report is informational: the exit status does not reflect coverage. Coverage
counts entries Chainguard built from source, so a package that is simply not
built from source is not a defect, and gating a build on the percentage is not
the intended use. Per-entry results are available with "-o json --detailed".

A NuGet package (.nupkg) is verified by the Chainguard package signature it
carries: an author signature under Chainguard's code-signing certificate, with a
timestamp, made for that exact package. The check reads only the package, so it
needs no token and no network. A remote reference to a .nupkg (remote: or
jfrog:) is downloaded and then checked the same way, with no Chainguard token.
A jfrog: download reads its API key from ARTIFACT_API_KEY or, if that is unset,
JFROG_API_KEY. A directory of .nupkg files is checked the same way, package by
package, and so is a NuGet global packages folder (~/.nuget/packages, or any
folder with its layout). In a global packages folder, the .nupkg NuGet keeps for
each package is checked, and then the files NuGet extracted beside it are
compared with the package's contents. A file that is missing, changed, or not in
the package makes the package not verified. NuGet's own files (.nupkg.metadata
and the .sha512 hash) are not compared, and a nuspec or IntelliSense XML file
that the restore left out is not counted as missing. A package with no .nupkg
kept, such as one restored from a fallback folder, is reported as unchecked. A
folder that also holds other artifacts outside its package directories is
checked as a plain directory, so that every artifact in it is checked.

Passing a NuGet lockfile (packages.lock.json, or a per-project name such as
packages.MyApp.lock.json) reports which of its package entries are Chainguard packages. Every target
framework and runtime section is read, and project references are skipped. Each
entry's package is read from the NuGet global packages folder: the folder that
--packages-dir names, else NUGET_PACKAGES, else ~/.nuget/packages. A
globalPackagesFolder set in nuget.config is not read, so pass --packages-dir
for such a folder. Run dotnet restore first. An entry is verified when its
package is checked as in a global packages folder (above), and the package also
matches the entry's contentHash, the SHA-512 of the package without its
signature. NuGet refuses a restore whose package does not match the contentHash,
so the match ties the entry to the bytes whose signature verified. An entry
whose package is not in the folder is reported as unchecked, not unverified,
unless --fetch-missing is set. An entry with a malformed id, version or
contentHash is reported at zero coverage. Like a .nupkg, a lockfile needs no
token and no network, unless --fetch-missing or --output-attestations is set.
A lockfile written against nuget.org does not
match packages restored from the Chainguard feed, because the two builds have
different contentHash values, so regenerate the lockfile after switching feeds.

With --fetch-missing, verify fetches the package of each lockfile entry that is
not in the packages folder from the Chainguard feed, at
\<feed>/dotnet/v3/flatcontainer/\<id>/\<version>/\<id>.\<version>.nupkg, and checks
it: the package signature and timestamp, the nuspec id and version against the
entry, and the entry's contentHash. A fetched package has no extracted files to
compare, and its details say that it was fetched. Entries whose packages are in
the folder are still read from the folder. An entry that the feed does not
serve is reported as not verified. An entry that the feed could not answer for
is reported as unchecked. The fetch needs a token. If the registry rejects the
credentials, verify fetches nothing more, reports the entries it could not
fetch as unchecked, and reports the rejection after the results.

Passing a published .NET app's deps file (\<app>.deps.json), a directory that
holds one, or a container image reports which of the app's NuGet packages are
Chainguard packages. The deps file names each package, its version, the SHA-512
of the package (the lockfile's contentHash), and the package files the app
holds. The deps file alone is a claim, so the app's files are compared with the
package: a package is verified when its .nupkg carries a Chainguard package
signature, it matches the deps file's SHA-512, and every file the deps file
lists is in the app directory, byte for byte as the package has it. The .nupkg
is read from the NuGet global packages folder (as for a lockfile) when the
folder holds that exact package. A package that is not there is unchecked,
unless --fetch-missing fetches it from the Chainguard feed, as for a lockfile.
So a deps file, or a directory whose only artifacts are deps files and .nupkg
files, needs no token without --fetch-missing. An image has no packages folder,
so its packages are always fetched, which needs a token. A package the feed does
not serve is not a Chainguard package. A file that differs, as a ReadyToRun or
trimmed publish makes them, leaves the package not verified, with the reason
"modified at publish". A file that is missing from the app leaves the package
unchecked. Coverage counts packages, not files. The app's own assemblies, the
.NET runtime, and packages with no file in the app are listed but not counted. A
file that carries a Chainguard Authenticode signature gets a note, which does
not count toward coverage. In an image, each file is read from the top layer
that holds it, and a file that a later layer deletes counts as missing. A file
reached through a symbolic link is not checked in an image. The deps files of
the .NET installation itself, in its sdk, shared and packs directories, are not
checked, since they describe Microsoft's tools and frameworks rather than an
app. Single-file apps, whose deps file is inside the executable, are not
supported.

With --output-attestations, verify also checks the provenance that the
Chainguard feed serves for each NuGet package. The provenance is a signed
SLSA statement that names the SHA-256 of the .nupkg. This check needs a token.
Either the package signature or the provenance verifies a package. If the
registry rejects the credentials, a package whose signature verified stays
verified, but verify saves no files for it and reports the rejection after
the results.

Remediated (CVE-patched) Java artifacts, whose versions carry a "-0.cgr.\<rev>" suffix
(e.g. 3.5.0-0.cgr.2), are resolved from the java-remediated repository; other Java
artifacts are resolved from the java repository.

With --output-attestations, available SBOMs and attestations are saved under
each verified artifact's repository path in --output-dir, which defaults to
./attestations in the current directory. This works for Java, JavaScript,
Python wheels, and NuGet packages. A NuGet package's files go in
\<id>/\<version>/, both lowercase: the provenance that verified, and the SPDX
SBOM when the provenance names its SHA-256. Unsupported inputs produce no
companion files.

```
chainctl libraries verify [path...] [flags]
```

### Examples

```
  # Analyze a local JAR file
  chainctl libraries verify myapp.jar

  # Analyze multiple files
  chainctl libraries verify build/libs/*.jar build/libs/*.war

  # Analyze a local Python virtual environment
  chainctl libraries verify ./venv/

  # Analyze a NuGet package
  chainctl libraries verify Newtonsoft.Json.13.0.3.nupkg

  # Analyze the NuGet packages restored to the global packages folder
  chainctl libraries verify ~/.nuget/packages

  # Verify a NuGet lockfile against the packages restored for it
  dotnet restore
  chainctl libraries verify packages.lock.json

  # Verify a NuGet lockfile with no restore, fetching its packages from the
  # Chainguard feed
  chainctl libraries verify --fetch-missing --parent example.com packages.lock.json

  # Verify the NuGet packages in a published .NET app
  dotnet publish -o out
  chainctl libraries verify out/MyApp.deps.json

  # Verify the NuGet packages in a .NET app in a container image
  chainctl libraries verify --parent example.com registry.example.com/my-app:latest

  # Verify a NuGet package's provenance too, and save it with its SBOM
  chainctl libraries verify semver.3.0.0.nupkg --output-attestations

  # Analyze with JSON output
  chainctl libraries verify -o json build/libs/*.jar

  # Download available SBOMs and attestations alongside verification
  chainctl libraries verify commons-lang3-3.17.0.jar --output-attestations

  # Analyze container images
  chainctl libraries verify cgr.dev/chainguard/maven:latest

  # Analyze remote artifact
  chainctl libraries verify remote:example.com/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar

  # Analyze a NuGet package in a JFrog repository (reads ARTIFACT_API_KEY,
  # or JFROG_API_KEY if that is unset)
  chainctl libraries verify jfrog:example.jfrog.io/artifactory/nuget-remote/polysharp.1.15.0.nupkg

  # Verify a lockfile without installing anything
  chainctl libraries verify package-lock.json
  chainctl libraries verify pnpm-lock.yaml

  # Per-entry results for machine consumption
  chainctl libraries verify package-lock.json -o json --detailed

  # Verify npm cache (auto-detected by _cacache/index-v5/ structure). Ask npm
  # from your home directory: inside an untrusted project, its configuration
  # can choose which npm runs.
  chainctl libraries verify "$(cd ~ && npm config get cache)"

  # Verify pnpm store (auto-detected; supports pnpm 10+ index dirs and the
  # pnpm 11 SQLite index, and the versioned path reported by newer pnpm).
  # Ask pnpm from your home directory, as with npm.
  chainctl libraries verify "$(cd ~ && pnpm store path)"

  # Verify Yarn Classic (v1.x) cache
  chainctl libraries verify yarn:
  chainctl libraries verify yarn:~/Library/Caches/Yarn/v6
```

### Options

```
      --concurrency int         Number of artifacts verified in parallel: nested archives within a single input, or inputs across a multi-path run (0 = default of 16)
  -d, --detailed                Show detailed per-artifact results
      --ecosystems-url string   URL for the Ecosystems Proxy (defaults to https://libraries.cgr.dev)
      --fetch-missing           Fetch a package that a NuGet lockfile or .NET deps file lists but the packages folder lacks from the Chainguard feed, and check it; needs a token
      --no-color                Disable colored output
  -o, --output string           Output format (text, json, yaml) (default "text")
      --output-attestations     Download available SBOMs and attestations for verified artifacts into --output-dir; ignored for unsupported ecosystems
      --output-dir string       Base directory for files downloaded by --output-attestations, laid out under each artifact's repository path. No effect without --output-attestations (default "attestations")
      --packages-dir string     NuGet global packages folder a NuGet lockfile's or .NET deps file's packages are read from (defaults to NUGET_PACKAGES, else ~/.nuget/packages)
      --parent string           Parent organization for authentication
      --verbose                 Enable verbose output
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
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.

