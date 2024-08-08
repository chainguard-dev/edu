---
title: "Using wolfictl to Manage Security Advisories"
linktitle: "Managing Advisories"
aliases: 
type: "article"
description: "Guide on how to use the wolfictl tool to create, update, and manage security advisories"
date: 2024-08-05T20:23:51+00:00
lastmod: 2024-08-05T20:23:51+00:00
draft: false
tags: ["Overview", "Product", "Chainguard Images", "CVE"]
images: []
menu:
  docs:
    parent: "security-advisories"
weight: 030
toc: true
---

Chainguard operates its own [Security Advisories](https://images.chainguard.dev/security/) page to alert users about the status of vulnerabilities found in Chainguard Images. To maintain this database, we use [`wolfictl`](https://github.com/wolfi-dev/wolfictl/), a tool developed for working with the [Wolfi un-distro](https://github.com/wolfi-dev/).

In this guide, we will walk through using `wolfictl` to create an advisory for a vulnerable package. We’ll also learn how to update this advisory as more information about the vulnerability is disclosed over time. To follow along, you will need to have [`git`](https://git-scm.com/) and the [Go programming language](https://go.dev/dl/) installed on your machine. 

This guide will focus on the packages and advisories issued for Wolfi.


## How to Install `wolfictl`

To work with security advisories, you will need to install the `wolfictl` tool onto your machine. First, execute the following command in your terminal to clone the `wolfictl` repository locally, and navigate to it. 

```shell
git clone git@github.com:wolfi-dev/wolfictl.git wolfictl && cd $_
```

Then, using `go`, install the `wolfictl` command:

```shell
go install
```
If you encounter any errors during installation, your installed version of `go` may be out of date. You can check what version of go you have installed by running `go version` in your terminal. Check the [`go.mod` file](https://github.com/wolfi-dev/wolfictl/blob/main/go.mod) in the `wolfictl` repository to determine what version of `go` you will need, and be sure to update `go` to this version or a later release to continue. Alternatively, you may need to add the `wolfictl` binary to your `$PATH` after installation if your system does not recognize the command.

You can verify that you have successfully installed `wolfictl` by executing the `wolfictl version` command in your terminal, with output expected to be shown as follows. Note that the exact output will vary over time as new `wolfictl` versions are released. 

```shell
wolfictl version
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


## Cloning Package and Advisory Repositories

You will need to clone a couple more repositories to continue: the `wolfi-dev/packages` repository and the `wolfi-dev/advisories` repository. Enter the following commands in your terminal to clone each of these repositories. We will also navigate to the `advisories` repository after cloning it.

```shell
git clone git@github.com:wolfi-dev/os.git 
```

```shell
git clone git@github.com:wolfi-dev/advisories.git && cd advisories
```


## Viewing Existing Advisories

Before we add to the database, we will take a look at the existing advisories issued for packages in Wolfi. Keep in mind that the results shown here, and on your own machine, are snapshots in time. You should regularly check for changes to the upstream repository as new packages and advisories are issued. 

We will be using the `wolfi advisory list` command to view existing advisories. There are a variety of flags which we can append to assist in our search.
* `-p` lists all advisories for a given package name.
* `-V` lists all advisories for a given CVE ID, across all packages.
* `-t` lists all advisories by their most recent event type.
* `-c` lists all advisories by detected component type.
* `--history` reports the full list of events for displayed advisories.

Multiple flags can be combined together to produce a more granular search. For a full listing of available flags, you can run the `wolfictl advisory list -h` command in your terminal.

For example, let’s say you want to find advisories for the `glibc` package, and we want to see the full history of these advisories. Note that the output of this command may change as vulnerability entries are added and updated over time.

```shell
wolfictl advisory list -p glibc
```

The following shows a small sample of output from this command at the time of this writing. Note that the output of this command may change as vulnerability entries are added and updated over time.
```
…
CGA-pjj8-8gh5-2qwh (CVE-2024-33599, GHSA-9gvm-vcgf-x5xw)   2024-05-14T11:00:49Z detected (glibc)
                                                                 2024-05-15T04:39:53Z fixed (2.39-r5)
      CGA-7fr2-v9gg-pg28 (CVE-2024-33600, GHSA-jv3g-6pg3-v9j8)   2024-05-14T11:00:51Z detected (glibc)
                                                                 2024-05-15T04:40:16Z fixed (2.39-r5)
      CGA-vjpp-g2r4-c8gc (CVE-2024-33601, GHSA-f4cf-2w52-c853)   2024-05-14T11:00:53Z detected (glibc)
                                                                 2024-05-15T04:40:32Z fixed (2.39-r5)
      CGA-wfxf-8642-f6f5 (CVE-2024-33602, GHSA-f4pv-q5f7-2h55)   2024-05-14T11:00:56Z detected (glibc)
                                                                 2024-05-15T04:40:42Z fixed (2.39-r5)

…
```

From this snapshot, we can get an idea of the timeline of a vulnerability’s remediation process. The first CVE displayed, CVE-2024-33599, was detected on 5/14/2023 and remediated within the next 24 hours. Similar results are shown for other advisories, including the versions of the package in which the vulnerability was remediated.

We encourage you to experiment with these flags to find what information you can gather from your various searches.

## Creating and Updating Advisories

To begin creating and updating security advisories, we will need to navigate back to the package repository we cloned.

```shell
cd ../os 
```

Here, we will run the `wolfictl advisory create` command to begin the process of adding a new advisory. This command will respond with a few prompts in the terminal requesting input of information used to create the advisory.

First, we will be asked to enter the package in which the CVE was found. For our demonstration we will use the `glibc` package. Then, we will be asked for the vulnerability ID that we wish to make an advisory for. This ID must be a CVE, CGA, GHSA, or Go vulnerability ID. Finally, we will be asked what the status for the advisory should be, from one of the following options:
- detection (Under investigation)
- true-positive-determination (Affected)
- fixed (Fixed)
- false-positive-determination (Not affected)
- fix-not-planned (Fix not planned)
- pending-upstream-fix (Pending upstream fix)

To learn more about the meanings of each of these identifiers, please refer to our [documentation on event types](https://github.com/wolfi-dev/advisories/blob/main/docs/event_types.md). The following shows an example of the `wolfictl advisory create` command in action. **Please note that the vulnerability exemplified here is an arbitary CVE ID for demonstration purposes and does not reflect an actual vulnerability found in the `glibc` package.**

```sh
Auto-detected distro: Wolfi

Package: glibc 
Vulnerability: CVE-2024-57230 
Type: 
  detection
```

We can now check that our advisory has been successfully added with the `wolfictl advisory diff` command. This will show us what advisories have been modified by us.

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

In this guide, you learned how to use the `wolfictl` tool to interact with Chainguard’s Security Advisories feed. You used `wolfictl` to explore existing advisories, and also created and updated your new security advisory. The steps shown in this guide allowed you to make local changes to your advisory feed. If you wish to contribute to the open-source Wolfi OS advisory feed, please read through our [How To Patch CVEs](
https://github.com/wolfi-dev/os/blob/main/HOW_TO_PATCH_CVES.md) guide and our [How Chainguard Issues Security Advisories](/chainguard/chainguard-images/working-with-images/security-advisories/how-chainguard-issues/) article first.

Be sure to routinely check [our Security Advisories page](https://images.chainguard.dev/security/) when your scanners pick up new CVEs in your images. If you want to learn more about how you can interpret a security advisory and what its status means for your security, read our [article on using advisories](/chainguard/chainguard-images/working-with-images/security-advisories/how-to-use/). 

We also have a video walkthrough showing how to use the [Security Advisories page and `chainctl diff` API](/chainguard/chainguard-images/videos/security_advisories/).
