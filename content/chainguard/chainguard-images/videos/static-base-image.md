---
title: "Using the Chainguard Static Base Image"
linktitle: "Using the Static Base Image"
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

<a href="https://youtu.be/ZT6177U0fUM?t=10" target="_blank">0:10</a> Well, there's plenty of choices but if everything else is equal, I would choose something very small and with a low known-vulnerability account, and an excellent example of this is a Chainguard static image.

<a href="https://youtu.be/ZT6177U0fUM?t=25" target="_blank">0:25</a> So some of you are probably familiar with the Google Distroless images and the Chainguard static image is very similar.

<a href="https://youtu.be/ZT6177U0fUM?t=33" target="_blank">0:33</a> So as some background, these images all came from a quest to produce the most minimal secure container images possible.

<a href="https://youtu.be/ZT6177U0fUM?t=42" target="_blank">0:42</a> The idea is that the less there is in a container image, it's not just easier to transfer, but it's also less complex and more secure.

<a href="https://youtu.be/ZT6177U0fUM?t=52" target="_blank">0:52</a> And this is borne out by just comparing common base images and the sizes and CVE count.

<a href="https://youtu.be/ZT6177U0fUM?t=58" target="_blank">0:58</a> For example, let's take a look at the Debian Image

<a href="https://youtu.be/ZT6177U0fUM?t=61" target="_blank">1:01</a> And we can see that's around 140 megabytes in size.

<a href="https://youtu.be/ZT6177U0fUM?t=68" target="_blank">1:08</a> We can compare that to Alpine.

<a href="https://youtu.be/ZT6177U0fUM?t=71" target="_blank">1:11</a> And Alpine is only 7.6 megabytes.

<a href="https://youtu.be/ZT6177U0fUM?t=75" target="_blank">1:15</a> And then if we look at the Google distroless image that's even smaller still at 2.45 megabytes and the Chainguard static images are roughly the same around two or three megabytes.

<a href="https://youtu.be/ZT6177U0fUM?t=93" target="_blank">1:33</a> The reason there's two images here is the latest glibc one is Wolfi based and the latest one is Alpine based, but they're both practically identical to be honest.

<a href="https://youtu.be/ZT6177U0fUM?t=106" target="_blank">1:46</a> So next, let's scan the images for CVEs.

<a href="https://youtu.be/ZT6177U0fUM?t=110" target="_blank">1:50</a> I'm going to use grype in this case, which is a common scanner and it's free to use so you can recreate these results.

<a href="https://youtu.be/ZT6177U0fUM?t=118" target="_blank">1:58</a> So if we look at Debian, Debian does have some vulnerabilities and we can see grype thinks there's one high, three low and 47 negligible vulnerabilities in this case.

<a href="https://youtu.be/ZT6177U0fUM?t=133" target="_blank">2:13</a> If we run on Alpine however, grype says there's no vulnerabilities.

<a href="https://youtu.be/ZT6177U0fUM?t=149" target="_blank">2:29</a> We run it on Google Distroless.

<a href="https://youtu.be/ZT6177U0fUM?t=152" target="_blank">2:32</a> It's the same story and also on the Chainguard static images, there's zero vulnerabilities.

<a href="https://youtu.be/ZT6177U0fUM?t=165" target="_blank">2:45</a> So simply by having less in an image, we have a stronger security posture because there's less attack surface.

<a href="https://youtu.be/ZT6177U0fUM?t=173" target="_blank">2:53</a> The distroless and Chainguard images take this to an extreme by not even having a shell or package manager in them.

<a href="https://youtu.be/ZT6177U0fUM?t=181" target="_blank">3:01</a> But if you don't have a shell or a package manager, how can you do anything with the image?

<a href="https://youtu.be/ZT6177U0fUM?t=187" target="_blank">3:07</a> And the answer is to use a multistage build.

<a href="https://youtu.be/ZT6177U0fUM?t=190" target="_blank">3:10</a> So I have an example here, the Dockerfile and you can see it builds a simple go program and copies the result into the Chainguard static image, we can build this with "docker build" and we can see it works.

<a href="https://youtu.be/ZT6177U0fUM?t=216" target="_blank">3:36</a> But the best thing is, if you look at the size of the image, it's tiny, it's only 3.93 megabytes.

<a href="https://youtu.be/ZT6177U0fUM?t=229" target="_blank">3:49</a> Now there is one final point.

<a href="https://youtu.be/ZT6177U0fUM?t=232" target="_blank">3:52</a> Some of you are probably thinking we can actually make this even smaller by using the empty scratch image.

<a href="https://youtu.be/ZT6177U0fUM?t=238" target="_blank">3:58</a> In this case, you'd be right.

<a href="https://youtu.be/ZT6177U0fUM?t=241" target="_blank">4:01</a> But in a lot of other cases, what you'll find is that applications require one or two things more.

<a href="https://youtu.be/ZT6177U0fUM?t=247" target="_blank">4:07</a> For example time zone data or TLS certificates.

<a href="https://youtu.be/ZT6177U0fUM?t=252" target="_blank">4:12</a> And they often expect certain directories to be available such as /tmp or /etc or /home.

<a href="https://youtu.be/ZT6177U0fUM?t=259" target="_blank">4:19</a> So the static image provides this and almost nothing else.

<a href="https://youtu.be/ZT6177U0fUM?t=263" target="_blank">4:23</a> For that reason, if you're using a tool chain that lets you build statically compiled binaries like rust or go and you want a secure and minimal base.

<a href="https://youtu.be/ZT6177U0fUM?t=273" target="_blank">4:33</a> It's really hard to do better than the Chainguard static image.
