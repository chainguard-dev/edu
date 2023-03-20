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
weight: 500
toc: true
---

`stable` [cgr.dev/chainguard/jdk](https://github.com/chainguard-images/images/tree/main/images/jdk)
| Tags             | Aliases                                                                               |
|------------------|---------------------------------------------------------------------------------------|
| `latest`         | `openjdk-17`, `openjdk-17.0`, `openjdk-17.0.6`, `openjdk-17.0.6-r1`                   |
| `latest-dev`     | `openjdk-17-dev`, `openjdk-17.0-dev`, `openjdk-17.0.6-dev`, `openjdk-17.0.6-r1-dev`   |
| `openjdk-11`     | `openjdk-11`, `openjdk-11.0`, `openjdk-11.0.18`, `openjdk-11.0.18-r1`                 |
| `openjdk-11-dev` | `openjdk-11-dev`, `openjdk-11.0-dev`, `openjdk-11.0.18-dev`, `openjdk-11.0.18-r1-dev` |



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
