---
title: "Debugging Distroless Container Images"
linktitle: "Debugging"
aliases:
- /chainguard/chainguard-images/debugging-distroless-images/
- /chainguard/chainguard-images/troubleshooting/debugging-distroless-images/
type: "article"
description: "In this article, we'll discuss a few different strategies to debug distroless images, considering these images typically don't include a shell or package managers."
date: 2023-05-18T08:49:31+00:00
lastmod: 2023-08-22T08:49:31+00:00
draft: false
tags: ["Chainguard Containers", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 005
toc: true
---

Because distroless images are minimal and don't include a package manager or a shell, debugging issues that occur at runtime may require a distinctive approach.

In this article, we'll discuss a few different strategies to debug distroless images.

## 1. Using Dev / Debug Image Variants

Before moving a workload to a distroless runtime image, it is important to make sure that it runs without issues in a similar but less restrictive environment, which allows for easier debugging. It is also possible to make a temporary base image change from a distroless image to a fully featured image that offers more debugging capabilities.

The `-dev` variants of [Chainguard Containers](/chainguard/chainguard-images/) are designed to replicate the same packages of their distroless version, but with additional software that helps in developing, building, and debugging applications in different language ecosystems.

For example, the following table shows a comparison between the `dev` variants of the PHP image, and which packages are included with each variant:


|                      	| latest | latest-dev | latest-fpm |
|--------------------------|--------|------------|------------|
| `wolfi-baselayout`   	| X  	| X      	| X      	|
| `ca-certificates-bundle` | X  	| X      	| X      	|
| `php`                	| X  	| X      	| X      	|
| `apk-tools`          	|    	| X      	|        	|
| `bash`               	|    	| X      	|        	|
| `busybox`            	|    	| X      	|        	|
| `git`                	|    	| X      	|        	|
| `composer`           	|    	| X      	|        	|
| `php-fpm`            	|    	|        	| X      	|

You can find similar detailed package information for all [Chainguard Containers](https://images.chainguard.dev) in their respective image details pages under the SBOM section.

Once you have changed your Dockerfile base image to use a `-dev` variant, you can overwrite the entry point command to get a shell on the container:

```shell
docker run -it --entrypoint /bin/sh cgr.dev/chainguard/php:latest-dev
```

Having a package manager and the ability to log into the image to debug any issues is very important at development time, but becomes unnecessary (and less safe) when talking about production environments. That's why we recommend using a distroless variant for production workloads.

### Chainguard Containers in Production
Although the `-dev` image variants have similar security features as their distroless versions, such as complete SBOMs and signatures, they feature additional software that is typically not necessary in production environments. The general recommendation is to use the `-dev` variants to build the application and then copy all application artifacts into a distroless image, which will result in a final container image that has a minimal attack surface and won't allow package installations or logins.

That being said, it's worth noting that the `-dev` variants of Chainguard Containers are still **more secure** than many popular container images based on fully-featured operating systems such as Debian and Ubuntu, because they carry less software, follow a more frequent patch cadence, and offer attestations for what is included.

### Language Ecosystem Guides
The following guides show how to use these `-dev` images in combination with their distroless variants in order to build a final image that is also distroless, but contains everything the application needs to run:

- [Getting Started with the Python Chainguard Container](/chainguard/chainguard-images/getting-started/python/)
- [Getting Started with the Ruby Chainguard Container](/chainguard/chainguard-images/getting-started/ruby/)
- [Getting Started with the Go Chainguard Container](/chainguard/chainguard-images/getting-started/go/)
- [Getting Started with the Node Chainguard Container](/chainguard/chainguard-images/getting-started/node/)
- [Getting Started with the PHP Chainguard Container](/chainguard/chainguard-images/getting-started/php/)

Check also the guide on [Creating Wolfi Container Images with Dockerfiles](/open-source/wolfi/wolfi-with-dockerfiles/) for guidance on how to build a custom image that can be used for development and debugging.


## 2. Using Ephemeral Debug Containers

Another method to debug distroless images running in production is to use ephemeral debug containers, a special type of container that is temporarily attached to an existing Pod to troubleshoot and inspect running services.

Suppose you have a Kubernetes cluster and one of the containers is having issues. Perhaps it doesn't seem to be able to connect to other services in the cluster, or expected processes aren't running. If the container has a shell, you'd be able to use `kubectl exec` to run debugging commands from inside the container to help diagnose the issue. With a minimal image, this isn't possible, but we can achieve something very similar using `kubectl debug` to launch an ephemeral container.

Let's review an example. We'll start by running a Chainguard NGINX image on a Kubernetes cluster:

```
kubectl run nginx --image=cgr.dev/chainguard/nginx:latest
```

Which should result in:

```
pod/nginx created
```

We can try to start a shell in this pod:

```
kubectl exec -it nginx -- sh
```

But the following error occurs:

```
error: Internal error occurred: error executing command in container: failed to exec in container: failed to start exec "67bd5164394b1170ac1846bd77ea0b826332365970fbde3b3201bb9abec9b72c": OCI runtime exec failed: exec failed: unable to start container process: exec: "sh": executable file not found in $PATH: unknown
```

Which is a long way of telling us there is no shell in the image. What we can do instead is use an ephemeral container. An ephemeral container will connect to the namespaces of an existing container, effectively allowing you to sideload debugging tools. Let's try that now:

```
kubectl debug -it nginx --image=cgr.dev/chainguard/wolfi-base --target=nginx
```

You should get output similar to:

```
Targeting container "nginx". If you don't see processes from this container it may be because the container runtime doesn't support this feature.
Defaulting debug container name to debugger-87792.
If you don't see a command prompt, try pressing enter.
nginx:/#
```

Now we can try running some debugging commands. Let's start by seeing what's running:

```
nginx:/# ps aux
PID   USER     TIME  COMMAND
    1 65532     0:00 nginx: master process /usr/sbin/nginx -c /etc/nginx/nginx.conf -e /dev/stderr
   10 65532     0:00 nginx: worker process
   11 65532     0:00 nginx: worker process
   12 65532     0:00 nginx: worker process
   13 65532     0:00 nginx: worker process
   14 65532     0:00 nginx: worker process
   15 65532     0:00 nginx: worker process
   16 65532     0:00 nginx: worker process
   23 root      0:00 /bin/sh -l
   32 root      0:00 ps aux
```

And the open ports:

```
nginx:/# netstat -lntu
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN
```

To facilitate accessing processes running in other containers without having to specify a target, you may enable [process namespace sharing](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) within your Pod setup. It's also worth noting that the filesystem may not be accessible due to default user permissions.

For more strategies on how to debug production distroless containers, check the [Kubernetes documentation on debugging running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/).

## Resources to Learn More

- [Minimal Container Images: Towards a More Secure Future ](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future) - Chainguard Blog
- [Why Distroless](https://edu.chainguard.dev/chainguard/chainguard-images/overview#why-distroless) - Chainguard Container Documentation
- [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) - Official Kubernetes Documentation
- [Introducing Ephemeral Containers](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html) - Google Open Source Blog
- Talk: [Running a Go Debugger in Kubernetes](https://www.youtube.com/watch?v=V3SrFyMxmq4&t=2691s) - Cloud Native Rejekts EU 23
