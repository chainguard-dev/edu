---
title: "Migrate a Java application to Chainguard Containers"
linktitle: "Java"
aliases:
- /chainguard/migration/migration-guides/java-images/
- /chainguard/chainguard-images/videos/java-images/
- /chainguard/migration/java-images/
- /chainguard/containers/videos/java-images/
- /get-started/migration/migration-guides/java-images/
- /chainguard/containers/migration/migration-guides/java-images/
description: "Learn how to port a Java Dockerfile to Chainguard's Maven, Gradle, JDK, and JRE containers, including a worked Spring Boot example and the differences from the Java images on Docker Hub"
type: "article"
date: 2024-04-02T15:21:01+00:00
lastmod: 2026-09-09T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Migration"]
images: []
weight: 020
toc: true
---

Chainguard's Java containers fill the same roles as the Java base images found on Docker Hub, such as `eclipse-temurin` and `maven`, but are built on [Wolfi](/open-source/wolfi/) with a much smaller package set. Chainguard builds its own JDK from source in Wolfi, and rebuilds these containers nightly so security patches land without manual intervention. Porting a Dockerfile takes a handful of changes, mostly around the non-root user and the absent shell, which [Differences from the Java images on Docker Hub](#differences-from-the-java-images-on-docker-hub) covers in full. For current CVE data on a specific container and tag, refer to the [JRE entry in the Chainguard Containers directory](https://images.chainguard.dev/directory/image/jre/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-java).

{{< details "What is Distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi OS?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "What are multi-stage builds?" >}}
{{< blurb/multistage >}}
{{< /details >}}

This guide is intended to help you port an existing Java Dockerfile to a Chainguard Containers base.

## Java Chainguard Containers

Chainguard publishes four containers for Java, split by the job they do:

| Container | Contents | Use it for |
| --- | --- | --- |
| [`maven`](https://images.chainguard.dev/directory/image/maven/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-java) | JDK plus Apache Maven | The build stage of a Maven project |
| [`gradle`](https://images.chainguard.dev/directory/image/gradle/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-java) | JDK plus Gradle | The build stage of a Gradle project |
| [`jdk`](https://images.chainguard.dev/directory/image/jdk/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-java) | Full Java Development Kit | Compiling inside the container without Maven or Gradle |
| [`jre`](https://images.chainguard.dev/directory/image/jre/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-java) | Java Runtime Environment only | Running a compiled JAR in production |

The `jre` container is the production target. It has no compiler, no build tooling, no shell, and no package manager, which keeps it small but also means you cannot extend it in place. The build containers include a shell and a package manager and can be extended freely.

Each of these also comes in a [development variant](/chainguard/containers/concepts/container-variants/), distinguished by the tag suffix (for example, `jre:latest-dev`). The development variants add a shell and package manager to a runtime container, which makes them useful for debugging and for the rare application that needs system tooling at runtime.

The recommended approach for migration is to use a multi-stage build: compile in `maven` or `gradle`, then copy the JAR into `jre`. This guide's [migration example](#migration-example) builds exactly that.

## Migrating from other distributions

Dockerfiles often contain commands specific to the Linux distribution they are based on. Most commonly this relates to package installation (`apt` versus `yum` versus `apk`), but it also covers the default shell (`bash` versus `ash`) and default utilities (`groupadd` versus `addgroup`). The high-level guide on [Migrating to Chainguard Containers](/chainguard/containers/migration/migrating-to-chainguard-images/) covers distro-based migration and package compatibility for Debian, Alpine, Ubuntu, and Red Hat UBI base images.

## Installing further dependencies

Java applications sometimes need native libraries at build time, runtime, or both. Wolfi has a large package repository, though package names may differ from other distributions.

The easiest way to search is with apk tools in a `wolfi-base` container:

```shell
docker run -it --rm cgr.dev/chainguard/wolfi-base
```

```shell
apk update
apk search freetype
```

Add the packages you find to the build stage of your Dockerfile. Note that `apk add` needs write access, so a Dockerfile that installs packages has to switch to the root user first with `USER root`. For more searching tips, check the [Searching for Packages](/chainguard/containers/migration/migrating-to-chainguard-images/#searching-for-packages) section of the base migration guide.

## Differences from the Java images on Docker Hub

If you are migrating from Docker Hub's `maven` image or from `eclipse-temurin`, a few differences matter:

- **The containers run as a non-root user.** UID `65532` is the default, where the Docker Hub images run as root. If a build step needs elevated privileges, add `USER root` before it, and switch back for the production stage.
- **`WORKDIR` differs by container.** It is `/app` in `jre`, and `/home/build` in `maven`, `gradle`, and `jdk`.
- **The entrypoint is the tool, not a shell.** `jre` sets `/usr/bin/java` and `maven` sets `/usr/bin/mvn`, so arguments you pass to `docker run` go to that program. For example, `docker run cgr.dev/chainguard/jre:latest -version` prints the container's Java version. To get a shell you need a `-dev` variant and an explicit entrypoint override: `docker run --entrypoint /bin/sh -it cgr.dev/chainguard/jre:latest-dev`.
- **`JAVA_HOME` is `/usr/lib/jvm/default-jvm`.** Scripts that hardcode a Temurin path need updating.
- **There are far fewer libraries and utilities present.** An application may turn out to have a dependency the container doesn't carry, which you need to add explicitly.

## Migration example

This example ports a Spring Boot application from Docker Hub's `maven` image to Chainguard's Maven and JRE containers, in two steps. The application listens on port `8080` and answers `/hello`. Its source is in the [`learning-labs-java` repository](https://github.com/chainguard-dev/learning-labs-java):

```shell
git clone https://github.com/chainguard-dev/learning-labs-java.git
cd learning-labs-java
```

Each step writes a new Dockerfile rather than editing one in place, so you can build all three and compare them side by side. The repository ships its own `Dockerfile` variants from when the accompanying video was recorded, but those pin container digests from 2024; the files you create here track current tags instead, which is what makes the size and CVE comparison meaningful.

### The starting point

Save the following as `Dockerfile.classic`. This Dockerfile is a single-stage build on Docker Hub's `maven` image, which is itself built on Eclipse Temurin:

```Dockerfile
FROM maven:latest

WORKDIR /work

COPY src/ src/
COPY pom.xml pom.xml

RUN mvn clean package

WORKDIR /app
RUN cp /work/target/java-demo-app-1.0.0.jar .

ENTRYPOINT ["java", "-jar", "java-demo-app-1.0.0.jar"]
```

Build and run it:

```shell
docker build -f Dockerfile.classic -t java-maven .
docker run --rm -d --name java-demo -p 8080:8080 java-maven
curl localhost:8080/hello
docker stop java-demo
```

The result is a working application in a large container. Everything Maven needed in order to build the JAR is still sitting in the image that runs it.

### Step 1: change the base container

Copy `Dockerfile.classic` to `Dockerfile.cg` and change a single line, the `FROM` instruction:

```Dockerfile
FROM cgr.dev/chainguard/maven:latest
```

The remainder of the file is unchanged. Build it under a new tag to allow a direct comparison:

```shell
docker build -f Dockerfile.cg -t java-maven-cg .
```

That single line cuts the image size substantially, and clears out the operating-system package findings a scanner reports, because there are far fewer packages left to report on. Compare the two directly:

```shell
docker images | grep java-maven
grype java-maven
grype java-maven-cg
```

This base swap replaces the operating system underneath your application, so findings against distribution packages largely go away. It does not touch your application's own dependencies: the JARs Maven resolved from `pom.xml` are identical in both images, so any CVEs in those survive the change. Fixing those means updating the dependencies themselves, which is what [Chainguard Libraries for Java](/chainguard/libraries/java/overview/) addresses.

If you prefer Docker Hub to `cgr.dev`, Chainguard's Free containers are mirrored there under the `chainguard` organization, so `FROM chainguard/maven:latest` also works.

### Step 2: split the build into two stages

The container still carries Maven and a full JDK into production. A multi-stage build compiles in the Maven container and copies only the JAR into the JRE container. Save the following as `Dockerfile.cg-multi`:

```Dockerfile
FROM cgr.dev/chainguard/maven:latest AS builder

WORKDIR /work

COPY src/ src/
COPY pom.xml pom.xml

RUN mvn clean package

FROM cgr.dev/chainguard/jre:latest AS runner

WORKDIR /app

COPY --from=builder /work/target/java-demo-app-1.0.0.jar .

ENTRYPOINT ["java", "-jar", "java-demo-app-1.0.0.jar"]
```

```shell
docker build -f Dockerfile.cg-multi -t java-maven-multi-cg .
docker run --rm -d --name java-demo -p 8080:8080 java-maven-multi-cg
curl localhost:8080/hello
docker stop java-demo
```

The application behaves the same, in a container roughly 250 MB smaller than the single-stage Chainguard build, because the build tooling never reaches the final stage. The `jre` container also has no shell, so there is nothing for an attacker who reaches the container to run.

This step cuts scanner findings a second time, and for a different reason than the base swap did. A single-stage build ships Maven's own bundled JARs and everything it downloaded into the local repository, and a scanner reports on all of them. Only the application JAR survives the copy into the final stage:

```shell
grype java-maven-multi-cg
```

There are two important things to note on the `COPY` line. The JAR filename comes from the project's `pom.xml`, so it differs in your application; a wildcard such as `COPY --from=builder /work/target/*.jar app.jar` avoids restating the version. Additionally, because `jre` already sets `WORKDIR` to `/app`, the `WORKDIR` line in the runner stage is explicit rather than required.

### Video demonstration

The following video walks through the same migration outlined in the previous steps:

{{< youtube FYOVcSv1-oY >}}

## Additional resources

- The [JRE container documentation](https://images.chainguard.dev/directory/image/jre/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-java) has full details on the Java containers, including usage, provenance, and security advisories.
- [Build Java containers with Jib](/chainguard/containers/building-and-modifying/build-tools/building-java-containers-with-jib/) covers building Java containers without writing a Dockerfile at all, using Jib's Maven and Gradle plugins.
- [Building minimal container images](/chainguard/containers/building-and-modifying/building-minimal-containers/) explains the multi-stage pattern this guide uses, and when a runtime container is the right final base.
- [Fully bootstrapping Java from source in Wolfi](https://www.chainguard.dev/unchained/fully-bootstrapping-java-from-source-in-wolfi) describes how Chainguard builds its JDK.
- [Debugging distroless container images](/chainguard/containers/troubleshooting/debugging-distroless-images/) covers working with a production container that has no shell.
- [How to port a sample application to Chainguard Containers](/chainguard/containers/migration/porting-apps-to-chainguard/) works through porting a legacy application.
