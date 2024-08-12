---
title: "How to Use Chainguard Security Advisories"
linktitle: "Using Advisories"
aliases: 
- /chainguard/chainguard-images/security-advisories
- /chainguard/chainguard-images/images-features/security-advisories
- /chainguard/chainguard-images/working-with-images/security-advisories/
type: "article"
description: "Article outlining how one can explore and use the Security Advisories found on the Chainguard Image Directory."
date: 2023-12-27T11:07:52+02:00
lastmod: 2023-12-27T11:07:52+02:00
draft: false
tags: ["Overview", "Product", "Chainguard Images", "CVE"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 010
toc: true
---

When you're checking to determine what vulnerabilities, if any, are present in a Chainguard Image, you may be using an image scanning tool like Grype or Docker Scout. Chainguard Images typically report few or zero CVEs, but when older versions of software are included in a given Image, a scanner may report more. Not all vulnerabilities are equal, and it may not be immediately clear whether a CVE found within a given Chainguard Image is likely to cause security issues in your software. Scanners can also misreport vulnerabilities found in Chainguard Images; they may return false positives that have, in reality, been fixed. 

To help demystify the nature of CVEs within Chainguard Images, we've created a self-service [Security Advisories page](https://images.chainguard.dev/security) that lists every security advisory published for Chainguard Images. Having this information available allows you to view whether Chainguard is aware of a specific vulnerability reported to exist within a Chainguard Image and whether we've mitigated or are planning to mitigate the CVE.

This guide outlines how you can use Chainguard's Security Advisories to learn more about the status of a CVE within a given package. It will walk through a practical example of discovering a vulnerability in a Chainguard Image, searching for Security Advisories associated with this vulnerability, and then comparing the original Image with a later version.


## Prerequisites

You don't need any special access or software to explore Chainguard's Security Advisories. However, this guide includes a few examples that use specific software tools in order to outline a practical example of how one might navigate and use the Security Advisories.

To follow along with these examples, you'll need the following tools installed.

* A security scanner like [Trivy](https://aquasecurity.github.io/trivy/v0.18.3/installation/), [Grype](https://github.com/anchore/grype#installation), or [Docker Scout](https://docs.docker.com/get-docker/) — This guide's examples use Docker Scout, a component of the Docker container platform, to scan container images and identify vulnerabilities. However, you should be able to follow along with any container vulnerability scanning tool.
* [`chainctl`](/chainguard/chainctl/) — Chainguard's command-line interface tool. To install `chainctl`, follow our [installation guide](/chainguard/administration/how-to-install-chainctl/). 
* [`jq`](https://jqlang.github.io/jq/) — `jq` is a command-line JSON processor that allows you to filter and manipulate streaming JSON data. Although it isn’t strictly necessary for the purposes of this guide, this tutorial includes commands that use `jq` to filter command output that would otherwise be difficult to read. You can install `jq` by following the instructions on [the project’s Download jq page](https://jqlang.github.io/jq/download/).


## So you've encountered a CVE in a Chainguard Image

Say you use a vulnerability scanner like Grype or Docker Scout to inspect a certain Chainguard Image. This example uses Docker Scout to scan a Chainguard Production Image, specifically one tagged with `1.21.2`.

As of this writing, the `go:1.21.2` image points to the image digest `sha256:04ab6905552b54a6977bed40a4105e9c95f78033e1cde67806259efc4beb959d`. Be aware that this tag will be withdrawn in the future, but the digest will remain available.

```sh
docker scout cves cgr.dev/chainguard-private/go:1.21.2
```

Because this is the digest for an older version of Chainguard's Go Image, this command's output will show a number of vulnerabilities that have been found to exist within this specific version of the Image. 

```
. . .

20 vulnerabilities found in 6 packages
  UNSPECIFIED  8  
  LOW      	1  
  MEDIUM   	3  
  HIGH     	6  
  CRITICAL 	2  
```

This output shows that this particular image has 20 vulnerabilities. The Docker Scout output also lists each of the packages affected by CVEs as well as the specific vulnerabilities it found for each.

> Note: All of these vulnerabilities have been addressed in newer versions of the Chainguard Go Image.

Scrolling to the listing immediately before the final vulnerability count, we'll find that in the case of this example, the package `nghttp2` is referenced. 

```
   0C 	1H 	0M 	0L 	1?  nghttp2 1.56.0-r0
pkg:apk/chainguard/nghttp2@1.56.0-r0?os_name=chainguard&os_version=rolling

	✗ HIGH CVE-2023-44487
  	https://scout.docker.com/v/CVE-2023-44487
  	Affected range : <1.57.0-r0  
  	Fixed version  : 1.57.0-r0   
    
	✗ UNSPECIFIED GHSA-qppj-fm5r-hxr3
  	https://scout.docker.com/v/GHSA-qppj-fm5r-hxr3
  	Affected range : <1.57.0-r0  
  	Fixed version  : 1.57.0-r0   
    
```

As of this writing, this lists one vulnerability associated with version `1.56.0` of `nghttp2` as being `HIGH` severity and one as `UNSPECIFIED`. We'll use the `HIGH` severity vulnerability listed here as an example when we explore Chainguard's Security Advisories in the next section.

Copy or note down the CVE identifier (`2023-44487` in this case). Additionally, note down the name of the affected package (`nghttp2`). You'll use these details to retrieve more information about the CVE shortly. 


## Searching the Security Advisories

After finding a vulnerability in a Chainguard Image, you can navigate to [Chainguard's **Security Advisories** page](https://images.chainguard.dev/security). This is a helpful resource you can use to determine the status for any CVE found within a Chainguard Image.

The Security Advisories page is self-service, allowing you to check whether Chainguard is aware of a specific vulnerability and whether it has been mitigated in a certain package version. You can search the Security Advisories page by entering any CVE identifier to find what packages are affected by that CVE. You can also enter the names of individual packages to find what CVEs have been reported within them.

Enter the CVE identifier you copied previously into the search box at the top of the page. This will immediately filter the list of security advisories to only show packages where that CVE has been reported. It will also show the **Status** of each.

![Screenshot showing the Chainguard Security Advisories page. The list of advisories has been filtered to only include those with a CVE ID of "CVE-2023-44487".](sec-adv-A.png)

If you click on any row in the filtered list, it will take you to the CVE's specific page. There, you'll find a list of every package where this CVE has been reported.

![Screenshot showing the Security Advisory page for CVE-2023-44487 and a partial list of its affected packages.](sec-adv-B.png)

As with the Security Advisories landing page, you can filter by package name here on the CVE's landing page as well. Enter the name of the package we highlighted previously (`nghttp2`) and the index will immediately filter out any packages that do not mention that string in their metadata.

![Screenshot showing a filtered list of packages affected by CVE-2023-44487, this time only showing packages that reference "nghttp2". The row for the nghttp2 package itself shows a "Status" of "Fixed", and a "Fixed Version" of "1.57.0-r0".](sec-adv-C.png)

As the previous screenshot highlights, for CVE-2023-44487, the `nghttp2` package's **Status** is marked as **Fixed** in version `1.57.0-r0` as of October 11, 2023.


## Comparing Images

Chainguard's Security Advisories have told us that the CVE-2023-44487 was fixed and removed from `nghttp2` with a more recent version than the one available in Chainguard's `go:1.21.2` Image. However, we don't have to take that report at face value; we can inspect a later version of the same Image and compare it with version `1.21.2` to determine whether the vulnerability is still present in the later version.

If you inspect a later version of the Image with Docker Scout, you'll find that this time it reports no CVEs. This example inspects version `1.21.5` of the Image.

```shell
docker scout cves cgr.dev/chainguard-private/go:1.21.5
```
```
## Overview

                	│         	Analyzed Image         	 
────────────────────┼─────────────────────────────────────────
  Target        	│  cgr.dev/chainguard-private/go:1.21.5   
	digest      	│  65008b35ef40                      	 
	platform    	│ linux/amd64                        	 
	vulnerabilities │	0C 	0H 	0M 	0L         	 
	size        	│ 232 MB                             	 
	packages    	│ 132                                	 


## Packages and Vulnerabilities

  No vulnerable packages detected
```

> Note: Version `1.21.5` was the current version of the Go Image at the time of this writing. It may have accumulated CVEs since this guide was published.

You can go a step further by comparing these two images directly with the `chainctl images diff` command, as in this example.

```sh
chainctl images diff \
cgr.dev/chainguard-private/go:1.21.2 \
cgr.dev/chainguard-private/go:1.21.5 | jq .
```

This example will return a lot of output, as there are significant differences from version `1.21.2` to `1.21.5` of the Go Image. If you scroll down to the `vulnerabilities` section of this output, you'll find a list of vulnerabilities that are present in version `1.21.2` but have been removed by version `1.21.5`.

```
  "vulnerabilities": {

. . .
  	
{
    	"id": "CVE-2023-44487",
    	"reference": "chainguard:distro:chainguard:rolling",
    	"severity": "High"
  	},

	. . .
```

As this output indicates, `CVE0223-44487` is no longer present in later versions of the Go Chainguard Image. If you were using version `1.21.2`, you should seriously consider upgrading to a later version.


## Learn More

The Security Advisories page serves as a helpful resource for anyone who wants to learn more about CVEs reported within Chainguard Images. You can search the database of advisories to learn more about any CVEs you encounter as you work with Chainguard Images.

Additionally, we encourage you to explore the [Chainguard Images Directory](https://images.chainguard.dev/), the parent site of the Security Advisories page. The Directory allows users to explore the complete inventory of Chainguard Images. You may also be interested in our guide on [How To Compare Chainguard Images with `chainctl`](/chainguard/chainguard-images/comparing-images/) to learn more about how you can use the Diff API to compare Chainguard Images. Finally, we encourage you to learn more about [noisy scan results](/chainguard/chainguard-images/scanners/false-results/) when scanning Chainguard Images. 
