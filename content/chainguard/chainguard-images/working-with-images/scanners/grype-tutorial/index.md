---
title: "Using the grype Container Scanner"
type: "article"
linktitle: "grype-tutorial"
aliases: 
- /chainguard/chainguard-images/working-with-images/scanners/grype-tutorial
description: "Learn to use grype to detect CVEs in images"
date: 2024-06-06:08:00+02:00
lastmod: 2024-06-06:08:00+00:00
tags: ["Conceptual", "CVE"]
draft: false
images: []
menu:
  docs:
    parent: "scanners"
weight: 100
toc: true
---

[grype](https://github.com/anchore/grype) is a vulnerability scanner for container images and filesystems developed and maintained by [Anchore](https://anchore.com/) and written in the Go programming language. grype can scan from Docker, OCI, Singularity, podman, image archives, and local directory. grype supports a variety of SBOM formats for faster scanning, and grype's [vulnerability database](https://github.com/anchore/grype-db) draws from a wide variety of sources, including [Wolfi SecDB]( https://pkg.go.dev/github.com/wolfi-dev/wolfictl/pkg/advisory/secdb),

grype is appropriate for one-off detection for manual CVE mitigation and in automated use in CI pipelines. Chainguard maintains a [low-to-no CVE Chainguard Image for grype](https://edu.chainguard.dev/chainguard/chainguard-images/reference/grype/) based on our lightweight Wolfi distribution.

## Installation

### Container Images

grype is readily available as a container image. To pull the low-to-no-CVE Chainguard Image for grype and perform a scan on the official Docker nginx image, run the following:

```bash
docker run -it cgr.dev/chainguard/grype nginx
```

Alternatively, you can scan using the official grype Docker image:

```
docker run -it anchore/grype:latest nginx
```

### Binary Installation

To install grype as a binary, find and download the appropriate package file or binary from the [official releases page](https://github.com/anchore/grype/releases). Place the binary on your system path or install the package using the conventions for your OS and distribution.

grype can also be [built from source](https://github.com/anchore/grype/blob/main/DEVELOPING.md#native-development).

### Install via Package Manager

grype can be installed using the following commands specific to your OS and distribution: 

#### Homebrew

```
brew tap anchore/grype
brew install grype
```

#### Chocolatey

```
choco install grype -y
```

## Basic Usage

Throughout this tutorial, we'll use the `grype` command to run grype. If you're running grype as an image, replace this command with the appropriate `docker run` command, such as `docker run -it cgr.dev/chainguard/grype`.

To run grype on an image in a Docker or OCI registry, pass the image name as an argument:

```bash
grype nginx
```

```bash
grype cgr.dev/chainguard/nginx
```

To scan an image stored to `.tar`, pas the path to the archive file as an argument:

```bash
docker pull cgr.dev/chainguard/nginx
docker save cgr.dev/chainguard/nginx > nginx_chainguard_image.tar.gz
grype nginx_chainguard_image.tar.gz
```

grype can scan local directories, such as Python virtual environment (venv) or `node_modules` folders.


```bash
python -m venv venv
./venv/bin/pip install WTForms==2.3.3 Werkzeug==2.0.1
grype venv
```

```bash
mkdir node_project && cd node_project
npm init -y
npm install qs@6.5.2
grype .
```

### Comprehending Grype Output

By default, grype output is divided into two sections, a summary of information on the scanned artifact and an itemized list of CVE.

 In this section, we'll use an alpine version of the official Python image as an example. Since we're specifying a version, you may encounter more CVE when following the examples than are shown here, as CVE will accumulate over time.

Scan the image with the following command:

```bash
grype python:3.10.14-alpine3.20
```

You should receive output similar to the following:

```
 ✔ Vulnerability DB                [no update av
 ✔ Parsed image                    sha256:f48490
 ✔ Cataloged contents              09feb83998b9d
   ├── ✔ Packages                        [47 pac
   │     └── ⠹ Linux kernel cataloger          
   ├── ✔ File digests                    [659 fi
   ├── ✔ File metadata                   [659 lo
   └── ✔ Executables                     [144 ex
 ✔ Scanned for vulnerabilities     [10 vulnerabi
   ├── by severity: 0 critical, 1 high, 8 medium
   └── by status:   7 fixed, 3 not-fixed, 0 igno
NAME           INSTALLED   FIXED-IN    TYPE    VULNERABILITY        SEVERITY 
busybox        1.36.1-r28  1.36.1-r29  apk     CVE-2023-42365       Medium    
busybox        1.36.1-r28  1.36.1-r29  apk     CVE-2023-42364       Medium    
busybox-binsh  1.36.1-r28  1.36.1-r29  apk     CVE-2023-42365       Medium    
busybox-binsh  1.36.1-r28  1.36.1-r29  apk     CVE-2023-42364       Medium    
pip            23.0.1      23.3        python  GHSA-mq26-g339-26xf  Medium    
python         3.10.14                 binary  CVE-2023-36632       High      
python         3.10.14                 binary  CVE-2023-27043       Medium    
python         3.10.14                 binary  CVE-2024-4030        Unknown   
ssl_client     1.36.1-r28  1.36.1-r29  apk     CVE-2023-42365       Medium    
ssl_client     1.36.1-r28  1.36.1-r29  apk     CVE-2023-42364       Medium
```

### Interpreting the Summary

In the initial portion of its results output, grype summarizes information on the scanned artifact and gives an overview of known vulnerabilities. In the case of a scanned image, the output includes the image digest, a unique hash of the image that can be used as an identifier. 

Overview output includes the number of packages, files, and executables found in the artifact. Generally speaking, CVE are detected against packages, but the number of executables detected can also give you an idea of the attack surface of the scanned image or filesystem.

Finally, this portion gives a count of the number of CVE detected by severity and fixed status. Severity categorization sorts CVE into four categories based on the Common Vulnerability Scoring System (CVSS).

{{< details "What is CVSS??" >}}
{{< blurb/cvss >}}
{{< /details >}}

In our output, we can see that we have 0 critical, 1 high, and 8 medium CVEs:

```
   ├── by severity: 0 critical, 1 high, 8 medium, 0 low, 0 negligible 
```
grype also counts the number of CVE by fixed status. If a CVE is marked as fixed, it can be resolved by updating to a newer version of the package. Our output suggests that 7 packages have been fixed and can be remediated with updates:

```
   └── by status:   7 fixed, 3 not-fixed, 0 ignored 
```
### Itemized CVEs

In addition to the summary, grype provides an itemized list of CVE. By default, these are in table format, and list the pakage name, current version, the package type (such as apt, apk, binary), and severity. If the package is fixed, grype will also indicate the version of the fix.

grype writes itemized CVE to stdout, so the report of itemized CVE can easily be redirected to a file:

```bash
grype python:3.10.14-alpine3.20 > report.txt
```
Alternately, you can use the `--file` flag to write to a file:


```bash
grype --file report.txt python:3.10.14-alpine3.20
```

Redirecting output can also be useful to suppress a long list of CVE so that the summary can more easily be viewed.

### Output Formats

Itemized CVEs can be written to a number of formats, including the XML- or JSON-based [cyclonedx](https://cyclonedx.org/) SBOM standard and the [SARIF](https://sarifweb.azurewebsites.net/) static analysis format. To maximize the information provided by grype, it is recommended to use the JSON output type:

```bash
 grype -o json python:3.10.14-alpine3.20 > report.json
```

When using these more detailed formats, grype provides additional useful fields, such as the data source of the CVE, URLs to information on the CVE, advisories, related vulnerabilities, and details on how the vulnerability was detected.

Additional output formats are available as Hugo templates. These include output templates for HTML and CSV, and a [full list](https://github.com/anchore/grype/tree/main/templates) can be found at the grype GitHub repository.

To generate a HTML file of the itemized CVEs, first clone the grype repository from GitHub, then provide the path to the template file in your grype command:

```bash
git clone git@github.com:anchore/grype.git ~/.grype
grype -o template -t ~/.grype/templates/html.tmpl python:3.10.14-alpine3.20 > report.html
```
![Screenshot of rendered HTML generated by the included grype HTML template](grype_html_output.png)

To generate a CSV:

```bash
git clone git@github.com:anchore/grype.git ~/.grype
grype -o template -t ~/.grype/templates/csv.tmpl python:3.10.14-alpine3.20 > report.csv
```

### Scanning from SBOMs

## grype Explain




## grype API
