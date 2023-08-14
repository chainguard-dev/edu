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
|  `latest`     | August 13th  | `sha256:365b37574279445638a6c23ed41292e822818eef6aa95102fd730c18374d05ce` |
|  `latest-dev` | August 13th  | `sha256:0bcb5c10479b358ae9841edbd4b13827398f6bac8883f28799cc6fab55385c09` |



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
RUN /usr/lib/jvm/java-17-openjdk/bin/javac HelloWolfi.java

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

