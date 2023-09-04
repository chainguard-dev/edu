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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 1st | `sha256:fdff829d8dc97b3cced2f3170e5719fa703b865c007e3d0e65f4c263d290e956` |
|  `latest`     | September 1st | `sha256:289823ff8a175d06551d1df3a00e695cdc4b5b73c6641adece1d2995f59fd19b` |



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

