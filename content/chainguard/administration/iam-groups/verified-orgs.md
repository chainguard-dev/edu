---
title : "Verified Organizations"
lead: ""
description: "An overview of how to verify your organization and the implications"
type: "article"
date: 2023-08-15T14:22:23-07:00
lastmod: 2023-10-26T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Conceptual"]
images: []
menu:
  docs:
    parent: "iam-groups"
weight: 025
toc: true
---

Resources on the Chainguard platform are organized in a hierarchical structure called [IAM Groups](/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/). A root-level IAM Group is called an _Organization_. Single customers or organizations typically use a single root-level _Organization_ to manage their
Chainguard resources.

Organizations can optionally be verified. Verification modifies some aspects of the Chainguard platform user experience to help large organizations guide their user base to the correct resources.

## Verifing your Organization

Verification is currently a manual process. To verify your organization, please contact your customer support contact. You can check if your organization is verified using [`chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/).

```sh
chainctl iam group ls -o json | jq
```

Verified organizations will have a field `verified: true` set.

```json
[
  {
    "id": "f5a2c73d75a8d7fe666ecb623c79a2b771d78765",
    "name": "example.com",
    "resourceLimits": {
        "clusters": 3,
        "idps": 1
    },
    "verified": true
  }
]
```

## Verified Organizations and Custom Identity providers

If you've configured a [custom identity provider](/chainguard/chainguard-enforce/authentication/custom-idps/) and your organization is verified, you can select your identity provider by providing the name of your organization when authenicating.

When authenticating with `chainctl`, the `--org-name` flag can be passed. Here, the command uses the example organization name `example.com`.

```sh
chainctl auth login --org-name example.com
```

As an alternative, you can set the organization name by editing the `chainctl` configuration file. You can do so with the following command.

```sh
chainctl config edit
```

This will open a text editor (nano, by default) where you can edit the local `chainctl` config. Add the following lines to this file.

```yaml
default:
  org-name: example.com
```

Once set, the configured identity provider will be used automatically any time you run `chainctl auth login`.

When authenticating via the Chainguard Console, your organization name is detected from your email address in most cases. If your organization name does not match your email domain, it can be input manually to select your custom identity provider.

## Verified Organizations and Chainguard Images

If you've purchased Chainguard Images, your images are available via a private catalog. Your images are available to pull via `cgr.dev/<org id>/<image name>`, where `<org id>` is the unique identifier for your organization. Once your organization is verified, you can use the name of your organization instead of your organization identifer. For example, if your organization is named `example.com` and is verified, you can pull private images from your catalog with `cgr.dev/example.com/<image name>`.

## Restrictions for Verified Organizations

Once an organization is verified, its name can be used interchangably with the organization's unique ID. Changes to the name can break Image pulls from your private catalog and break authentication for users that have configured custom identity providers. For that reason, modifying the name of a verified organization is not currently possible. If you need to modify the name of your verified organization, please contact support.
