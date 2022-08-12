---
title: "Troubleshooting melange Builds"
type: "article"
lead: "Debugging and common errors"
date: 2022-08-10T11:07:52+02:00
lastmod: 2022-08-10T11:07:52+02:00
contributors: ["Erika Heidi"]
draft: false
images: []
menu:
  docs:
    parent: "melange"
weight: 200
toc: true
---

## Debug Options
To include debug-level information on melange builds, edit your `melange.yaml` file and include `set -x` in your pipeline. You can add this flag at any point of your pipeline commands to further debug a specific section of your build.

```yaml
...
pipeline:
  - name: Build Minicli application
    runs: |
      set -x
      APP_HOME="${{targets.destdir}}/usr/share/hello-minicli"
...
```
## Common Errors

>Error: failed to build package: unable to run pipeline: exit status 127

The build could not be completed due to an error at some point of your pipeline. Enable debug by including `set -x` at the beginning of your build pipeline so that you can nail down where the issue occurs.

### Missing QEMU kernel headers

Linux users using the Docker melange image may get errors when building packages for other architectures than `x86` and `x86_64`. This won't happen for Docker Desktop users, since the additional architectures are automatically enabled upon installation.

To enable additional architectures, you'll need to enable them within your kernel with the following command:

```shell
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```
