---
title: "Temporary anonymous registry (tmp.cgruser.dev)"
linktitle: "Temporary registry"
type: "article"
description: "Push and pull temporary container images with no account, no login, and no configuration. Images expire automatically."
date: 2026-10-21T12:00:00+00:00
lastmod: 2026-10-21T12:00:00+00:00
draft: false
images: []
tags: ["Registry"]
menu:
  docs:
    parent: "registry"
weight: 40
toc: true
---

`tmp.cgruser.dev` is a free, anonymous, ephemeral OCI registry run by Chainguard. Push an image with no account, no login, and no configuration, hand the reference to a teammate or a test cluster, and it works until it expires. It is handy for sharing a quick build, testing CI pipelines, or pulling into a Kubernetes cluster without configuring pull secrets.

> **This service is experimental.** It has no SLA, its hostname may change, and anything on it can disappear at any time. Never use it for production images, and never push anything secret: everything on this registry is publicly readable, writable, and deletable by anyone.

## Quick start

Standard OCI clients just work, because there is no auth to configure:

```sh
# Something to push
cat > Dockerfile <<'DOCKERFILE'
FROM cgr.dev/chainguard/busybox:latest
CMD ["echo", "hello from the temporary registry"]
DOCKERFILE

# Pick a random name once so build, push, and pull all agree
IMAGE="tmp.cgruser.dev/$(uuidgen | tr 'A-F' 'a-f')/demo:1h"

docker build -t "$IMAGE" .
docker push "$IMAGE"

# Anyone with the reference can pull it, from anywhere, with no login
docker pull "$IMAGE"
```

Or skip the build entirely and copy an existing image with [crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane):

```sh
crane copy cgr.dev/chainguard/busybox:latest \
  "tmp.cgruser.dev/$(uuidgen | tr 'A-F' 'a-f')/busybox:30m"
```

## The tag is the time-to-live

A tag whose name is a duration sets how long the tag is served, up to a maximum of 24 hours:

| Tag | Served for |
| --- | --- |
| `:5m` | 5 minutes |
| `:100s` | 100 seconds |
| `:3h` | 3 hours |
| `:1d` | 24 hours |
| `:25h` | 24 hours (longer durations are capped) |
| `:latest`, `:v1`, anything else | up to 24 hours |

Details worth knowing:

- Every push restarts the clock, including re-pushing identical bytes to the same tag.
- When a duration tag's time is up, pulling it by tag stops working and it disappears from tag listings. Pulling by digest keeps working until the content itself is removed.
- A duration must be a whole number with one unit (`s`, `m`, `h`, or `d`). Compound forms like `1h30m` are treated as ordinary tag names.
- Expiry is a ceiling, not a guarantee of availability: any content may be removed at any time.

## Pulling from Kubernetes

Because pulls are anonymous, a cluster needs no `imagePullSecrets`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tmp-registry-demo
spec:
  containers:
    - name: demo
      image: tmp.cgruser.dev/<your-random-name>/demo:1h
```

## Ground rules

- **Everything is public and anonymous.** Anyone can pull, overwrite, or delete any tag. Use a long random repository name (the `uuidgen` trick above) and pull by digest when integrity matters:

  ```sh
  docker pull tmp.cgruser.dev/<name>/demo@sha256:<digest>
  ```

- **Repositories cannot be listed.** There is no catalog endpoint, so content is only reachable by someone who knows the name. Tag listing works within a repository you already know.
- **Reserved namespaces are rejected.** Pushes under `chainguard`, `cgr`, `wolfi`, and lookalike names are refused, so content here cannot impersonate Chainguard's own images. Chainguard's real images live at [cgr.dev](/chainguard/containers/registry/overview/).
- **Every response carries a warning.** The registry sends an [OCI `Warning` header](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#warnings) reminding you that content is anonymous and unreviewed; clients like crane display it on every push and pull.
- **Content is not scanned or endorsed by Chainguard.** Treat anything you pull from this registry exactly as you would a file from an unknown stranger, because that is what it is.

## What this registry is not

The temporary registry is completely separate from [Chainguard's main registry](/chainguard/containers/registry/overview/) at `cgr.dev`: different infrastructure, different storage, and no connection to Chainguard accounts, entitlements, or the guarded images catalog. If you need secure, minimal, signed images with real support, that is what [Chainguard Containers](/chainguard/containers/overview/) are for.
