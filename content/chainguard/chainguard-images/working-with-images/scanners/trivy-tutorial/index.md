---
title: "Using Trivy to Scan Container Images for Vulnerabilities"
type: "article"
linktitle: "trivy-tutorial"
aliases: 
- /chainguard/chainguard-images/working-with-images/scanners/trivy-tutorial
description: "Learn to use Trivy to analyze images and other software artifacts"
date: 2024-06-06:20:00+02:00
lastmod: 2024-06-06:20:00+00:00
tags: ["Conceptual", "CVE"]
draft: false
images: []
menu:
  docs:
    parent: "scanners"
weight: 100
toc: true
---

[Trivy](https://github.com/aquasecurity/trivy) is a vulnerability scanner for a wide variety of software artifacts and deployments. Trivy is written in the Go programming language and is maintained by [Aqua Security](https://www.aquasec.com/). Trivy targets container images, VMs, filesystems, remote GitHub repositories, and Kubernetes and Amazon Web Services deployments. The tool can be used to detect known vulnerabilities (CVEs), generate SBOMs, analyze licenses, and scan for misconfigurations and exposed secrets.

## Installation

### Container Image

Container images for Trivy are hosted on a variety of registries. When running Trivy as a container image, it is recommended to mount a cache directory as a volume. For scanning container images, it is also recommended to mount `docker.sock`. 

Thefollowing command will pull Trivy from Docker Hub, mount the two volumes, run the Trivy container, and use the running container to scan the official nginx image on Docker Hub:

```bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $HOME/Library/Caches:/root/.cache/ \
  aquasec/trivy:0.52.2 \
  image nginx
```

### Binary Installation

Aqua Security provides an [installation script for Trivy](https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh). To install Trivy with the script, change the `/usr/local/bin` argument to the desired installation location on your path before running the following command:

```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.52.2
```

On many system configurations, you may need to provide elevated permissions via `sudo`:

```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin v0.52.2
```

You can also manually install Trivy by downloading the binary for your operating system and architecture from the [Trivy releases page](https://github.com/aquasecurity/trivy/releases/tag/v0.52.2) and manually placing the biary on your path.

### Package Managers

For Homebrew, use:

```bash
brew install trivy
```
Aqua Security [maintains sources and packages for a variety of additional operating systems and distributions](https://aquasecurity.github.io/trivy/v0.52/getting-started/installation#install-using-package-manage) on their installation page.

## Basic Usage

Throughout this tutorial, we'll use the `trivy` command to run Trivy. If you're running Trivy as a container image, replace this command with the [appropriate `docker run` command](#container-image).

To use Trivy, provide a subcommand indicating the type of artifact or deployment to be scanned along with the location of the target. For example, to scan the official Python image on Docker Hub:

```bash
trivy image python
```

Trivy will output a series of informational messages, a short summary of CVEs found, including severity, and an itemized list of CVEs. 

### Valid Targets

Trivy can scan a wide variety of artifacts, collections, or deployments, collectively called targets. Each type of software artifact has a specific set of Trivy scanners enabled by default. For example, when scanning container images, Trivy will look for vulnerabilities and exposed secrets by default.

### Scanning a Container Image

To scan a container image on Docker Hub, use the `image` subcommand and the name of the image as an  argument:

```bash
trivy image nginx
```

For images on other registries:

```bash
trivy image cgr.dev/chainguard/nginx:latest
```

#### Scanning a Filesystem

Trivy can recursively scan directories on a local machine.. To run a filesystem scan, run:

```bash
trivy fs <path>
```

where `<path>` indicates the root folder where the scan will begin. Trivy looks out for specific files containing lists of packages, such as Python's `requirements.txt` or `poetry.lock`, PHP's `composer.lock`, or Node's `package-lock.json`.

The following creates a Python project folder with virtual environment, installs a set of older packages, generates a `requirements.txt` file itemizing all transitive dependencies, and scans the project folder using Trivy:

```
mkdir python-project && cd python-project
python -m venv venv
./venv/bin/pip install WTForms==2.3.3 Werkzeug==2.0.1
./venv/bin/pip freeze > requirements.txt
trivy fs .
```
The following creates a default Node project, installs an older package with `npm`, and scans the project with Trivy:

```bash
mkdir node_project && cd node_project
npm init -y
npm install qs@6.5.2
trivy fs .
```

You should see a summary and itemized list of CVEs for the outdated Node package.

#### Scanning Clusters

To scan a Kubernetes cluster:

```bash
trivy k8s --report summary <cluster-name>
```

To try out the above command on a test Kubernetes cluster, First install [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation), a utility allowing Kubernetes to be run on your local machine.

Once Kind is installed and accessible on your path, run the following to create a cluster:

```bash
kind create cluster --name test-cluster
```

Run the following to scan the new cluster with Trivy:

```bash
trivy k8s --report summary kind-test-cluster
```

When scanning clusters, requesting only summary output is recommended, as tables in more verbose output may not display correctly.

### Scanning SBOMs

Trivy can both generate and scan SBOMs.

{{< details "What is an SBOM?" >}}
{{< blurb/sbom >}}
{{< /details >}}

First, generate an SBOM file in CycloneDX format to scan

```bash
trivy image -f cyclonedx -o results.cdx.json nginx
```

Trivy can scan this generated CycloneDX SBOM with the following:

```bash
trivy sbom results.cdx.json
```

Read more on SBOMs and other output formats in the section on [specifying output formats](#specifying-output-formats).

## Scanners

### Specifying Scanners

Trivy can scan not only for known vulnerabilities, but also for misconfigurations, exposed secrets, and license risks. When scanning container images or filesystems, Trivy scans for vulnerabilities and exposed secrets by default.

Individual scanners can be selected by passing a comma-separated list after the `--scanners` flag. To add a misconfigurations scan to an analysis of a container image:

```bash
trivy image --scanners vuln,misconfig,secret nginx
```

To recursively scan only for exposed secrets on a filesystem, starting at the current working directory:

```bash
trivy fs --scanners secret .
```

### License Scanning

Trivy provides an opinionated license scan that flags license clauses that may pose a business risk. To perform a license scan on a container image:

```
trivy image --scanners license nginx
```

By default, the Trivy license scan only looks at packages installed by managers such as `apt` or `apk`. To scan other files, add the `--license-full` flag:

```bash
trivy image --scanners license --license-full nginx
```
Using the `--license-full`flag will also show results for "loose" licenses, such as those provided as text files in project folders.

## Output Formats and Verbosity

### Specifying Output Formats

Trivy allows output in JSON, SARIF, CycloneDX, SPDX, SPDX-JSON, and GitHub formats. If no output or format flags are specified, Trivy first prints a series of informative messages and warnings to `stderr` and then prints a table of results to `stdout`.

The `-q` or `--quiet` flag suppresses the logging output normally printed to `stderr`. The following returns just the line summarizing the number and severity of issues:

```bash
trivy image -q nginx | grep Total:
```

```
Total: 173 (UNKNOWN: 2, LOW: 88, MEDIUM: 59, HIGH: 22, CRITICAL: 2)

```

The `-f` or `--format` flag specifies the output format, and the `-o` or `--output` flag specifies an output file. The following writes a JSON-formatted report to a `results.json` file.

```bash
trivy image -f json -o results.json nginx
```
Similarly, the following would write a report in CycloneDX format:

```bash
trivy image -f sarif -o results.sarif nginx
```
Other formats can be generated by passing the appropriate format type with the `-f` or `--format` flag.

### Generating SBOMs

The CycloneDX, SPDX, and SPDX-JSON output formats are considered SBOMs, and can be scanned with the `trivy sbom` subcommand. The following command will generate an SBOM in CycloneDX format:

```bash
trivy image -f cyclonedx -o results.cdx.json nginx
```

By default, the `sbom` subcommand scans only for vulnerabilities.., but license scanning can be enabled using the `--scanners license` flag.

### Generating a Report from a Template

Trivy can generate reports in additional formats from user-contributed templates. To use templates, first clone the Trivy GitHub repository to your home folder:

```bash
git clone https://github.com/aquasecurity/trivy.git
```
To generate a report using the HTML template, specify the path to the template in the cloned repository:

```bash
trivy image --format template --template ,@.trivy/contrib/html.tpl" -o report.html nginx
```

This HTML output can be significantly more readable than Trivy's default table output:

![Screenshot of rendered HTML generated by the Trivy HTML template](trivy-html-report.png)

Other template-based output formats can be browsed in the [Trivy contrib directory](https://github.com/aquasecurity/trivy/tree/main/contrib).

## Trivy Resources

- [Trivy Documenation](https://aquasecurity.github.io/trivy/latest)
- [TrivyOperator for Kubernetes](https://github.com/aquasecurity/trivy-operator)
- [Trivy Announcements](https://github.com/aquasecurity/trivy/discussions/categories/announcements)






