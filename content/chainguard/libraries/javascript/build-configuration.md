---
title: "Build Configuration"
linktitle: "Build Configuration  "
description: "Configuring Chainguard Libraries for Javascript on your workstation"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-06-05T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Javascript"]
menu:
  docs:
    parent: "javascript"
weight: 053
toc: true
---

tbd

## npm

```
npm config set registry http://localhost:8081/repository/javascript-all/
```

## pnpm

pnpm config set registry=http://localhost:8081/repository/javascript-all/

https://pnpm.io/settings#registry--authentication-settings



## yarn

tbd

 ```
 yarn config set registry http://localhost:8081/repository/javascript-all/

 ```

for newer yarn

```
yarn config set npmRegistryServer http://localhost:8081/repository/javascript-all/
``` 