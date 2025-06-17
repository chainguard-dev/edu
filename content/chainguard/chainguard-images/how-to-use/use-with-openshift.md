---
title: "How to Use Chainguard Containers with OpenShift"
linktitle: "Use With OpenShift"
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

When [Using Chainguard Containers](./how-to-use-chainguard-images.md) with OpenShift, there are some adjustments that need to be made to the usual process.

# Adjust Ownership and Permissions

By default, OpenShift Container Platform runs containers using an arbitrarily assigned User ID (UID), as described in the [Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/images/creating-images#use-uid_create-images).

There are required access settings for an image to support running as an arbitrary user:

- Directories and files that are written to by processes in the image must be owned by the `root` group and that group must have both `read` and `write` permissions
- Files that will be executed must also have group execute permissions

Following the Red Hat requirements, to use Chainguard Containers you must make the following change in your Dockerfile to set the required ownership and permissions:

```
RUN chgrp -R 0 /some/directory && \
    chmod -R g=u /some/directory
```

# Create `/app` Directory and `HOME`

When running on OpenShift clusters, you will find that the OpenShift user cannot create config files inside their home directory. This is because [OpenShift is designed to start container instances using a random User ID](https://www.redhat.com/en/blog/a-guide-to-openshift-and-uids).

To avoid this being an issue when using Chainguard Containers, set a `HOME` variable for the user (it would otherwise be set as `/` for root) and create an `/app` directory in every Dockerfile.

This can help you avoid or limit switching to the `root` user during the build phase when no package installation is required.

This involves:
 - Creating the `/app` directory
 - Setting its permissions to `chmod 755` and `chown 65532:0`
 - Setting a `HOME` variable

 Here's a sample Dockerfile excerpt covering this process.

 ```
USER 0

RUN mkdir -m 775 /app && chown -R 65532:0 /app

COPY --chown=65532:0 src/Sample.Service/bin/Release/net9.0/publish /app

USER 65532

WORKDIR /app

ENV HOME=/app

ENTRYPOINT ["dotnet", "Sample.Service.dll"]**
 ```


# Hard-coded User IDs

There are cases where Red Hat hard codes UIDs for specific applications, for example, the user for postgres is set to UID 26. See the [Red Hat documentation](https://access.redhat.com/solutions/6996195) for more details.

In this instance, Chainguard has built a special image for postgres on OpenShift with a different release tag. Where the postgres release version is `17.5` and the regular Chainguard Container image would be released with the tag `17.5`, there is another image released with the tag `17.5-openshift`.


# Security Context Constraints (SCCs)

OpenShift Container Platform includes [security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html-single/authentication_and_authorization/index#managing-pod-security-policies) (SCCs) that you can use to control permissions for the pods in your cluster. SCCs determine the actions that a pod can perform and what resources it can access.

SCCs in OpenShift will by default prevent a root user from running with the Chainguard Containers `-dev` variants.
