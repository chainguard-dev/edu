---
title: "Build Java Containers with Jib"
linktitle: "Jib"
type: "article"
description: "In this tutorial, you'll learn how to build minimal Java containers using Jib and Chainguard base images"
date: 2025-09-23:49:31+00:00
lastmod: 2025-09-23:49:31+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 001
toc: true
---

[Google's Jib](https://github.com/GoogleContainerTools/jib) is a container
image build tool designed specifically for Java applications. Unlike other
approaches, Jib does not depend on Docker or require users to write
Dockerfiles. Instead, Jib integrates directly with the Maven and Gradle build
systems to create container images for Java applications. When paired with
[Chainguard Java
Containers](https://images.chainguard.dev/directory/image/jre/versions), Jib
provides a streamlined path to building secure, minimal container images for
Java applications.

This tutorial will walk you through building a demo application with Maven,
Jib, and Chainguard Containers.  

## Prerequisites

Before proceeding, you'll need to meet the following requirements:

 - A Linux or macOS system with terminal access
 - Java Development Kit (JDK) 21 or later installed
 - Maven 3.6+ installed
 - Docker to test the containerized application

## Understanding Chainguard Java Images

Chainguard provides several Java-related images optimized for different use
cases. Understanding which image to use depends on your application's
requirements:

 - cgr.dev/chainguard/jre: Java Runtime Environment only; for running pre-compiled Java applications
 - cgr.dev/chainguard/jdk: Full Java Development Kit; use if your build process requires compilation within the container
 - cgr.dev/chainguard/maven: Pre-configured with Apache Maven for build environments
 - cgr.dev/chainguard/gradle: Pre-configured with Gradle for build environments

For most production applications built with Jib, the JRE image is appropriate
since Jib handles the compilation outside the container. 

You can verify the version of Java in a container as follows:

```
docker run --rm cgr.dev/chainguard/jre:latest -version
```

This will display the Java version information from the image:

```
openjdk version "24.0.2" 2025-07-15
OpenJDK Runtime Environment (build 24.0.2+-wolfi-r5)
OpenJDK 64-Bit Server VM (build 24.0.2+-wolfi-r5, mixed mode, sharing)
```

Note that the latest version of the JRE (currently 24) is freely available from
Chainguard but access to other versions requires a subscription.


## Step 1 — Creating a Demo Java Application

Start by creating a demo Java application to demonstrate Jib's containerization
capabilities. This example uses a basic Spring Boot application, but the
principles apply to any Java application.

Create a new directory for your project and navigate into it:

```shell
mkdir jib-demo
cd jib-demo
```

Next, create the following source code directory for your application:

```shell
mkdir -p src/main/java/com/example/demo
```

You can now create the main application class. The following command creates a
new `DemoApplication.java` file defining a Spring Boot application with two
endpoints that you can use to verify that the containerized application works
correctly:

```
cat > src/main/java/com/example/demo/DemoApplication.java <<EOF
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @GetMapping("/")
    public String hello() {
        return "Hello from Jib and Chainguard!";
    }

    @GetMapping("/health")
    public String health() {
        return "Application is healthy";
    }
}
EOF
```

The application is bootstrapped, but still needs build details for Maven. The
following command will create the pom.xml file with basic build settings for
Java 21:

cat > pom.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0           http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>jib-demo</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>
  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <maven.compiler.target>21</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.build.timestamp.format>yyyyMMddHHmmss</maven.build.timestamp.format>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
      <version>3.5.5</version>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <version>3.5.5</version>
        <executions>
          <execution>
            <goals>
              <goal>repackage</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
EOF

To run the build, run the following command:

```
mvn clean install 
```

Observe the  output indicating that the build was successful:

```
...
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  6.741 s
[INFO] Finished at: 2025-08-19T16:54:25+02:00
[INFO] -
```

Now you can run the application with the following command:

```
java -jar target/jib-demo-1.0.0.jar
```

The application exposes a web server on port `8080`. You can test the application
with a `curl` request from another terminal window: 

```
curl localhost:8080
```

You should get output like the following:

```
Hello from Jib and Chainguard!
```

After validating that the application builds successfully and works as
expected, you can stop the server by pressing `Ctrl+C` in the terminal where it's
running.

## Step 2 — Configuring Jib with Chainguard Containers

The next step is to include and configure Jib as a plugin in the `pom.xml`
file. 

Locate the `<plugins>` section of your `pom.xml` file. Add the Jib plugin
definition like this:

```
      <plugin>
        <groupId>com.google.cloud.tools</groupId>
        <artifactId>jib-maven-plugin</artifactId>
        <version>3.4.6</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>dockerBuild</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <from>
            <image>cgr.dev/chainguard/jre:latest</image>
            <platforms>
              <platform>
                <os>linux</os>
                <architecture>amd64</architecture>
              </platform>
              <platform>
                <os>linux</os>
                <architecture>arm64</architecture>
              </platform>
            </platforms>
          </from>
          <to>
            <image>linky</image>
          </to>
          <container>
            <ports>
              <port>8080</port>
            </ports>
            <creationTime>USE_CURRENT_TIMESTAMP</creationTime>
          </container>
        </configuration>
      </plugin>
```


The configuration specifies several settings:

  - **Build goal**: The execution goal is defined as `dockerBuild`. This will build a container image for the application and then load the built image into the local Docker instance, allowing you to immediately run and test the container. 
  - **Base (or "from") image**: Uses Chainguard's JRE image (`cgr.dev/chainguard/jre:latest`). This example explicitly specifies both `arm64` and `amd64` architectures. If you don't do this, Jib will build an `amd64` image only, regardless of host architecture. 
  - **Target image**: Name of the image to build (`linky`). The tag will default to `latest` if not specified.
  - **Port**: Documents that port `8080` is used for the Spring Boot application
  - **Creation time**: Uses the current timestamp


## Step 3 — Building Container Images with Jib

With Jib configured, you can now build your containerized Java application.
Because we have specified `dockerBuild` as the execution goal, this step will
require a local Docker install. If you want to avoid using Docker and push the
image straight to a registry, jump to step 5.

Run:

```shell
mvn clean install
```

You’ll get output like the following:

```
...
[WARNING] Detected multi-platform configuration, only building image that matches the local Docker Engine's os and architecture (linux/arm64) or the first platform specified
[INFO]
[INFO]
[INFO] Container entrypoint set to [java, -cp, @/app/jib-classpath-file, com.example.demo.DemoApplication]
[INFO] Container entrypoint set to [java, -cp, @/app/jib-classpath-file, com.example.demo.DemoApplication]
[INFO]
[INFO] Built image to Docker daemon as linky
...
```


This command has compiled the application, built the container, and loaded it
into the local Docker instance.

To verify that the image was built:

```shell
docker images linky
```

Which will provide details on the new image:

```
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
linky        latest    43171844f68e   3 minutes ago   465MB
```

You should also scan the image for CVEs. This example uses
[grype](https://github.com/anchore/grype), but you can use your preferred
scanner: 

```
grype linky
```

This should give you output similar to the following:

```
✔ Vulnerability DB                [updated]
 ✔ Loaded image                                                                 linky:latest
 ✔ Parsed image                    sha256:078478c4d49bae684d8337c3a97df00722f7d1c0d8507e6e1ae
 ✔ Cataloged contents              a7123bf3bfc2296155ab226593f9f0d79b322c29da5d94af90fdc267cc
   ├── ✔ Packages                        [75 packages]
   ├── ✔ File metadata                   [1,391 locations]
   ├── ✔ Executables                     [124 executables]
   └── ✔ File digests                    [1,391 files]
 ✔ Scanned for vulnerabilities     [0 vulnerability matches]
   ├── by severity: 0 critical, 0 high, 0 medium, 0 low, 0 negligible
No vulnerabilities found
```

In this case, there were no CVEs found. Try comparing those results to images built with different base images.

## Step 4 — Testing the Containerized Application

After building your container image, test it to ensure it works correctly.
Start by running the container locally:

```shell
docker run -p 8080:8080 linky
```

The application will start, and you'll see Spring Boot's startup logs. In a
separate terminal, test the endpoints:

```shell
curl http://localhost:8080/
```

This should return:

```
Hello from Jib and Chainguard!
```

Test the health endpoint:

```shell
curl http://localhost:8080/health
```

Expected output:

```
Application is healthy
```

Stop the container by pressing `Ctrl+C` in the terminal where it's running.

## Step 5 — Building and pushing to a remote registry

One of the strongest points of jib is that you don't need Docker installed to
build and distribute container images. In this step we will change `pom.xml` to
push the image directly to a container registry.

This example uses `ttl.sh`, which is a free-to-use Docker registry for short-lived hosting of images. You can also change the code to use your own registry such as a local one or the Docker Hub.

Replace the previous plugin definition with this one (or add this one if you skipped step 3):


```xml
 <plugin>
        <groupId>com.google.cloud.tools</groupId>
        <artifactId>jib-maven-plugin</artifactId>
        <version>3.4.6</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>build</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <from>
            <image>cgr.dev/chainguard/jre:latest</image>
            <platforms>
              <platform>
                <os>linux</os>
                <architecture>amd64</architecture>
              </platform>
              <platform>
                <os>linux</os>
                <architecture>arm64</architecture>
              </platform>
            </platforms>
          </from>
          <to>
            <image>ttl.sh/jib-demo-${maven.build.timestamp}:20m</image>
          </to>
          <container>
            <ports>
              <port>8080</port>
            </ports>
            <creationTime>USE_CURRENT_TIMESTAMP</creationTime>
          </container>
        </configuration>
      </plugin>
```

This contains a couple of changes:

  - The execution goal is now `build`. This will push to the registry rather than the
local Docker instance.  
  - The image name now refers to the `ttl.sh` registry and includes a timestamp for uniqueness.

Run the build again:     

```shell
mvn clean install
```

You’ll get output like this:

```
...
[INFO] Using base image with digest: sha256:e210680d61b774aa26e76d169ecc036d1fd90e1e5bada56818747cf2b848e2ea
[INFO]
[INFO] Container entrypoint set to [java, -cp, @/app/jib-classpath-file, com.example.demo.DemoApplication]
[INFO]
[INFO] Container entrypoint set to [java, -cp, @/app/jib-classpath-file, com.example.demo.DemoApplication]
[INFO]
[INFO] Built and pushed image as ttl.sh/jib-demo-20250912095951:20m
...
```

The image name is parameterised with a timestamp, so yours will look different.
The image won't be in your local Docker instance, but you can pull it as
normal:

```shell
docker pull ttl.sh/jib-demo-20250912095951:20m
```


The `ttl.sh` registry is only for temporary testing of images and your image
will be deleted in 20 minutes. 

This time the built image is a multi-platform image -- if you pull the image
from an `amd64` host you will get the `amd64` version and if you pull from an
`arm64` host you will get the `arm64` version. You can also force the platform
when pulling:

```shell
docker pull --platform amd64 ttl.sh/jib-demo-20250912095951:20m
```

## Other Features

### Building a tar archive

If you want a local copy of the image as a file that can be later loaded by a
container runtime or saved to a file server, you can instead build the image as
a tar archive.

This doesn't work for multiplatform images unfortunately, so to test you will
need to remove one of the platforms in the from definition. (Or alternatively,
pull the architecture setting into a parameter.)

The following plugin definition will build a tarball for the amd64 platform:

```xml
<plugin>
        <groupId>com.google.cloud.tools</groupId>
        <artifactId>jib-maven-plugin</artifactId>
        <version>3.4.6</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>buildTar</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <from>
            <image>cgr.dev/chainguard/jre:latest</image>
            <platforms>
              <platform>
                <os>linux</os>
                <architecture>amd64</architecture>
              </platform>
            </platforms>
          </from>
          <to>
            <image>linky</image>
          </to>
          <container>
            <ports>
              <port>8080</port>
            </ports>
            <creationTime>USE_CURRENT_TIMESTAMP</creationTime>
          </container>
        </configuration>
      </plugin>
```


After replacing the plugin definition, run:

```shell
mvn clean install
```
     
And the output should give you the location of the built tarball:

```
...
[INFO]
[INFO] Built image tarball at /Users/amouat/proj/jib-demo/target/jib-image.tar
...
```

You can directly load this tarball into Docker:

```shell
docker load < target/jib-image.tar
```

This should respond with the name of the built image:

```
Loaded image: linky:latest
```

If required, the image can then be retagged and pushed to a registry.

### Calling goals directly

In these examples, you've been editing the pom.xml to configure the execution goal. You can also directly call these from Maven e.g:

```shell
mvn install jib:dockerBuild
```

For full details of Jib plugin configuration and features, see the [guide on GitHub](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin).

## Next Steps

You've successfully containerized a Java application using Jib and Chainguard's
minimal container images. This approach provides several advantages: improved
security through minimal base images, faster builds through layer optimization,
and simplified CI/CD integration without Docker daemon requirements.

To continue learning about container security and optimization for the Java ecosystem, consider exploring:

  - [Chainguard Libraries for
    Java](https://edu.chainguard.dev/chainguard/libraries/java/overview/):
provides enhanced security for the Java ecosystem by rebuilding popular Maven
dependencies with the latest patches and comprehensive supply chain protection.

  - [How to Migrate a Java Application to Chainguard
    Images](https://edu.chainguard.dev/chainguard/migration/migration-guides/java-images/):
in this video, learn how to migrate Java applications to Chainguard Containers
for reduced vulnerabilities, smaller images, and comprehensive JDK/JRE support
with daily security updates.  

By combining Jib's build optimization with Chainguard's security-focused
images, you've established a foundation for building secure, efficient
container images as part of your Java development workflow.

