---
title: "How to Sign Blobs and Standard Files with Cosign"
type: "article"
description: "Use Cosign to sign non-container software artifacts"
lead: "Cosign can sign software artifacts beyond containers"
date: 2022-13-07T15:22:20+01:00
lastmod: 2022-13-07T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "cosign"
weight: 620
toc: true
---

_An earlier version of this material was published in the [Cosign chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@204b98f35bca48c194d1868e0356bef1/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@2f0ad9cb8f124a39ab555ac8bf1a114c) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Cosign can sign more than just containers. Blobs, or binary large objects, and standard files can be signed in a similar way. You can publish a blob or other artifact to an OCI (Open Container Initiative) registry with Cosign. 

First, we’ll create an artifact (in this case, a standard file that contains text). We’ll call the file `artifact` and fill it with the “hello, cosign” text.

```sh
echo "hello, cosign" > artifact
```

Cosign offers support for signing blobs with the `cosign sign-blob` and `cosign verify-blob` commands. To sign our file, we’ll pass our signing key and the name of our file to the `cosign sign-blob` command.

```sh
cosign sign-blob --key cosign.key artifact
```

You’ll get output similar to the following, and a prompt to enter your password for your signing key. 

```
Using payload from: artifact
Enter password for private key:
```

With your password entered, you’ll receive your signature output. 

```
MEUCIAb9Jxbbk9w8QF4/m5ADd+AvvT6pm/gp0HE6RMPp3SfOAiEAsWnpkaVZanjhQDyk5b0UPnlsMhodCcvYaGl1sj9exJI= 
```

You will need this signature output to verify the artifact signature. Use the `cosign verify-blob` command and pass in the public key, the signature, and the name of your file. 

```sh
cosign verify-blob --key cosign.pub --signature MEUCIAb9Jxbbk9w8QF4/m5ADd+AvvT6pm/gp0HE6RMPp3SfOAiEAsWnpkaVZanjhQDyk5b0UPnlsMhodCcvYaGl1sj9exJI= artifact  
```

Note that the whole output of the signature needed to be passed to this command. You’ll get feedback that the blob’s signature was verified.

```
Verified OK
```

You can also publish the artifact to a container registry such as Docker Hub and sign the artifact’s generated image with Cosign. Running this command will create a new repository in your Docker Hub account . We will call this `artifact` but you can use an alternate meaningful name for you. 

```sh
cosign upload blob -f artifact docker-username/artifact
```

You’ll receive feedback that the file was uploaded, and it will already have the SHA signature as part of the artifact.

```
Uploading file from [artifact] to [index.docker.io/docker-username/artifact:latest] with media type [text/plain]
File [artifact] is available directly at [index.docker.io/v2/docker-username/artifact/blobs/sha256:dcf8ff…
Uploaded image to:
index.docker.io/docker-username/artifact@sha256:d10846…
```

Being able to sign blobs provides you with the opportunity to sign README files and scripts rather than just containers. This can ensure that every piece of a software project is accounted for through signatures and provenance. 
