---
title: "Image Overview: jre"
type: "article"
description: "Overview: jre Chainguard Images"
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

`stable` [cgr.dev/chainguard/jre](https://github.com/chainguard-images/images/tree/main/images/jre)
| Tags             | Aliases                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------|
| `latest`         | `openjdk17`, `openjdk17.0`, `openjdk17.0.8`, `openjdk17.0.8.2`, `openjdk17.0.8.2-r0`                        |
| `latest-dev`     | `openjdk17-dev`, `openjdk17.0-dev`, `openjdk17.0.8-dev`, `openjdk17.0.8.2-dev`, `openjdk17.0.8.2-r0-dev`    |
| `openjdk-11`     | `openjdk11`, `openjdk11.0`, `openjdk11.0.20`, `openjdk11.0.20.2`, `openjdk11.0.20.2-r3`                     |
| `openjdk-11-dev` | `openjdk11-dev`, `openjdk11.0-dev`, `openjdk11.0.20-dev`, `openjdk11.0.20.2-dev`, `openjdk11.0.20.2-r3-dev` |



Minimalist Wolfi-based Java JRE image using OpenJDK.  Used for running Java applications.

- [Documentation](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jre)
- [Getting Started Guide](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jre/overview/#use-it)
- [Provenance Information](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jre/provenance_info/)

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jre:latest
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
FROM cgr.dev/chainguard/jdk:openjdk-17

COPY HelloWolfi.java /home/build/
RUN /usr/lib/jvm/openjdk/bin/javac HelloWolfi.java

FROM cgr.dev/chainguard/jre:openjdk-17

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

