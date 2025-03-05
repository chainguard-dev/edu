---
title: "Getting Started with chainctl"
lead: ""
description: "chainctl basics for beginners"
type: "article"
date: 2025-03-0320T08:49:15+00:00
lastmod: 2025-03-0320T08:49:15+00:00
draft: false
tags: ["chainctl", "Getting Started", "Product", "Basics"]
images: []
weight: 100
---

This page presents some of the more commonly used basic `chainctl` commands to help you get started. For a full reference of all commands with details and switches, see [chainctl Reference](../chainctl/_index.md).


## Authenticate and Check Auth Status

To use `chainctl`, the first thing you must do is authenticate with the Chainguard platform. Do so with:

```
chainctl auth login
```

This will present a list of identity providers for you to select from. Use the one that is tied to your Chainguard Account. Once you select the one you wish to use, such as Google, `chainctl` will open a browser window for you to log in with your credentials. Upon successful login, you will have the option to save this identity provider as your default for future logins. Then a token will be exchanged and you will be able to use `chainctl`.

To check your authentication status at any time, enter:

```
chainctl auth status
```

This will list your identity and other attributes tied to your account, including your account's assigned roles and capabilities.

To create a pull token, use:

```
chainctl auth pull-token
```

To configure a Docker credential helper, which will use a token to pull images when using Docker, use:

```
chainctl auth configure-docker
```


## Update chainctl to the Latest Release

To see which `chainctl` version you have installed, use:

```
chainctl version
```

To update your `chainctl` installation, use:

```
chainctl update
```

Updating requires administrative privileges, so be prepared to enter your machine's admin password.


## Configure chainctl

`chainctl` comes with a default configuration, but there are aspects of it that can be adjusted. Examples include setting the registry location that will be used when one is not mentioned in an issued command. To edit the current configuration, use:

```
chainctl config edit
```

If you make a mistake and can't recall the original settings, reset the configuration to default settings with:

```
chainctl config reset
```


## List Available Images

To see which Chainguard Images are available to your account, use:

```
chainctl images list
```

Be warned, that list may take a while to generate and is likely to scroll past quickly in your command line terminal.


## Compare Two Image Versions

Let's say you want to compare two versions of an image for the same package. You need to know the URL for your repo, the image name, and the two versions you want to compare. For versions, you can use release numbers like `8.12.0` or you can use `latest` or `latest-dev`.

Use this, where we show the repo used by our Chainguard Developer Education team and where both instances of `<image_name>` are the same:

```
chainctl images diff cgr.dev/chainguard.edu/<image_name>:latest cgr.dev/chainguard.edu/<image_name>:latest-dev
```

The output returned will be in JSON format.

If a requested image or release being requested is not available in the repo you are using, this will return a `Forbidden` error, just like if you tried to pull an image you did not have access to or from a repository your account is not authorized to use.


## List Available Package Versions

If you want to get details about the various package versions available that can be used in images, use:

```
chainctl packages versions list <package_name>
```

This will list all the versions that Chainguard has built and the end-of-life date for each version that has one assigned. It will also list older package versions that are no longer available.
