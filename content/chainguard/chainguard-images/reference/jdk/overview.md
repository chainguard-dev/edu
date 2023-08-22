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
|  `latest-dev` | August 17th  | `sha256:aebe68c73a82a8820fafaf6727eb78254ff493a32cc18d6dd19a0f0558f9a91f` |
|  `latest`     | August 17th  | `sha256:cc07626156ef83b4428d223e3833032d49f62aac80d1cf5c86f4f1d0e45f6ae4` |



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

