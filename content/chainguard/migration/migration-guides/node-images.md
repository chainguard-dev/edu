---
title: "How to Migrate a Node.js Application to Chainguard Images"
linktitle: "Video: Node.js"
aliases:
- /chainguard/chainguard-images/videos/node-images/
- /chainguard/migration/node-images/
- /chainguard/migration/migration-guides/node-images/
lead: ""
description: "How to migrate an existing Dockerfile for a Node.js application to use Chainguard Images in order to improve security and reduce image size."
type: "article"
date: 2024-04-25T15:21:01+00:00
lastmod: 2024-04-25T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "migration-guides"
weight: 015
toc: true
---

{{< youtube hfpVS-UP4Yw >}}

## Tools used in this video

* [Docker](https://docker.com)

## Resources

* Tutorial on [Porting a Sample Application](/chainguard/migration/porting-apps-to-chainguard/)
* [Example Application Git repository](https://github.com/chainguard-dev/identidock-cg/) with code used in demo

## Transcript

Today, we're going to look at how easy it is to port a Dockerfile for a Node.js application to use
a Chainguard Image base and how it can help improve the image, especially in terms of security.

I'll be using the free tier of Chainguard Images here, so you can do everything in this video
yourself today.

OK, over to the terminal.

So I have a directory here with a simple Node.js application.

I think the first thing we should do is just see it running so you understand what it does.

OK, so it's running on port 8080.

If I do a curl, what we're going to do is curl port 8080.

We're going to hit the monster endpoint and give it some input and a size.

And what you'll see is we get an image back.

So basically, it produces like an identicon, if you know what an identicon is, or a unique avatar
for its input.

So if I give it an input, so I'll give my manager Lisa's name here, and you get the appropriate
avatar out.

So we can put in anything we like here.

And if you put the same thing in again, you should get the same thing back out.

And it's sometimes used as a default image for users on a website, such as GitHub.

OK, so let's take a look at the Dockerfile for this application.

You can see that it uses the Node official image from Docker Hub.

It installs quite a few dependencies that are needed for the graphics capability, creates a non-root
user, copies over the package JSON, and installs some Node modules.

Then it copies over the code, changes to the dnmonster user, and calls `npm start`.

So that all makes sense.

Let's have a go at building it.

And that was all cached, so that was really fast.

But let's have a look at what it's built.

So that image is 1.22 gigabytes in size.

So it's a pretty large image.

If we run it through Docker Scout, to look at the CVEs.

I tend to use Docker Scout.

It has quite nice summary output.

But you can, of course, use Grype or whatever, et cetera.

And what it's telling me is this image has two high, seven medium, and 109 low CVEs.

It is saying that I can change to the `slim` image, and I will reduce that to three medium and 24
low vulnerabilities.

But we're not going to do either of that.

We're going to change to use a Chainguard Image and see how that affects things.

So I'm going to use the [Chainguard Registry](/chainguard/chainguard-registry/overview/) here at cgr.dev.

And we're going to use the `latest-dev` image.

So there's a couple of things here.

I'm using a Chainguard Registry.

I could also use the Docker Hub.

So Chainguard Images are available on the Docker Hub, just in the Chainguard user or namespace.

But in this case, we're using the Chainguard Registry.

For free, we provide the `latest` and `latest-dev` images.

The difference between the `latest` and `latest-dev` is `latest-dev` includes a package manager and
a shell, which I'm going to need in this case to install some dependencies.

Now, these dependencies are all `apt-get` based.

And Chainguard Images, we have APK tools.

We're not an Alpine distribution, we use our own Linux distribution called Wolfi.

But we do also use the APK tools.

So first thing I'm going to do is switch this line to be the equivalent in Wolfi.

So first thing you do is change to the root user so I can install software.

So the Chainguard Images typically do not run as root by default.

And then I'm going to use APK add to install our software.

And you can see the fairly similar package names to the app packages.

We've got Cairo here.

We've got Cairo there, for example, and libjpeg, et cetera, et cetera.

But they are slightly different names.

OK.

Then what do I need to do?

So the next part is the `groupadd`.

So again, that's typically different in Wolfi images as we generally use the BusyBox tools.

So that's not `groupadd`.

It's `addgroup`.

So this line is going to change to look like that.

`install` can remain the same.

We do have another difference down the bottom, though.

This `npm start`.

So because Chainguard Images by default don't have a shell, this doesn't work.

Basically, this will get passed to the node binary to be interpreted, which isn't what we want.

So what I'm going to do is change this to be an `entrypoint` command.

And then I know it's not going to be passed as an argument to the node binary.

And that should work.

Let's try building it.

This time we'll call it dnmonster-cg.

Again, it was cached, so that was pretty fast.

If I can spell.

And now this time it's 880 megabytes.

So that's, what, 340 megabytes saving, which is pretty good.

But more interestingly, what's happened to the CVEs?

Yeah, there's no CVEs in this image.

So that's a very big jump and great to see.

I would say 880 megabytes is still quite a large image.

So let's see if we can get it down a bit further.

And what we can do is we can change to use a multi-stage build.

So here everything is getting installed in this node `latest-dev` image.

And we even have things like a C compiler in this image, which we don't really want in our final
production image.

So what we're going to do is we're going to change to use a multi-stage build.

First thing I'm going to do is call this the build stage.

And then we're going to have a second stage where we copy the assets out of this image and into the
production image.

And I'm just going to copy one I made before.

So here we're using `wolfi-base`.

I can't use the Node `latest` image because we need to install these dependencies.

So for that reason, I've used `wolfi-base`.

So this image will end up with a package manager and a shell in it.

But it's still a lot smaller than the `latest-dev` image because we don't have things like a C
compiler and other build tooling in there.

Note that I did have to add `nodejs` to this list to explicitly install Node.js.

But otherwise, we're just copying over the build assets from the previous stage and setting the
`entrypoint`.

We no longer have NPM, so I've explicitly set it to call Node with `server.js`.

OK, so let's try building this one.

We call it multi, if I can spell.

OK, again, that was cached, so that's been fast.

Right, now we're down to 334 megabytes, so a much better size.

And just for the sake of checking, we should also run it through Docker Scout.

I hope we've not somehow managed to add in vulnerabilities.

We shouldn't have.

Yeah, there's no vulnerability, so that's great.

But there is still a problem with this image.

So let's try running it.

It should still work.

So there's Lisa's avatar again.

But if I try and stop this, so `docker stop 12386`, it hangs.

And that's not great.

And the reason it's hanging is because the Node binary doesn't handle signals properly, or isn't set
up to handle signals properly.

And basically, the Docker sends a `SIGTERM` to the container.

It doesn't respond to the `SIGTERM`, so a few seconds later, it sends a `SIGKILL`.

And that's not really what you want for a clean shutdown.

So what we're going to do is we're going to add a tool called `tini`, which is basically an init
system to this image.

And we're going to add that to the entrypoint as well.

So now the PID 1 in this container isn't going to be Node, it's going to be tini.

And tini will take care of handling signals and also reaping children and things like that.

OK, so if we run this again. We need to build it first.

And if we run it again, should still work.

Yes.

But this time, if I do `docker stop 1ad2`, it stops immediately because tini has correctly handled
the signals.

OK, so that's pretty much all I have.

We've seen how moving a Node application to Chainguard Images can significantly reduce the size of
the image and completely cut the CVE count in the image.

Please do give this a try and let me know how you get on.
