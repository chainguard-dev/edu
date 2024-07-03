---
title: "Image Overview: jre"
linktitle: "jre"
type: "article"
layout: "single"
description: "Overview: jre Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Java JRE image using [OpenJDK](https://openjdk.org/projects/jdk/). Used for running Java applications.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jre:latest
```


<!--body:start-->

The latest builds of Chainguard's JRE image passes the TCK for OpenJDK Java 21.0.3 and Java 22.0.1 as provided by (Oracle under the OpenJDK Community TCK License Agreement)[https://openjdk.org/groups/conformance/JckAccess/index.html] (OCTLA) and are Java Compatibility Kit (JCK) conformant.

## Java Application Example

This section outlines how you can build a Java application with the Chainguard JRE Image.

Start by creating a sample Java class named `HelloWolfi.java`:

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

Then create a multistage Dockerfile, adding the Java class you just created:

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

Following that, you can build the image:

```sh
docker build -t my-java-app .
```

Note that this example tags the image with `my-java-app`. You can now run the image by referencing this tag, as in the following command:

```sh
docker run my-java-app
```
```
Hello Wolfi users!
```
<!--body:end-->

