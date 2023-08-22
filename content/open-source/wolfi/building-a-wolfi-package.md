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

Wolfi is a Linux distro created specifically to build stripped down container images that only include the essential packages needed to run applications in containers. This makes it more secure, as there are fewer potential attack vectors due to the reduced surface area. Another important attribute that contributes to Wolfi's status as a security-first distribution is how fast packages are updated, thanks to a fine-tuned maintenance process combining top-notch automation and established best practices from maintainers. This ensures that Wolfi users get patches and latest versions of packages at a much faster pace than other distributions. Additionally, Wolfi includes a number of features that help to ensure the provenance and authenticity of packages. For example, all packages are built directly from source and signed with cryptographic signatures. This helps to prevent malicious code from being introduced into the system. Wolfi also provides a high-quality build-time [SBOM](https://edu.chainguard.dev/open-source/sbom/what-is-an-sbom/) as standard for all packages.

That being said, it's important to note that Wolfi is rather new; it just recently crossed the mark of 1,000 packages in the Wolfi OS repository. That means some packages that you would find in a more established distro won't be available yet in Wolfi. In this article, we'll cover the whole process involved in building a new Wolfi package, or how a Wolfi package comes to be.

Note: Many of the examples shown in this article are based on the [Wolfi PHP package](https://github.com/wolfi-dev/os/blob/main/php.yaml), which is a slightly complex build that generates several subpackages from a single melange YAML file. You can keep that link open in a separate tab to use as reference as you go through this guide.
## How Does it Compile?
The first step in building a new Wolfi package is finding official documentation with guidance on how to build the package from source. All Wolfi packages need to be built from source in order to assure provenance and authenticity of package contents.

Because Wolfi uses [apk](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper) and thus has some similar design principles as Alpine, it is a good idea to have a look at the [Alpine package index](https://pkgs.alpinelinux.org/packages) to find out how the package is built there. This can give you insights about configuration options, dependencies, and eventual subpackages that can be stripped from the main package. For example, when compiling PHP from source, you have the choice of compiling several extensions either as built-in or as shared libraries. Although compiling said extensions as built-in packages makes for a simpler build, it also increases the size of the original package and creates a wider surface for possible vulnerabilities.

If you aren't very familiar with building packages from source using tools such as `cmake` and `autoconf`, it's a good idea to compile the package locally first - you don't need to run "make install"  at the end to get the package installed on your own system, but running the configure and make processes will give you a better understanding of the build requirements and configure options.
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

- **Package name**: convention is to use the same name as the YAML file without extension. This is what people will search for, so it's a good idea to keep it consistent with how the package is named in other distributions.
- **Description**: this information shows up when searching for the package with apk.
- **Version**: the version of the package.
- **Epoch**: this is a numeric field set to zero by default, that only needs to be incremented when there is a non-version change in the package. For instance, when build options such as compiler flags have changed or new subpackages have been added but the upstream package version hasn't changed - in such cases, you'd need to "bump the epoch" in order to trigger the build.
- **License**: the package license. It is important to note that only packages with OSI-approved licenses can be included in Wolfi. You can check the relevant package info in the [licenses page at opensource.org](https://opensource.org/licenses/).
- **Runtime dependencies**: any dependencies needed by your package at runtime. Not to be confused with build dependencies, these will come up in the environment section of the file.

### The `environment` Section

The next section is the environment section. It defines how the build environment should look in order to build your package. Packages listed in this section won't be included in the final package, because they are only needed at build time.

When building locally, you'll also need to include information about where to find Wolfi packages. This is not needed when submitting the package to the Wolfi OS repository. The `contents` node is used for that:

```yaml
environment:
  contents:
    repositories:
      - https://packages.wolfi.dev/bootstrap/stage3
      - https://packages.wolfi.dev/os
    keyring:
      - https://packages.wolfi.dev/bootstrap/stage3/wolfi-signing.rsa.pub
      - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
```

Dependencies are defined in a `packages` section. An example excerpt from the Wolfi PHP package, which is a fairly complex build with many dependencies, is below:

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

One thing that may happen during this process is finding out that one or more dependencies needed by your package are not yet available in Wolfi, so they need to be built first. It is a normal part of the process, so don't worry – you will be able to build incrementally and test everything locally.

### The `pipeline` Section

With package metadata and build environment defined, it's time to create the pipeline that will build your package. The pipeline section looks a lot like a GitHub Actions workflow, defining a series of steps that must be executed in the same order they are defined, creating output that will be packaged into one or more apk packages.

A package build pipeline typically starts with fetching the package (as a tarball or directly from a Git branch) and matching the downloaded artifact against an expected sha hash.

Some of the actions executed in build pipelines are very similar across packages: downloading a package, running configure and make, fetching a package from git… Luckily for us, melange bakes a lot of repetitive tasks into reusable [pipelines](https://github.com/chainguard-dev/melange/tree/main/pkg/build/pipelines):

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

Each pipeline can have one or more parameters that should be provided as keypairs in a `with` entry. For example, this is how a download-and-check step looks like in the melange YAML, using the built-in pipeline `fetch`:

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

You can find more details about available pipelines in the [melange pipelines documentation](https://edu.chainguard.dev/open-source/melange/melange-pipelines).

### The `subpackages` Section
As mentioned above, a package may extract parts of its contents into subpackages, in order to make for a slimmer final apk. Many packages have resources that are not required at execution time: development headers, man pages, shared libraries that are optional… you name it. This part is really important in Wolfi, because we want packages to be minimal. The `subpackages` section of the melange YAML file looks a lot like the pipeline section, and it essentially works the same way. You'll just have to make sure you place any subpackage files in the `targets.subpkgdir` location.

The `split` built-in pipelines were created to facilitate the creation of subpackages. They implement code to remove development headers (`split/dev`), man pages (`split/manpages`), among other resources that aren't typically required at runtime. You can experiment with those, just be aware that they use standard path locations and some compiled packages may use different paths for certain resources.

For example, this is how a step in the subpackages section would be written, using the `split/dev` built-in pipeline to generate the `php-dev` subpackage:

```yaml
  - name: php-dev
    description: PHP 8.2 development headers
    pipeline:
      - uses: split/dev
```

#### Looping with Ranges
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

#### The `update` Section
This final section of the YAML file is only required when submitting the package to the Wolfi OS repository. The update section is used by Wolfi CI/CD systems to detect new package releases.

Wolfi uses multiple tools and services to keep track of upstream releases, including the [Release Monitoring](https://release-monitoring.org/) service. For packages that are released via GitHub, tracking is made via the project org/name and a monitored tag.

Here's an example of the update section of the PHP package, which uses the Release Monitoring service:

```yaml
update:
  enabled: true
  release-monitor:
    identifier: 3627
```
The identifier can be obtained from the [release monitoring page](https://release-monitoring.org/) - search for the package and grab the ID that shows up at the URL.

Here is another example, this time from a package that is released via GitHub:

```yaml
update:
  enabled: true
  github:
    identifier: php-amqp/php-amqp
    strip-prefix: v
    tag-filter: v
```
Again, this section is only required when submitting the package to Wolfi.

## Building the Packages
When you feel your YAML is good to run, it's time to build the packages with melange. In this guide we'll use Docker to execute melange in a local environment. The procedure is explained in more detail in our [Getting Started with melange](https://edu.chainguard.dev/open-source/melange/tutorials/getting-started-with-melange/) tutorial.

First, you'll need to generate a melange key. This is required to sign the apks, and the same key will need to be used when installing these packages in an image with apko.

Make sure you have an updated version of the melange image:

```shell
docker pull cgr.dev/chainguard/melange
```

Then, run the following command to generate the key:

```shell
docker run --rm -v "${PWD}":/work cgr.dev/chainguard/melange keygen
```

Once you have the key, you can run the `build` command. A few explanations before you hit the keyboard:

- **Building as root:** building packages require you to run melange as root, thus the `--privileged` parameter.
- **Volumes:** here we set up **two** volumes: the current folder is shared with the /work location in the container, so that the packages generated will be available in your local system at the ./packages location. The second volume shares the `/tmp/melange_out` location in the container with your `/tmp` folder, so that you can have access to melange's working files even when the build fails. This helps a lot with debugging!
- **Architecture:** limit the build to your own system's architecture while you are developing the package, this will make the build faster and avoid issues.
- **Signing key:** remember this key will be required later as well, when you install the package in a container image using apko.

Here is the full command:

```shell
docker run --privileged --rm -v "${PWD}":/work -v /tmp/melange_out:/tmp \
  cgr.dev/chainguard/melange build my-package.yaml \
  --arch x86_64 \
  --signing-key melange.rsa
```

### When the build fails
It is likely that your build won't work on the first run, and that is completely normal because there are many moving parts and hidden dependencies when building packages from source. Check the errors and iterate until you have a successful build. Use `set -x` before commands in your pipeline to get extended debug information:

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
      - https://packages.wolfi.dev/bootstrap/stage3
      - https://packages.wolfi.dev/os
      - '@local /work/packages'
    keyring:
      - https://packages.wolfi.dev/bootstrap/stage3/wolfi-signing.rsa.pub
      - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
    packages:
      - busybox
      - mypackage@local
```

This will look for a package named "mypackage" in your local packages/ folder.

### When the build is successful
First of all, celebrate!: 🎉 Check the packages folder, you should see a directory for each built architecture (in my case I get x86_64) with your built apks (package + subpackages) AND an `APKINDEX.tar.gz` file:

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
## Does it Work? Try with apko
Once you have packages ready to be installed, you may try them with an apko build. The syntax used by apko YAML files is very similar to what we've seen with melange. There are just a few minor differences in structure. Here is an example apko file to build a PHP image using some of the subpackages created with my previous build commands:

```yaml
contents:
  keyring:
    - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
    - /work/melange.rsa.pub
  repositories:
    - https://packages.wolfi.dev/os
    - '@local /work/packages'
  packages:
    - ca-certificates
    - curl
    - php@local
    - php-curl@local
    - php-openssl@local
    - php-iconv@local
    - php-mbstring@local

entrypoint:
  command: /bin/php

environment:
  PATH: /usr/sbin:/sbin:/usr/bin:/bin

paths:
  - path: /app
    type: directory
    permissions: 0o777
    uid: 65532
    gid: 65532

work-dir: /app

accounts:
  groups:
    - groupname: php
      gid: 65532
  users:
    - username: php
      uid: 65532
      gid: 65532
  run-as: 65532

```

Notice that we have added the "local" repository pointing to our local packages folder, and we also added the `melange.rsa.pub` key to the keyring section.

To build this image, run:

```shell
docker run --rm -v ${PWD}:/work cgr.dev/chainguard/apko build --debug php.apko.yaml php:test php-test.zip -k melange.rsa.pub --arch=amd64
```

Then, you can load the generated tarball to Docker with:

```shell
docker load < php-test.zip
```

Then run the image to see if the package works as expected.

More info about building container images with apko can be found in [this Academy link](https://edu.chainguard.dev/open-source/apko/getting-started-with-apko/).
Submitting the Package to Wolfi OS
Once you are satisfied with your set of packages and subpackages, you may consider submitting your package to [Wolfi OS](https://github.com/wolfi-dev/os).

From this point, the process is essentially the following:

- Create a fork of the [wolfi-dev/os](https://github.com/wolfi-dev/os) repository
- Create a branch with the name of your package, for instance: add-php-package
- Remove the **repositories** and **keyring** sections of the YAML file
- Add the `release-monitor` info to the YAML file
- Add the package to the bottom of the `packages.txt` file in the root of the Wolfi OS repository
- Create a signed commit
- Open a pull request following the instructions from the PR template.


If you haven't yet, check the [Wolfi PHP package source file](https://github.com/wolfi-dev/os/blob/main/php.yaml) for a more comprehensive view of the melange YAML structure and how that looks in a more complex build.

## Resources to Learn More

If you'd like to learn more about Wolfi, check the [documentation](https://edu.chainguard.dev/open-source/wolfi/overview/) and [FAQ](https://edu.chainguard.dev/open-source/wolfi/faq/) for more details about the ecosystem surrounding it. You can also join our monthly Wolfi community calls to connect with Wolfi users and developers. The meetings happen on the first Wednesday of each month, and typically showcase talks and interesting use cases related to Wolfi and container security in general. You can add [Wolfi's public](https://calendar.google.com/calendar/u/0/embed?src=c_7ec60f485931f9056040a3e24273400de41a143ec60703b411d77b1f534ec15f@group.calendar.google.com) calendar to your agenda to be notified about upcoming events.

