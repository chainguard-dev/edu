---
title: "How to Use Container Container Digests to Improve Reproducibility "
linktitle: "Digests"
aliases:
- /chainguard/chainguard-images/videos/container-image-digests/
- /chainguard/chainguard-images/how-to-use/container-image-digests/
lead: ""
description: "Video demonstration of using digests with Chainguard Containers"
type: "article"
date: 2023-08-07T15:21:01+02:00
lastmod: 2025-04-08T15:21:01+02:00
draft: false
tags: ["Chainguard Containers", "Product", "Video" ]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 037
toc: true
---

{{< youtube xYlLfjgG64E >}}

## Tools used in this video

* [Docker](https://docker.io)
* [Crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane)

## Commands used

```sh
docker pull cgr.dev/chainguard/node
```

```sh
docker manifest inspect cgr.dev/chainguard/node@sha256:ede7ef4ca485553f5313f7a02ad3537db1fe337079fc7cfb879f44cf709326db
```

```sh
crane digest --full-ref cgr.dev/chainguard/node
```

```sh
docker pull cgr.dev/chainguard/node:latest@sha256:ede7ef4ca485553f5313f7a02ad3537db1fe337079fc7cfb879f44cf709326db
```

## Dockerfile

```dockerfile
FROM cgr.dev/chainguard/go:latest@sha256:7e60584b9ae1eec6ddc6bc72161f4712bcca066d5b1f511d740bcc0f65b05949 AS build 

WORKDIR /src
RUN CGO_ENABLED=0 go build -o /bin/server ./src


FROM cgr.dev/chainguard/static AS prod

COPY --from=build /bin/server /bin/
EXPOSE 8000
ENTRYPOINT [ "/bin/server" ]
```

## Transcript

<a href="https://youtu.be/xYlLfjgG64E?t=5" target="_blank">0:05</a> You might have heard the advice to pin to a digest when using container images.

<a href="https://youtu.be/xYlLfjgG64E?t=10" target="_blank">0:10</a> But what does this mean?

<a href="https://youtu.be/xYlLfjgG64E?t=11" target="_blank">0:11</a> Why is it useful and how can you do it?

<a href="https://youtu.be/xYlLfjgG64E?t=15" target="_blank">0:15</a> So a digest is a content based hash of a unique container image.

<a href="https://youtu.be/xYlLfjgG64E?t=19" target="_blank">0:19</a> No two container images can have the same digest.

<a href="https://youtu.be/xYlLfjgG64E?t=23" target="_blank">0:23</a> If you pull an image by the digest, you are guaranteed to get exactly the same image each time.

<a href="https://youtu.be/xYlLfjgG64E?t=30" target="_blank">0:30</a> And this contrasts with tags like latest or 3.0 which are continually updated and changed.

<a href="https://youtu.be/xYlLfjgG64E?t=37" target="_blank">0:37</a> So you run pull twice, you might well get a different image.

<a href="https://youtu.be/xYlLfjgG64E?t=41" target="_blank">0:41</a> And this has implications for reproducibility.

<a href="https://youtu.be/xYlLfjgG64E?t=46" target="_blank">0:46</a> If images are changing how can I be sure if it works for me it will work for anybody else or myself in the future?

<a href="https://youtu.be/xYlLfjgG64E?t=52" target="_blank">0:52</a> So what's the easiest way to get the digest of an image?

<a href="https://youtu.be/xYlLfjgG64E?t=56" target="_blank">0:56</a> You can run Docker pull and grab it directly from there, for example.

<a href="https://youtu.be/xYlLfjgG64E?t=62" target="_blank">1:02</a> And you can see the digest right here, but do note that this digest will refer to the index of the image which will list different images for different platforms.

<a href="https://youtu.be/xYlLfjgG64E?t=75" target="_blank">1:15</a> And most likely this is what you want.

<a href="https://youtu.be/xYlLfjgG64E?t=78" target="_blank">1:18</a> But we can see what I mean by using the Docker manifest inspect tool.

<a href="https://youtu.be/xYlLfjgG64E?t=88" target="_blank">1:28</a> And we'll use this digest and we'll pipe it through jq.

<a href="https://youtu.be/xYlLfjgG64E?t=100" target="_blank">1:40</a> And so note that this is the index of the image and it actually lists two more digests that point to actual platform specific images.

<a href="https://youtu.be/xYlLfjgG64E?t=108" target="_blank">1:48</a> In this case, the arm64 image and the amd64 image.

<a href="https://youtu.be/xYlLfjgG64E?t=114" target="_blank">1:54</a> If you wanted the image for a specific platform, you could use the address listed here, but not that that might break for some people.

<a href="https://youtu.be/xYlLfjgG64E?t=122" target="_blank">2:02</a> So make sure you know what you're doing before using that.

<a href="https://youtu.be/xYlLfjgG64E?t=126" target="_blank">2:06</a> And I should also mention the crane tool which is a little bit easier to use in scripts as you don't have to parse the output. If I can spell.

<a href="https://youtu.be/xYlLfjgG64E?t=136" target="_blank">2:16</a> There we go.

<a href="https://youtu.be/xYlLfjgG64E?t=138" target="_blank">2:18</a> So here I've run crane digest.

<a href="https://youtu.be/xYlLfjgG64E?t=140" target="_blank">2:20</a> I've asked for the full reference which makes it output the beginning part again.

<a href="https://youtu.be/xYlLfjgG64E?t=144" target="_blank">2:24</a> So we got the digest for the node image as a single line in output.

<a href="https://youtu.be/xYlLfjgG64E?t=149" target="_blank">2:29</a> And you can also pass a `--platform`` argument which will return the digest for specific platform.

<a href="https://youtu.be/xYlLfjgG64E?t=158" target="_blank">2:38</a> So I could ask for the arm64 platform and get this digest back.

<a href="https://youtu.be/xYlLfjgG64E?t=162" target="_blank">2:42</a> OK.

<a href="https://youtu.be/xYlLfjgG64E?t=163" target="_blank">2:43</a> So now that we have the digest, how can we use it?

<a href="https://youtu.be/xYlLfjgG64E?t=166" target="_blank">2:46</a> Well, the most obvious way is to just do a Docker pull.

<a href="https://youtu.be/xYlLfjgG64E?t=173" target="_blank">2:53</a> So here we've done a docker pull on node:latest, using this above digest and that works.

<a href="https://youtu.be/xYlLfjgG64E?t=181" target="_blank">3:01</a> We get back exactly the same image.

<a href="https://youtu.be/xYlLfjgG64E?t=183" target="_blank">3:03</a> One of the interesting things there and you might have noticed as I went backwards from history is that we can change this tag here.

<a href="https://youtu.be/xYlLfjgG64E?t=190" target="_blank">3:10</a> It doesn't, and it turns out Docker or Docker Hub and registries don't actually care what this tag is when you specify an digest - that part gets ignored.

<a href="https://youtu.be/xYlLfjgG64E?t=201" target="_blank">3:21</a> So we can put anything at all there and you can use it for metadata.

<a href="https://youtu.be/xYlLfjgG64E?t=206" target="_blank">3:26</a> But where you're most likely to use a digest is in the configuration file like a Dockerfile, a compose file or Kubernetes yaml file.

<a href="https://youtu.be/xYlLfjgG64E?t=215" target="_blank">3:35</a> So I have an example here using the Dockerfile here.

<a href="https://youtu.be/xYlLfjgG64E?t=219" target="_blank">3:39</a> We've pinned the version of the Go compiler.

<a href="https://youtu.be/xYlLfjgG64E?t=223" target="_blank">3:43</a> And what that means is every time I run the docker build, I'll be using exactly the same Go compiler.

<a href="https://youtu.be/xYlLfjgG64E?t=230" target="_blank">3:50</a> So I'm absolutely sure that nothing's changed in the Go compiler that might cause this build to fail.

<a href="https://youtu.be/xYlLfjgG64E?t=236" target="_blank">3:56</a> And by using digest in Dockerfiles, we make the whole process much more reproducible; things won't break because the underlying image has changed in this case.

<a href="https://youtu.be/xYlLfjgG64E?t=248" target="_blank">4:08</a> And that's really about it.

<a href="https://youtu.be/xYlLfjgG64E?t=249" target="_blank">4:09</a> We've looked at what our digest is, how you can get it and how you can use it to improve reproducibility.