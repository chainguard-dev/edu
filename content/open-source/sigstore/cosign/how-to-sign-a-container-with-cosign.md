---
title: "How to Sign a Container with Cosign"
type: "article"
lead: "Container signing using Cosign"
description: "Signing containers with Cosign"
date: 2022-07-13T13:26:54+01:00
lastmod: 2024-07-29T15:12:18+00:00
draft: false
tags: ["Cosign", "Procedural"]
images: []
menu:
  docs:
    parent: "cosign"
weight: 003
terminalImage: cosign:latest
toc: true
---

_An earlier version of this material was published in the [Cosign chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@204b98f35bca48c194d1868e0356bef1/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@2f0ad9cb8f124a39ab555ac8bf1a114c) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Cosign is a tool you can use to sign software artifacts, which in turn allows you to verify that you are who you say you are, and instills trust across the software ecosystem. Signing software also allows people to understand the provenance of the software, and prevents tampering. 

Let’s step through signing a container with Cosign. We are using a container to provide a sense of how you may use Sigstore with containerized workloads, but the steps we are taking to sign a container are very similar to the steps that we would take to sign any other software artifact that can be published in a container registry, and we will discuss signing blobs a little later. 

## Prerequisites

Before beginning this section, ensure that you have Docker installed and that you are running Docker Desktop if that is relevant for your operating system. For guidance on installing and using Docker, refer to the [official Docker documentation](https://docs.docker.com/get-docker/). In order to push to the Docker container registry, you will need a [Docker Hub account](https://hub.docker.com/signup). If you are familiar with using a different container registry, feel free to use that. 

Additionally, you will need Cosign installed, which you can achieve by following our [How to Install Cosign guide](/open-source/sigstore/cosign/how-to-install-cosign/).

## Creating a Container

You’ll now be creating a new container. Create a new directory within your user directory that is the same as your Docker username and, within that, a directory called `hello-container`. If you will be opting to use a registry other than Docker, feel free to use the relevant username for that registry. 

```sh
mkdir -p ~/docker-username/hello-container
```

Move into the directory.

```sh
cd ~/docker-username/hello-container
```

Let’s create the Dockerfile that describes the container. This will be essentially a “Hello, World” container for demonstration purposes.

Use the text editor of your choice to create the Dockerfile. You can use [Visual Studio Code](https://code.visualstudio.com/) or a command line text editor like nano. Just ensure that the file is called exactly `Dockerfile` with a titlecase and no extension. 

```sh
nano Dockerfile
```

Type the following into your editor:

```Dockerfile
FROM alpine
CMD ["echo", "Hello, Cosign!"]
```

This file is instructing the container to use the Alpine Linux distribution, which is lightweight and secure. Then, it prints a “Hello, Cosign!” message onto the command-line interface.

Once you are satisfied that your Dockerfile is the same as the text above, you can save and close the file. Now you are ready to build the container. 

## Building and Running a Container

Within the same `hello-container` directory, you can build the container. You should use the format `docker-username/image-name` to tag your image, since you'll be publishing it to a registry.

```sh
docker build -t docker-username/hello-container .
```

If you receive an error message or a “failed” message, check that your user is part of the `docker` group and that you have the right permissions to run Docker. For testing, you may also try to run the above command with `sudo`.

You should get guidance in the output that your build was successful when you receive no errors.

```
=> => naming to docker.io/docker-username/hello-container    
```

At this point your container is built and you can verify that the container is working as expected by running the container. 

```sh
docker run docker-username/hello-container
```

You should receive the expected output of the echo message you added to the Dockerfile. 

```
Hello, Cosign!
```

You can further confirm that the Docker container is among your listed containers by listing all of your active containers.

```sh
docker ps -a
```

```
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS                     PORTS     NAMES
c828db494203   hello-container   "echo 'Hello, Cosign…"   13 seconds ago   Exited (0) 9 seconds ago             confident_lamarr
```

Your output will be similar to the above, but the timestamps and name will be different.

Now that you have built your container and are satisfied that it is working as expected, you can publish and sign your container. 

## Publishing a Container to a Registry

We will be publishing our container to the Docker registry. If you are opting to use a different registry, your steps will be similar. 

At this point, you can access the Docker container registry at [hub.docker.com](https://hub.docker.com/) and create a new repository under your username called `hello-container`. We will be making this public, but you can make it private if you prefer. If you are happy for it to be public, you can skip this step as the repository will be created when pushing the container. In any case, you can delete this once you are satisfied that you have signed the container. 

Once this is set up, you can push the container you created to the Docker Hub repository. 

```sh
docker push docker-username/hello-container
```

You should be able to now access your published container via your Docker Hub account. Once you ensure that this is there, you are ready to push a signature to the container. 

## Signing a Container and Pushing the Signature to a Registry

Now that the container is in a registry (in our example, it is in Docker Hub), you are ready to sign the container and push that signature to the registry.

You will call your registry user name and container name with the following `cosign` command. Note that we are signing the image in Docker Hub keylessly with Cosign.

```sh
cosign sign docker-username/hello-container
```

You will be asked to verify that you agree with having your information in the transparency log and will be taken through an OIDC workflow.

```
Generating ephemeral keys...
Retrieving signed certificate...

	Note that there may be personally identifiable information associated with this signed artifact.
	This may include the email address associated with the account with which you authenticate.
	This information will be used for signing this artifact and will be stored in public transparency logs and cannot be removed later.

By typing 'y', you attest that you grant (or have permission to grant) and agree to have this information stored permanently in transparency logs.
Are you sure you would like to continue? [y/N] 
Your browser will now be opened to:
...
```

You’ll receive output indicating that the signature was pushed to the container registry.

```
Successfully verified SCT...
tlog entry created with index: 
Pushing signature to: index.docker.io/docker-username/hello-container
```

In the case of Docker Hub, on the web interface there should be a SHA (secure hash algorithm) added to the tag, enabling you to confirm that your pushed signature was registered. We’ll now manually verify the signature with Cosign.

## Verify a Container’s Signature

We’ll be demonstrating this on the container we just pushed to a registry, but you can also verify a signature on any other signed container using the same steps. While you will more likely be verifying signatures in workloads versus manually, it is still helpful to understand how everything works and is formatted.

Let’s use Cosign to verify that the signature exists on the transparency log and matches our expected information. You will need to know some information in order to verify the entry. You'll need to use the identity flags `--certificate-identity` which corresponds to the email address of the signer, and `--certificate-oidc-issuer` which corresponds to the OIDC provider that the signer used. For example, a Gmail account using Google as the OIDC issuer, will be able to be verified with the following command.

```sh
cosign verify \
    --certificate-identity username@gmail.com \
    --certificate-oidc-issuer https://accounts.google.com \
    docker-username/hello-container 
```

Here, we are passing the public key contained in the cosign.pub file to the `cosign verify` command. 

You should receive output indicating that the Cosign claims were validated. 

```
Verification for index.docker.io/docker-username/hello-container:latest --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key

[{"critical":{"identity":{"docker-reference":"index.docker.io/docker-username/hello-container"},"image":{"docker-manifest-digest":"sha256:690ecfd885f008330a66d08be13dc6c115a439e1cc935c04d181d7116e198f9c"},"type":"cosign container image signature"},"optional":null}]
```

The whole output will include JSON format which includes the digest of the container image, which is how we can be sure these detached signatures cover the correct image.
