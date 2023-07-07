---
title: "Getting Software Versions from Chainguard Images"
linktitle: "Software Versions"
lead: ""
description: "Video demonstration of how to get the software version information from Chainguard Images"
type: "article"
date: 2023-07-07T15:21:01+02:00
lastmod: 2023-07-07T15:21:01+02:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 10
toc: true
---

{{< youtube K60-jhVf2I4 >}}

## Tools used in this video

* [Docker](https://docker.com)
* [Cosign](https://github.com/sigstore/cosign)

## Commands used

```sh
cosign download attestation --platform=linux/amd64 \
    --predicate-type=https://spdx.dev/Document \
    cgr.dev/chainguard/python:latest | jq -r .payload | base64 -d \
    | jq -r '.predicate.packages[] | "\(.name) \(.versionInfo)"'
```

```sh
docker run cgr.dev/chainguard/wolfi-base ls /var/lib/db/sbom
```

## Transcript

Hi, I want to record a very short video on how to get software version information out of Chainguard
Images.

[0:14](https://youtu.be/K60-jhVf2I4?t=14)
This is particularly useful if you're using the public tier of Chainguard Images and only have
access to the latest tag and it can be difficult to ascertain the version that this refers to.

[0:25](https://youtu.be/K60-jhVf2I4?t=25)
So all Chainguard Images have an SBOM or Software Bill Of Materials associated with them.

[0:31](https://youtu.be/K60-jhVf2I4?t=31)
This is a complex and long document, but we can parse it to extract just the info we are interested in.

[0:38](https://youtu.be/K60-jhVf2I4?t=38)
Now the SBOM is stored as an attestation in the container registry.

[0:42](https://youtu.be/K60-jhVf2I4?t=42)
And also in the image itself, we can download the SBOM from the registry by using the cosign tool.

[0:50](https://youtu.be/K60-jhVf2I4?t=50)
And let's look at an example of this.

[0:53](https://youtu.be/K60-jhVf2I4?t=53)
So we have this script here.

[0:57](https://youtu.be/K60-jhVf2I4?t=57)
And what the script is going to do is download the Linux amd64 version of Python -- it's not going
to get the image itself, but it's actually going to ask for this predicate type which is SPDX, which
corresponds to the SBOM type -- SPDX is an SBOM standard.

[1:18](https://youtu.be/K60-jhVf2I4?t=78)
And once we have that, we're going to pass it through jq and base64 to decode it.

[1:24](https://youtu.be/K60-jhVf2I4?t=84)
And then we're going to do a little bit more jq to extract the name and version info for each package.

[1:32](https://youtu.be/K60-jhVf2I4?t=92)
Ok.

[1:33](https://youtu.be/K60-jhVf2I4?t=93)
So let's see that in action.

[1:40](https://youtu.be/K60-jhVf2I4?t=100)
So down at the bottom here, we see the version information for Python, which is the main package
we're interested in and we can see its version 3.11.4-r0.

[1:53](https://youtu.be/K60-jhVf2I4?t=113)
But there's also full information on all the other packages and the image.

[1:58](https://youtu.be/K60-jhVf2I4?t=118)
So you can see things like the version of glibc and readline, etcetera.

[2:03](https://youtu.be/K60-jhVf2I4?t=123)
Now, in this case, I just asked for information on the latest tag.

[2:07](https://youtu.be/K60-jhVf2I4?t=127)
If you have a downloaded image, you'd want to use a digest of that image to get the correct details from the registry.

[2:13](https://youtu.be/K60-jhVf2I4?t=133)
But alternatively, you can get the SBOM data direct from the image itself.

[2:19](https://youtu.be/K60-jhVf2I4?t=139)
And let's take a look at an example of that.

[2:24](https://youtu.be/K60-jhVf2I4?t=144)
So what I've done here is run ls on the /var/lib/db/sbom directory inside the container and that's listed a bunch of Jason files, one for each package in the image.

[2:39](https://youtu.be/K60-jhVf2I4?t=159)
Now these JSON files are actually SPDX documents, but the file names themselves contain the the version info that we're interested in.

[2:47](https://youtu.be/K60-jhVf2I4?t=167)
So we can see this image doesn't include a lot except busybox and a few system libraries.

[2:55](https://youtu.be/K60-jhVf2I4?t=175)
Now, this works because wolfi-base includes a shell -- busybox -- with the ls command that we ran.
But lots of Chainguard images don't have this.

[3:05](https://youtu.be/K60-jhVf2I4?t=185)
So you'll need to either copy this /var/lib/db/sbom directory out with something like "docker cp" or
use a -dev variant of the image that does include a shell and ls.

[3:18](https://youtu.be/K60-jhVf2I4?t=198)
But there you have it two easy ways to get full version info on all packages in a Chainguard Image.

[3:25](https://youtu.be/K60-jhVf2I4?t=205)
I hope that was helpful to you.
