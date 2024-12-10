---
title: "Using wolfictl to Manage Security Advisories"
linktitle: "Managing Advisories"
aliases: 
type: "article"
description: "Guide on how to use the wolfictl tool to create, update, and manage security advisories"
date: 2024-08-05T20:23:51+00:00
lastmod: 2024-08-09T14:55:03+00:00
draft: false
tags: ["Overview", "Product", "Chainguard Images", "CVE"]
images: []
menu:
  docs:
    parent: "security-advisories"
weight: 030
toc: true
---

Chainguard operates its own [Security Advisories](https://images.chainguard.dev/security/?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-security-advisories-managing-advisories) page to alert users about the status of vulnerabilities found in Chainguard Images. To maintain this database, we use [`wolfictl`](https://github.com/wolfi-dev/wolfictl/), a tool developed for working with the [Wolfi un-distro](https://github.com/wolfi-dev/).

In this guide, you will walk through using `wolfictl` to create an advisory for a vulnerable package. You’ll also learn how to update this advisory as more information about the vulnerability is disclosed over time. To follow along, you will need to have [`git`](https://git-scm.com/) and the [Go programming language](https://go.dev/dl/) installed on your machine. 

This guide will focus on the packages and advisories issued for Wolfi.


## How to Install `wolfictl`

To work with security advisories, you will need to install the `wolfictl` tool onto your machine. First, execute the following command in your terminal to clone the `wolfictl` repository locally, and navigate to it. 

```sh
git clone git@github.com:wolfi-dev/wolfictl.git wolfictl && cd $_
```

Then, using `go`, install the `wolfictl` tool:

```sh
go install
```
If you encounter any errors during installation, your installed version of `go` may be out of date. You can check what version of `go` you have installed by running `go version` in your terminal. Check the [`go.mod` file](https://github.com/wolfi-dev/wolfictl/blob/main/go.mod) in the `wolfictl` repository to determine what version of `go` you will need, and be sure to update `go` to this version or a later release to continue. Alternatively, you may need to add the `wolfictl` binary to your `$PATH` after installation if your system does not recognize the command.

You can verify that you have successfully installed `wolfictl` by executing the `wolfictl version` command in your terminal.

```sh
wolfictl version
```
A successful installation of `wolfictl` will display output similar to the following. Note that the exact output will vary over time as new `wolfictl` versions are released. 

```Output
 __        __   ___    _       _____   ___    ____   _____   _
 \ \      / /  / _ \  | |     |  ___| |_ _|  / ___| |_   _| | |
  \ \ /\ / /  | | | | | |     | |_     | |  | |       | |   | |
   \ V  V /   | |_| | | |___  |  _|    | |  | |___    | |   | |___
    \_/\_/     \___/  |_____| |_|     |___|  \____|   |_|   |_____|
wolfictl: A CLI helper for developing Wolfi

GitVersion:    devel
GitCommit:     6c98dc69a559192575d085d87fd916d8281dd67d
GitTreeState:  clean
BuildDate:     2024-07-23T01:57:17
GoVersion:     go1.22.5
Compiler:      gc
Platform:      darwin/arm64
```

In the next section, you will complete your local setup so you can begin using the `wolfictl` tool to work with advisories.

## Cloning Package and Advisory Repositories

Before you can interact with security advisories, the  `wolfictl` tool will need access to existing Wolfi package and advisory information.

You will need to clone two additional repositories: the [`wolfi-dev/os`](https://github.com/wolfi-dev/os) repository and the [`wolfi-dev/advisories`](https://github.com/wolfi-dev/advisories) repository. Execute the following commands to clone each of these repositories to your machine and then navigate to the `advisories` directory.

```sh
git clone git@github.com:wolfi-dev/os.git 
git clone git@github.com:wolfi-dev/advisories.git && cd advisories
```

With `wolfictl` installed and these two repositories cloned locally, you are now ready to interact with the security advisory database.


## Viewing Existing Advisories

First we will take a look at the existing advisories issued for packages in Wolfi. Keep in mind that the results shown here, and on your own machine, are snapshots in time. You should regularly check for changes to the upstream repository as new packages and advisories are issued. 

You will be using the `wolfictl advisory list` command to view existing advisories. There are a variety of flags which you can append to assist in your search.
* `-p` lists all advisories for a given package name.
* `-V` lists all advisories for a given CVE ID, across all packages.
* `-t` lists all advisories by their most recent event type.
* `-c` lists all advisories by detected component type.
* `--history` reports the full list of events for displayed advisories.

You can combine multiple flags together to conduct a more granular search. For a complete listing of available command options, you can run the `wolfictl advisory list -h` command in your terminal.

For example, let’s say you want to find advisories for the `glibc` package as well as the full history of these advisories. 

```sh
wolfictl advisory list -p glibc --history
```

The following shows a small sample of output from this command at the time of this writing. Note that the output of this command may change as vulnerability entries are added and updated over time.
```Output
glibc CGA-49g3-q5cv-7m6g (CVE-2023-4527, GHSA-hmf7-f8gf-8f4p)    2023-09-22T14:14:01Z fixed (2.38-r2)
      CGA-573p-mg38-75fh (CVE-2019-1010024, GHSA-3q29-89cr-qgvj) 2023-03-06T13:22:06Z false positive (vulnerability-record-analysis-contested)
      CGA-57wh-hj4x-5342 (CVE-2023-4911, GHSA-m77w-6vjw-wh2f)    2023-10-03T22:58:32Z fixed (2.38-r5)
      CGA-5vfg-gqch-hcj5 (CVE-2010-4756, GHSA-x2r9-jfjp-jvp9)    2023-03-06T17:47:28Z false positive (vulnerability-record-analysis-contested)
                                                                 2024-07-26T16:49:42Z fixed (2.40-r0)
      CGA-7fr2-v9gg-pg28 (CVE-2024-33600, GHSA-jv3g-6pg3-v9j8)   2024-05-14T11:00:51Z detected (glibc)
                                                                 2024-05-15T04:40:16Z fixed (2.39-r5)
…
```

From this snapshot, you can get an idea of the timeline of a vulnerability’s remediation process. For example, CVE-2024-33600 was detected on May 14th, 2024, and was remediated within the next 24 hours. Similar results are shown for other advisories, including the versions of the package in which the vulnerability was remediated.

We encourage you to experiment with these flags to find what information you can gather from your various searches.

## Creating and Updating Advisories

To begin creating and updating security advisories, you will need to navigate back to the Wolfi package repository you cloned.

```sh
cd ../os 
```

Here, you will run the `wolfictl advisory create` command to begin the process of adding a new advisory. This command will respond with a few prompts in the terminal requesting input of information used to create the advisory.

First, you will be asked to enter the package in which the CVE was found. For this demonstration we will use the `glibc` package. Then, you will be asked for the vulnerability ID that you wish to make an advisory for. This ID must be a CVE, CGA, GHSA, or Go vulnerability ID. Finally, you will be asked what the status for the advisory should be, from one of the following options:
- `detection` (Under investigation)
- `true-positive-determination` (Affected)
- `fixed` (Fixed)
- `false-positive-determination` (Not affected)
- `fix-not-planned` (Fix not planned)
- `pending-upstream-fix` (Pending upstream fix)

To learn more about the meanings of each of these identifiers, please refer to our [documentation on event types](https://github.com/wolfi-dev/advisories/blob/main/docs/event_types.md). The following shows an example of the `wolfictl advisory create` command in action. **Please note that the vulnerability referenced is an arbitrary CVE ID for demonstration purposes and does not reflect an actual vulnerability found in the `glibc` package.**

```sh
Auto-detected distro: Wolfi

Package: glibc 
Vulnerability: CVE-2024-57230 
Type: 
  detection
```

You can now check that your advisory has been successfully added with the `wolfictl advisory diff` command, as follows:

```sh
wolfictl advisory diff
```

From this command, you can see the local addition of your new advisory for the `glibc` package.

```Output
Auto-detected distro: Wolfi

( - removed / ~ modified / + added )

~ document "glibc"
  + advisory "CGA-pwm8-5rj4-phww"
```

Let’s say that you upgrade a vulnerable package to a newer, patched version. You are now ready to update the security advisory so its status is now “Fixed”. You can do so using the `wolfictl advisory update` command. Again, this command will walk you through the steps of updating an advisory by requesting information about the advisory you wish to modify. The following shows an example of this workflow in action.

```sh
Auto-detected distro: Wolfi

Package: glibc 
Vulnerability: CVE-2024-57230
Type: 
  fixed
Fixed Version: 2.39-r7 
```

The same process can be followed for other status updates, whether you wish to mark a vulnerability as “Not affected” in the case of a [false positive finding](/chainguard/chainguard-images/recommended-practices/false-results/), “Fix not planned”, or another applicable status. 

## Further Reading

In this guide, you learned how to use the `wolfictl` tool to interact with Chainguard’s Security Advisories feed. You used `wolfictl` to explore existing advisories, and also created and updated a new security advisory. The steps shown in this guide allowed you to make local changes to your advisory feed. If you wish to contribute to the open-source Wolfi OS advisory feed, please read through our [How To Patch CVEs](
https://github.com/wolfi-dev/os/blob/main/HOW_TO_PATCH_CVES.md) guide and our [How Chainguard Issues Security Advisories](/chainguard/chainguard-images/working-with-images/security-advisories/how-chainguard-issues/) article first.

Be sure to routinely check [our Security Advisories page](https://images.chainguard.dev/security/?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-security-advisories-managing-advisories) when your scanners pick up new CVEs in your images. If you want to learn more about how you can interpret a security advisory and what its status means for your security, read our [article on using advisories](/chainguard/chainguard-images/working-with-images/security-advisories/how-to-use/). 

We also have a video walkthrough showing how to use the [Security Advisories page and `chainctl diff` API](/chainguard/chainguard-images/videos/security_advisories/).
