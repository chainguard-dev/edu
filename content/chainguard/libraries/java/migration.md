---
title: "Migrating a Java project to Chainguard Libraries"
type: "article"
linktitle: "Migrate to Chainguard"
description: "How to migrate an existing Java project to pull dependencies from Chainguard Libraries"
date: 2026-07-02T00:00:00+00:00
lastmod: 2026-07-02T00:00:00+00:00
tags: ["Chainguard Libraries", "Java"]
menu:
  docs:
    parent: java
    identifier: Java Migration
weight: 056
toc: true
---

Chainguard Libraries for Java provides a curated repository of packages rebuilt from upstream sources and [scanned for malware](/chainguard/libraries/overview/#malware-and-greyware-detection). Because Chainguard Libraries uses the standard Maven repository format, switching an existing project requires only a repository configuration change — no changes to your application code or dependency versions.

This guide walks through migrating an existing Java project to Chainguard Libraries, covering the two most common setups:

- Direct access — your build tool connects directly to libraries.cgr.dev. This option is faster for initial evaluation and smaller-scale setups.
- Repository manager — your build tool connects to a repository manager ([Cloudsmith](/chainguard/libraries/java/global-configuration/#cloudsmith), [Google Artifact Registry](/chainguard/libraries/java/global-configuration/#google-artifact-registry), [JFrog Artifactory](/chainguard/libraries/java/global-configuration/#jfrog-artifactory), or [Sonatype Nexus](/chainguard/libraries/java/global-configuration/#sonatype-nexus-repository)), which proxies requests to Chainguard Libraries.

## Prerequisites

Before you begin, you need:

- An existing Java project
- [`chainctl` installed and authenticated](/chainguard/chainctl-usage/how-to-install-chainctl/)

### Create an entitlement

You must have an [entitlement to Chainguard Libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_create/) for Java with [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) enabled.

To create an entitlement to Chainguard Libraries for Java and enable upstream fallback, which includes a default 7-day cooldown, run the following command:

```shell
chainctl libraries entitlements create --ecosystems=JAVA --policy=CHAINGUARD_AND_UPSTREAM
```

Alternatively, you can create an entitlement in the Chainguard Console: while viewing the Java ecosystem page, follow the prompts to create an access token.

You can also configure cooldown policies after you create the entitlement. For example, to create and enforce a policy that disables the cooldown:

```shell
chainctl libraries policy create --name=java-disable-cooldown --cooldown-days=0
chainctl libraries policy enable --policy=java-disable-cooldown --ecosystem=JAVA --mode=ENFORCE
```

It can take up to 30 minutes for the fallback and cooldown policies to take effect. Learn more about cooldown and other policies in the [Chainguard Libraries Access documentation](/chainguard/libraries/access/#manage-library-policies).

> **Note**: If you choose to manage your own fallback to upstream repositories, see the following docs pages for more information: [Build configuration](/chainguard/libraries/java/build-configuration/) for direct access instructions or [Global configuration](/chainguard/libraries/java/global-configuration/) for repo manager instructions. Note that configuring a public fallback bypasses the protections provided by Chainguard.

## Step 1: Confirm your baseline build

Before making any changes, confirm your project builds cleanly against Maven Central.

{{< tabs >}}

{{% tab title="Maven" %}}

```shell
cd your-project
./mvnw install
```

{{% /tab %}}

{{% tab title="Gradle" %}}

```shell
cd your-project
./gradlew build
```

{{% /tab %}}

{{% tab title="Bazel" %}}

```shell
cd your-project
bazel build //...
```

{{% /tab %}}

{{< /tabs >}}

All dependencies should download from Central and tests should pass. This gives you a baseline to compare against after migration.

## Step 2: Generate a pull token

You must be an Owner or have the `libraries.java.pull_token_creator` permission to create a pull token.
You can [create a pull token in the Chainguard Console](/chainguard/libraries/access/#creating-pull-tokens-with-the-chainguard-console), or via `chainctl`.

The following command creates the token and populates environment variables directly. Make sure to replace `example.org` with your own Chainguard org name:

```shell
eval $(chainctl auth pull-token --parent=example.org --repository=java --name=my-java-token --output=env)
```

This results in values for the `CHAINGUARD_JAVA_IDENTITY_ID` and `CHAINGUARD_JAVA_TOKEN` variables. The token is named `my-java-token`, with a default expiration of 30 days. To configure the expiration, use the `--ttl` flag.

Learn more about command options in the [chainctl documentation](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/).

When configuring direct access, note that environment variables do not persist between terminal sessions. You must re-export them each time you open a new terminal, or add them to your shell profile. Learn more about pull tokens in the [Access documentation](https://edu.chainguard.dev/chainguard/libraries/access/).

### Do not commit credentials to version control

The Gradle `build.gradle` file and the Maven `pom.xml` are typically committed to a repository — always use environment variables for credentials rather than hardcoding token values directly in the file. Maven credentials live in `~/.m2/settings.xml`, which is outside the project directory and not committed by default, but take care not to add it to your repository. Store tokens as CI secrets referenced via environment variables instead. If you accidentally commit credentials, [delete the exposed token](/chainguard/libraries/access/#pull-token-management).

For more secure credential management, consider using a secrets manager such as 1Password CLI or Bitwarden, which can dynamically inject environment variables at runtime without storing token values in shell profiles or env files.

### Verify your setup

Run the following command for a connectivity and authentication check:

```bash
curl -u "$CHAINGUARD_JAVA_IDENTITY_ID:$CHAINGUARD_JAVA_TOKEN" \
  https://libraries.cgr.dev/java/
```

The command returns an HTML page listing repository directories. If credentials are invalid or expired, the command returns a 403 error instead of the directory listing.

## Step 3: Configure repository access

The `https://libraries.cgr.dev/java/` endpoint is also the [Chainguard Repository](/chainguard/chainguard-repository/overview/) endpoint for Java. By default, it serves only Chainguard-built artifacts. When upstream fallback is enabled for your organization, the same endpoint can also serve requested versions from Maven Central under Chainguard security controls.

### Direct access

{{< tabs >}}

{{% tab title="Maven" %}}

Maven repository and credentials configuration lives in a `settings.xml` file. For a project-local setup, place this file in the `.mvn` folder of your project and pass `-s .mvn/settings.xml` when running Maven commands. 

First, create a `.mvn` directory if it doesn't already exist:

```bash
mkdir -p .mvn
```

Next, create a `.mvn/settings.xml` file with the following content. This configuration sets the Chainguard [remediated repository](/chainguard/libraries/cve-remediation/) as the first source, followed by the standard Chainguard repository, with Maven Central set as `invalid` to avoid accidental unintended fallback to the public repository:

```xml
<settings>
  <servers>
    <server>
      <id>chainguard-remediated</id>
      <username>${env.CHAINGUARD_JAVA_IDENTITY_ID}</username>
      <password>${env.CHAINGUARD_JAVA_TOKEN}</password>
    </server>
    <server>
      <id>chainguard</id>
      <username>${env.CHAINGUARD_JAVA_IDENTITY_ID}</username>
      <password>${env.CHAINGUARD_JAVA_TOKEN}</password>
    </server>
  </servers>

  <profiles>
    <profile>
      <id>chainguard</id>
      <repositories>
        <repository>
          <id>chainguard-remediated</id>
          <url>https://libraries.cgr.dev/java-remediated/</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>false</enabled></snapshots>
        </repository>
        <repository>
          <id>chainguard</id>
          <url>https://libraries.cgr.dev/java/</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>false</enabled></snapshots>
        </repository>
        <repository>
          <id>central</id>
          <url>https://invalid</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>false</enabled></snapshots>
        </repository>
      </repositories>

      <pluginRepositories>
        <pluginRepository>
          <id>chainguard-remediated</id>
          <url>https://libraries.cgr.dev/java-remediated/</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>false</enabled></snapshots>
        </pluginRepository>
        <pluginRepository>
          <id>chainguard</id>
          <url>https://libraries.cgr.dev/java/</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>false</enabled></snapshots>
        </pluginRepository>
        <pluginRepository>
          <id>central</id>
          <url>https://invalid</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>false</enabled></snapshots>
        </pluginRepository>
      </pluginRepositories>

    </profile>
  </profiles>
  <activeProfiles>
    <activeProfile>chainguard</activeProfile>
  </activeProfiles>
</settings>
```

> **Note**: Add `.mvn/settings.xml` to your `.gitignore` to avoid accidentally committing it, since it references credentials via environment variables but should not itself be committed to version control.

{{% /tab %}}

{{% tab title="Gradle" %}}

Update the repositories block in `app/build.gradle` to point to Chainguard Libraries. If you are using the remediated repository, set it first.

> **Note**: If your project manages repositories in `settings.gradle`, add the Chainguard repositories there instead.

```build.gradle
repositories {
    maven {
        url = uri("https://libraries.cgr.dev/java-remediated/")
        credentials {
            username = providers.environmentVariable("CHAINGUARD_JAVA_IDENTITY_ID").orNull
            password = providers.environmentVariable("CHAINGUARD_JAVA_TOKEN").orNull
        }
    }
    maven {
        url = uri("https://libraries.cgr.dev/java/")
        credentials {
            username = providers.environmentVariable("CHAINGUARD_JAVA_IDENTITY_ID").orNull
            password = providers.environmentVariable("CHAINGUARD_JAVA_TOKEN").orNull
        }
    }
    mavenCentral()
}
```

If a dependency's pom file is found in Chainguard but the JAR is not, Gradle fails rather than falling back to Central automatically. If this happens, check whether a newer version of the dependency is available in Chainguard's catalog and update the version in your `build.gradle`.

{{% /tab %}}

{{% tab title="Bazel" %}}

Bazel uses `MODULE.bazel` to configure repositories via `rules_jvm_external`. The configuration described on this page uses `~/.netrc`, but note that `.netrc` only supports one set of credentials per hostname. Since all Chainguard Libraries are served from `libraries.cgr.dev`, configuring `.netrc` for Java will override credentials for any other ecosystem.

First, set up `~/.netrc` with your Chainguard credentials:

```bash
printf 'machine libraries.cgr.dev\nlogin %s\npassword %s\n' "$CHAINGUARD_JAVA_IDENTITY_ID" "$CHAINGUARD_JAVA_TOKEN" > ~/.netrc
chmod 600 ~/.netrc
```

> **Note**: `~/.netrc` stores credentials in plaintext on disk. Be careful not to copy `.netrc` into a project directory where it could be accidentally committed to version control. Use short-lived tokens and rotate them regularly. In CI environments, prefer writing credentials to a temporary `.netrc` file that is cleaned up after the build, or use your CI platform's secrets management to inject credentials as environment variables instead. If you accidentally expose credentials, [delete the exposed token](/chainguard/libraries/access/#pull-token-management).

Next, update the `MODULE.bazel` to point to Chainguard Libraries. If you are using the remediated repository, add `https://libraries.cgr.dev/java-remediated/` first:

```module.bazel
maven.install(
    artifacts = [
        # your artifacts here
    ],
    repositories = [
        "https://libraries.cgr.dev/java-remediated/",
        "https://libraries.cgr.dev/java/",
    ],
    use_credentials_from_home_netrc_file = True,
)
```

The `use_credentials_from_home_netrc_file = True` attribute tells the dependency resolver to read credentials from `~/.netrc` when authenticating with repositories. Without this flag, the `~/.netrc` is ignored, and requests to Chainguard fail authentication silently.

{{% /tab %}}

{{< /tabs >}}

### Repository manager

If your organization uses a repository manager, configure it to use Chainguard Libraries as an upstream source first. Follow the [global configuration documentation](/chainguard/libraries/java/global-configuration/) for your repository manager.

Once configured, point your build tool at your repository manager URL. In this setup, the credentials your build tool uses are your repository manager credentials — not a Chainguard pull token.

{{< tabs >}}

{{% tab title="Maven" %}}

Create or update `~/.m2/settings.xml` to point Maven at your repository manager and override Central with invalid URLs. See examples in [Chainguard's demo repository on GitHub](https://github.com/chainguard-demo/chainguard-libraries-java/tree/main/tools) for different repository managers. 

Use a configuration similar to the following. Make sure to update the credentials in the `server` section to use your repository manager account credentials, using environment variables when possible:

```xml
<settings>

  <mirrors>
    <mirror>
      <!-- Set the identifier for the server credentials for repository manager access
      must match server name in "servers" -->
      <id>example</id>
      <!-- Send all requests to the repository manager URL -->
      <mirrorOf>*</mirrorOf>
      <!-- Ordered repository group with
        - java-remediated
        - java
        - Maven central
        - anything else needed, including internal repos
      -->
      <!--<url>https://repo.example.com:8443/repository/java-all/</url>-->
      <url>http://localhost:8081/repository/java-all/</url>
    </mirror>
  </mirrors>

  <!-- Activate repo manager and override central repo from Maven itself with invalid URLs -->
  <activeProfiles>
    <activeProfile>repo-manager</activeProfile>
  </activeProfiles>
  <profiles>
    <profile>
      <id>repo-manager</id>
      <repositories>
        <repository>
          <id>central</id>
          <url>http://central</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>central</id>
          <url>http://central</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>

  <servers>
    <server>
      <id>repo-manager</id>
      <username>YOUR_REPO_MANAGER_USERNAME</username>
      <password>YOUR_REPO_MANAGER_PASSWORD</password>
    </server>
  </servers>
</settings>
```

{{% /tab %}}

{{% tab title="Gradle" %}}

Update the `repositories` block in `app/build.gradle` to point to your repository manager, removing any direct references to `mavenCentral()` or other repositories if your repository manager already proxies them:

```groovy
repositories {
    maven {
        url = uri("https://repo.example.com/java-all/")
        credentials {
            username = providers.environmentVariable("REPO_MANAGER_USERNAME").orNull
            password = providers.environmentVariable("REPO_MANAGER_PASSWORD").orNull
        }
    }
}

```

{{% /tab %}}

{{% tab title="Bazel" %}}

First, configure your repo manager authentication in `~/.netrc`:

```netrc
machine repo.example.com
login YOUR_REPO_MANAGER_USERNAME
password YOUR_REPO_MANAGER_PASSWORD
```

Then update MODULE.bazel to point to your repo manager:

```module.bazel
maven.install(
    artifacts = [
        # your artifacts here
    ],
    repositories = [
        "https://repo.example.com/java-all/",
    ],
    use_credentials_from_home_netrc_file = True,
)
```

{{% /tab %}}

{{< /tabs >}}

Replace `https://repo.example.com/java-all/` with your repo manager's virtual repository URL, and update the username and password.

## Step 4: Refresh dependencies

To force re-resolution from Chainguard, you can clear local caches or clear only relevant artifacts.

{{< tabs >}}

{{% tab title="Maven" %}}

Remove local cache:

```bash
rm -rf ~/.m2/repository
```

Remove specific artifact:

```bash
rm -rf ~/.m2/repository/<group>/<artifact>
```

{{% /tab %}}

{{% tab title="Gradle" %}}

Remove local caches and stop any running daemons:

```bash
rm -rf ~/.gradle/caches
./gradlew --stop
```

> **Note**: Run `./gradlew --stop` after clearing the Gradle cache to stop any running daemons. Skipping this step can cause build errors on the next run.

{{% /tab %}}

{{% tab title="Bazel" %}}

Remove the Bazel cache, including all downloaded artifacts and build outputs:

```shell
bazel clean --expunge
```

{{% /tab %}}

{{< /tabs >}}

## Step 5: Build the project

Run a full build and capture the output.

{{< tabs >}}

{{% tab title="Maven" %}}

```bash
cd your-project
./mvnw install 2>&1 | tee /tmp/mvn-output.txt
```

To check which repositories served completed downloads:

```bash
grep "Downloaded from" /tmp/mvn-output.txt
```

All downloads should come from `chainguard` or `chainguard-remediated`.

{{% /tab %}}

{{% tab title="Gradle" %}}

```bash
cd your-project
./gradlew build --info 2>&1 | tee /tmp/gradle-output.txt
```

{{% /tab %}}

{{% tab title="Bazel" %}}

```bash
bazel build //... 2>&1 | tee /tmp/bazel-output.txt
```

Bazel embeds the source repository URL in the cache path for each downloaded artifact.

{{% /tab %}}

{{< /tabs >}}

Look for lines beginning with `Downloaded from chainguard:` or `Downloaded from chainguard-remediated:` to confirm artifacts are being served by Chainguard.

If all artifacts download from Central, your credentials may be invalid or expired. Regenerate your pull token, re-export the pull token credentials as environment variables, then clear the cache and rebuild.

## Step 6: Verify artifacts

To check whether a specific artifact was built by Chainguard, use `chainctl libraries verify /full/path/to/artifact.jar`. Verify artifacts immediately after a clean build, before any repackaging.

{{< tabs >}}

{{% tab title="Maven" %}}

To list all downloaded JARs:

```bash
find ~/.m2/repository -name "*.jar"
```

Pick any JAR from the output to verify. For example:

```bash
chainctl libraries verify \
  ~/.m2/repository/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.jar
```

A checksum mismatch means the artifact came from Central rather than Chainguard. This can happen if the artifact was cached from a previous build. To resolve, delete the specific artifact and re-download it:

```bash
rm ~/.m2/repository/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.jar
./mvnw dependency:get -Dartifact=org.apache.commons:commons-lang3:3.13.0
```

Then run `chainctl libraries verify` again.

{{% /tab %}}

{{% tab title="Gradle" %}}

Gradle stores JARs in a content-addressed cache. To list all downloaded JARs:

```bash
find ~/.gradle/caches/ -name "*.jar"
```

This command returns the full paths of your project dependencies. Choose one of the JARs, and verify it using the full path. For example:

```bash
chainctl libraries verify ~/.gradle/caches/modules-2/files-2.1/com.google.guava/guava/20.0/c2ea0b73679bc223a7ab119afd0ece31636173bc/guava-20.0.jar
```

A checksum mismatch means the artifact came from Central rather than Chainguard. This can happen if the artifact was cached from a previous build. To resolve, delete the specific artifact and re-download it. For example:

```bash
rm -rf ~/.gradle/caches/modules-2/files-2.1/commons-collections
./gradlew dependencies
```

Then run `chainctl libraries verify` again.

{{% /tab %}}

{{% tab title="Bazel" %}}

Bazel embeds the source repository URL in the cache path, making it easy to identify which JARs came from Chainguard. Use `find` to locate a JAR. For example:

Linux:

```bash
find ~/.cache/bazel -path "*cgr.dev*" -name "jackson-databind*.jar" 2>/dev/null
```

MacOS:

```bash
find ~/Library/Caches/bazel -path "*cgr.dev*" -name "jackson-databind*.jar" 2>/dev/null
```

Then verify using the full path. For example:

```bash
chainctl libraries verify ~/Library/Caches/bazel/_bazel_example/c22a55500fa8462e9bf6b663d5366abd/external/rules_jvm_external++maven+maven/v1/https/45a0c61ea6fd977f050c5fb9ac06a69eed764595/1f4231148aeda823%40libraries.cgr.dev/java/com/fasterxml/jackson/core/jackson-databind/2.9.10/jackson-databind-2.9.10.jar
```

{{% /tab %}}

{{< /tabs >}}

A successfully verified artifact produces output similar to:

```bash
Artifact: /path/to/artifact.jar
Verification Coverage: 100.00%
```
