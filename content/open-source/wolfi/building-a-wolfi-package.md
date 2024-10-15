---
title: "Building a Wolfi Package"
type: "article"
description: "A deep-dive into the process of getting a new package into Wolfi OS"
date: 2023-08-21T08:49:31+00:00
lastmod: 2023-08-21T08:49:31+00:00
draft: false
tags: ["Wolfi", "Procedural"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 300
toc: true
---

Wolfi is a Linux distro created specifically for building stripped-down container images that only include the essential packages needed to run applications in containers. This makes it more secure, as there are fewer potential attack vectors due to the reduced surface area.

Thanks to a fine-tuned maintenance process combining top-notch automation and established best practices from maintainers, Wolfi packages are updated quickly. This ensures that Wolfi users get patches and latest versions of packages at a much faster pace than other distributions. Additionally, Wolfi includes a number of features that help to ensure the provenance and authenticity of packages. For example, all packages are built directly from source and signed with cryptographic signatures. This helps to prevent malicious code from being introduced into the system. Wolfi also provides a high-quality build-time [SBOM](https://edu.chainguard.dev/open-source/sbom/what-is-an-sbom/) as standard for all packages.

That being said, it's important to note that Wolfi is rather new; it just recently crossed the mark of 1,000 packages in the Wolfi OS repository. That means some packages that you would find in a more established distro won't be available yet in Wolfi. In this article, we'll cover the whole process involved in building a new Wolfi package, or how a Wolfi package comes to be.

> Note: Many of the examples shown in this article are based on the [Wolfi PHP package](https://github.com/wolfi-dev/os/blob/main/php-8.2.yaml), which is a slightly complex build that generates several subpackages from a single melange YAML file. You can keep that link open in a separate tab to use as reference as you go through this guide.

## How Does it Compile?

The first step in building a new Wolfi package is finding official documentation with guidance on how to build the package from source. All Wolfi packages need to be built from source in order to assure provenance and authenticity of package contents.

Because Wolfi uses [apk](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper) and thus has some similar design principles to Alpine, it is a good idea to review the [Alpine package index](https://pkgs.alpinelinux.org/packages) to find out how the package is built there. This can give you insights about configuration options, dependencies, and eventual subpackages that can be stripped from the main package. For example, when compiling PHP from source, you have the choice of compiling several extensions either as built-in or as shared libraries. Although compiling said extensions as built-in packages makes for a simpler build, it also increases the size of the original package and creates a wider surface for possible vulnerabilities.

If you aren't very familiar with building packages from source using tools such as `cmake` and `autoconf`, it's a good idea to compile the package locally first - you don't need to run `make install`  at the end to get the package installed on your own system, but running the `configure` and `make` processes will give you a better understanding of the build requirements and configure options.

## The melange YAML File

The melange YAML file is where you'll define the details about the package and its build pipeline. If you are familiar with GitHub Actions, you'll find out that melange definitions are very similar to GitHub Actions workflows.

### The `package` Section

The melange YAML file starts with a `package` section, used to define metadata information and runtime dependencies. The following excerpt demonstrates how this section is declared in the Wolfi [PHP package](https://github.com/wolfi-dev/os/blob/34aa71ac4898c2b7c529548eafa51b0ea7a4dbd3/php.yaml#L1C3-L1C3) YAML:

```yaml
package:
  name: php
  version: 8.2.8
  epoch: 0
  description: the PHP programming language
  copyright:
    - license: PHP-3.01
  dependencies:
    runtime:
      - libxml2
```

- **Package name**: the current convention is to use the same name as the YAML file without extension. This is what people will search for, so it's a good idea to keep it consistent with how the package is named in other distributions.
- **Description**: this information shows up when searching for the package with apk.
- **Version**: the version of the package.
- **Epoch**: a numeric field set to zero by default; this only needs to be incremented when there is a non-version change in the package. For instance, when build options such as compiler flags have changed or new subpackages have been added but the upstream package version hasn't changed — in such cases, you'd need to "bump the epoch" in order to trigger the build.
- **License**: the package license. It is important to note that only packages with OSI-approved licenses can be included in Wolfi. You can check the relevant package info in the [licenses page at opensource.org](https://opensource.org/licenses/).
- **Runtime dependencies**: any dependencies needed by your package at runtime. Not to be confused with build dependencies, these will come up in the environment section of the file.

### The `environment` Section

The next section is the `environment` section. It defines how the build environment should look in order to build your package. Packages listed in this section won't be included in the final package, because they are only needed at build time.

When building locally, you'll also need to include information about where to find Wolfi packages. This is not needed when submitting the package to the Wolfi OS repository. The `contents` node is used for that:

```yaml
environment:
  contents:
    repositories:
      - https://packages.wolfi.dev/os
    keyring:
      - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
```

The `packages` section is where you can define dependencies. The following example is an excerpt from the Wolfi PHP package, which is a fairly complex build with many dependencies:

```yaml
environment:
  contents:
    packages:
      - build-base
      - busybox
      - file
      - bison
      - libtool
      - ca-certificates-bundle
      - bzip2-dev
      - libxml2-dev
      - curl-dev
      - openssl-dev
      - readline-dev
      - sqlite-dev
      - libsodium-dev
      - libpng-dev
      - libjpeg-turbo-dev
      - libavif-dev
      - libwebp-dev
      - libxpm-dev
      - libx11-dev
      - freetype-dev
      - gmp-dev
      - icu-dev
      - openldap-dev
      - oniguruma-dev
      - libxslt-dev
      - postgresql-15-dev
      - libzip
```

Don't worry if you don't know everything you'll need upfront at build time. Even if you build the package locally first, your system most likely has many dependencies already installed; by paying attention to the output provided by melange, you will be able to figure out what is missing, and iterate until your build environment looks right.

One thing that may happen during this process is finding out that one or more dependencies needed by your package are not yet available in Wolfi, so they need to be built first. It is a normal part of the process, so don't worry — you will be able to build incrementally and test everything locally.

### The `pipeline` Section

With package metadata and build environment defined, it's time to create the pipeline that will build your package. The `pipeline` section has a structure similar to a GitHub Actions workflow, defining a series of steps that must be executed in the same order they are defined, creating output that will be packaged into one or more apk packages.

A package build pipeline typically starts with fetching the package (as a tarball or directly from a Git branch) and matching the downloaded artifact against an expected sha hash.

Some of the actions executed in build pipelines are very similar across packages: downloading a package, running configure and make, fetching a package from git, etc. Luckily for us, melange bakes a lot of repetitive tasks into reusable [pipelines](https://github.com/chainguard-dev/melange/tree/main/pkg/build/pipelines):

- Downloading Packages
  - `fetch`
  - `git-checkout`
- Autoconf
  - `autoconf/configure`
  - `autoconf/make`
  - `autoconf/make-install`
- Cmake
  - `cmake/build`
  - `cmake/configure`
  - `cmake/install`
- Go
  - `go/build`
  - `go/install`
- Meson
  - `meson/compile`
  - `meson/configure`
  - `meson/install`
- Ruby
  - `ruby/build`
  - `ruby/clean`
  - `ruby/install`
- Split
  - `split/debug`
  - `split/dev`
  - `split/infodir`
  - `split/locales`
  - `split/manpages`
  - `split/static`
- Other
  - `strip`
  - `patch`

Each pipeline can have one or more parameters that should be provided as keypairs in a `with` entry. For example, a download-and-check has the following structure in the melange YAML, using the built-in pipeline `fetch`:

```yaml
  - uses: fetch
    with:
      uri: https://libzip.org/download/libzip-${{package.version}}.tar.gz
      expected-sha256: 52a60b46182587e083b71e2b82fcaaba64dd5eb01c5b1f1bc71069a3858e40fe
```

Naturally, you can also run raw bash commands in your pipeline. The following example shows the build of [Composer](https://getcomposer.org/), the PHP package manager, which is not compiled as a typical package:

```yaml
  - name: Install Composer
    runs: |
      EXEC_DIR="${{targets.destdir}}/usr/bin"
      mkdir -p "${EXEC_DIR}"
      mv composer.phar "${EXEC_DIR}/composer"
      chmod +x "${EXEC_DIR}/composer"
```

As indicated, a pipeline step will have either a `uses` or a `run` directive. You can have as many steps as you need, and you can use special variable substitutions inside steps:

- `${{package.name}}`: Package name.
- `${{package.version}}`: Package version.
- `${{package.epoch}}`: Package epoch.
- `${{targets.destdir}}`: Directory where final package files will be stored. Everything that lives here will be packed into your final apk.
- `${{targets.subpkgdir}}`: Directory where final subpackage files will be stored. Works the same way as `targets.destdir`, but for subpackages.

You can find more details about available pipelines in the [melange pipelines documentation](https://github.com/chainguard-dev/melange/blob/main/docs/PIPELINES.md).

### The `subpackages` Section
As mentioned previously, a package may extract parts of its contents into subpackages in order to make for a slimmer final apk. Many packages have resources that are not required at execution time, including development headers, man pages, shared libraries that are optional. This part is really important in Wolfi, because we want packages to be minimal. The `subpackages` section of the melange YAML file looks a lot like the pipeline section, and it essentially works the same way. You'll just have to make sure you place any subpackage files in the `targets.subpkgdir` location.

The `split` built-in pipelines were created to facilitate the creation of subpackages. They implement code to remove development headers (`split/dev`), man pages (`split/manpages`), among other resources that aren't typically required at runtime. You can experiment with those, just be aware that they use standard path locations and some compiled packages may use different paths for certain resources.

For example, this is how a step in the subpackages section would be written, using the `split/dev` built-in pipeline to generate the `php-dev` subpackage:

```yaml
  - name: php-dev
    description: PHP 8.2 development headers
    pipeline:
      - uses: split/dev
```

### Looping with Ranges

In some cases, you may find yourself repeating the same task over and over with just a couple different values (such as package names). In such scenarios, you can define a range of data that you can "loop" through in a step. For example, let's have a look at how the PHP package uses this feature to create its subpackages.

First, we define an `extensions` range. This should go on a `data` node at the same level as the `pipelines` section of your YAML:

```yaml
data:
  - name: extensions
    items:
      bz2: Bzip2
      curl: cURL
      gd: GD imaging
      gmp: GNU GMP support
      ldap: LDAP
      mysqlnd: MySQLnd
      openssl: OpenSSL
      pdo_mysql: MySQL driver for PDO
      pdo_sqlite: SQLite 3.x driver for PDO
      soap: SOAP
      sodium: Sodium
      calendar: Calendar
```

In the subpackages section, we define a pipeline for that range:

```yaml
  - range: extensions
    name: "php-${{range.key}}"
    description: "The ${{range.value}} extension"
    pipeline:
      - runs: |
        export EXTENSIONS_DIR=usr/lib/php/modules
        export CONF_DIR="${{targets.subpkgdir}}/etc/php/conf.d"
        mkdir -p "${{targets.subpkgdir}}"/$EXTENSIONS_DIR $CONF_DIR
        mv "${{targets.destdir}}/$EXTENSIONS_DIR/${{range.key}}.so" \
          "${{targets.subpkgdir}}/$EXTENSIONS_DIR/${{range.key}}.so"
        prefix=
        [ "${{range.key}}" != "opcache" ] || prefix="zend_"
        echo "${prefix}extension=${{range.key}}.so" > $CONF_DIR/"${{range.key}}.ini"
```

And this will loop through all values of the `extensions` range and execute the described pipeline.

### The `update` Section

This final section of the YAML file is only required when submitting the package to the Wolfi OS repository. The `update` section is used by Wolfi CI/CD systems to detect new package releases.

Wolfi uses multiple tools and services to keep track of upstream releases, including the [Release Monitoring](https://release-monitoring.org/) service. For packages that are released via GitHub, tracking occurs using the project org/name and a monitored tag.

Here's an example of the update section of the PHP package, which uses the Release Monitoring service:

```yaml
update:
  enabled: true
  release-monitor:
    identifier: 3627
```
You can obtain the identifier from the [release monitoring page](https://release-monitoring.org/) - search for the package and grab the ID that shows up at the URL.

Here is another example, this time from a package that is released via GitHub:

```yaml
update:
  enabled: true
  github:
    identifier: php-amqp/php-amqp
    strip-prefix: v
    tag-filter: v
```
Again, this section is only required when submitting the package to Wolfi. For more details about Wolfi's automated package updates, check [the official docs](https://github.com/wolfi-dev/os/blob/main/docs/UPDATES.md) on the subject.

## Building Packages

When you feel your YAML is good for a first run, it's time to build the package with melange. In this guide we'll use Docker to execute melange in a local environment, using [Wolfi's SDK](https://github.com/wolfi-dev/tools/pkgs/container/sdk) image. This image contains everything you need to build Wolfi packages with melange and Wolfi-based images with apko.

The procedure to build apk packages with melange is explained in more detail in our [Getting Started with melange](https://edu.chainguard.dev/open-source/melange/tutorials/getting-started-with-melange/) tutorial.

### Setting Up a Local Development Environment

Start by cloning the [Wolfi-os](https://github.com/wolfi-dev/os) repository to your local machine. If you plan on sending a pull request to Wolfi later, you may want to create a fork now and clone your fork instead.

```shell
git clone https://github.com/wolfi-dev/os.git
```

From the root of the project, run the following command to build your Docker-based development environment:

```shell
make dev-container
```

This will create an ephemeral container based on the Wolfi SDK image, with a few predefined settings. We'll call this your **Wolfi development environment**.

```
❯ make dev-container
docker run --privileged --rm -it \
    -v "/home/erika/Projects/os:/home/erika/Projects/os" \
    -w "/home/erika/Projects/os" \
    -e SOURCE_DATE_EPOCH=0 \
    ghcr.io/wolfi-dev/sdk:latest@sha256:99babbe4897d68ec1a342bd958fda7274a072bf112670fa691f64753b04774a9

Welcome to the development environment!


[sdk] ❯
```

You are now ready to build your Wolfi package.

### Building a Package

To build a package, run the following command from your Wolfi SDK environment:

```shell
make package/<your-package-name>
```

For instance, to build PHP 8.3, which is defined in a file named `php-8.3.yaml`, you would run `make package/php-8.3`:

```
[sdk] ❯ make package/php-8.3
make yamlfile=php-8.3.yaml pkgname=php-8.3 packages/x86_64/php-8.3-8.3_rc3-r1.apk
make[1]: Entering directory '/home/erika/Projects/os'
##############################################################
#          build output - removed for readability            #
##############################################################
ℹ️            | signing apk index at packages/x86_64/APKINDEX.tar.gz
ℹ️            | signing index packages/x86_64/APKINDEX.tar.gz with key local-melange.rsa
ℹ️            | appending signature to index packages/x86_64/APKINDEX.tar.gz
ℹ️            | writing signed index to packages/x86_64/APKINDEX.tar.gz
ℹ️            | signed index packages/x86_64/APKINDEX.tar.gz with key local-melange.rsa
make[1]: Leaving directory '/home/erika/Projects/os'
[sdk] ❯
```

When the build is finished, you can find the newly built apk(s) in a `./packages` directory, in the root of your cloned Wolfi repository.

### When the build fails

It is likely that your build won't work on the first run, and that is completely normal because there are many moving parts and hidden dependencies when building packages from source.

In this scenario, it is often useful to check the build environment, which is preserved for debugging. The build output will inform you where to find these files in your development environment.

```
2023/10/25 15:37:27 ERROR: failed to build package. the build environment has been preserved:
ℹ️  x86_64    |   workspace dir: /tmp/melange-workspace-4269468499
ℹ️  x86_64    |   guest dir: /tmp/melange-guest-3734950176
```
The **workspace dir** is where you will find the `melange_out` directory, which contains the output of your package. The **guest dir** directory contains the filesystem of your build environment.

Another useful strategy is to include `set -x` before commands in your pipeline, in order to get extended debug information.

```yaml
  - name: Install Composer
    runs: |
      set -x
      EXEC_DIR="${{targets.destdir}}/usr/bin"
      mkdir -p "${EXEC_DIR}"
      mv composer.phar "${EXEC_DIR}/composer"
      chmod +x "${EXEC_DIR}/composer"
```

Most build issues are caused by missed dependencies, even when the error message might be misleading. Another common reason for build errors are wrong file or directory paths. The [melange documentation](https://edu.chainguard.dev/open-source/melange/troubleshooting/) has more pointers to help with debugging, in case you need it.

As mentioned before, there might be cases where you'll need to first build a dependency, and then use this dependency to build the package you need.

When working with local dependencies, use the following notation in your `packages` list, inside the `environment` section:

```yaml
environment:
  contents:
    repositories:
      - https://packages.wolfi.dev/os
      - '@local /work/packages'
    keyring:
      - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
    packages:
      - busybox
      - mypackage@local
```

This will look for a package named "mypackage" in your local packages/ folder.

### When the build is successful

First of all, celebrate! 🎉

Check the packages folder, you should find a directory for each built architecture (in my case I get x86_64) with your built apks (package + subpackages) along with an `APKINDEX.tar.gz` file:

```shell
./php-full-wolfi-demo/packages/x86_64
├── APKINDEX.tar.gz
├── php-8.2.7-r1.apk
├── php-amqp-1.11.0-r0.apk
├── php-bcmath-8.2.7-r1.apk
├── php-bz2-8.2.7-r1.apk
├── php-calendar-8.2.7-r1.apk
├── php-cgi-8.2.7-r1.apk
├── php-ctype-8.2.7-r1.apk
├── php-curl-8.2.7-r1.apk
├── php-dbg-8.2.7-r1.apk
├── php-dev-8.2.7-r1.apk
├── php-dom-8.2.7-r1.apk
├── php-exif-8.2.7-r1.apk
…
```

In the next section, we'll demonstrate how you can use the Wolfi SDK for running these checks.

## Testing your Packages

With a successful build, it's time to test the packages to make sure they are installable and functional, and also to verify they are free of CVEs.

### Local Installation

The first test you'll want to run with your package is to check if you can use `apk` to install it without errors. For that, we'll use the `local-wolfi` environment, which brings up a new container environment using the Wolfi-base image, with additional settings to make your new package available in the test environment alongside the melange keys that were created to sign your package at build time. We'll call this your **Wolfi Test Environment**.

```shell
make local-wolfi
```
```
❯ make local-wolfi
docker run --rm -it \
	--mount type=bind,source="/home/erika/Projects/os/packages",destination="/work/packages",readonly \
	--mount type=bind,source="/home/erika/Projects/os/local-melange.rsa.pub",destination="/etc/apk/keys/local-melange.rsa.pub",readonly \
	--mount type=bind,source="/tmp/tmp.LXnQu0hkFn/repositories",destination="/etc/apk/repositories",readonly \
	-w "/work/packages" \
	cgr.dev/chainguard/wolfi-base:latest
d2df519c59df:/work/packages#
```

Your newly built packages should now be available for installation from this environment via `apk add`. You should use the full path to the `.apk` file, for instance:

```shell
apk add ./x86_64/composer-2.6.5-r0.apk
```

Make sure the package can be installed without errors, including dependencies.

### Checking for CVEs

Checking the package for CVEs is a good practice to avoid submitting unpatched packages into Wolfi. If CVEs are found, you may want to apply a security patch before submitting your package, if that is available.

From your **Wolfi development environment**, run the following command, providing the full path to your `.apk` file:

```shell
[sdk] ❯ wolfictl scan ./packages/x86_64/composer-2.6.5-r0.apk
🔎 Scanning "./packages/x86_64/composer-2.6.5-r0.apk"
✅ No vulnerabilities found
[sdk] ❯
```

For more information about patching CVEs in Wolfi, check [the official docs on this subject](https://github.com/wolfi-dev/os/blob/main/HOW_TO_PATCH_CVES.md).

## Submitting the Package to Wolfi OS

Once you are satisfied with your set of packages and subpackages, you may consider submitting your package to [Wolfi OS](https://github.com/wolfi-dev/os).

From this point, the process is essentially the following:

- Create a fork of the [wolfi-dev/os](https://github.com/wolfi-dev/os) repository
- Create a branch with the name of your package, for instance: add-php-package
- Remove the `repositories` and `keyring` sections of the YAML file
- Add the `release-monitor` info to the YAML file
- Run [`yam`](https://github.com/wolfi-dev/os/blob/main/docs/UPDATES.md) to fix any YAML formatting issues
- Create a signed commit
- Open a pull request following the instructions from the PR template.

The [Wolfi Contributing Guide](https://github.com/wolfi-dev/os/blob/main/CONTRIBUTING.md) on GitHub has more details about this process.

## Resources to Learn More

If you haven't yet, check the [Wolfi PHP package source file](https://github.com/wolfi-dev/os/blob/main/php-8.2.yaml) for a more comprehensive view of the melange YAML structure and how that looks in a more complex build.

If you'd like to learn more about Wolfi, check the [documentation](https://edu.chainguard.dev/open-source/wolfi/overview/) and [FAQ](https://edu.chainguard.dev/open-source/wolfi/faq/) for more details about the ecosystem surrounding it.

