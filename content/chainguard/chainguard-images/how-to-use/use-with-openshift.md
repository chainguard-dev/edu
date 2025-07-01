---
title: "How to Use Chainguard Containers with OpenShift"
linktitle: "Using With OpenShift"
type: "article"
description: "Special considerations for using Chainguard Containers with OpenShift"
date: 2025-06-17T08:49:31+00:00
lastmod: 2025-06-17T08:49:31+00:00
draft: false
tags: ["Chainguard Containers", "OpenShift", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 008
toc: true
---

In this guide, you'll find general instructions for how to get started using Chainguard Containers on Red Hat OpenShift Container Platform.

[Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) is an application platform that orchestrates and manages your systems and resources. While it is based on open source software like Kubernetes, OpenShift includes a suite of applications with additional functionality that are configured to work together.

Adding Chainguard Containers to your OpenShift deployment saves you the effort of CVE remediation and speeds up your security and compliance efforts.

When [Using Chainguard Containers](/chainguard/chainguard-images/how-to-use/how-to-use-chainguard-images/) with OpenShift, there are some adjustments that need to be made to the usual process. This guide provides guidance. See the [OpenShift docs](https://docs.redhat.com/en/documentation/openshift_container_platform/) for more details.


# Adjust Ownership and Permissions

By default, OpenShift Container Platform runs containers using an arbitrarily assigned User ID (UID), as described in the [Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/images/creating-images#use-uid_create-images).

There are required access settings for an image to support running as an arbitrary user:

- Directories and files that are written to by processes in the image must be owned by the `root` group and that group must have both `read` and `write` permissions
- Files that will be executed must also have group execute permissions

Following the Red Hat requirements, to use Chainguard Containers you must make a change in your Dockerfile to set the required ownership and permissions. For example, if you have one or more files that you need to execute stored in `/some/directory`, then you would do this:

```
RUN chgrp -R 0 /some/directory && \
    chmod -R g=u /some/directory
```

# Create `/app` Directory and `HOME`

When running on OpenShift clusters, you will find that the OpenShift user cannot create config files inside their home directory. This is because [OpenShift is designed to start container instances using a random User ID](https://www.redhat.com/en/blog/a-guide-to-openshift-and-uids).

To avoid this being an issue when using Chainguard Containers:

1. Set a `HOME` variable for the user (it would otherwise be set as `/` for root)
1. Create an `/app` directory in every Dockerfile
1. Set `/app` directory permissions to `755` and ownership to `65532:0`

This can help you avoid or limit switching to the `root` user during the build phase when no package installation is required.

Here's a sample Dockerfile covering this process.

 ```
# Change this to reference the image you want to pull and
# if needed, to use the location of your custom image repo

FROM cgr.dev/$ORGANIZATION/aspnet-runtime-db:9

USER 0

RUN mkdir -m 775 /app && chown -R 65532:0 /app

COPY --chown=65532:0 src/Sample.Service/bin/Release/net9.0/publish /app

USER 65532

WORKDIR /app

ENV HOME=/app

ENTRYPOINT ["dotnet", "Sample.Service.dll"]
 ```


# Use Special Container Images for Hard-coded User IDs

There are cases where Red Hat hard codes UIDs for specific applications, for example, the user for Postgres is set to UID 26. See the [Red Hat documentation](https://access.redhat.com/solutions/6996195) for more details.

In this instance, Chainguard has built a special image for Postgres on OpenShift with a different release tag. Where the Postgres release version is `17.5` and the regular Chainguard Container would be released with the tag `17.5`, there is another image released with the tag `17.5-openshift`.


# Understand Security Context Constraints (SCCs)

OpenShift Container Platform includes [security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html-single/authentication_and_authorization/index#managing-pod-security-policies) (SCCs) that you can use to control permissions for the pods in your cluster. SCCs determine the actions that a pod can perform and what resources it can access.

SCCs in OpenShift will by default prevent a root user from running with the Chainguard Containers `-dev` variants.
