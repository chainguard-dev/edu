---
title: "Image Overview: jdk"
type: "article"
description: "Overview: jdk Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 600
toc: true
---

`stable` [cgr.dev/chainguard/jdk](https://github.com/chainguard-images/images/tree/main/images/jdk)
| Tags             | Aliases                                                               |
|------------------|-----------------------------------------------------------------------|
| `latest`         | `openjdk-17`, `openjdk-17.0`, `openjdk-17.0.6`, `openjdk-17.0.6-r1`   |
| `openjdk-11`     | `openjdk-11`, `openjdk-11.0`, `openjdk-11.0.18`, `openjdk-11.0.18-r1` |
| `latest-dev`     |                                                                       |
| `openjdk-11-dev` |                                                                       |



Java JDK image using OpenJDK via [Adoptium Temurin](https://adoptium.net/en-GB/temurin/) sources.

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
FROM cgr.dev/chainguard/jdk:openjdk-17

COPY HelloWolfi.java /home/build/
RUN /usr/lib/jvm/openjdk/bin/javac HelloWolfi.java

FROM cgr.dev/chainguard/jre:openjdk-jre-17

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
