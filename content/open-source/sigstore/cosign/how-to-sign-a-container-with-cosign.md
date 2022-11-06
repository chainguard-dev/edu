---
title: "How to Sign a Container with Cosign"
type: "article"
lead: "Container signing using Cosign"
description: "Signing containers with Cosign"
date: 2022-13-07T13:26:54+01:00
lastmod: 2022-13-07T13:26:54+01:00
draft: false
images: []
menu:
  docs:
    parent: "cosign"
weight: 003
terminalImage: gcloud:latest
toc: true
---

_An earlier version of this material was published in the [Cosign chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@204b98f35bca48c194d1868e0356bef1/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@2f0ad9cb8f124a39ab555ac8bf1a114c) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Cosign is a tool you can use to sign software artifacts, which in turn allows you to verify that you are who you say you are, and instills trust across the software ecosystem. Signing software also allows people to understand the provenance of the software, and prevents tampering. 

Let’s step through signing a container with Cosign. We are using a container to provide a sense of how you may use Sigstore with containerized workloads, but the steps we are taking to sign a container are very similar to the steps that we would take to sign any other software artifact that can be published in a container registry, and we will discuss signing blobs a little later. 

## Prerequisites

Before beginning this section, ensure that you have Docker installed and that you are running Docker Desktop if that is relevant for your operating system. For guidance on installing and using Docker, refer to the [official Docker documentation](https://docs.docker.com/get-docker/). In order to push to the Docker container registry, you will need a [Docker Hub account](https://hub.docker.com/signup). If you are familiar with using a different container registry, feel free to use that. 

Additionally, you will need Cosign installed, which you can achieve by following our [How to Install Cosign guide](../how-to-install-cosign/).

## Generating a Cosign Key Pair

Before creating your first Cosign key pair, navigate to the directory you would like your key pair to live. In our example, we will use the user directory, but you should be in the directory that makes the most sense for you. 

```sh
cd ~
```

You’ll use Cosign to create the key pair now. 

```sh
cosign generate-key-pair
```

Once you run this command, you’ll receive output asking you to create a password for the private key. It is recommended to have a password for an extra layer of security, but you can also leave this field blank, especially if you are just using this key pair for testing purposes. You’ll be prompted to enter this password twice. 

```
Enter password for private key:
Enter again:
```

Once you have entered the private key password, you’ll receive the feedback that the private key and public key were written. 

```
Private key written to cosign.key
Public key written to cosign.pub
```

Your private key, stored in the `cosign.key` file, should not be shared with anyone. Your public key, stored in the `cosign.pub` file, will be used to identify that you are the key holder who is signing your software artifacts. 

Now both of these files exist in your home user directory (don’t forget where they are!), and you can inspect them if you would like by using the `cat` command, as in:

```sh
cat ​​cosign.pub
```

You’ll get output that indicates the beginning and end of your public key, with a large string of mixed-case alphanumeric values in between.

```
-----BEGIN PUBLIC KEY-----
…
-----END PUBLIC KEY-----
```

With your keys set up, you are ready to move onto creating and signing a container. 

## Creating a Container

With your keys set up, you’ll now be creating a new container. Create a new directory within your user directory that is the same as your Docker username and, within that, a directory called `hello-container`. If you will be opting to use a registry other than Docker, feel free to use the relevant username for that registry. 

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

```
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

Make sure you are in the right directory for your Cosign key pair. 

```sh
cd ~
```

From there, you will call your registry user name and container name with the following Cosign command. Note that we are signing the image in Docker Hub with our private key which is held locally in the `cosign.key` file. 

```sh
cosign sign --key cosign.key docker-username/hello-container
```

You will be prompted for the password, even if you have left the password blank.

```
Enter password for private key: 
```

Enter your password (or press `ENTER` if you don’t have a password), and then press `ENTER`.

You’ll receive output indicating that the signature was pushed to the container registry.

```
Pushing signature to: index.docker.io/docker-username/hello-container
```

In the case of Docker Hub, on the web interface there should be a SHA (secure hash algorithm) added to the tag, enabling you to confirm that your pushed signature was registered. We’ll now manually verify the signature with Cosign.

## Verify a Container’s Signature

We’ll be demonstrating this on the container we just pushed to a registry, but you can also verify a signature on any other signed container using the same steps. While you will more likely be verifying signatures in workloads versus manually, it is still helpful to understand how everything works and is formatted.

Let’s use Cosign to verify that the formatted signature for the image matches the public key. 

```sh
cosign verify --key cosign.pub docker-username/hello-container
```

Here, we are passing the public key contained in the cosign.pub file to the cosign verify command. 

You should receive output indicating that the Cosign claims were validated. 

```
Verification for index.docker.io/docker-username/hello-container:latest --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key

[{"critical":{"identity":{"docker-reference":"index.docker.io/docker-username/hello-container"},"image":{"docker-manifest-digest":"sha256:690ecfd885f008330a66d08be13dc6c115a439e1cc935c04d181d7116e198f9c"},"type":"cosign container image signature"},"optional":null}]
```

The whole output will include JSON format which includes the digest of the container image, which is how we can be sure these detached signatures cover the correct image.

## Adding an Additional Signature

If multiple people are working on the same container, or you need a team signature in addition to an individual developer signature, you can add more than one signature to a container. You’ll need to generate keys specifically for each signatory. 

It may be helpful to also add the `-a` flag to add annotations so that others can check to verify different keys. For example, we’ll annotate this signature to state that this is the organization signature. 

```sh
cosign sign --key other.key -a organization=signature docker-username/hello-container
```

As before, the user signing will be prompted to enter their password for the key. When someone verifies the signatures on this key, they’ll receive the values entered in the annotation as part of the signed JSON payload under the `optional` section at the end.

```
…
[{"critical":{"identity":{"docker-reference":"index.docker.io/docker-username/hello-container"},"image":{"docker-manifest-digest":"sha256:690ecfd885f008330a66d08be13dc6c115a439e1cc935c04d181d7116e198f9c"},"type":"cosign container image signature"},"optional":{"organization":"signature"}}]
```

This container now has two signatures, with one signature that has additional annotation.
