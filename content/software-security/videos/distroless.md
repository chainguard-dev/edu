---
title: "WTF is a distroless container?"
lead: ""
description: "Why we should use distroless"
type: "article"
date: 2022-08-01T15:21:01+02:00
lastmod: 2022-08-01T15:21:01+02:00
draft: false
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

{{< youtube rCy7PrS2REY >}}

Have you heard of distroless container images? This video is going to break down what they are, how they work, and why they're better. 

The easiest way to explain what a distroless container image is and how it differs from a traditional fat container image is by starting with the fat container image, then we'll point out the parts that aren't necessary and how distroless images let you build smaller, leaner, more secure container images.

In a traditional fat container image like this one shown in the video, we have a bunch of different stuff installed in it. We start out with a package manager that we typically use to install a bunch of dependencies and then all the way on the other side we have our application. The dependencies that we install with the package manager might be needed to build our application or to operate it at runtime. Additionally, the package manager itself is an application and that comes with its own set of dependencies which we can see here. Some of those dependencies are used for our application because they might be shared or used for a bunch of different things, but some of those dependencies are only used for the package manager. All of those build tools and the package manager dependencies are left in the container image at the end, making it larger, taking up space, and potentially introducing an increased attack surface.

The package manager itself and all of its dependencies and build tools aren't actually needed at run time to operate our application, so a distroless container image works by stripping all of those out so that the only thing left in the image at runtime is your application and the exact dependencies that it needs. You don't have the build tools, the compilers, the package manager or its dependencies. 

A fun metaphor or comparison is this massive ship here, full of giant containers and cranes used to load all of them. This is like a typical fat container image. 

Distroless images are so slim, you can hold them in your hand. It also makes them a lot more transparent and easier to use and see what's inside of them. 

Another metaphor here is this massive ship that has a crane on the ship itself. Sure that crane is useful for loading and unloading the packages once you get to the ports, but it's much more efficient to leave the cranes at those ports so you can have smaller ships. 

A distroless analogy would be small ships here, holding exactly one container each. There's no extra or wasted space, there's no crane to load or unload them; you have to do that from the outside before you go on your journey.

To figure out how they work, let's again start with the traditional fat container image. These images are built up in layers. You start with a base image that contains the package manager, a shell, and other tools you might need to get your application inside. Then you add on layers, one at a time. These layers can only really add things they can add compiled executables or new packages. You can't remove things from previous layers.