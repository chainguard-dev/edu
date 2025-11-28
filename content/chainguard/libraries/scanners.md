---
title: "Vulnerability Scanners and Chainguard Libraries"
linktitle: "Vulnerability Scanners"
description: "Details for using vulnerability scanners with Chainguard Libraries."
type: "article"
date: 2025-10-04T12:00:00+00:00
lastmod: 2025-10-04T12:00:00+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 006
toc: true
---

Vulnerability scanners enable you to understand the potential security risks
from libraries used within your applications.

Chainguard Libraries provides a trusted source for libraries typically
downloaded from public repositories. Chainguard Libraries are rebuilt from the
upstream open source project code repository content only. This prevents malware
without published source code and reduces almost all risk for software supply
chain attacks. In addition, some library versions are available with CVE fixes
applied. These fixes are backported from newer versions of the open source
project by Chainguard to create new libraries of older versions containing these
newer changes. Find more details in [CVE
Remediation](/chainguard/libraries/cve-remediation/).

This article provides an overview of vulnerability scanning for libraries and
the use of specific scanning applications in the following sections. For more
information on scanning containers, refer to our guide on [Working with
Container Image
Scanners](/chainguard/chainguard-images/staying-secure/working-with-scanners/).

## Vulnerability Scanning

Vulnerability scanning can be performed at various stages throughout the
software development lifecycle. Scanning earlier in the process helps identify
and remediate issues before they reach production environments. Common scenarios
for scanning include:

- **Before libraries enter the organization:** Scan dependencies as they are
  added to repository managers, developer machines, or during initial CI runs.
- **During application development:** Scan libraries and dependencies on the
  developer machine to catch vulnerabilities early.
- **At build time:** Scan application binaries, such as tarballs or other
  deployment artifacts, during the build process on the developer machine or any
  CI infrastructure.
- **During container image creation:** Scan container images as they are built
  to ensure included libraries are secure.
- **In container registries:** Scan images stored in registries before
  deployment to production.
- **During deployment:** Scan running applications or containers to detect
  vulnerabilities in the deployed environment.

Scanners can be used in different ways depending on the workflow:

- **Standalone CLI tools:** Run scans manually or as part of scripts.
- **Integration with repository managers:** Automatically scan dependencies as
  they are added or updated.
- **Integration with build tools:** Incorporate scanning into build pipelines
  for continuous security checks.
- **IDE integrations:** Many vulnerability scanners offer plugins or extensions
  for popular integrated development environments (IDE). These integrations
  allow developers to scan dependencies and code for vulnerabilities directly
  within their development workflow, providing immediate feedback and helping to
  remediate issues early in the process.
- **Other integrations:** Use scanners with CI/CD platforms, deployment tools,
  or monitoring systems.

Selecting the appropriate scanning approach and timing helps maintain a secure
software supply chain and reduces the risk of introducing vulnerabilities.

All the preceding considerations for vulnerability scanning apply when scanning
for Chainguard Libraries. Different vulnerability scanners offer varying
features, capabilities, and integration options for detecting vulnerabilities in
these libraries. Details about how specific scanners work with Chainguard
Libraries are provided in the following sections.

## Grype

[Grype](https://github.com/anchore/grype) supports detection of remediated
Chainguard Libraries starting with Grype **version 0.100.0**. You can use Grype
in multiple ways:

- Scan the Python virtual environment directly. If your Python application is
  not containerized, this is recommended.
- Alternatively, scan the container image for your Python application. Grype
  detects and accounts for remediated library versions inside the image.

When scanning a Python project source directory that contains a dependency file
such as `requirements.txt`, Grype reports against the declared versions rather
than the installed versions. As a result, Chainguard’s remediated Python package
versions are not recognized in this mode. To ensure accurate results, we
recommend scanning the installed environment, such as a Python virtual
environment directory, instead. 

For example, the entry `werkzeug==3.0.2` in the `requirements.txt` file results
in the use of the local version `werkzeug==3.0.2+cg4.1` that includes the
remediation for the CVE. This is apparent in the log output from `pip install`:

```output
Collecting werkzeug==3.0.2 (from -r requirements.txt (line 11))
  Downloading https://repo.example.com:8443/repository/python-all-remediated/packages/werkzeug/3.0.2%2Bcgr.1/werkzeug-3.0.2%2Bcgr.1-py3-none-any.whl (236 kB)
...
Installing collected packages: MarkupSafe, werkzeug
Successfully installed MarkupSafe-3.0.3 werkzeug-3.0.2+cgr.1
```

Use the following command to scan the project directory and, accordingly, the
`requirements.txt` file content:

```shell
grype .
```

The resulting output shows entries for both versions, including the high
severity vulnerability that is fixed in `3.0.2+cgr.1`:

```output
NAME      INSTALLED    FIXED IN  TYPE    VULNERABILITY        SEVERITY  EPSS           RISK
werkzeug  3.0.2        3.0.6     python  GHSA-q34m-jh98-gwm2  Medium    0.9% (74th)    0.5
werkzeug  3.0.2+cgr.1  3.0.6     python  GHSA-q34m-jh98-gwm2  Medium    0.9% (74th)    0.5
werkzeug  3.0.2        3.0.3     python  GHSA-2g68-c3qc-8985  High      0.2% (43rd)    0.2
werkzeug  3.0.2        3.0.6     python  GHSA-f9vj-2wh5-fj8j  Medium    < 0.1% (19th)  < 0.1
werkzeug  3.0.2+cgr.1  3.0.6     python  GHSA-f9vj-2wh5-fj8j  Medium    < 0.1% (19th)  < 0.1
```

Scan the virtual environment in the `venv` directory instead:

```shell
grype venv
```

The output only shows entries for `3.0.2+cgr.1`, the version that is actually
used. The output indicates that the high vulnerability `GHSA-2g68-c3qc-8985` is
no longer applicable:

```output
NAME      INSTALLED    FIXED IN  TYPE    VULNERABILITY        SEVERITY  EPSS           RISK
werkzeug  3.0.2+cgr.1  3.0.6     python  GHSA-q34m-jh98-gwm2  Medium    0.9% (74th)    0.5
werkzeug  3.0.2+cgr.1  3.0.6     python  GHSA-f9vj-2wh5-fj8j  Medium    < 0.1% (19th)  < 0.1
```

For additional guidance for Grype users, refer to our guide [Using Grype
to Scan Software
Artifacts](/chainguard/chainguard-images/staying-secure/working-with-scanners/grype-tutorial/)
and the [official documentation](https://github.com/anchore/grype).

## Anchore Enterprise

Anchore Enterprise supports the detection of remediated Chainguard Libraries starting with **version 5.23.0**, once the required configuration is applied.

To ensure remediated CVEs are filtered out by default, disable CPE matching for the ecosystem in which you are using Chainguard Libraries. Instructions for disabling CPE matching are available in the [Anchore documentation](https://docs.anchore.com/current/docs/vulnerability_management/).

This limitation is planned to be resolved in Anchore Enterprise v5.24.0.

## Trivy

[Trivy](https://github.com/aquasecurity/trivy) versions 0.54 and newer support
detection of remediated Chainguard Libraries after applying necessary
configuration.

Use the experimental VEX Repo feature of Trivy with the [VEX feed for Chainguard
Libraries](/chainguard/libraries/cve-remediation/#vex). Configure the Chainguard
VEX feed locally:

```shell
trivy vex repo init
```

The command logs the path to the created configuration file:

```output
INFO [vex] The default repository config has been created  file_path="~/.trivy/vex/repository.yaml"
```

The default configuration includes only the feed from the makers of Trivy, Aqua
Security:

```yaml
repositories:
  - name: default
    url: https://github.com/aquasecurity/vexhub
    enabled: true
    username: ""
    password: ""
    token: ""
```

Add the Chainguard feed to the top of the repository list:

```yaml
repositories:
  - name: chainguard-libraries
    url: https://libraries.cgr.dev/openvex/v1
    enabled: true
  - name: default
    url: https://github.com/aquasecurity/vexhub
    enabled: true
    username: ""
    password: ""
    token: ""
```

Run a scan with the Trivy CLI by explicitly specifying the `--vex repo` flag.
Use the `--show-suppressed` flag to show which CVEs have been resolved by
Chainguard:

```shell
trivy filesystem . --vex repo --show-suppressed
```

Running the command on a Python project managed with `pip` and a dependency
declaration in `requirements.txt` of `werkzeug==3.0.2+cgr.1` shows the
suppressed vulnerability `CVE-2024-340691`:

```output
Suppressed Vulnerabilities (Total: 1)

┌──────────┬────────────────┬──────────┬────────┬───────────┬────────────────────────────────────────┐
│ Library  │ Vulnerability  │ Severity │ Status │ Statement │                 Source                 │
├──────────┼────────────────┼──────────┼────────┼───────────┼────────────────────────────────────────┤
│ werkzeug │ CVE-2024-34069 │ HIGH     │ fixed  │ N/A       │ VEX Repository: chainguard-libraries   │
│          │                │          │        │           │ (https://libraries.cgr.dev/openvex/v1) │
└──────────┴────────────────┴──────────┴────────┴───────────┴────────────────────────────────────────┘
```

Note that using the definition `werkzeug==3.0.2` without the local version
qualifier in `requirements.txt` causes Trivy to wrongly assume the use of that
specific version and therefore reports an invalid vulnerability.

For additional guidance for Trivy users, refer to our guide [Using Trivy to Scan
Software
Artifacts](/chainguard/chainguard-images/staying-secure/working-with-scanners/trivy-tutorial/)
as well as the [official documentation](https://trivy.dev/docs/latest/).

## AWS Inspector

Chainguard Libraries for Python is now supported by Amazon Inspector’s enhanced scanning for Amazon ECR. This integration brings high-impact CVE remediation directly into your AWS vulnerability management workflows. Refer to the [AWS docs](https://docs.aws.amazon.com/inspector/latest/user/supported.html#:~:text=Supported%20programming%20languages%3A%20Amazon%20ECR%20scanning) for additional details.
