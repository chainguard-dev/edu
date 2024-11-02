---
title: "What are Containers?"
linktitle: "Containers"
description: "An overview of the structure, contents, and applications of container technology"
lead: "An overview of the structure, contents, and applications of container technology"
type: "article"
date: 2023-10-17T20:02:23+00:00
lastmod: 22023-10-31T15:12:31+00:00
contributors: ["Michelle McAveety"]
draft: false
tags: ["Conceptual", "Overview"]
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

Maximizing the performance of computer hardware has been a critical undertaking for software engineers for decades. In the 1960s, the advent of virtual machines (VMs) marked a significant milestone in this pursuit. VMs allowed a single computer to host multiple, isolated operating systems, enabling different guest users or processes to share physical infrastructure while maintaining separation in their concurrent operations. This isolation was crucial for security and resource management, as it allowed multiple applications to run on the same hardware without interfering with one another.

However, VMs come with notable drawbacks. They are typically slow to initialize, requiring a significant amount of time and resources to boot up a full operating system for each instance. Additionally, each VM operates with its own virtual kernel, leading to increased resource consumption and reduced efficiency, particularly in environments where rapid scaling is needed.

In response to these limitations, a modern solution emerged in the early 2000s: Containers. Unlike VMs, containers share a common operating system kernel, allowing them to run multiple applications in isolated environments without the overhead associated with full operating system instances. This architectural shift enables containers to start up almost instantaneously and use system resources more efficiently. As a result, containers have become increasingly popular for deploying applications in a wide range of environments, from development to production, due to their lightweight nature, portability in deploying applications across systems for a low resource cost, and ease of use.

This article provides an exploration of Container images - *The fundamental building blocks of container technology*. We will examine the key components that make up container images, as well as the processes involved in creating them. For instance, a container image for a Node.js application might include the Node.js runtime, your application code, and any necessary libraries or dependencies.

You will gain insights into how containers function within their container engine, such as Docker, and the underlying infrastructure that supports them. For example, when you run a containerized web application using Docker, the Docker Engine manages the lifecycle of the container, allowing it to communicate with the host system and other containers seamlessly.

Additionally, this article will guide you through the practical aspects of working with containers. You will learn how to:

- **Build** container images tailored to your specific applications.
- **Choose** the right container images from available repositories to meet your needs.
- **Deploy** container images effectively in various environments.

## Structure of a Container Image

To build a container for your application, you must start with a container image. A container image is a static, immutable filesystem bundle that serves as a blueprint for creating containers. Think of it as a snapshot of everything needed to run an application in a self-contained environment.

Inside every container image is a curated collection of files, dependencies, and code necessary for executing the application. This typically includes:

- **Application Code:** The actual codebase of your application, such as Python scripts, Java classes, or compiled binaries.
- **Dependencies:** Libraries and packages required by your application to function correctly. For example, a Node.js application might include the node_modules directory, while a Java application might contain specific JAR files.
- **Configuration Files:** Files that define environment variables, settings, or other configurations needed for the application to run smoothly.
- **Runtime Environment:** The base operating system layer, which can vary depending on the image you choose. For instance, you might use an Ubuntu base image or a lightweight Alpine Linux image.

At runtime, when a container is instantiated from an image, the resultant container inherits all characteristics of the container image it is based on. This means that the container will have access to all the files and configurations specified in the image, allowing it to run the application as intended. **For example,** if you create a container from an image that includes a web server and your application code, the container will be able to serve web requests immediately upon startup, with all necessary dependencies already in place.

![A container built from an image inherits all characterisitcs of the image it is built from.](image_to_container.png)

To start creating a container image, you must first select a *base image*. A base image is a foundational image that can be built upon through the addition of image *layers*. Typically, base images come pre-bundled with a specific Linux distribution. Every distribution differs in its size, dependencies, and functionality, making certain distributions better suited for certain images over others.

For example, to select a Python base image, you might use:

```bash
FROM cgr.dev/chainguard/python:latest
```

After selecting a base image, there are a few different ways you can introduce tailored functionality (such as your application-specific code or dependencies) to the image. Many developers today use [Docker](https://www.docker.com/).Docker allows developers to deploy containerized applications efficiently and uses a configuration file known as a Dockerfile. This Dockerfile is a machine-readable document that outlines the instructions for assembling an image, layer by layer. 

In addition to Docker, there are other tools available for building container images, such as **apko** and **ko**. These tools take a different approach to image construction, typically producing single-layer images.

- **[apko](/open-source/apko/overview/)**: Designed to work seamlessly with Alpine and similar distributions, apko simplifies the image-building process by allowing you to define your image requirements in a straightforward manner.
- **[ko](https://github.com/ko-build/ko)**: This tool is particularly useful for building images directly from Go applications, enabling developers to build and deploy applications in a streamlined fashion.

For instance, If you want to build a container to run your Python application. You can start your container image with a Python base image, such as a [Wolfi-based image](/open-source/wolfi/wolfi-with-dockerfiles/). Once you have your base image, you can enhance it by adding your application code and any relevant dependencies to the image through the layers in a Dockerfile. After completing the configuration in your Dockerfile, the resulting image will be ready for deployment, containing your Python application bundled within. This approach not only simplifies the deployment process but also guarantees that your application runs consistently across different environments.

For a practical example of how to create a Python application using a Wolfi-based image, you can explore [Getting Started with the Python Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/)

## Instantiating Containers

Once you have selected or assembled a container image for your application, the next step is to instantiate a running container from that image. To deploy live containers, you will need a container engine. This software is responsible for managing and orchestrating multiple containers on a single machine, enabling them to run concurrently while sharing system resources. The container engine ensures that each container operates in its own isolated environment, allowing for efficient resource utilization and seamless application deployment. [Docker Engine](https://docs.docker.com/engine/) is a prominent example of a container engine.

*The following graphic depicts  hierarchical relationship between containers and the container engine.*

![Containers run independently of each other on a container engine, the software that communicates with a host operating system kernel. Each container contains the application and dependencies it needs to run.](container_structure.png)

## Getting Started with Containers

Depending on your application’s requirements, you may not need to build your own container images from scratch. Instead, you can easily pull pre-built container images from a *container registry*. These registries serve as centralized repositories where a wide variety of images are available for download and use. A popular container registry, [Docker Hub](https://hub.docker.com/), hosts hundreds of thousands of open source container images that can be pulled and used. Other notable container registries include the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) and the [Google Container Registry](https://console.cloud.google.com/marketplace/product/google-cloud-platform/container-registry). Additionally, the [Chainguard Registry](/chainguard/chainguard-registry/overview/) offers a free public catalog of secure, minimal base images that provide a strong foundation for containerizing your applications.

When selecting a container image for your application, there are several important factors to consider to ensure optimal performance, security, and reliability. At a minimum, your chosen container image should include the core packages and components necessary to support your application. However, with thousands of options available, it’s crucial to evaluate which images are best suited for your specific use case.

Here are some key considerations when choosing a container image:

- **Core Functionality:** Ensure that the image contains all the essential libraries and dependencies your application needs to run effectively.
- **Security:** Opt for images that are regularly updated and maintained. Images that are frequently patched reduce the risk of vulnerabilities. Look for images that have been scanned for security issues and adhere to best practices for container security.
- **Minimalism:** Choose lightweight images that contain only the necessary components for your application. Images that include unnecessary packages can increase the attack surface and contribute to higher data egress costs. Minimal images also tend to have faster startup times and consume fewer resources.
- **Reliability:** Consider the reputation of the image and the community or organization that maintains it. Well-established images with a strong user base are likely to be more reliable.
- **Compatibility:** Ensure that the container image is compatible with your application’s requirements and the container orchestration platform you plan to use, such as Kubernetes or Docker Swarm.
- **Documentation and Support:** Look for images that come with comprehensive documentation and community support. This can be invaluable when troubleshooting issues or seeking guidance on best practices.

To learn more about choosing a container image that is right for your applications, check out our article on Chainguard Academy [Selecting a Base Image](/software-security/selecting-a-base-image/).

## Learn More

This article covered the fundamentals of container technology, including the processes involved in building container images tailored to your specific needs. You learned how to deploy containers from images for your applications using a container engine. Additionally, you explored various container registries from which you can pull images for your next project.

To get started with using containers for the first time, check out our documentation on [Chainguard Images](/chainguard/chainguard-images/), our hardened, minimal images ideal for deploying secure containerized applications. If you want to build your own images, check out [Wolfi](/open-source/wolfi/), the Linux undistro ideal as a base of lightweight containers. Lastly, you may also be interested in learning about the Open Container Initiative (OCI), which establishes standards for image formats, runtimes, and distributions. We encourage you to check out our article titled ["What is the Open Container Initiative?"](/open-source/oci/what-is-the-oci/).
