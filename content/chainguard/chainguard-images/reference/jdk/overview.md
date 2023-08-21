---
title: "Image Overview: jdk"
type: "article"
description: "Overview: jdk Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/jdk](https://github.com/chainguard-images/images/tree/main/images/jdk)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 16th  | `sha256:bdc7bb8dae1a0bafe8a8611cd3d4650c1a565c92fd43e6a97eeb5291908a8e2b` |
|  `latest-dev` | August 16th  | `sha256:1ae92e3b382e9fae1b9f59fc62fe32df03e22057259e363559ddb14b5046372b` |



Minimalist Wolfi-based Java JDK image using OpenJDK.  Used for compiling Java applications.

- [Documentation](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jdk)
- [Getting Started Guide](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jdk/overview/#use-it)
- [Provenance Information](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jdk/provenance_info/)

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jdk:latest
```

## Use it

Create a simple Java class

```sh
cat >HelloWolfi.java <<EOL
class HelloWolfi
{
    public static void main(String args[])
    {
        System.out.println("Hello Wolfi users!");
    }
}
EOL
```

Next create a multistage Dockerfile and add the Java class

```sh
cat >Dockerfile <<EOL
FROM cgr.dev/chainguard/jdk

COPY HelloWolfi.java /home/build/
RUN javac HelloWolfi.java

FROM cgr.dev/chainguard/jre

COPY --from=0 /home/build/HelloWolfi.class /app/
CMD ["HelloWolfi"]
EOL
```

Build the image

```sh
docker build -t my-simple-java-app .
```

Run the image
```sh
docker run my-simple-java-app
```

