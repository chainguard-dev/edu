---
title: "Image Overview: Jre"
type: "article"
description: "Overview: Jre Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:80920112fe2a9b9d35cabbf3e986fdb92057c3bf7f1ac67a24bbec7a35449d22` |
| `latest-dev` | 20 hours ago | `sha256:eb181693e9bd0d605b5fdb1febb55ac1568bd24accef6d54fde4887408187c19` |



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
