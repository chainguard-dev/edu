---
title: "Configure Chainguard Libraries access in container builds"
linktitle: "Container builds"
description: "Authenticate to Chainguard Libraries during a container build without baking credentials into the final image."
type: "article"
date: 2026-09-09T00:00:00+00:00
lastmod: 2026-09-09T00:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Integration"]
menu:
  docs:
    parent: "policies-and-security"
weight: 075
toc: true
aliases:
  - /chainguard/libraries/build-containers/
---

When you build a container that installs from Chainguard Libraries, the build must authenticate to Chainguard Libraries — or to a repository manager that proxies it — without baking credentials into the final image.

The package-manager configuration differs by language, but the container-build pattern is the same: pass the credentials into the build stage only for the install step that needs them. For the credentials file, target filename, and file format expected by each package manager, see the ecosystem-specific build configuration page:

* [Java build configuration](/chainguard/libraries/java/build-configuration/)
* [JavaScript build configuration](/chainguard/libraries/javascript/build-configuration/)
* [Python build configuration](/chainguard/libraries/python/build-configuration/)
    * Some Chainguard Libraries for Python packages currently lack macOS-compatible wheels. When the dependency you need is available only as a Chainguard Linux wheel, local installation and testing against the Chainguard-built package must happen in a container. A working build-time secret mount is therefore part of local development on macOS, not only a CI/CD concern.

The repository can be Chainguard Libraries directly or a repository manager that proxies Chainguard Libraries. The secret-mount pattern is the same in either setup.

## Do not bake credentials into image layers

Avoid both of the following approaches:

* Do not `COPY` a credentials file into the build stage. Deleting the file in a later `RUN` instruction does not remove it from the layer history; it can still be extracted with `docker history` or by inspecting the image layers.
* Do not pass credentials through `ARG` or `ENV`. Build arguments and environment variables can be recorded in image metadata and exposed to anyone with access to the image.

Also avoid printing the secret or copying it to another persistent path during the `RUN` instruction that consumes it. A secret mount protects the mounted file; it cannot protect a copy that your build writes into a layer.

## Use BuildKit secret mounts

Docker BuildKit's `--secret` flag mounts a file for a single `RUN` instruction. The file is available only while that instruction runs, is not written to an image layer, and does not appear in the image history.

```dockerfile
# syntax=docker/dockerfile:1
FROM cgr.dev/chainguard/python:latest-dev AS build

RUN --mount=type=secret,id=netrc,target=/home/nonroot/.netrc,uid=65532,gid=65532 \
    pip install -r requirements.txt
```

Supply the secret when you build the image:

```bash
docker build \
  --secret id=netrc,src="$HOME/.netrc" \
  -t myimage .
```

For a multi-stage build, consume the secret in the build stage and copy only the application artifacts into the final stage:

```dockerfile
# syntax=docker/dockerfile:1
FROM cgr.dev/chainguard/python:latest-dev AS build
WORKDIR /app

COPY requirements.txt .
RUN --mount=type=secret,id=netrc,target=/home/nonroot/.netrc,uid=65532,gid=65532 \
    python -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

FROM cgr.dev/chainguard/python:latest
WORKDIR /app
COPY --from=build /app /app
ENV PATH="/app/venv/bin:$PATH"
CMD ["python", "app.py"]
```

The final stage has no secret mount and does not copy the credentials file. Only the built application and its dependencies are copied from the build stage.

The secret can come from a local file, a CI secret store, or another build-time secret source. Do not put it in the Dockerfile or the build context.

The `id` value connects the command-line secret to the `RUN` instruction. The `target` value is the path where the package manager expects the credentials file. Both values are package-manager and image specific.

## Account for the nonroot default user

Chainguard `-dev` images run as a nonroot user by default. This differs from many Debian- and Alpine-based build images, which run as `root` unless you set another user.

BuildKit secret mounts are read-only and are owned by `root` unless you set the mount ownership. If the `RUN` instruction executes as the default nonroot user, the package manager cannot read the file:

```text
cat: can't open '/home/nonroot/.netrc': Permission denied
```

For Chainguard's default nonroot user, set both `uid` and `gid` to `65532`:

```dockerfile
RUN --mount=type=secret,id=netrc,target=/home/nonroot/.netrc,uid=65532,gid=65532 \
    pip install -r requirements.txt
```

The UID/GID is consistent across Chainguard `-dev` images, but the username and home directory are not. Use the target path for the specific image in your `FROM` instruction:

| Image | Default user | Home directory | Example secret target |
| --- | --- | --- | --- |
| `python:latest-dev` | `nonroot` | `/home/nonroot` | `/home/nonroot/.netrc` |
| `node:latest-dev` | `node` | `/home/node` | `/home/node/.npmrc` |
| `jdk:latest-dev` | `java` | `/home/java` | `/home/java/.m2/settings.xml` |
| `maven:latest-dev` | `nonroot` | `/home/nonroot` | `/home/nonroot/.m2/settings.xml` |

If a stage switches to `USER root` before installing packages, the mount target and ownership must match the user active in the `RUN` instruction that reads the credentials. In that case, a root-owned mount should use a root-accessible target such as `/root/.netrc`, not the nonroot path and ownership from the table.

## Package-manager reference

The mount mechanics are shared across languages. Only the target filename and file format change:

| Ecosystem | Typical credentials file | See |
| --- | --- | --- |
| Python | `.netrc` | [Python build configuration](/chainguard/libraries/python/build-configuration/) |
| JavaScript | `.npmrc` | [JavaScript build configuration](/chainguard/libraries/javascript/build-configuration/) |
| Java | Maven `settings.xml` or a Gradle init script | [Java build configuration](/chainguard/libraries/java/build-configuration/) |

The ecosystem-specific page is also the source of truth for repository URLs, authentication fields, fallback behavior, lockfile handling, and package-manager-specific troubleshooting.

## CI/CD

Use the same `--secret` flag in CI/CD. Read the credential from the CI system's secret store and pass it to BuildKit as an environment-backed secret rather than writing it to the workspace.

```yaml
- name: Build image
  run: |
    docker build \
      --secret id=netrc,env=NETRC_CONTENTS \
      -t myimage .
  env:
    NETRC_CONTENTS: ${{ secrets.CHAINGUARD_PYTHON_NETRC }}
```

The same pattern applies to `.npmrc`, Maven `settings.xml`, and other package-manager configuration files: mount the file only for the install step that needs it, and keep it out of the final runtime stage.
