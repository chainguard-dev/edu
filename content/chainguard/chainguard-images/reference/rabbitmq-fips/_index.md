---
title: "Image Overview: rabbitmq-fips"
linktitle: "rabbitmq-fips"
type: "article"
layout: "single"
description: "Overview: rabbitmq-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rabbitmq-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rabbitmq-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq-fips/provenance_info/" >}}
{{</ tabs >}}

## Using rabbitmq in FIPS mode

To use this image in FIPS mode, the rabbitmq server application needs to load an extra configuration file containing the following (in the old Rabbitmq config format):

```
[
    {crypto, [
        {fips_mode, true}
    ]}
].
```

The file is located in `/etc/erlang/releases/26/sys.config` in this image.

The file can be loaded by setting an environment variable that points to the file:

```
RABBITMQ_ADVANCED_CONFIG_FILE=/etc/erlang/releases/26/sys.config
```

### Verifying rabbitmq is in FIPS mode

To verify if rabbitmq is running with FIPS enabled, use the following command:

```
/usr/lib/rabbitmq/bin/rabbitmqctl environment |grep fips
```

If FIPS is enabled, the result will look like the following:
```
 {crypto,[{fips_mode,true},{rand_cache_size,896}]},
```

The `rabbitmqctl` command also outputs JSON, which can be parsed like this:

```
/usr/lib/rabbitmq/bin/rabbitmqctl environment --formatter json |jq '.crypto .fips_mode'
```

The result will be `true` if FIPS is enabled, or `false` if it is not.

