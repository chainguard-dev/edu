---
title: "Browsing Chainguard Libraries"
linktitle: "Browsing"
description: "Searching, browsing, and inspecting Chainguard Libraries in the console"
type: "article"
date: 2025-07-03T14:00:00+00:00
lastmod: 2026-07-28T15:05:15+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 007
toc: true
---

Chainguard Libraries includes thousands of libraries and many more individual
library versions and artifacts. In the Chainguard Console, you can
browse all available libraries and their versions, and inspect their
characteristics before using them in your application development.

## Access libraries in the Chainguard Console

Log in to the Chainguard Console at
[https://console.chainguard.dev/](https://console.chainguard.dev/).

In the left-hand navigation under **Libraries**, expand **Ecosystems** to find
links for browsing Chainguard's [**Java**](/chainguard/libraries/java/overview/), [**JavaScript**](/chainguard/libraries/javascript/overview/), and [**Python**](/chainguard/libraries/python/overview/) libraries.

<a id="initial-display"></a>

### Browse the libraries list

When you open a specific ecosystem, you'll see a search input box and a list of
libraries. Click any row to open the [library detail page](#library-page).

The list includes the following columns:

* **Name**: The full library name, excluding any version identifiers.
    * Python library names are simple strings, such as `setuptools` or
  `Flask-Admin`.
    * Java library names are the concatenation of the Maven
  coordinate values `groupId` and `artifactId`, separated by `:`. Examples are
  `org.springframework:spring-core` or `org.eclipse.jetty:jetty-http`.
* **Latest version**: The latest released and available version of the library
  and the total number of available versions.
* **Updated**: The most recent date when any version of this library was built
and published by Chainguard, or cached from the upstream fallback (when upstream fallback is enabled).

At the bottom of the page, see a total count of available libraries.

#### Upstream fallback details

The upstream fallback is available for JavaScript, Python, and Java Libraries. The upstream fallback can be enabled or disabled using the `chainctl libraries entitlements` commands, per ecosystem. Currently, the Chainguard Console can be used to enable, disable, and view the status of the upstream fallback for JavaScript only. At the top of the JavaScript page in the Console, you can see whether [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) is enabled.

Learn more in the [Libraries Overview documentation](/chainguard/libraries/overview/#upstream-fallback-and-controls).

When fallback is configured for your organization, you will see all JavaScript packages -- including those built by Chainguard and those that are mirrored from upstream npm -- in the Console. For a given package, you can see whether it is being served from Chainguard's rebuilt artifacts or proxied from upstream npm. For Java and Python, you cannot currently view upstream vs. Chainguard-built packages via the Chainguard Console.

<a id="search"></a>

### Search the libraries list

Use the **Search** text input at the top of the libraries list to
narrow down the list and to locate a specific library.

Click into a row to view a [specific library page](#library-page).

<a id="library-page"></a>

### View remediated libraries

[CVE remediation](/chainguard/libraries/cve-remediation/) is available for a
subset of Chainguard Libraries for Python and Java. You can view remediated libraries in
the Chainguard Console.

In the Python and Java libraries directories, click the **Remediated** tab to view a list
of remediated libraries. Click into a library to see which versions have
remediated CVEs.

While viewing the list of remediated versions for a library, click into a
version to view more details: which CVEs were remediated, the date that the
version was patched, and links to additional resources.

Learn more about browsing remediations in [CVE remediation for Chainguard
Libraries](/chainguard/libraries/cve-remediation/#about-cve-remediation).

### View malware information

For the JavaScript and Python ecosystems, click the **Malware** tab to learn how many packages have been blocked by Chainguard due to malware or greyware detection.

The list at the bottom of the page displays all blocked packages, including the package name, blocked version, the date it was blocked on, its MAL ID if available, and signals detected.

#### Malware and greyware signal categories

Some categories describe confirmed malicious behavior, while others describe greyware or supply-chain risk indicators that may justify blocking even when there is no public malware advisory. Categories include:

* `Suspicious network activity`: The package contains unusual network behavior, such as unexpected outbound connections, obfuscated endpoints, or references to uncommon network destinations. This can indicate an attempt to contact attacker-controlled infrastructure or fetch additional payloads at runtime.
* `Data exfiltration`: The package appears to send sensitive data out of the environment, such as credentials, environment variables, or other local information. This signal is intended for packages that look like they are collecting data and transmitting it elsewhere.
* `Malicious install script`: The package includes install-time behavior that goes beyond normal setup work, such as opening network connections, spawning subprocesses, or writing outside the package directory. Because install scripts run automatically during dependency installation, malicious behavior here is especially risky.
* `Suspicious execution technique`: The package uses execution patterns that are commonly associated with malicious behavior, such as dynamic code loading, evasion, persistence, destructive actions, or hidden runtime execution paths. These techniques do not always prove intent on their own, but they are strong indicators that the package deserves scrutiny.
* `Contacts known-malicious infrastructure`: The package references or attempts to contact infrastructure already associated with known malicious activity, such as command-and-control hosts or campaign-linked domains. This signal indicates overlap with infrastructure that has already been identified as hostile.
* `Accesses credentials`: The package appears to read or target credentials, secrets, wallet keys, SSH material, or other sensitive authentication data. This signal is meant to capture behavior consistent with credential harvesting or unauthorized secret access.
* `Obfuscated or hidden payload`: The package contains code or content that appears intentionally hidden, encoded, encrypted, staged, or otherwise difficult to inspect. Obfuscation alone is not the attack, but it is a common technique used to conceal malicious behavior or payload delivery.
* `AI/LLM attack content`: The package includes content that appears designed to manipulate, evade, or attack AI or LLM-based systems. This can include prompt injection or other inputs intended to influence downstream AI behavior in unsafe ways.
* `Contains an exposed secret`: The package includes a secret that should not be present in published source or package contents, such as an API key or token. Exposed secrets create immediate risk because they may allow unauthorized access even if the rest of the package is not overtly malicious.
* `Spreads to other packages (worm)`: The package shows signs of self-propagation or attempts to copy itself into other packages or projects. This behavior is characteristic of worm-like malware that tries to spread automatically across ecosystems or environments.
* `Embedded binary in source`: The source package contains a prebuilt binary or executable content where source-based review would normally be expected. This can be a sign that opaque or modified code was inserted into the package outside normal source review paths.
* `Typosquatting or impersonation`: The package name appears designed to mimic a legitimate or well-known package so that users install it by mistake. This category is used for package impersonation tactics, including close spelling variants, homoglyph tricks, or cross-ecosystem naming collisions.
* `Dependency confusion`: The package appears related to a dependency confusion pattern, where an internal or expected dependency name is claimed in a public ecosystem and can be resolved unintentionally. This can allow attacker-controlled packages to be installed in place of the intended dependency.
* `Signs of maintainer account compromise`: The package shows anomalies suggesting that a maintainer or publisher account may have been taken over or is behaving inconsistently with its normal history. Examples include unexpected maintainer changes, spoofed identities, or unusual publisher-domain behavior.
* `Cryptomining`: The package appears to perform or enable unauthorized cryptocurrency mining. This kind of behavior can consume system resources, increase operational cost, and indicate broader malicious intent.
* `Linked to known malware`: The package shares indicators with malware that is already known, such as campaign markers, shared attacker infrastructure, or dependency links to confirmed malicious packages. This category highlights packages that are connected to existing malicious activity even if the exact payload differs.
* `No trusted provenance or signed release`: The package release cannot be tied back to trusted provenance, a verifiable source repository, or a signed release path. This does not prove maliciousness, but it weakens confidence that the published artifact matches a trustworthy source.
* `Published with a legacy token (not OIDC)`: The package was published using an older token-based workflow instead of a more modern trusted publishing flow such as OIDC. This can increase the risk of credential theft, token misuse, or less-auditable release practices.
* `Declares install scripts`: The package declares lifecycle or install scripts that execute automatically during installation. Many legitimate packages use these scripts, but they expand the attack surface and deserve additional scrutiny because they run code at install time.
* `Weak build-pipeline security`: The project’s release or CI/CD workflow shows signs of weak build security, such as unpinned actions, risky workflow settings, or insecure runner choices. These issues increase the chance that a legitimate project could be compromised during the build or publishing process.
* `Release integrity anomaly`: The release shows signs that the published artifact, tag, checksum, or release metadata may not line up cleanly with the expected source history. This points to possible tampering, silent replacement, or other integrity issues in the release process.
* `Anomalous release change`: The release changed in ways that stand out from the project’s normal history, such as sudden dependency additions, rapid republishing, or unusual version behavior. These anomalies do not automatically mean malware, but they can be signals of elevated supply-chain risk.
* `Anomalous package contents`: The contents of the package differ sharply from previous releases, such as unusual file growth, unexpected bundled material, or other abnormal content changes. This category helps flag packages whose contents changed in ways that merit inspection.
* `Untrusted dependency source`: The package depends on code from sources that are harder to verify or control, such as direct Git URLs instead of standard registry-managed releases. This increases supply-chain risk because the dependency may bypass the normal trust and review path.

## Library page

To access a library page, click on the row for a specific library in the search
results or the [initial library list](#initial-display).

On a library's page, use the search bar at the top to search for specific
versions.

The list of library versions includes the following columns:

* **Version** - the version of the library. Library versions are strings.
  Depending on the ecosystem and library they can follow naming patterns and
  other restrictions that allow ordering by version.
* **Size** - the size of the library.
    * The displayed size reflects the primary file(s) only: `.jar`/`.pom` for
      Java, and `.whl`/`.tar.gz` for Python. It is not an aggregation of all
      files under a given version.
* **Built** - The date when this version was built and published by Chainguard.

Click on the column titles to change the **sort** order of the list.

## View repository configuration in the Chainguard Console

The Chainguard Console provides visibility into your repository configuration and the packages being served. When the upstream fallback is configured for your organization, you will see all packages including those built by Chainguard and those that are mirrored from upstream npm.

## Other resources

* [Chainguard Console](/platform/console/): Learn about using the Chainguard Console to browse container images.
* [Libraries Overview](/chainguard/libraries/overview/): Learn about criteria for building a library, upstream fallback and policy controls, and more.
