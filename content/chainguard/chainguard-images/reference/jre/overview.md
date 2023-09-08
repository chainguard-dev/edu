---
title: "Image Overview: jre"
type: "article"
description: "Overview: jre Chainguard Image"
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

[cgr.dev/chainguard/jre](https://github.com/chainguard-images/images/tree/main/images/jre)

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 7th | `sha256:4b2fa1c7c92983084973be241267d17afb709ac8829da045d6ac716336f56b4a` |
|  `latest`     | September 7th | `sha256:067446d9df89ac3cbf0201945a738646ff53ee3531511a666b4dca108a8e64f6` |



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

