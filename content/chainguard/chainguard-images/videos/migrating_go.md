---
title: "Migrating a Dockerfile for a Go application to use Chainguard Images"
linktitle: "Migrating Go Applications to Chainguard"
lead: ""
description: "How to migrate an existing Dockerfile for an application that can be statically compiled to Chainguard Images in order to improve security and reduce file size."
type: "article"
date: 2024-02-07T01:21:01+00:00
lastmod: 2024-02-07T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 060
toc: true
---

{{< youtube IuEOyACeJE8 >}}

## Tools used in this video

* [Docker](https://docker.com)

## Resources

[Statically Linking Go](https://mt165.co.uk/blog/static-link-go/)

## Transcript

In this video, I'm going to show how easy it is to port an existing Dockerfile to use a Chainguard Image base, and how that can help to improve the image, especially in terms of security.

I'll be using the free tier of Chainguard Images here, so you can do everything in this video on your own projects today.

The example I'm going to use is porting an existing Golang project to use the Chainguard Go and Static images, but a very similar technique can be used for other compiled languages, such as Rust and C, especially where you can produce a statically linked executable.

Okay, so over to the terminal.

Okay, so I have this simple Go project.

We can take a look at the main part of the code.

It's extremely simple.

All we're doing is creating a web server that listens on port 8080 and responds with the text: "Hello world."

We also have a Dockerfile to build our application.

It's extremely simple as well.

We're using the Dockerhub Golang image, copying over the source, and running Go build.

So let's try building that.

I've built it before, so that ran really fast.

We can try running it.

I should be able to access it.

Okay, so that all works.

It's a really nice, simple Go web server.

Let's take a look at how we can change it to use a Chainguard Image.

The easiest thing we can do, literally a one-line change, is just to modify this to point out the Chainguard Go image.

With any luck, that will build just the same.

So I'll go back to this original build statement.

We'll call it something different so we can compare it later.

Okay, that's built.

Now we want to check it runs.

I do need to first stop the old one.

Okay, let's try running it again.

It's running.

Let's check it works.

Okay, so that works identically.

A one-line change, and we've made no difference to the actual running application.

But let's investigate this a little bit more.

So if I do `docker images` on `go-web-app`, well this is a pretty large image at 892 megabytes.

If I run it on our new image, it's 775 megabytes.

So that's 120 megabytes saving, but still quite a large image.

More interestingly, if I try Docker Scout Quick View to take a look at the CVEs, if I run it on Go web app, we can see there's 42 lower vulnerabilities in there.

So there's quite a bit going on in there.

We can also see there's 303 packages.

So there's a lot of stuff in this image.

Let's compare it to the Chainguard Image.

There's no CVEs and there's only 85 packages.

So this one change has really improved the security posture by getting rid of these 42 low CVEs.

But there's a lot more we can do.

Let's take a look at the Dockerfile again.

So we're using this Chainguard Go image, but we don't need everything in this image when we're actually running the image.

We just need the Go compiler, for instance, to build the server, but we don't need the Go compiler in the final image.

So what we can do is create a multi-stage build.

And I'm going to use the Chainguard static image to house the final production application.

So the static image is really simple.

It has very little in it, just sort of the minimum you need to run a typical Linux application.

So it has TLS certificates so you can talk to web applications over TLS.

It has Unix directories like `/tmp` and `/home`, and it doesn't have a lot else.

It's only a few megabytes in size, but contains a few more things than say scratch that you need for typical applications.

OK, what we're going to do here is I'm going to copy from the previous build to the Dockerfile up here.

I'm going to copy the `hello` executable, which is at `/work/hello` to `/hello`.

Now it said copy from builder, so I'll need to name this first step builder.

And that will build this hello executable and copy it into my production image.

And then my entry point is now `/hello`.

So there is one more thing we need to do.

The static image does not include any libraries like Glibc or anything.

It just has enough for running statically compiled binaries.

So we need to tell Go to produce a statically compiled binary that contains everything it needs to run and doesn't rely on system libraries.

And we can do that by saying cgo enabled equals zero.

In some cases, you might find you need to pass a few more flags, depending on which Go libraries you use.

And I'll link a blog in the notes that explains when you need to do this and what you need to do.

But in this case, `CGO_enabled=0` will allow us to build our static binary.

So I think that's all I need to do.

We'll see if I got it right.

Let's find the Docker build step.

I'm going to call this distroless.

So when you create an image with just the bare minimum in it to run your application, we quite often call it a distroless image.

No, it doesn't even have a shell or a package manager.

OK, let's see.

Let's see if that builds.

Yep, that built.

Excellent.

I think I still have the old one running.

So let's get rid of the old web app.

No, I always get that wrong.

OK, and let's run this one.

I call it `web-app-distroless`.

I hope so.

That's running.

Let's see if it works.

Excellent.

So this application still works exactly the same as it did at the start of this video.

But if I take a look at the web app distroless, the big difference is that now it's only 8.5 megabytes in size.

So we went from the original Golang image, which is 892 megabytes, to a Chainguard Image, which was 775 megabytes, down to 8.51 megabytes.

And it still all works the same.

So that's a big saving in terms of space.

It also means it's a lot quicker to transfer about.

It's a lot quicker to start up on your nodes, etc.

And most importantly, it should still have zero CVEs.

Yes.

If you don't have access to Docker Scout quick view, you can use other scanners, of course.

There's things like Snyk and Grype.

It's a great free one that we use quite a lot in Chainguard.

But that's really all I want to talk about.

So please do go and try out our static images.

They do work great with go, but also they work with Rust, C, etc.

And we also have a variance that include things like the Glibc libraries.

If you just need a very minimal image with Glibc and nothing else to run your application.

OK, please try it out and let me know how you get on.
