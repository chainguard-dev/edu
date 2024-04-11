---
title: "Image Overview: docker-selenium"
linktitle: "docker-selenium"
type: "article"
layout: "single"
description: "Overview: docker-selenium Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/docker-selenium/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/docker-selenium/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/docker-selenium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/docker-selenium/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [docker-selenium](https://github.com/SeleniumHQ/docker-selenium) container image with Chromium.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/docker-selenium:latest
```


<!--body:start-->

## Usage

Run the container with the following command:

```bash
docker run --shm-size="2g" -p 4444:4444 -p 7900:7900 cgr.dev/chainguard/docker-selenium:latest
```

Verify Selenium is running:

```bash
curl -sL http://localhost:4444/status` should return a `200` status code, and the response body should contain `{"value":{"ready":true}}` with 1 `availability: UP` node.
```

Access Selenium:

```bash
http://localhost:4444
```

Access noVNC:

```bash
http://localhost:7900/vnc.html`:
```

* Login with the password `secret`.

Any WebDriver tests should point to Selenium on on port 4444.

The following is an example ChromeDriver test using Selenium to retrieve Chainguard's homepage:

```python
from selenium import webdriver
from time import sleep

print("Testing ChromeDriver...")

options = webdriver.ChromeOptions()

driver = webdriver.Remote(
  command_executor='http://localhost:4444/wd/hub',
  options=options
)

'''Maximize window'''
driver.maximize_window()
sleep(5)

'''Retrieve Chainguards homepage'''
driver.get("https://www.chainguard.dev/")
sleep(5)

'''Exit'''
driver.close()
driver.quit()
print("ChromeDriver test successful!")
```

Please note that Chromium is ran in a headless state with the sandbox with GPU access disabled with the flags:

```
--headless --no-sandbox --disable-gpu
```

Chromium is ran headless with GPU access disabled as the container does not have GPU access.

Chromium's sandbox has been disabled as the container is sandboxed from the host environment, and because the
container is running as the root user.

This can be overriden via the environment variable `CHROMIUM_USER_FLAGS` though this is unsupported.

<!--body:end-->

