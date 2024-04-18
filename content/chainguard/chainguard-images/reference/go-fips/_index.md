---
title: "Image Overview: go-fips"
linktitle: "go-fips"
type: "article"
layout: "single"
description: "Overview: go-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-18 00:43:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/go-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/go-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/go-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image for building Go applications with FIPS
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/go-fips:latest
```


<!--body:start-->
## Go FIPS with OpenSSL

This image provides go toolchain that produces FIPS compliant binaries. It is go toolchain compiled with [golang-fips/go](https://github.com/golang-fips/go) patches applied. They are further enhanced to always default to FIPS mode, without ability to opt out. For non-FIPS toolchain see `go` container image.

Binaries built with this edition of go on Linux:

 * require OpenSSL at runtime
 * require OpenSSL FIPS provider at runtime
 * will abort execution if above conditions are not satisfied

Whilst Chainguard's edition of OpenSSL FIPS is recommended, the resulting binaries are vendor-agnostic and can be used at runtime with OpenSSL FIPS providers on other OpenSSL FIPS hosts.

FIPS compliance is achieved by not using any native golang cryptographic functionality and redirecting all calls to OpenSSL at runtime. Specifically the following modules are patched to redirect to the OpenSSL FIPS provider:

 * `crypto`
 * `crypto/tls`
 * subset of `golang.org/x/crypto` that use stock `crypto` primitives only

If no other cryptographic algorithms are implemented or used, certification status will depend on the runtime OpenSSL FIPS certification. For Chainguard that is [#4282](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282) and the submitted rebrand of that.

Notable exceptions are:

 * `crypto/md5` available for non-cryptographically secure use cases only

If your application uses `crypto/md5` or any other third-party golang cryptographic modules, do engage with a CST testing laboratory for audit and certification needs.

## Usage guidance

 * Use native architecture builds (no-cross compilation)
 * Ensure default build settings are used
 * Do not customize toolchain `-tags`,  `GOEXPERIMENT`, `CGO_ENABLED`

## Interactive build with FIPS operation validation

This section contains two examples of how you can use the Go FIPS Chainguard Image to build an example Go application. For more information on working with this Image, check out our [Getting Started with the Go Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/getting-started-go/) guide.

Start interractive shell in the `go-fips` image:

```sh
docker run --rm -ti --entrypoint bash -w /root cgr.dev/chainguard-private/go-fips:latest
```

Install a golang demo application `helloserver`:

```sh
# go install golang.org/x/example/helloserver@latest
go: downloading golang.org/x/example v0.0.0-20240205180059-32022caedd6a
go: downloading golang.org/x/example/helloserver v0.0.0-20240205180059-32022caedd6a
```

Observe toolchain flags used to build the binary:

```sh
# go version go/bin/helloserver
go/bin/helloserver: go1.22.2 X:boringcrypto
```

This indicates the binary was built with `1.22.2` version of go, with `X:boringcrypto` experiment enabled as an indicator that FIPS is in use. Please note that whilst the toolchain experiment is called `boringcrypto` the actual implementation uses OpenSSL as evident from symbols table (see below).

Observe further build settings used on the binary:

```sh
# go version -m go/bin/helloserver
go/bin/helloserver: go1.22.2 X:boringcrypto
	path	golang.org/x/example/helloserver
	mod	golang.org/x/example/helloserver	v0.0.0-20240205180059-32022caedd6a	h1:zS1QYVOUpIsBoK6hpWlanELg0mrDgjk+mWqblK1nkjM=
	build	-buildmode=exe
	build	-compiler=gc
	build	DefaultGODEBUG=httplaxcontentlength=1,httpmuxgo121=1,panicnil=1,tls10server=1,tlsrsakex=1,tlsunsafeekm=1
	build	CGO_ENABLED=1
	build	CGO_CFLAGS=
	build	CGO_CPPFLAGS=
	build	CGO_CXXFLAGS=
	build	CGO_LDFLAGS=
	build	GOARCH=amd64
	build	GOEXPERIMENT=boringcrypto
	build	GOOS=linux
	build	GOAMD64=v1
```

Observe the following:

 * `build CGO_ENABLED=1` setting is in place
 * `build GOEXPERIMENT=boringcrypto` setting is in place

Verify that OpenSSL symbols are used by the binary:

```sh
# go tool nm go/bin/helloserver | grep -e OpenSSL_version
  6511f0 T _cgo_f207f3f06c6f_Cfunc_go_openssl_OpenSSL_version
  964960 D _g_OpenSSL_version
  4df600 t vendor/github.com/golang-fips/openssl/v2._Cfunc_go_openssl_OpenSSL_version.abi0
  8d09b0 d vendor/github.com/golang-fips/openssl/v2._cgo_f207f3f06c6f_Cfunc_go_openssl_OpenSSL_version
```

Note that golang-fips/openssl contains bindings for all available APIs, even if individual binary may not use all of them.

Verify binary execution with suitable OpenSSL FIPS provider (use `Ctrl+C` to terminate):

```sh
# go/bin/helloserver
2024/04/15 10:22:21 serving http://localhost:8080
^C
```

Now tamper with the fips provider to observe failure to start the application in FIPS mode

```sh
# cp /etc/ssl/fipsmodule.cnf fipsmodule.cnf.back
# cat fipsmodule.cnf.back | tr 89 98 > /etc/ssl/fipsmodule.cnf
# go/bin/helloserver
panic: opensslcrypto: can't enable FIPS mode for OpenSSL 3.3.0 9 Apr 2024: OSSL_PROVIDER_try_load
openssl error(s):
error:1C8000D4:Provider routines::invalid state
	providers/fips/self_test.c:262
error:1C8000D8:Provider routines::self test post failure
	providers/fips/fipsprov.c:707
error:078C0105:common libcrypto routines::init fail
	crypto/provider_core.c:966

goroutine 1 [running]:
crypto/internal/backend.init.0()
	/usr/lib/go/src/crypto/internal/backend/openssl.go:55 +0x13f
```

As you can see above `helloserver` panics when on startup OpenSSL FIPS fails self tests.

Now restore `fipsmodule.cnf` to get back into operational state:

```sh
cp fipsmodule.cnf.back /etc/ssl/fipsmodule.cnf
```

## Dockerfile example

The following example Dockerfile builds a helloserver program in Go and copies it on top of the `cgr.dev/chainguard-private/glibc-openssl-fips:latest` base image:

```dockerfile
FROM cgr.dev/chainguard-private/go-fips:latest as build

RUN go install golang.org/x/example/helloserver@latest

FROM cgr.dev/chainguard-private/glibc-openssl-fips:latest

COPY --from=build /root/go/bin/helloserver /helloserver
CMD ["/helloserver"]
```

Run the following command to build the demo image and tag it as `go-helloserver-fips`:

```sh
docker build -t go-helloserver-fips .
```

Now you can run the image with:

```sh
docker run go-helloserver-fips
```
<!--body:end-->

