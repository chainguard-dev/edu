---
title: "How to Migrate a Java Application to Chainguard Images"
linktitle: "Migrate Java Applications to Chainguard"
lead: ""
description: "How to migrate an existing Dockerfile for a Java application to use Chainguard Images
in order to improve security and reduce image size."
type: "article"
date: 2024-04-02T15:21:01+00:00
lastmod: 2024-04-02T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 60
toc: true
---

{{< youtube FYOVcSv1-oY >}}

## Tools used in this video

* [Docker](https://docker.com)

## Resources

* Blog on [bootstrapping Java in Wolfi](https://www.chainguard.dev/unchained/fully-bootstrapping-java-from-source-in-wolfi)
* [Learning Labs Git repository](https://github.com/chainguard-dev/learning-labs-java) with code used in demo

## Transcript

Okay, I want to give a quick overview of how to use the Chainguard Java images.

And in particular, I want to show how to port an existing application to use the Chainguard Java images.

So our images are largely equivalent to the existing Java images that you can find on the Docker Hub, such as the Eclipse Temurin ones.

The difference is that we're much more focused on producing minimal images with a low CVE count.

We do build our own JDK and there's a [really great blog](https://www.chainguard.dev/unchained/fully-bootstrapping-java-from-source-in-wolfi) on the Chainguard site that explains how we do this and how we bootstrap from the really early versions of Java, which I thoroughly recommend checking out and I will link in the notes.

For this video I'm going to use an example created by my colleague Mauren Berti, so all the hard work in this video is actually down to her.

So the starting point for this video is this example app.

It's a Spring Boot app and all it does is listen on port 8080 and return "Hello world" effectively.

So here is the Dockerfile and we can see it starts with `FROM maven`.

So this is using the Docker official image for maven which itself is built on top of Eclipse Temurin.

All we're doing then is copying over some source code, building it with maven, doing a little bit of cleanup on this step to get rid of some build artifacts and then we're copying the jar file to the app directory and setting an entrypoint.

So we should be able to build that fairly easily and now I should be able to run it.

That was pretty quick because it was cached already.

If you build it yourself it will take a little bit longer because it will have to download all the various dependencies.

So let's see if I can get this right.

`docker run --rm -d --port 8080`

to port 8080 on the host.

Image was called `java-maven`.

So now hopefully if I do `curl localhost:8080/hello` I get "Hello world" back.

So that's the application working.

We can take a look at the logs if we like.

Okay nothing surprising there.

It's a Tomcat application.

So if we look at the size of the image we can see it's 585 megabytes.

So quite a large container but nothing too surprising for a Java image.

If we look at the CVEs -- I'm going to use Docker Scout, use grype or whatever -- then you can see Docker Scout is reporting there's 10 medium and 17 low CVEs.

Honestly I don't think it's a terrible result but let's see if we can do better.

So let's take a look at this Dockerfile and what I'm going to do here is change to use `cgr.dev/chainguard/maven`.

So that's using the `cgr.dev`, Chainguard's registry.

You could just delete the `cgr.dev` and use the Docker Hub because we now have Chainguard images on the Docker Hub under the Chainguard workspace.

But let's just do that for the minute and we will rebuild it.

This time I'll add "cg" on the end so we can see the difference.

And there we go.

So let's take a look at `java-maven-cg`.

So I think we are 585 megabytes.

So we've dropped it by 220 megabytes or 225 megabytes to 360 megabytes.

So that's a fairly big saving by just making -- just adding -- `cgr.dev/chainguard` to the start.

But more interestingly what happens to the CVEs?

So if I run Docker Scout on this image we see there's zero CVEs.

So I've made a very small change and we've dropped the size of the image and we've removed all the known CVEs.

So that's a pretty effective change in my book.

But we can still take it further.

I'm going to use Mauren's hard work and we'll look at how you can create a multi-stage Docker build.

I've done `docker reset`.

I meant to do `git reset`.

Okay.

`git switch` to the Chainguard multi-stage JRE image.

And if we look at the Dockerfile and what we now have is a multi-stage build.

So we're using the maven image as a builder.

So we've got this "as builder" step but now we've got a second build step down here where we say "as runner".

So this code is more or less the same.

We have taken out the entrypoint but now we're copying the jar file from the builder and running it here.

And this image is just a JRE image.

So it doesn't have all the build tooling associated with the maven image.

Okay let's try building that.

That looks good.

So if I do... well I guess we should prove it still works.

So if I do `docker run`.

I'll do `docker ps` first.

`docker rm -f 12`

Now if I do `docker run` again.

So `java-maven-multi-chainguard`.

`curl localhost 8080/hello`

So still working just the same as before but now `java-maven-multi-cg` -- we can see we've got the size down a little bit further.

So I think it was what 360 megabytes and now we've got it down to 325 megabytes.

So we've removed 35 megabytes of build tooling in there.

And also if we check the CVEs again hopefully that will still be zero.

Yeah, so zero CVEs but we've reduced the size and number of packages in the image.

So that's quite a big win.

Took a little bit more work to get to the multi-stage build but not a ridiculous amount.

So that's about it.

We've seen how you can use Chainguard's maven and JRE images to reduce the size and CVE count in a Java application with relatively little work.

Please do take a look and let me know how you get on.

