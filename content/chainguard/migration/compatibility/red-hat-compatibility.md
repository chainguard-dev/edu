---
title: "Red Hat UBI Compatibility"
linktitle: "Red Hat"
aliases:
- /chainguard/migration/red-hat-compatibility/
- /chainguard/migration/compatibility/red-hat-compatibility/
type: "article"
description: "Differences between Chainguard Images and Red Hat UBI third-party images"
date: 2024-02-23T15:56:52-07:00
lastmod: 2024-03-08T15:56:52-07:00
draft: false
tags: ["IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "compatibility"
weight: 020
toc: true
---

Chainguard Images and Red Hat UBI base images have different binaries and scripts included in their respective `busybox` and `coreutils` packages. Note that Red Hat UBI images by default do not have a `busybox` package.

The following table lists common tools and their corresponding package(s) in both Wolfi and Red Hat distributions.

Note that `$PATH` locations like `/usr/bin` or `/sbin` are not included here. If you have compatibility issues with tools that are included in both `busybox` and `coreutils`, be sure to check `$PATH` order and confirm which version of a tool is being run.

Generally, if a tool exists in `busybox` but does not have a `coreutils` counterpart, there will be a specific package that includes it. For example the `zcat` utility is included in the `gzip` package in both Wolfi and Red Hat.

You can use the `apk search` command in Wolfi, or the `yum search` or `dnf search` commands in Red Hat to find out which package includes a tool.

| Utility         | Wolfi busybox | Redhat-ubi busybox | Wolfi coreutils | Redhat-ubi coreutils |
| --------------- | :-----------: | :----------------: | :-------------: | :------------------: |
| `[`             |      ✅       |                    |       ✅        |          ✅          |
| `[[`            |      ✅       |                    |                 |                      |
| `add-shell`     |      ✅       |                    |                 |                      |
| `addgroup`      |      ✅       |                    |                 |                      |
| `adduser`       |      ✅       |                    |                 |                      |
| `adjtimex`      |      ✅       |                    |                 |                      |
| `arch`          |      ✅       |                    |                 |          ✅          |
| `arping`        |      ✅       |                    |                 |                      |
| `ash`           |      ✅       |                    |                 |                      |
| `awk`           |      ✅       |                    |                 |                      |
| `b2sum`         |               |                    |       ✅        |          ✅          |
| `base32`        |               |                    |       ✅        |          ✅          |
| `base64`        |      ✅       |                    |       ✅        |          ✅          |
| `basename`      |      ✅       |                    |       ✅        |          ✅          |
| `basenc`        |               |                    |       ✅        |                      |
| `bbconfig`      |      ✅       |                    |                 |                      |
| `bc`            |      ✅       |                    |                 |                      |
| `beep`          |      ✅       |                    |                 |                      |
| `bunzip2`       |      ✅       |                    |                 |                      |
| `bzcat`         |      ✅       |                    |                 |                      |
| `bzip2`         |      ✅       |                    |                 |                      |
| `cal`           |      ✅       |                    |                 |                      |
| `cat`           |      ✅       |                    |       ✅        |          ✅          |
| `chattr`        |      ✅       |                    |                 |                      |
| `chcon`         |               |                    |       ✅        |          ✅          |
| `chgrp`         |      ✅       |                    |       ✅        |          ✅          |
| `chmod`         |      ✅       |                    |       ✅        |          ✅          |
| `chown`         |      ✅       |                    |       ✅        |          ✅          |
| `chpasswd`      |      ✅       |                    |                 |                      |
| `chroot`        |      ✅       |                    |       ✅        |          ✅          |
| `chrt`          |      ✅       |                    |                 |                      |
| `cksum`         |      ✅       |                    |       ✅        |          ✅          |
| `clear`         |      ✅       |                    |                 |                      |
| `cmp`           |      ✅       |                    |                 |                      |
| `comm`          |      ✅       |                    |       ✅        |          ✅          |
| `coreutils`     |               |                    |       ✅        |          ✅          |
| `cp`            |      ✅       |                    |       ✅        |          ✅          |
| `cpio`          |      ✅       |                    |                 |                      |
| `cryptpw`       |      ✅       |                    |                 |                      |
| `csplit`        |               |                    |       ✅        |          ✅          |
| `cut`           |      ✅       |                    |       ✅        |          ✅          |
| `date`          |      ✅       |                    |       ✅        |          ✅          |
| `dc`            |      ✅       |                    |                 |                      |
| `dd`            |      ✅       |                    |       ✅        |          ✅          |
| `delgroup`      |      ✅       |                    |                 |                      |
| `deluser`       |      ✅       |                    |                 |                      |
| `df`            |      ✅       |                    |       ✅        |          ✅          |
| `diff`          |      ✅       |                    |                 |                      |
| `dir`           |               |                    |       ✅        |          ✅          |
| `dircolors`     |               |                    |       ✅        |          ✅          |
| `dirname`       |      ✅       |                    |       ✅        |          ✅          |
| `dmesg`         |      ✅       |                    |                 |                      |
| `dnsdomainname` |      ✅       |                    |                 |                      |
| `dos2unix`      |      ✅       |                    |                 |                      |
| `du`            |      ✅       |                    |       ✅        |          ✅          |
| `echo`          |      ✅       |                    |       ✅        |          ✅          |
| `ed`            |      ✅       |                    |                 |                      |
| `egrep`         |      ✅       |                    |                 |                      |
| `env`           |      ✅       |                    |       ✅        |          ✅          |
| `expand`        |      ✅       |                    |       ✅        |          ✅          |
| `expr`          |      ✅       |                    |       ✅        |          ✅          |
| `factor`        |      ✅       |                    |       ✅        |          ✅          |
| `fallocate`     |      ✅       |                    |                 |                      |
| `false`         |      ✅       |                    |       ✅        |          ✅          |
| `fgrep`         |      ✅       |                    |                 |                      |
| `find`          |      ✅       |                    |                 |                      |
| `findfs`        |      ✅       |                    |                 |                      |
| `flock`         |      ✅       |                    |                 |                      |
| `fmt`           |               |                    |       ✅        |          ✅          |
| `fold`          |      ✅       |                    |       ✅        |          ✅          |
| `free`          |      ✅       |                    |                 |                      |
| `fsync`         |      ✅       |                    |                 |                      |
| `fuser`         |      ✅       |                    |                 |                      |
| `getopt`        |      ✅       |                    |                 |                      |
| `getty`         |      ✅       |                    |                 |                      |
| `grep`          |      ✅       |                    |                 |                      |
| `groups`        |      ✅       |                    |                 |          ✅          |
| `gunzip`        |      ✅       |                    |                 |                      |
| `gzip`          |      ✅       |                    |                 |                      |
| `hd`            |      ✅       |                    |                 |                      |
| `head`          |      ✅       |                    |       ✅        |          ✅          |
| `hexdump`       |      ✅       |                    |                 |                      |
| `hostid`        |      ✅       |                    |       ✅        |          ✅          |
| `hostname`      |      ✅       |                    |                 |                      |
| `id`            |      ✅       |                    |       ✅        |          ✅          |
| `inotifyd`      |      ✅       |                    |                 |                      |
| `install`       |      ✅       |                    |       ✅        |          ✅          |
| `ionice`        |      ✅       |                    |                 |                      |
| `iostat`        |      ✅       |                    |                 |                      |
| `ipcrm`         |      ✅       |                    |                 |                      |
| `ipcs`          |      ✅       |                    |                 |                      |
| `join`          |               |                    |       ✅        |          ✅          |
| `kill`          |      ✅       |                    |                 |                      |
| `killall`       |      ✅       |                    |                 |                      |
| `killall5`      |      ✅       |                    |                 |                      |
| `less`          |      ✅       |                    |                 |                      |
| `link`          |      ✅       |                    |       ✅        |          ✅          |
| `linux32`       |      ✅       |                    |                 |                      |
| `linux64`       |      ✅       |                    |                 |                      |
| `ln`            |      ✅       |                    |       ✅        |          ✅          |
| `logger`        |      ✅       |                    |                 |                      |
| `login`         |      ✅       |                    |                 |                      |
| `logname`       |               |                    |       ✅        |          ✅          |
| `ls`            |      ✅       |                    |       ✅        |          ✅          |
| `lsattr`        |      ✅       |                    |                 |                      |
| `lsof`          |      ✅       |                    |                 |                      |
| `lzcat`         |      ✅       |                    |                 |                      |
| `lzma`          |      ✅       |                    |                 |                      |
| `lzop`          |      ✅       |                    |                 |                      |
| `lzopcat`       |      ✅       |                    |                 |                      |
| `md5sum`        |      ✅       |                    |       ✅        |          ✅          |
| `microcom`      |      ✅       |                    |                 |                      |
| `mkdir`         |      ✅       |                    |       ✅        |          ✅          |
| `mkfifo`        |      ✅       |                    |       ✅        |          ✅          |
| `mknod`         |      ✅       |                    |       ✅        |          ✅          |
| `mkpasswd`      |      ✅       |                    |                 |                      |
| `mktemp`        |      ✅       |                    |       ✅        |          ✅          |
| `more`          |      ✅       |                    |                 |                      |
| `mountpoint`    |      ✅       |                    |                 |                      |
| `mpstat`        |      ✅       |                    |                 |                      |
| `mv`            |      ✅       |                    |       ✅        |          ✅          |
| `netstat`       |      ✅       |                    |                 |                      |
| `nice`          |      ✅       |                    |       ✅        |          ✅          |
| `nl`            |      ✅       |                    |       ✅        |          ✅          |
| `nmeter`        |      ✅       |                    |                 |                      |
| `nohup`         |      ✅       |                    |       ✅        |          ✅          |
| `nologin`       |      ✅       |                    |                 |                      |
| `nproc`         |      ✅       |                    |       ✅        |          ✅          |
| `nsenter`       |      ✅       |                    |                 |                      |
| `numfmt`        |               |                    |       ✅        |          ✅          |
| `od`            |      ✅       |                    |       ✅        |          ✅          |
| `passwd`        |      ✅       |                    |                 |                      |
| `paste`         |      ✅       |                    |       ✅        |          ✅          |
| `pathchk`       |               |                    |       ✅        |          ✅          |
| `pgrep`         |      ✅       |                    |                 |                      |
| `pidof`         |      ✅       |                    |                 |                      |
| `ping`          |      ✅       |                    |                 |                      |
| `ping6`         |      ✅       |                    |                 |                      |
| `pinky`         |               |                    |       ✅        |          ✅          |
| `pipe_progress` |      ✅       |                    |                 |                      |
| `pivot_root`    |      ✅       |                    |                 |                      |
| `pkill`         |      ✅       |                    |                 |                      |
| `pmap`          |      ✅       |                    |                 |                      |
| `pr`            |               |                    |       ✅        |          ✅          |
| `printenv`      |      ✅       |                    |       ✅        |          ✅          |
| `printf`        |      ✅       |                    |       ✅        |          ✅          |
| `ps`            |      ✅       |                    |                 |                      |
| `pstree`        |      ✅       |                    |                 |                      |
| `ptx`           |               |                    |       ✅        |          ✅          |
| `pwd`           |      ✅       |                    |       ✅        |          ✅          |
| `pwdx`          |      ✅       |                    |                 |                      |
| `rdev`          |      ✅       |                    |                 |                      |
| `readahead`     |      ✅       |                    |                 |                      |
| `readlink`      |      ✅       |                    |       ✅        |          ✅          |
| `realpath`      |      ✅       |                    |       ✅        |          ✅          |
| `remove-shell`  |      ✅       |                    |                 |                      |
| `renice`        |      ✅       |                    |                 |                      |
| `reset`         |      ✅       |                    |                 |                      |
| `resize`        |      ✅       |                    |                 |                      |
| `rev`           |      ✅       |                    |                 |                      |
| `rm`            |      ✅       |                    |       ✅        |          ✅          |
| `rmdir`         |      ✅       |                    |       ✅        |          ✅          |
| `run-parts`     |      ✅       |                    |                 |                      |
| `runcon`        |               |                    |       ✅        |          ✅          |
| `sed`           |      ✅       |                    |                 |                      |
| `seq`           |      ✅       |                    |       ✅        |          ✅          |
| `setpriv`       |      ✅       |                    |                 |                      |
| `setserial`     |      ✅       |                    |                 |                      |
| `setsid`        |      ✅       |                    |                 |                      |
| `sh`            |      ✅       |                    |                 |                      |
| `sha1sum`       |      ✅       |                    |       ✅        |          ✅          |
| `sha224sum`     |               |                    |       ✅        |          ✅          |
| `sha256sum`     |      ✅       |                    |       ✅        |          ✅          |
| `sha384sum`     |               |                    |       ✅        |          ✅          |
| `sha3sum`       |      ✅       |                    |                 |                      |
| `sha512sum`     |      ✅       |                    |       ✅        |          ✅          |
| `shred`         |      ✅       |                    |       ✅        |          ✅          |
| `shuf`          |      ✅       |                    |       ✅        |          ✅          |
| `sleep`         |      ✅       |                    |       ✅        |          ✅          |
| `sort`          |      ✅       |                    |       ✅        |          ✅          |
| `split`         |      ✅       |                    |       ✅        |          ✅          |
| `stat`          |      ✅       |                    |       ✅        |          ✅          |
| `stdbuf`        |               |                    |       ✅        |          ✅          |
| `strings`       |      ✅       |                    |                 |                      |
| `stty`          |      ✅       |                    |       ✅        |          ✅          |
| `su`            |      ✅       |                    |                 |                      |
| `sum`           |      ✅       |                    |       ✅        |          ✅          |
| `sync`          |      ✅       |                    |       ✅        |          ✅          |
| `sysctl`        |      ✅       |                    |                 |                      |
| `tac`           |      ✅       |                    |       ✅        |          ✅          |
| `tail`          |      ✅       |                    |       ✅        |          ✅          |
| `tar`           |      ✅       |                    |                 |                      |
| `tee`           |      ✅       |                    |       ✅        |          ✅          |
| `test`          |      ✅       |                    |       ✅        |          ✅          |
| `time`          |      ✅       |                    |                 |                      |
| `timeout`       |      ✅       |                    |       ✅        |          ✅          |
| `top`           |      ✅       |                    |                 |                      |
| `touch`         |      ✅       |                    |       ✅        |          ✅          |
| `tr`            |      ✅       |                    |       ✅        |          ✅          |
| `traceroute`    |      ✅       |                    |                 |                      |
| `traceroute6`   |      ✅       |                    |                 |                      |
| `tree`          |      ✅       |                    |                 |                      |
| `true`          |      ✅       |                    |       ✅        |          ✅          |
| `truncate`      |      ✅       |                    |       ✅        |          ✅          |
| `tsort`         |      ✅       |                    |       ✅        |          ✅          |
| `tty`           |      ✅       |                    |       ✅        |          ✅          |
| `ttysize`       |      ✅       |                    |                 |                      |
| `tunctl`        |      ✅       |                    |                 |                      |
| `uname`         |      ✅       |                    |       ✅        |          ✅          |
| `unexpand`      |      ✅       |                    |       ✅        |          ✅          |
| `uniq`          |      ✅       |                    |       ✅        |          ✅          |
| `unix2dos`      |      ✅       |                    |                 |                      |
| `unlink`        |      ✅       |                    |       ✅        |          ✅          |
| `unlzma`        |      ✅       |                    |                 |                      |
| `unlzop`        |      ✅       |                    |                 |                      |
| `unxz`          |      ✅       |                    |                 |                      |
| `unzip`         |      ✅       |                    |                 |                      |
| `uptime`        |      ✅       |                    |                 |                      |
| `users`         |               |                    |       ✅        |          ✅          |
| `usleep`        |      ✅       |                    |                 |                      |
| `uudecode`      |      ✅       |                    |                 |                      |
| `uuencode`      |      ✅       |                    |                 |                      |
| `vconfig`       |      ✅       |                    |                 |                      |
| `vdir`          |               |                    |       ✅        |          ✅          |
| `vi`            |      ✅       |                    |                 |                      |
| `vlock`         |      ✅       |                    |                 |                      |
| `watch`         |      ✅       |                    |                 |                      |
| `wc`            |      ✅       |                    |       ✅        |          ✅          |
| `which`         |      ✅       |                    |                 |                      |
| `who`           |      ✅       |                    |       ✅        |          ✅          |
| `whoami`        |      ✅       |                    |       ✅        |          ✅          |
| `xargs`         |      ✅       |                    |                 |                      |
| `xxd`           |      ✅       |                    |                 |                      |
| `xzcat`         |      ✅       |                    |                 |                      |
| `yes`           |      ✅       |                    |       ✅        |          ✅          |
| `zcat`          |      ✅       |                    |                 |                      |
