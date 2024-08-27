---
title: "glibc vs. musl"
linktitle: "glibc vs. musl"
aliases: 
type: "article"
description: "An overview of the differences between glibc and musl."
date: 2024-08-26T18:42:57+00:00
lastmod: 2024-08-27T10:42:34+00:00
draft: false
tags: ["Chainguard Images", "Product", "Cheatsheet"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 210
toc: true
---

Over the years, various implementations of the [C standard library](https://en.wikipedia.org/wiki/C_standard_library), such as the [GNU C library](https://www.gnu.org/software/libc/), [musl](https://musl.libc.org/about.html), [dietlibc](https://www.fefe.de/dietlibc/), [μClibc](https://uclibc.org/), and many others, have emerged with different goals and characteristics. These various implementations exist because the C standard library defines the required functionality for operating system services (e.g., file input/output, memory management) but does not specify implementation details. Among these implementations, the GNU C Library ([glibc](https://www.gnu.org/software/libc/)) and [musl](https://musl.libc.org/about.html) are of the most popular. Here, we'll provide insights into the differences between the two implementations so you can understand some of Chainguard's choices for using glibc over musl.

The GNU C Library ([glibc](https://www.gnu.org/software/libc/)), driven by the [GNU Project](https://www.gnu.org/gnu/thegnuproject.en.html), was first released in 1988. glibc aims to provide a consistent interface for developers to help them write software that will work across multiple platforms. Today, glibc has become the default implementation of the C standard library across the majority of Linux distributions, including Ubuntu, Debian, Fedora, and even Chainguard's Wolfi.

[musl](https://musl.libc.org/about.html) (pronounced "muscle") was first released in 2011 as an alternative to glibc. The goal of musl is to strive for "simplicity, resource efficiency, attention to correctness, safety, ease of deployment, and support for UTF-8/multilingual text." While not as widely used as glibc, some Linux distributions are [based on musl](https://wiki.musl-libc.org/projects-using-musl), the most notable being Alpine Linux.

Below, we highlight common differences between glibc and musl.

**Table 1**: Common differences between glibc and musl.
| Criteria            | glibc                                                          | musl                                                                   |
| ------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| First Release       | 1988                                                           | 2011                                                                   |
| License             | GNU Lesser General Public License (LGPL)                       | MIT License (more permissive)                                          |
| Binary Size         | Larger Binaries                                                | Smaller Binaries                                                       |
| Runtime Performance | Optimized for performance                                      | Slower performance                                                     |
| Build Performance   | Slower                                                         | Faster                                                                 |
| POSIX Compliance    | High, complete implementation                                  | Subset, core functionalities                                           |
| Memory Usage        | Efficient, higher memory usage                                 | Potential performance issues with large memory allocations (e.g. Rust) |
| Dynamic Linking     | Supports lazy binding, unloads libraries                       | No lazy binding, libraries loaded permanently                          |
| Threading           | Native POSIX Thread Library, robust thread safety              | Simpler threading model, not fully thread-safe                         |
| Thread Stack Size   | Varies (2-10 MB), based on resource limits                     | Default size is 128K, can lead to crashes in some multithreaded code   |
| Portability Issues  | Fewer portability issues, widely used                          | Potential issues due to different system call behaviors                |
| Python Support      | Fast build times, supports precompiled wheels                  | Slower build times, often requires source compilation                  |
| NVIDIA Support      | Supported by NVIDIA for CUDA                                   | Not supported by NVIDIA for CUDA                                       |
| Node.js Support     | Tier 1 Support - Full Support                                  | Experimental - May not compile or test suite may not pass              |
| Debug Support       | Several debug features available such as sanitizers, profilers | Does not support sanitizers and limited profilers                      |
| DNS Implementation  | Stable and well-supported                                      | Historical reports of occasional DNS resolution issues                 |

## Library and Binary Size

Musl is significantly smaller than glibc. A primary reason for this is due to the differing approaches adhering to the Portable Operating System Interface ([POSIX](https://en.wikipedia.org/wiki/POSIX)). POSIX is a family of standards specified by the IEEE Computer Society to ensure consistent application behavior across different systems. musl adheres strictly to POSIX standards without incorporating additional extensions. glibc, while adhering to the POSIX standards, includes additional GNU-specific extensions and features. These extensions provide enhanced functionality and convenience, offering developers comprehensive tools. As an example, glibc provides support for Intel Control Enforcement Technology (CET) when running on compatible hardware, providing control flow security guarantees at runtime - a feature that doesn't exist on musl. However, this extensive functionality results in larger library sizes for glibc, with glibc's [function index](http://gnu.org/software/libc/manual/html_node/Function-Index.html) listing over 1700 functions. The backtrace function is an example of this, not included in POSIX but available in glibc.

What does this look like in practice? The decreased binary size for musl is noticeable in a simple "hello world" program, whether linked statically or dynamically. As we can observe, since musl is much smaller than glibc, the statically linked binary is much smaller on Alpine. In the case of dynamic linking, the binary size is smaller for musl compared to glibc due to a simplified implementation of the dynamic linker as can be seen in the [design philosophy](https://wiki.musl-libc.org/design-concepts) of musl.

**Table 2**: Binary size of a "hello world" program demonstrating static and dynamic linking. Setup Dockerfiles found [here](https://github.com/ashamedbit/musl-vs-glibc/tree/main/binary-bloat). The smaller the binary size, the better the system is at debloating.

| Distro                    | Static linking | Dynamic linking |
| ------------------------- | -------------- | --------------- |
| Alpine (musl) binary size | 132K           | 12K             |
| Wolfi (glibc) binary size | 892K           | 16K             |

## Portability of Applications

The portability of an application refers to its ability to run on various hardware or software environments without requiring significant modifications. Developers can encounter portability issues when moving an application from one libc implementation to another. That said, [Hyrum's Law](https://www.hyrumslaw.com/) reminds us that achieving perfect portability is tough. Even when you design an application to be portable, it might still unintentionally depend on certain quirks of the environment or libc implementation.

One issue encountered is the [smaller thread stack size](https://ariadne.space/2021/06/25/understanding-thread-stack-sizes-and-how-alpine-is-different/) used by musl. Musl has a default thread stack size of 128k. glibc has varying stack sizes, determined based on the resource limit, but usually ends up being 2-10 MB. Therefore, this can lead to crashes with multithreaded code in musl, which assumes it has > 2MiB available for each thread (as in a glibc system). Such issues cause [application crashes](https://www.madetech.com/blog/a-tale-in-adopting-alpine-linux-for-docker-problems-we-faced-with-rspec-testing/) and potentially [introduce new vulnerabilities](https://github.com/devpi/devpi/issues/474), such as stack overflows.

## Building from Source Performance

Now we look at the build from source performance for individual projects using the [musl-gcc](https://wiki.musl-libc.org/getting-started.html) [compiler](https://wiki.musl-libc.org/getting-started.html) toolchain used in Alpine and [gcc compiler](https://gcc.gnu.org/) toolchain used in [Chainguard Wolfi](https://github.com/wolfi-dev/os/blob/main/gcc.yaml). We compare the build from source times of both ecosystems. The results can be found below:

**Table 3**: Compilation times between Wolfi (glibc) and musl-gcc. Scripts can be found [here](https://github.com/ashamedbit/musl-vs-glibc/tree/main/build-comparison). The shorter the build time, the better the system's performance.

| Repository   | Wolfi compilation time | musl-gcc compilation | Build successful with musl?     |
| ------------ | ---------------------- | -------------------- | ------------------------------- |
| binutils-gdb | 18m 3.11s              | *   <br>             | No - C++17 features unsupported |
| Little-CMS   | 29.44s                 | 24.13s               | Yes                             |
| zlib         | 11.48s                 | 9.37s                | Yes                             |
| libpcap      | 8.19s                  | 5.61s                | Yes                             |
| gmp          | 98.91s                 | 99.38s               | Yes                             |
| openssl      | 849.08s                | 671.92s              | Yes                             |
| curl         | 92.33s                 | 79.15s               | Yes                             |
| usrsctp      | 55.39s                 | 48.38s               | Yes                             |

From the table, we observe that musl-gcc has **a lower compilation time** than gcc on Wolfi for these projects **if it can build the project successfully.**

musl-gcc fails to compile binutils-gdb because it conforms to POSIX standards, and binutils-gdb uses certain code features that are not conformant to these standards. The [binutils project](https://github.com/bminor/binutils-gdb) on the main branch fails to configure with native musl-gcc.

## Python Builds

Since July 2023, Python has been the [most popular programming language](https://www.tiobe.com/tiobe-index/). A common way to use existing Python packages is through precompiled binary wheels distributed from the Python Package Index ([PyPI](https://pypi.org/)). The wheels are typically built against glibc. Because musl and glibc are different implementations of the C standard library, binaries compiled against glibc may not work correctly or at all on systems using musl. Due to the incompatibility of many glibc-based precompiled binary wheels with musl, PyPI defaults to compiling from source on Alpine Linux. This implies you need to **compile all the C source code** required for every Python package.

This also means you must determine every system library dependency needed to build the Python package from the source. i.e., You have to install the dependencies beforehand using 'apk add <long list of dependencies>' before you perform 'pip install X.'

**Table 4**: PIP install times across Alpine (musl) and Wolfi (glibc). Scripts can be found [here](https://github.com/ashamedbit/musl-vs-glibc/tree/main/python-build-comparison). The shorter the build time, the better the system's performance.

| Python Package     | Alpine (musl) | Wolfi (glibc) |
| ------------------ | ------------- | ------------- |
| Matplotlib, pandas | 21m 30.196s   | 0m 24.3s      |
| tensorflow         | 104m 21.904s  | 2m  54.5s     |
| pwntools           | 29m 45.952s   | 21.5s         |

This results in long build times whenever you want to use Python-based applications with musl.

Below, we also show an example of the difficulty of installing certain Python packages. Take the example of pwntools, a Python package that allows for the construction of exploits in software. When using glibc-based distros, the installation would be in the form 'pip3 install pwntools'. To install pwntools on a musl-based distro (i.e., Alpine), the [Dockerfile](https://github.com/ashamedbit/musl-vs-glibc/blob/main/python-build-comparison/alpine/alpine-pwntools/Dockerfile) is much more complicated:

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

As we can see from the Dockerfile, pwntools requires a set of other packages, which in turn require the most up-to-date version of Rust and cmake, which is not available in the default prebuilt packages in Alpine. Therefore, you would have to build both from source before installing the Python dependencies and, finally, pwntools. Such dependencies will have to be identified iteratively through the trial and error process while building from source.

## Runtime Performance

Time is critical. One bottleneck is often in allocating large chunks of memory repeatedly. Various [reports](https://elixirforum.com/t/using-alpine-and-musl-instead-of-gnu-libc-affect-performance/57670) have shown musl to be slower in this aspect. We compare this memory allocation performance between Wolfi and the latest Alpine [here](https://github.com/ashamedbit/musl-vs-glibc/blob/main/musl-performance-issues/allocations-slowdown.sh). The benchmark uses JSON dumping, which is known to be [highly memory intensive](https://stackoverflow.com/questions/24239613/memoryerror-using-json-dumps).

**Table 5**: Memory Allocation Performance Benchmark across Alpine (musl) and Wolfi (glibc). The shorter the runtime, the better the system's performance.

| Runtime                      | Alpine (musl) | Wolfi (glibc) |
| ---------------------------- | ------------- | ------------- |
| Memory Allocations Benchmark | 102.25 sec    | 51.01 sec     |

Excessive memory allocations can cause musl (used by Alpine) to perform up to **2x slower** than glibc (used by Wolfi). Therefore, a memory-intensive application needs to be wary of performance issues when migrating to the musl-alpine ecosystem. Technical details on why memory allocation (malloc) is slow can be found in the [musl discussion thread](https://musl.openwall.narkive.com/J9ymcXt2/what-s-wrong-with-s-malloc).

Apart from memory allocations, multi-threading has also been problematic for musl (in [GitHub issues](https://github.com/rust-lang/rust/issues/70108) and [discussion threads](https://news.ycombinator.com/item?id=38616023)). Glibc provides a thread-safe system, while musl is not thread-safe. The POSIX standard only requires stream operations to be atomic; there are no requirements on thread safety, so musl does not provide additional thread-safe features. This means unexpected behavior or race conditions can occur during multiple threads.

We used a Rust script (referenced from the [github issue](https://github.com/rust-lang/rust/issues/70108)) to test single-thread and multi-thread performance on Alpine (musl) and Wolfi (glibc).

**Table 6**: Performance benchmark across single-threaded and multi-threaded Rust application. The shorter the runtime, the better the system's performance.

| Runtime                       | Alpine (musl) | Wolfi (glibc) |
| ----------------------------- | ------------- | ------------- |
| Single-thread (avg of 5 runs) | 1735 ms       | 1300 ms       |
| Multi-thread (avg of 5 runs)  | 1178 ms       | 293 ms        |

Alpine (musl) has the worst performance out of the two, taking around 4x more time for multi-thread when compared to Wolfi (glibc). As discussed previously, the real source of thread contention is in the malloc implementation of musl. Multiple threads may allocate memory at once, or free memory may be allocated to other threads. Thus, the thread synchronization logic is a bottleneck for performance.

## NVIDIA Support

NVIDIA dominates the market for artificial intelligence chips, taking up [70% to 95% of the market](https://www.cnbc.com/2024/06/02/nvidia-dominates-the-ai-chip-market-but-theres-rising-competition-.html). NVIDIA CUDA (Compute Unified Device Architecture) speeds up computation time massively by using parallel computing. This means if your company is in the market for ML/AI, you'll want your software supported by NVIDIA. Currently, CUDA [system requirements](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements) only support glibc. Other libc libraries (including musl) are not currently supported, and [NVIDIA does not plan on adding support for musl](https://forums.developer.nvidia.com/t/provide-driver-for-muslc-to-install-it-in-musl-distros/219586/10).

## Experimental Warnings

Developers will most likely encounter musl through Alpine image variants, such as Node.js ([node:alpine](https://github.com/nodejs/docker-node?tab=readme-ov-file#nodealpine)) and Go ([golang:alpine](https://hub.docker.com/_/golang)). Both images have similar warnings that they use musl libc instead of glibc, pointing users to this [Hacker News comment thread⁠](https://news.ycombinator.com/item?id=10782897) to discuss further pro/con comparisons of using Alpine-based images.

Additionally, Node.js mentions in their [building documentation](https://github.com/nodejs/node/blob/main/BUILDING.md#platform-list): "For production applications, run Node.js on supported platforms only." musl and Alpine are experimental supports, whereas glibc is Tier 1 support.

The [Go](https://hub.docker.com/_/golang) image also mentions that Alpine is not officially supported and experimental: "This (Alpine) variant is highly experimental, and *not* officially supported by the Go project (see [golang/go#19938⁠](https://github.com/golang/go/issues/19938) for details)."

## Unsupported Debug Features

Certain applications that rely on debug features for testing, [such as sanitizers](https://wiki.musl-libc.org/open-issues#Sanitizer-compatibility) ([Addressanitizer](https://clang.llvm.org/docs/AddressSanitizer.html), [threadsanitizer](https://clang.llvm.org/docs/ThreadSanitizer.html), etc.) and profilers (e.g., [gprof](https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html)), are not supported by musl.

Sanitizers help debug and detect behaviors such as buffer overflows or dangling pointers. According to the [musl wiki open issues](https://wiki.musl-libc.org/open-issues), GCC and LLVM sanitizer implementations rely on libc internals and are incompatible with musl. Feature requests ([issue1](https://github.com/google/sanitizers/issues/1080), [issue2](https://github.com/google/sanitizers/issues/1544)) have been made in the LLVM sanitizer repository for support for musl, but they have not been addressed and closed.

## Buffer Overflows

Musl lacks default protection against buffer overflows, potentially causing undefined behavior, while glibc has built-in stack smashing protection. Running a vulnerable C program, glibc terminates with an error upon detecting an overflow, whereas musl allows it without warnings. Even using FORTIFY_SOURCE or -fstack-protector-all did not prevent the overflow in musl.

What does this look like in practice? We have a simple vulnerable C program below demonstrating a buffer overflow.

Vulnerable Program (vulnerable.c):
```c
#include <stdio.h>
#include <string.h>

int main() {
  char buffer[10];

  strcpy(buffer, "This is a very long string that will overflow the buffer.");

  printf("Buffer content: %sn", buffer);

  return 0;
}
```

Dockerfile for musl:

```dockerfile
FROM alpine:latest

RUN apk add --no-cache gcc musl-dev

COPY vulnerable.c /vulnerable.c

RUN gcc -o /vulnerable_musl /vulnerable.c

CMD ["vulnerable_musl"]
```

Dockerfile for glibc:
```dockerfile
# Build stage
FROM cgr.dev/chainguard/gcc-glibc as build

WORKDIR /work

COPY vulnerable.c /work/vulnerable.c

RUN gcc vulnerable.c -o vulnerable_glibc

# Runtime stage
FROM cgr.dev/chainguard/glibc-dynamic

COPY --from=build /work/vulnerable_glibc /vulnerable_glibc

CMD ["/vulnerable_glibc"]
```

Build the images:
```shell
$ docker build -t musl-test -f Dockerfile.musl .

$ docker build -t glibc-test -f Dockerfile.glibc .
```

Run the containers:
```shell
$ docker run --rm musl-test
Buffer content: This is a very long string that will overflow the buffer.

$ docker run --rm glibc-test
*** stack smashing detected ***: terminated
```

glibc naturally provides buffer overflow detection, whereas musl does not.

## DNS issues

The Domain Name System (DNS) is the backbone of the internet. It is like the phonebook of the internet, mapping internet protocol (IP) addresses to easy-to-remember website names. Multiple historical sources (see below) on the web have pointed out DNS issues when using musl-related distros. Some have pointed out issues with TCP (which is [fixed in Alpine 3.18](https://www.theregister.com/2023/05/16/alpine_linux_318/)), and others have pointed out random cases with DNS resolution issues.

Further resources regarding musl's history of DNS can be found at the following links:

-   [DNS Resolution in K3s using Alpine Linux](https://github.com/k3s-io/k3s/issues/6132) - GitHub Issue

-   [The tragedy of gethostbyname](https://ariadne.space/2022/03/27/the-tragedy-of-gethostbyname/) - Blog

-   [Does Alpine resolve DNS properly?](https://purplecarrot.co.uk/post/2021-09-04-does_alpine-resolve_dns_properly/) - Blog

-   [musl-libc - Alpine's Greatest Weakness](https://www.linkedin.com/pulse/musl-libc-alpines-greatest-weakness-rogan-lynch/) - Blog

## Additional References

Below is an additional set of articles and discussions about others experiences with musl:

-   [Why I Will Never Use Alpine Linux Ever Again](https://martinheinz.dev/blog/92) - Blog

-   [Why does musl make my Rust code so slow?](https://andygrove.io/2020/05/why-musl-extremely-slow/) - Blog

-   [What's wrong with musl's malloc](https://musl.openwall.narkive.com/J9ymcXt2/what-s-wrong-with-s-malloc) - Mailing List

-   [Using Alpine and musl instead of GNU libc affect performance?](https://elixirforum.com/t/using-alpine-and-musl-instead-of-gnu-libc-affect-performance/57670) - Forum

-   [Github issue: Investigate musl performance issues](https://github.com/EmbarkStudios/texture-synthesis/issues/8) - GitHub Issue

-   [Using Alpine can make Python Docker builds 50× slower](https://pythonspeed.com/articles/alpine-docker-python/) - Blog

-   [Why is the Alpine Docker image over 50% slower than the Ubuntu image?](https://superuser.com/questions/1219609/why-is-the-alpine-docker-image-over-50-slower-than-the-ubuntu-image) - Forum

-   [Comparison of C/POSIX standard library implementations for Linux](http://www.etalabs.net/compare_libcs.html) - Blog

-   [[Chore] Officially support musl the same way glibc is supported](https://github.com/php/php-src/issues/13877) - GitHub Issue

-   [Musl as default instead of glibc](https://github.com/NixOS/nixpkgs/issues/90147) - GitHub Issue

-   [Convert docker builds to use debian/glibc images, away from docker alpine/musl.](https://github.com/LemmyNet/lemmy/issues/3972) - GitHub Issue

## Contributing

If you spot anything we've overlooked regarding glibc or musl or have additional insights to contribute, please feel free to raise the issue in [chainguard-dev/edu](https://github.com/chainguard-dev/edu). We welcome further discussion on weaknesses in glibc, such as its larger codebase and complexity compared to musl. Additionally, insights into the intricacies of compiler toolchains for cross-compilation are welcomed, especially when dealing with glibc and musl.