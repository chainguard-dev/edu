---
title: "Getting Software Versions from Chainguard Images"
linktitle: "Software Versions"
lead: ""
description: "Video demonstration of how to get the software version information from Chainguard Images"
type: "article"
date: 2023-07-07T15:21:01+02:00
lastmod: 2023-07-10T15:21:01+02:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 020
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

<a href="https://youtu.be/K60-jhVf2I4?t=14" target="_blank">0:14</a>
This is particularly useful if you're using the public tier of Chainguard Images and only have
access to the `latest` tag and it can be difficult to ascertain the version that this refers to.

<a href="https://youtu.be/K60-jhVf2I4?t=25" target="_blank">0:25</a>
So all Chainguard Images have an SBOM or Software Bill Of Materials associated with them.

<a href="https://youtu.be/K60-jhVf2I4?t=31" target="_blank">0:31</a>
This is a complex and long document, but we can parse it to extract just the info we are interested in.

<a href="https://youtu.be/K60-jhVf2I4?t=38" target="_blank">0:38</a>
Now the SBOM is stored as an attestation in the container registry.

<a href="https://youtu.be/K60-jhVf2I4?t=42" target="_blank">0:42</a>
And also in the image itself, we can download the SBOM from the registry by using the Cosign tool.

<a href="https://youtu.be/K60-jhVf2I4?t=50" target="_blank">0:50</a>
And let's look at an example of this.

<a href="https://youtu.be/K60-jhVf2I4?t=53" target="_blank">0:53</a>
So we have this script here.

<a href="https://youtu.be/K60-jhVf2I4?t=57" target="_blank">0:57</a>
And what the script is going to do is download the Linux amd64 version of Python — it's not going
to get the image itself, but it's actually going to ask for this predicate type which is SPDX, which
corresponds to the SBOM type — SPDX is an SBOM standard.

<a href="https://youtu.be/K60-jhVf2I4?t=78" target="_blank">1:18</a>
And once we have that, we're going to pass it through jq and base64 to decode it.

<a href="https://youtu.be/K60-jhVf2I4?t=84" target="_blank">1:24</a>
And then we're going to do a little bit more jq to extract the name and version info for each package.

<a href="https://youtu.be/K60-jhVf2I4?t=93" target="_blank">1:33</a>
So let's see that in action.

<a href="https://youtu.be/K60-jhVf2I4?t=100" target="_blank">1:40</a>
So down at the bottom here, we see the version information for Python, which is the main package
we're interested in and we can see its version 3.11.4-r0.

<a href="https://youtu.be/K60-jhVf2I4?t=113" target="_blank">1:53</a>
But there's also full information on all the other packages and the image.

<a href="https://youtu.be/K60-jhVf2I4?t=118" target="_blank">1:58</a>
So you can see things like the version of glibc and readline, etc.

<a href="https://youtu.be/K60-jhVf2I4?t=123" target="_blank">2:03</a>
Now, in this case, I just asked for information on the latest tag.

<a href="https://youtu.be/K60-jhVf2I4?t=127" target="_blank">2:07</a>
If you have a downloaded image, you'd want to use a digest of that image to get the correct details from the registry.

<a href="https://youtu.be/K60-jhVf2I4?t=133" target="_blank">2:13</a>
But alternatively, you can get the SBOM data direct from the image itself.

<a href="https://youtu.be/K60-jhVf2I4?t=139" target="_blank">2:19</a>
And let's take a look at an example of that.

<a href="https://youtu.be/K60-jhVf2I4?t=144" target="_blank">2:24</a>
So what I've done here is run ls on the /var/lib/db/sbom directory inside the container and that's listed a bunch of Jason files, one for each package in the image.

<a href="https://youtu.be/K60-jhVf2I4?t=159" target="_blank">2:39</a>
Now these JSON files are actually SPDX documents, but the file names themselves contain the the version info that we're interested in.

<a href="https://youtu.be/K60-jhVf2I4?t=167" target="_blank">2:47</a>
So we can see this image doesn't include a lot except busybox and a few system libraries.

<a href="https://youtu.be/K60-jhVf2I4?t=175" target="_blank">2:55</a>
Now, this works because wolfi-base includes a shell — busybox — with the ls command that we ran.
But lots of Chainguard images don't have this.

<a href="https://youtu.be/K60-jhVf2I4?t=185" target="_blank">3:05</a>
So you'll need to either copy this /var/lib/db/sbom directory out with something like `docker cp` or
use a `-dev` variant of the image that does include a shell and ls.

<a href="https://youtu.be/K60-jhVf2I4?t=198" target="_blank">3:18</a>
But there you have it two easy ways to get full version info on all packages in a Chainguard Image.

<a href="https://youtu.be/K60-jhVf2I4?t=205" target="_blank">3:25</a>
I hope that was helpful to you.
