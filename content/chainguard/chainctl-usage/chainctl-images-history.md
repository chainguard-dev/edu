---
title: "chainctl images history"
lead: ""
description: "chainctl images history basics"
type: "article"
date: 2025-04-09T08:49:15+00:00
lastmod: 2025-04-09T08:49:15+00:00
draft: false
tags: ["chainctl", "images", "history", "Product"]
images: []
weight: 75
---

This page demonstrates how to use the `chainctl images history` command. For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).

At times it may be useful to examine the history of an image tag in chainctl, such as to find when it was updated and the associated digests for each update. This is done using `chainctl images history`, which is part of the [chainctl images](./chainctl-images.md) set of commands.

Let's walk through a typical scenario. In our example we use an internal organization created for the Developer Enablement team to use when creating educational resources. Change our examples to use your org. You can do this by selecting from the options presented in a menu as you issue commands, as in [List chainctl images](#list-chainctl-images)


## List images

First, you will want to know which Chainguard Images are available to your account. To do this, use:

```shell
chainctl images list
```

You will be presented with a list of organizations available to your account. For most users, there will only be one entry in the list. This example shows an account with access to several organizations within the fictional MyCorp.

```shell
    Which organization would you like to list images from?                                                       
                                                                                                                        
  > [MyCorp-prod]     This group holds the production Chainguard Images hosted under    cgr.dev/MyCorp-prod                   
    [MyCorp-starter]     This group holds the starter Chainguard Images hosted under    cgr.dev/MyCorp-starter  
    [MyCorp-eval]     This group holds the evaluation Chainguard Images hosted under    cgr.dev/MyCorp-eval  
```

Move the `>` up and down with the arrow keys and hit `Enter` to select the org you want to you.

Be warned, that list may take a while to generate and is likely to scroll past quickly in your command line terminal. You may prefer to direct the output into a file. Here's a sample of what you will see:

```shell
├ [python]
│ ├ sha256:038449621d30e512645107e6b141fbfb5320d8f0caacd3d788e5a3be8da16def
│ │ ├ [3.11]
│ │ └ [3.11.12]
│ ├ sha256:07756f3cf511a6227ae70d816c57b01a6fd9e805a587db5ebb4e17a5954b38c4
│ │ └ [3.11.9]
│ ├ sha256:088b946519e5c766685e335366abe8a6160e3bd108a6525309f7186e943a4666
│ │ └ [3.11.9-dev]
│ ├ sha256:09cb17be345eac82e3fdb017590d5907c582b4bd5ac86ed5e054bae739a9babd
│ │ └ [3.13.0]
│ ├ sha256:16b52893f316d9d7074b9c24c30f82eab1e94356461439d4be1a62fe229e6933
│ │ └ [3.12.7]
│ ├ sha256:1b53a821fe44d699687d1ca2318e3f90fed4af97833ab40384ea77c746b54ed9
│ │ └ [3.10.16]
│ ├ sha256:1c3e412aff5bddf54718d1bc0b4598ea30d18005e7dbfeb7e68bdae0f874682b
│ │ ├ [3]
│ │ ├ [3.13]
│ │ ├ [3.13.3]
│ │ └ [latest]
```


This will continue until all images (like `python` above) are listed with all their variants (releases like `3.13.3`). Notice that the list is not necessarily in order of release.

What if I am interested in knowing how many times a variant has been built and for which platforms, along with the time and digests for each? Read on.


## Examine images history

To examine the history use this command, shown with an optional `--parent=$ORGANIZATION` switch demonstrating how to designate your org without using the menu shown earlier:

```shell
chainctl images history $IMAGE:$VARIANT --parent=$ORGANIZATION
```


For example, let's find the history of one of the `python` images from our previous list, `3.12.7`. So we enter:

```shell
chainctl images history python:3.12.7 --parent=chainguard.edu
```


The returned list is longer than we'll show here, but here's an excerpt:

```shell
- time: 2024-11-29 08:11:03 UTC
  digest: sha256:16b52893f316d9d7074b9c24c30f82eab1e94356461439d4be1a62fe229e6933
  architectures:
    amd64: sha256:755b79b43c1e76472cc467c4636bdb75bf4c2fcc551103087df0a4b0dc039164 (23.14 MB)
    arm64: sha256:d7dfaf24f292f490279611afcec49289aa528dba531590bebae059c7d3139ed6 (22.13 MB)
- time: 2024-11-25 23:45:42 UTC
  digest: sha256:025bbe734f9bb3550ea845f028f28c76c6dff742527e2764f4ba40b3773ee4f8
  architectures:
    amd64: sha256:c7b70882c6fe9b563aa5d5bdfb1a960c65b8c73e0830fc809ceb977e7f778e98 (23.14 MB)
    arm64: sha256:864f735794264120aabdc9eda9e1126140762e1c11eed96a89b0ab2056cc3662 (22.13 MB)
- time: 2024-11-22 01:32:55 UTC
  digest: sha256:2a936c40669150e1a92e4c80b27410786925b8619c0ecc1679ec0a0f6b707235
  architectures:
    amd64: sha256:8db3676319588dca04664a4a57c9fa464398fa2fc6874d5a1500273cabdbde04 (23.16 MB)
    arm64: sha256:ec8b8ef474ad6be50649cd9403882569d2cd1e71ac65e3bc263fc78aaef7608e (22.13 MB)

...

- time: 2024-10-02 23:56:00 UTC
  digest: sha256:c7cf9f46124502b9e8aadf26b4c58e0cdbd5a08b0b97b6d3a451b89563a308e8
  architectures:
    amd64: sha256:d4606173598e7103015b37dec4894771bf9cc221db6f7b102006eb81962c0696 (23.43 MB)
    arm64: sha256:f76a0a2f49418b030f3a31bcd2c8bddb8bbef7b006006aa59b74282955ab671d (22.41 MB)
- time: 2024-10-01 23:40:56 UTC
  digest: sha256:0b0daf09eeb92741efe0eae51dbdeea5a66bed870e0e00895630de729b233b7f
  architectures:
    amd64: sha256:637af1b20e5f8cee7e538b07a1ae3934297769216a65acc454e34fac3dcd3828 (23.46 MB)
    arm64: sha256:8dce068942fa4dd155c87b6b8a3e4b8e2482a5fdb5232cb9dd73c39e63003038 (22.41 MB)

```

The command returns a reverse-chronological list of image builds with timestamps, digests for the build processes, and digests for specific architecture builds with build sizes.