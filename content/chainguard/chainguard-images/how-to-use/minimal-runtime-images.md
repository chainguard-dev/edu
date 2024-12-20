---
title: "Building Minimal Images for Applications with Runtimes"
linktitle: "Video: Minimal Runtime Images"
aliases:
- /chainguard/chainguard-images/videos/minimal-runtime-images/
- /chainguard/chainguard-images/how-to-use/minimal-runtime-images/
lead: ""
description: "Video demonstration of creating minimal images for applications with runtimes, such as Java"
type: "article"
date: 2023-09-06T01:21:01+00:00
lastmod: 2023-09-06T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 045
toc: true
---

{{< youtube P7pmV-s5ZYY >}}

## Tools used in this video

* [Docker](https://docker.com)

## Resources

The Dockerfiles used in this video and other supporting documentation are [available on GitHub](https://github.com/chainguard-dev/minimal_images_for_language_runtimes).

## Transcript

Today, I'd like to talk about how to create minimal secure images when using a language that requires a runtime.

<a href="https://youtu.be/P7pmV-s5ZYY?t=12" target="_blank">0:12</a> So here we're thinking of things like Java, .NET or Python.

<a href="https://youtu.be/P7pmV-s5ZYY?t=17" target="_blank">0:17</a> In these cases, you won't be able to use the scratch image or the Chainguard or Google distroless static images, as they won't include the files for the runtime.

<a href="https://youtu.be/P7pmV-s5ZYY?t=28" target="_blank">0:28</a> In cases like these, we can still follow the approach of having a multistage build with the separate development and production image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=36" target="_blank">0:36</a> But this time our production image will need to have the files for the runtime installed.

<a href="https://youtu.be/P7pmV-s5ZYY?t=42" target="_blank">0:42</a> So I'd like to work through an example with the Chainguard Maven and JRE images.

<a href="https://youtu.be/P7pmV-s5ZYY?t=48" target="_blank">0:48</a> In this example, we're using code from the pet clinic example application, but we've added our own Dockerfiles.

<a href="https://youtu.be/P7pmV-s5ZYY?t=57" target="_blank">0:57</a> So you can see here we're using a Chainguard Maven image to build.

<a href="https://youtu.be/P7pmV-s5ZYY?t=62" target="_blank">1:02</a> All we really do is copy in the sources and then run the Maven wrapper script with a package argument and that's going to produce our JAR file.

<a href="https://youtu.be/P7pmV-s5ZYY?t=72" target="_blank">1:12</a> Then in the production image, all we really do is copy the JAR file that's produced here into the image and set an appropriate entrypoint.

<a href="https://youtu.be/P7pmV-s5ZYY?t=84" target="_blank">1:24</a> OK.

<a href="https://youtu.be/P7pmV-s5ZYY?t=84" target="_blank">1:24</a> So let's create this Docker image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=87" target="_blank">1:27</a> But the first thing I want to build is actually the "build" target.

<a href="https://youtu.be/P7pmV-s5ZYY?t=90" target="_blank">1:30</a> So just building the build image to begin with. Now, because of the Docker cache, my last build that was pretty fast, but if you rebuild this yourself it's gonna take a little bit longer.

<a href="https://youtu.be/P7pmV-s5ZYY?t=103" target="_blank">1:43</a> OK.

<a href="https://youtu.be/P7pmV-s5ZYY?t=104" target="_blank">1:44</a> Let's take a look at that image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=107" target="_blank">1:47</a> I can see it's pretty big.

<a href="https://youtu.be/P7pmV-s5ZYY?t=108" target="_blank">1:48</a> So it's 723 megabytes.

<a href="https://youtu.be/P7pmV-s5ZYY?t=111" target="_blank">1:51</a> That's not too surprising because you've got the JDK, Maven and all the resources required to build the JAR in there.

<a href="https://youtu.be/P7pmV-s5ZYY?t=118" target="_blank">1:58</a> But it's not something you'd want to transfer around too much.

<a href="https://youtu.be/P7pmV-s5ZYY?t=122" target="_blank">2:02</a> OK.

<a href="https://youtu.be/P7pmV-s5ZYY?t=123" target="_blank">2:03</a> So let's take a look at the production image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=126" target="_blank">2:06</a> I'll get rid of this target part and will rename it.

<a href="https://youtu.be/P7pmV-s5ZYY?t=135" target="_blank">2:15</a> And again, it was cached, but this time it's much smaller.

<a href="https://youtu.be/P7pmV-s5ZYY?t=143" target="_blank">2:23</a> So that's around half the size of the previous image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=148" target="_blank">2:28</a> Now, like the static images, we don't have a shell or a package manager in this image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=155" target="_blank">2:35</a> Now, in this case, we didn't specify a tag.

<a href="https://youtu.be/P7pmV-s5ZYY?t=158" target="_blank">2:38</a> So we've used the latest version of both Maven and the JRE image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=165" target="_blank">2:45</a> This is fine for a lot of use cases, but sometimes you'll want more control over the exact version of Java you're using for the JDK and the runtime.

<a href="https://youtu.be/P7pmV-s5ZYY?t=175" target="_blank">2:55</a> You can purchase a subscription to Chainguard images and that will give you access to tagged versions of the Java and Maven images.

<a href="https://youtu.be/P7pmV-s5ZYY?t=184" target="_blank">3:04</a> But if that's not feasible, another option is to use the Wolfi base image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=189" target="_blank">3:09</a> This allows us to effectively build our own Java image and specify the exact versions we require.

<a href="https://youtu.be/P7pmV-s5ZYY?t=201" target="_blank">3:21</a> So we can modify the previous Dockerfile look like this.

<a href="https://youtu.be/P7pmV-s5ZYY?t=207" target="_blank">3:27</a> where "FROM wolfi-base" is the major change.

<a href="https://youtu.be/P7pmV-s5ZYY?t=211" target="_blank">3:31</a> And then we're explicitly adding in open JDK version 17 and Maven version 3.9. We also set the Java HOME environment variable, but otherwise, it's pretty much the same as before.

<a href="https://youtu.be/P7pmV-s5ZYY?t=226" target="_blank">3:46</a> Then in the production image, we also use wolfi-base as the base and we add in open JDK version 17
again.

<a href="https://youtu.be/P7pmV-s5ZYY?t=234" target="_blank">3:54</a> We also set the non root user.

<a href="https://youtu.be/P7pmV-s5ZYY?t=237" target="_blank">3:57</a> So we don't run as root in production and copy in the JAR as before.

<a href="https://youtu.be/P7pmV-s5ZYY?t=244" target="_blank">4:04</a> OK.

<a href="https://youtu.be/P7pmV-s5ZYY?t=244" target="_blank">4:04</a> So let's build this image again.

<a href="https://youtu.be/P7pmV-s5ZYY?t=251" target="_blank">4:11</a> I have a cached version.

<a href="https://youtu.be/P7pmV-s5ZYY?t=252" target="_blank">4:12</a> So that was pretty fast.

<a href="https://youtu.be/P7pmV-s5ZYY?t=255" target="_blank">4:15</a> Now note that this solution isn't perfect.

<a href="https://youtu.be/P7pmV-s5ZYY?t=258" target="_blank">4:18</a> And most notably, the final image is gonna include a shell and a package manager that wasn't present in the previous build.

<a href="https://youtu.be/P7pmV-s5ZYY?t=266" target="_blank">4:26</a> But interestingly, despite that this image is actually smaller than the other image.

<a href="https://youtu.be/P7pmV-s5ZYY?t=277" target="_blank">4:37</a> Now, the reason for that is that the JRE image by default includes some locale data and that's important to some Java applications and not important to some other ones.

<a href="https://youtu.be/P7pmV-s5ZYY?t=291" target="_blank">4:51</a> So if you're running a Java application where you need locale data, you're going to need to add in a line, something like this and that will make your final image that bit bigger.

<a href="https://youtu.be/P7pmV-s5ZYY?t=304" target="_blank">5:04</a> OK.

<a href="https://youtu.be/P7pmV-s5ZYY?t=304" target="_blank">5:04</a> Just to round things off.

<a href="https://youtu.be/P7pmV-s5ZYY?t=305" target="_blank">5:05</a> Let's see the image running.

<a href="https://youtu.be/P7pmV-s5ZYY?t=313" target="_blank">5:13</a> OK.

<a href="https://youtu.be/P7pmV-s5ZYY?t=314" target="_blank">5:14</a> That seems to work.

<a href="https://youtu.be/P7pmV-s5ZYY?t=316" target="_blank">5:16</a> So we've covered how you can use Chainguard images in applications that require run time.

<a href="https://youtu.be/P7pmV-s5ZYY?t=321" target="_blank">5:21</a> And also what your options are if you need a specific version. I'll add some links in the description that allow you to grab the code that I've gone through here.

<a href="https://youtu.be/P7pmV-s5ZYY?t=331" target="_blank">5:31</a> But please let me know if you try this out and how it compares to other solutions.

<a href="https://youtu.be/P7pmV-s5ZYY?t=336" target="_blank">5:36</a> Ok.

<a href="https://youtu.be/P7pmV-s5ZYY?t=336" target="_blank">5:36</a> Thank you for listening.
