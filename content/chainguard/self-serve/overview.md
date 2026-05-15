---
title : "Self-serve overview"
lead: ""
description: "Signing yourself up for Chainguard products"
type: "article"
date: 2026-05-12T01:00:01+00:00
lastmod: 2026-05-12T01:00:01+00:00
draft: false
weight: 010
---

**Self-Serve** is a general term to capture all forms of users
being able to use Chainguard products (images etc.) on their own
without any direct help or involvement of Chainguard employees.

**Catalog Starter** refers to a specific plan that enables users
to self-serve up to 5 images for free.

The Catalog Starter plan has the following restrictions:

You must be authenticated with a business email address using one of the following:

- Email and password
- Google (only if your business uses a Google Workspace account)

Other limitations include:

- Only a maximum of 5 Chainguard Images can be used
- Only images from the following tiers are available:
  - AI
  - APPLICATION
  - BASE
- No access to nested UIDP image repos, such as Helm charts

## Sign up with `chainctl`

The current method for signing up is with `chainctl`.

To begin, sign up with a brand new account (identity)
using the following interactive command:

```shell
chainctl starter init
```

This will require selection of a valid authentication option:

```shell
    Choose an identity provider to login to Chainguard

  > Email and password
    Google
```

Use the arrow keys and click 'Enter' to select either, which will launch a browser window to the Chainguard console to complete sign-up.

## Add images

You can see which images are available [using the Chainguard Directory](chainguard/chainguard-images/how-to-use/chainguard-directory/), but remember the images available are limited to the tiers mentioned above.

To add one or more images, run the following command, substituting the desired image names for the variables:

```shell
chainctl starter add-images $IMAGE1 [$IMAGE2]
```

After the Chainguard system has processed your request, the image(s) will be accessible. This can take up to a few hours. When available, you will be able to pull the images like this, replacing `$ORGANIZATION` with your organization's name and `$IMAGE` with the desired image's name.

```shell
docker pull cgr.dev/$ORGANIZATION/$IMAGE:latest
```

## Find status

To show the status of your catalog starter organization, including the registry path, account provisioning status, image quota usage, and per-image readiness, use:

```shell
chainctl starter status
```

## Add additional users

To request access for additional users for your organization, use:

```shell
chainctl starter request-access
```
