---
title: "glibc vs. musl"
linktitle: "glibc vs. musl"
aliases:
- /chainguard/chainguard-images/working-with-images/images-compiled-programs/glibc-vs-musl/
type: "article"
description: "An overview of the differences between glibc and musl."
date: 2024-08-26T18:42:57+00:00
lastmod: 2025-07-23T16:52:56+00:00
draft: false
tags: ["Chainguard Containers", "cheatsheet"]
images: []
menu:
  docs:
    parent: "about"
weight: 210
toc: true
---

Over the years, various implementations of the [C standard library](https://en.wikipedia.org/wiki/C_standard_library) — such as the [GNU C library](https://www.gnu.org/software/libc/), [musl](https://musl.libc.org/about.html), [uClibc-ng](https://www.uclibc-ng.org/), and many others — have emerged with different goals and characteristics. These various implementations exist because the C standard library defines the required functionality for operating system services (such as file input/output and memory management) but does not specify implementation details. Among these implementations, the GNU C Library ([glibc](https://www.gnu.org/software/libc/)) and [musl](https://musl.libc.org/about.html) are among the most popular.

When developing [Wolfi](/open-source/wolfi/overview/), the "undistro" on which all Chainguard Containers are built, Chainguard elected to have it use glibc instead of another implementation like musl. This conceptual article aims to highlight the differences between these two implementations within the context of Chainguard's choice of using glibc over musl as the default implementation for the Wolfi undistro.

> **Note**: Several sections of this guide present data about the differences between glibc and musl across various categories. You can recreate some of these examples used to find this data with the Dockerfiles and C program files hosted in the `glibc-vs-musl` directory of the [Chainguard Academy Containers Demos repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/glibc-vs-musl).


## High-level Differences between glibc and musl

The GNU C Library ([glibc](https://www.gnu.org/software/libc/)), driven by the [GNU Project](https://www.gnu.org/gnu/thegnuproject.en.html), was first released in 1988. glibc aims to provide a consistent interface for developers to help them write software that will work across multiple platforms. Today, glibc has become the default implementation of the C standard library across the majority of Linux distributions, including Ubuntu, Debian, Fedora, and even Chainguard's Wolfi.

[musl](https://musl.libc.org/about.html) (pronounced "muscle") was first released in 2011 as an alternative to glibc. The goal of musl is to strive for "simplicity, resource efficiency, attention to correctness, safety, ease of deployment, and support for UTF-8/multilingual text." While not as widely used as glibc, some Linux distributions are [based on musl](https://wiki.musl-libc.org/projects-using-musl), the most notable being Alpine Linux.

The following table highlights some of the main differences between glibc and musl.

| Criteria        	| glibc                                                      	| musl                                                               	|
| ------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| First Release   	| 1988                                                       	| 2011                                                               	|
| License         	| GNU Lesser General Public License (LGPL)                   	| MIT License (more permissive)                                      	|
| Binary Size     	| Larger Binaries                                            	| Smaller Binaries                                                   	|
| Runtime Performance | Optimized for performance                                  	| Slower performance                                                 	|
| Build Performance   | Slower                                                     	| Faster                                                             	|
| Compatibility | POSIX Compliant + GNU Extensions | POSIX Compliant
| Memory Usage    	| Efficient, higher memory usage                             	| Potential performance issues with large memory allocations (e.g. Rust) |
| Dynamic Linking 	| Supports lazy binding, unloads libraries                   	| No lazy binding, libraries loaded permanently                      	|
| Portability Issues  | Fewer portability issues, widely used                      	| Potential issues due to different system call behaviors            	|
| Python Support  	| Fast build times, supports precompiled wheels              	| Slower build times, often requires source compilation              	|
| NVIDIA Support  	| Supported by NVIDIA for CUDA                               	| Not supported by NVIDIA for CUDA                                   	|

Be aware that binaries are not compatible between Alpine and Wolfi. You **should not** attempt to copy Alpine binaries into a Wolfi-based container image.

> **Note**: As mentioned previously, several of the remaining sections in this guide present data about the differences between glibc and musl across various categories. You can recreate some of these examples by following the same procedure of setting creating and testing container images based on the Dockerfiles and program files relevant to the example you're exploring. You can find the appropriate files in the `glibc-vs-musl` directory of the [Chainguard Academy Containers Demos repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/glibc-vs-musl).


## Library and Binary Size

musl is significantly smaller than glibc. A primary reason for this is due to the differing approaches adhering to the Portable Operating System Interface ([POSIX](https://en.wikipedia.org/wiki/POSIX)). POSIX is a family of standards specified by the IEEE Computer Society to ensure consistent application behavior across different systems. musl adheres strictly to POSIX standards without incorporating additional extensions.

glibc, while adhering to the POSIX standards, includes additional GNU-specific extensions and features. These extensions provide enhanced functionality and convenience, offering developers comprehensive tools. As an example, glibc provides support for Intel Control Enforcement Technology (CET) when running on compatible hardware, providing control flow security guarantees at runtime — a feature that doesn't exist on musl. However, this extensive functionality results in larger library sizes for glibc, with glibc's [function index](https://www.gnu.org/software/libc/manual/html_node/Function-Index.html) listing over 1700 functions.

You might notice the decreased binary size for musl in a simple `hello world` program, whether linked statically or dynamically. As we can observe, since musl is much smaller than glibc, the statically linked binary is much smaller on Alpine. In the case of dynamic linking, the binary size is smaller for musl compared to glibc because of its simplified implementation of the dynamic linker as outlined in [musl project'sdesign philosophy](https://wiki.musl-libc.org/design-concepts).

The following table shows the difference in binary size of statically and dynamically linked `hello world` programs:

| Distro                	| Static linking | Dynamic linking |
| ------------------------- | -------------- | --------------- |
| Alpine (musl) binary size | 132K       	| 12K         	|
| Wolfi (glibc) binary size | 892K       	| 16K         	|

The smaller the binary size, the better the system is at debloating. You can find the Dockerfiles used in this setup in the [`binary-bloat` directory of this guide's example's repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/glibc-vs-musl/binary-bloat).


## Portability of Applications

The *portability* of an application refers to its ability to run on various hardware or software environments without requiring significant modifications. In practice, many developers target glibc specifically rather than a generic POSIX C library, much like writing scripts for bash rather than a POSIX-compliant shell. Consequently, developers can encounter portability issues when moving an application from one libc implementation to another. That said, [Hyrum's Law](https://www.hyrumslaw.com/) reminds us that achieving perfect portability is tough. Even when you design an application to be portable, it might still unintentionally depend on certain quirks of the environment or libc implementation.


## Building from Source Performance

We've compared the build from source performance for individual projects using the [musl-gcc compiler](https://wiki.musl-libc.org/getting-started.html) toolchain used in Alpine and [gcc compiler](https://gcc.gnu.org/) toolchain used in [Chainguard Wolfi](https://github.com/wolfi-dev/os/blob/main/gcc.yaml). We compare the build from source times of both ecosystems.

The following table highlights the results of this comparison by highlighting the compilation times between Wolfi (glibc) and musl-gcc. The shorter the build time, the better the system's performance.

| Repository   | Wolfi compilation time | musl-gcc compilation | Build successful with musl? 	|
| ------------ | ---------------------- | -------------------- | ------------------------------- |
| binutils-gdb | 18m 3.11s          	| *   <br>         	| No - C++17 features unsupported |
| Little-CMS   | 29.44s             	| 24.13s           	| Yes                         	|
| zlib     	| 11.48s             	| 9.37s            	| Yes                         	|
| libpcap  	| 8.19s              	| 5.61s            	| Yes                         	|
| gmp      	| 98.91s             	| 99.38s           	| Yes                         	|
| openssl  	| 849.08s            	| 671.92s          	| Yes                         	|
| curl     	| 92.33s             	| 79.15s           	| Yes                         	|
| usrsctp  	| 55.39s             	| 48.38s           	| Yes                         	|

You can find the Dockerfiles used in this setup in the [`build-comparison` directory of this guide's example's repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/glibc-vs-musl/build-comparison).

This table shows that musl-gcc has **a lower compilation time** than gcc on Wolfi for these projects **if it can build the project successfully.**

musl-gcc fails to compile binutils-gdb because it conforms to POSIX standards, and binutils-gdb uses certain code features that are not conformant to these standards.

## Python Builds

A common way to use existing Python packages is through precompiled binary wheels distributed from the Python Package Index ([PyPI](https://pypi.org/)). Python wheels are typically built against glibc; because musl and glibc are different implementations of the C standard library, binaries compiled against glibc may not work correctly or at all on systems using musl. Due to this incompatibility, PyPI defaults to compiling from source on Alpine Linux. This implies you need to **compile all the C source code** required for every Python package.

This also means you must determine every system library dependency needed to build the Python package from the source. For example, you have to install the dependencies beforehand, using `apk add <long list of dependencies>` before you perform `pip install X`.

The following table shows PIP install times across Alpine (musl) and Wolfi (glibc). You can find the Dockerfiles used in this setup in the [`python-build-comparison` directory of this guide's example's repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/glibc-vs-musl/python-build-comparison).

| Python Package 	| Alpine (musl) | Wolfi (glibc) |
| ------------------ | ------------- | ------------- |
| Matplotlib, pandas | 21m 30.196s   | 0m 24.3s  	|
| tensorflow     	| 104m 21.904s  | 2m  54.5s 	|
| pwntools       	| 29m 45.952s   | 21.5s     	|

As this table shows, this results in long build times whenever you want to use Python-based applications with musl.

Take the example of `pwntools`, a Python package that allows for the construction of exploits in software. When using glibc-based distros, the installation would be in the form `pip3 install pwntools`. To install `pwntools` on a musl-based distro (such as Alpine), the [Dockerfile](https://github.com/chainguard-dev/edu-images-demos/blob/main/glibc-vs-musl/python-build-comparison/alpine/alpine-pwntools/Dockerfile) is much more complicated:

```dockerfile
FROM alpine:latest

# Prebuilt Alpine packages required to build from source
RUN apk add --no-cache musl-dev gcc python3 python3-dev libffi-dev libcap-dev make curl git pkgconfig openssl-dev bash alpine-sdk py3-pip
RUN python -m venv my-venv
RUN my-venv/bin/python -m pip install --upgrade pip

# Build from source cmake for latest version
RUN git clone https://github.com/Kitware/CMake.git && cd CMake && ./bootstrap && make && make install
ENV PATH=$PATH:/usr/local/bin

# Build from source Rust for latest version
RUN curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf > setup-rust.sh
RUN bash setup-rust.sh -y
ENV PATH=$PATH:/root/.cargo/bin

# Finally install pwntools
RUN pip3 install pwn
```

As this Dockerfile shows, `pwntools` requires a set of other packages. These in turn require the most up-to-date versions of Rust and cmake, which are not available in the default prebuilt packages in Alpine. You would have to build both from source before installing the Python dependencies and, finally, `pwntools`. Such dependencies will have to be identified iteratively through a process of trial and error while building from source.

## Runtime Performance

Time is critical. One common bottleneck occurs when allocating large chunks of memory repeatedly. We compare this memory allocation performance between Wolfi and the latest Alpine [here](https://github.com/chainguard-dev/edu-images-demos/blob/main/glibc-vs-musl/musl-performance-issues/allocations-slowdown.sh). The benchmark uses JSON dumping, a highly memory intensive operation.

| Runtime                  	| Alpine (musl) | Wolfi (glibc) |
| ---------------------------- | ------------- | ------------- |
| Memory Allocations Benchmark | 102.25 sec	| 51.01 sec 	|

This table highlights how excessive memory allocations can cause musl (used by Alpine) to perform up to **2x slower** than glibc (used by Wolfi). A memory-intensive application needs to be wary of performance issues when migrating to the musl-alpine ecosystem. Technical details on why memory allocation (`malloc`) is slow can be found in this [musl discussion thread](https://musl.openwall.narkive.com/J9ymcXt2/what-s-wrong-with-s-malloc).

Apart from memory allocations, multi-threading has also been problematic for musl, as shown in various [GitHub issues](https://github.com/rust-lang/rust/issues/70108). glibc provides a thread-safe system, while musl is not thread-safe. The POSIX standard only requires stream operations to be atomic; there are no requirements on thread safety, so musl does not provide additional thread-safe features. This means unexpected behavior or race conditions can occur during multiple threads.

We used a Rust script (referenced from the [GitHub issue](https://github.com/rust-lang/rust/issues/70108)) to test single-thread and multi-thread performance on Alpine (musl) and Wolfi (glibc). The next table shows performance benchmarks across single-threaded and multi-threaded Rust applications.

| Runtime                   	| Alpine (musl) | Wolfi (glibc) |
| ----------------------------- | ------------- | ------------- |
| Single-thread (avg of 5 runs) | 1735 ms   	| 1300 ms   	|
| Multi-thread (avg of 5 runs)  | 1178 ms   	| 293 ms    	|

Alpine (musl) has the worse performance out of the two, taking around 4x more time for multi-thread when compared to Wolfi (glibc). As discussed previously, the real source of thread contention is in the `malloc` implementation of musl. Multiple threads may allocate memory at once, or free memory may be allocated to other threads. Therefore, the thread synchronization logic is a bottleneck for performance.


## Conclusion

glibc and musl both serve well as C implementations. Our goal for this article is to explain Chainguard's rationale for choosing to use glibc for Wolfi. We believe that's what made the most sense for our project, but you should continue your own research to determine if one C implementation would suit your needs better than another.

If you spot anything we've overlooked regarding glibc or musl or have additional insights to contribute, please feel free to raise the issue in [chainguard-dev/edu](https://github.com/chainguard-dev/edu). We welcome further discussion on weaknesses in glibc, such as its larger codebase and complexity compared to musl. Additionally, insights into the intricacies of compiler toolchains for cross-compilation are welcomed, especially when dealing with glibc and musl.


## Additional References

For more information, we recommend the following resources:

* [Understanding thread stack sizes and how Alpine is different](https://ariadne.space/2021/06/24/understanding-thread-stack-sizes-and.html): Explains why applications built for glibc can encounter issues on musl.
* [The tragedy of gethostbyname](https://ariadne.space/2022/03/26/the-tragedy-of-gethostbyname.html): Details why legacy libc DNS APIs are often unreliable across systems.
