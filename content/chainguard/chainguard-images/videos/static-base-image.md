---
title: "Using the Chainguard Static Base Image"
linktitle: "Static Base"
lead: ""
description: "Video demonstration of how to use the Chainguard static base image to create minimal images"
type: "article"
date: 2023-08-30T15:21:01+00:00
lastmod: 2023-08-30T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 10
toc: true
---

{{< youtube ZT6177U0fUM >}}

## Tools used in this video

* [Docker](https://docker.com)
* [Grype](https://github.com/anchore/grype)

## Dockerfile

```Dockerfile
FROM cgr.dev/chainguard/go as build


COPY main.go /main.go
RUN CG_ENABLED=0 go build -o /hello /main.go


FROM cgr.dev/chainguard/static
COPY --from=build /hello /usr/local/bin/
CMD ["hello"]
```

## Transcript

So what's the best container base image to use?

0:10
Well, there's plenty of choices but if everything else is equal, I would choose something very small and with a low known-vulnerability account, and an excellent example of this is a ChainGuard static image.

0:25
So some of you are probably familiar with the Google Distroless images and the ChainGuard static image is very similar.

0:33
So as some background, these images all came from a quest to produce the most minimal secure container images possible.

0:42
The idea is that the less there is in a container image, it's not just easier to transfer, but it's also less complex and more secure.

0:52
And this is borne out by just comparing common base images and the sizes and CVE count.

0:58
For example, let's take a look at the Debian Image

1:01
And we can see that's around 140 megabytes in size.

1:08
We can compare that to Alpine.

1:11
And Alpine is only 7.6 megabytes.

1:15
And then if we look at the Google distroless image that's even smaller still at 2.45 megabytes and the Chainguard static images are roughly the same around two or three megabytes.

1:33
The reason there's two images here is the latest glibc one is Wolfi based and the latest one is Alpine based, but they're both practically identical to be honest.

1:46
So next, let's scan the images for CVEs.

1:50
I'm going to use grype in this case, which is a common scanner and it's free to use so you can recreate these results.

1:58
So if we look at Debian, Debian does have some vulnerabilities and we can see grype thinks there's one high, three low and 47 negligible vulnerabilities in this case.

2:13
If we run on Alpine however, grype says there's no vulnerabilities.

2:29
We run it on Google Distroless.

2:32
It's the same story and also on the Chainguard static images, there's zero vulnerabilities.

2:45
So simply by having less in an image, we have a stronger security posture because there's less attack surface.

2:53
The distroless and Chainguard images take this to an extreme by not even having a shell or package manager in them.

3:01
But if you don't have a shell or a package manager, how can you do anything with the image?

3:07
And the answer is to use a multistage build.

3:10
So I have an example here, the Dockerfile and you can see it builds a simple go program and copies the result into the Chainguard static image, we can build this with "docker build" and we can see it works.

3:36
But the best thing is, if you look at the size of the image, it's tiny, it's only 3.93 megabytes.

3:49
Now there is one final point.

3:52
Some of you are probably thinking we can actually make this even smaller by using the empty scratch image.

3:58
In this case, you'd be right.

4:01
But in a lot of other cases, what you'll find is that applications require one or two things more.

4:07
For example time zone data or TLS certificates.

4:12
And they often expect certain directories to be available such as /tmp or /etc or /home.

4:19
So the static image provides this and almost nothing else.

4:23
For that reason, if you're using a tool chain that lets you build statically compiled binaries like rust or go and you want a secure and minimal base.

4:33
It's really hard to do better than the Chainguard static image.
