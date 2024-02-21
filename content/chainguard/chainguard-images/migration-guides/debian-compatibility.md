---
title: "Debian Compatibility"
linktitle: "Debian Compatibility"
type: "article"
description: "Differences between Chainguard Images and Debian third-party images"
date: 2024-02-08T15:56:52-07:00
lastmod: 2024-02-08T15:56:52-07:00
draft: false
tags: ["IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 600
toc: true
---

Chainguard Images and Debian base images have different binaries and scripts included in their respective `busybox` and `coreutils` packages.

The following table lists common tools and their corresponding package(s) in both Wolfi and Debian distributions.

Note that `$PATH` locations like `/usr/bin` or `/sbin` are not included here. If you have compatibiltiy issues with tools that are included in both `busybox` and `coreutils`, be sure to check `$PATH` order and confirm which version of a tool is being run.

Generally, if a tool exists in `busybox` but does not have a `coreutils` counterpart, there will be a specific package that includes it. For example the `zcat` utility is included in the `gzip` package in both Wolfi and Debian.

You can use the `apk search` command in Wolfi, and the `apt-cache search` command in Debian to find out which package includes a tool.

| Utility                      | Wolfi busybox | Debian busybox | Wolfi coreutils | Debian coreutils |
| ---------------------------- | ------------- | -------------- | --------------- | ---------------- |
| `[`                          | ✅            | ✅             | ✅              | ✅               |
| `[[`                         | ✅            | ✅             |                 |                  |
| `acpid`                      |               | ✅             |                 |                  |
| `add-shell`                  | ✅            |                |                 |                  |
| `addgroup`                   | ✅            |                |                 |                  |
| `adduser`                    | ✅            |                |                 |                  |
| `adjtimex`                   | ✅            | ✅             |                 |                  |
| `ar`                         |               | ✅             |                 |                  |
| `arch`                       | ✅            | ✅             | ✅              |                  |
| `arp`                        |               | ✅             |                 |                  |
| `arping`                     | ✅            | ✅             |                 |                  |
| `ascii`                      |               | ✅             |                 |                  |
| `ash`                        | ✅            | ✅             |                 |                  |
| `awk`                        | ✅            | ✅             |                 |                  |
| `b2sum`                      |               |                | ✅              | ✅               |
| `base32`                     |               |                | ✅              | ✅               |
| `base64`                     | ✅            | ✅             | ✅              | ✅               |
| `basename`                   | ✅            | ✅             | ✅              | ✅               |
| `basenc`                     |               |                | ✅              | ✅               |
| `bbconfig`                   | ✅            |                |                 |                  |
| `bc`                         | ✅            | ✅             |                 |                  |
| `beep`                       | ✅            |                |                 |                  |
| `bin`                        |               |                | ✅              |                  |
| `blkdiscard`                 |               | ✅             |                 |                  |
| `blkid`                      |               | ✅             |                 |                  |
| `blockdev`                   |               | ✅             |                 |                  |
| `brctl`                      |               | ✅             |                 |                  |
| `bunzip2`                    | ✅            | ✅             |                 |                  |
| `bzcat`                      | ✅            | ✅             |                 |                  |
| `bzip2`                      | ✅            | ✅             |                 |                  |
| `cal`                        | ✅            | ✅             |                 |                  |
| `cat`                        | ✅            | ✅             | ✅              | ✅               |
| `chattr`                     | ✅            |                |                 |                  |
| `chcon`                      |               |                | ✅              | ✅               |
| `chgrp`                      | ✅            | ✅             | ✅              | ✅               |
| `chmod`                      | ✅            | ✅             | ✅              | ✅               |
| `chown`                      | ✅            | ✅             | ✅              | ✅               |
| `chpasswd`                   | ✅            |                |                 |                  |
| `chroot`                     | ✅            | ✅             | ✅              | ✅               |
| `chrt`                       | ✅            |                |                 |                  |
| `chvt`                       |               | ✅             |                 |                  |
| `cksum`                      | ✅            |                | ✅              | ✅               |
| `clear`                      | ✅            | ✅             |                 |                  |
| `cmp`                        | ✅            | ✅             |                 |                  |
| `comm`                       | ✅            |                | ✅              | ✅               |
| `coreutils`                  |               |                |                 | ✅               |
| `coreutils-9.4-r4.spdx.json` |               |                |                 | ✅               |
| `cp`                         | ✅            | ✅             | ✅              | ✅               |
| `cpio`                       | ✅            | ✅             |                 |                  |
| `crc32`                      |               | ✅             |                 |                  |
| `crond`                      |               | ✅             |                 |                  |
| `crontab`                    |               | ✅             |                 |                  |
| `cryptpw`                    | ✅            |                |                 |                  |
| `csplit`                     |               |                | ✅              | ✅               |
| `cttyhack`                   |               | ✅             |                 |                  |
| `cut`                        | ✅            | ✅             | ✅              | ✅               |
| `date`                       | ✅            | ✅             | ✅              | ✅               |
| `dc`                         | ✅            | ✅             |                 |                  |
| `dd`                         | ✅            | ✅             | ✅              | ✅               |
| `deallocvt`                  |               | ✅             |                 |                  |
| `delgroup`                   | ✅            |                |                 |                  |
| `deluser`                    | ✅            |                |                 |                  |
| `depmod`                     |               | ✅             |                 |                  |
| `devmem`                     |               | ✅             |                 |                  |
| `df`                         | ✅            | ✅             | ✅              | ✅               |
| `diff`                       | ✅            | ✅             |                 |                  |
| `dir`                        |               |                | ✅              | ✅               |
| `dircolors`                  |               |                | ✅              | ✅               |
| `dirname`                    | ✅            | ✅             | ✅              | ✅               |
| `dmesg`                      | ✅            | ✅             |                 |                  |
| `dnsdomainname`              | ✅            | ✅             |                 |                  |
| `dos2unix`                   | ✅            | ✅             |                 |                  |
| `dpkg`                       |               | ✅             |                 |                  |
| `dpkg-deb`                   |               | ✅             |                 |                  |
| `du`                         | ✅            | ✅             | ✅              | ✅               |
| `dumpkmap`                   |               | ✅             |                 |                  |
| `dumpleases`                 |               | ✅             |                 |                  |
| `echo`                       | ✅            | ✅             | ✅              | ✅               |
| `ed`                         | ✅            | ✅             |                 |                  |
| `egrep`                      | ✅            | ✅             |                 |                  |
| `env`                        | ✅            | ✅             | ✅              | ✅               |
| `expand`                     | ✅            | ✅             | ✅              | ✅               |
| `expr`                       | ✅            | ✅             | ✅              | ✅               |
| `factor`                     | ✅            | ✅             | ✅              | ✅               |
| `fallocate`                  | ✅            | ✅             |                 |                  |
| `false`                      | ✅            | ✅             | ✅              | ✅               |
| `fatattr`                    |               | ✅             |                 |                  |
| `fdisk`                      |               | ✅             |                 |                  |
| `fgrep`                      | ✅            | ✅             |                 |                  |
| `find`                       | ✅            | ✅             |                 |                  |
| `findfs`                     | ✅            | ✅             |                 |                  |
| `flock`                      | ✅            |                |                 |                  |
| `fmt`                        |               |                | ✅              | ✅               |
| `fold`                       | ✅            | ✅             | ✅              | ✅               |
| `free`                       | ✅            | ✅             |                 |                  |
| `freeramdisk`                |               | ✅             |                 |                  |
| `fsfreeze`                   |               | ✅             |                 |                  |
| `fstrim`                     |               | ✅             |                 |                  |
| `fsync`                      | ✅            |                |                 |                  |
| `ftpget`                     |               | ✅             |                 |                  |
| `ftpput`                     |               | ✅             |                 |                  |
| `fuser`                      | ✅            |                |                 |                  |
| `getopt`                     | ✅            | ✅             |                 |                  |
| `getty`                      | ✅            | ✅             |                 |                  |
| `grep`                       | ✅            | ✅             |                 |                  |
| `groups`                     | ✅            | ✅             | ✅              |                  |
| `gunzip`                     | ✅            | ✅             |                 |                  |
| `gzip`                       | ✅            | ✅             |                 |                  |
| `halt`                       |               | ✅             |                 |                  |
| `hd`                         | ✅            |                |                 |                  |
| `head`                       | ✅            | ✅             | ✅              | ✅               |
| `hexdump`                    | ✅            | ✅             |                 |                  |
| `hostid`                     | ✅            | ✅             | ✅              | ✅               |
| `hostname`                   | ✅            | ✅             |                 |                  |
| `httpd`                      |               | ✅             |                 |                  |
| `hwclock`                    |               | ✅             |                 |                  |
| `i2cdetect`                  |               | ✅             |                 |                  |
| `i2cdump`                    |               | ✅             |                 |                  |
| `i2cget`                     |               | ✅             |                 |                  |
| `i2cset`                     |               | ✅             |                 |                  |
| `i2ctransfer`                |               | ✅             |                 |                  |
| `id`                         | ✅            | ✅             | ✅              | ✅               |
| `ifconfig`                   |               | ✅             |                 |                  |
| `ifdown`                     |               | ✅             |                 |                  |
| `ifup`                       |               | ✅             |                 |                  |
| `init`                       |               | ✅             |                 |                  |
| `inotifyd`                   | ✅            |                |                 |                  |
| `insmod`                     |               | ✅             |                 |                  |
| `install`                    | ✅            |                | ✅              | ✅               |
| `ionice`                     | ✅            | ✅             |                 |                  |
| `iostat`                     | ✅            |                |                 |                  |
| `ip`                         |               | ✅             |                 |                  |
| `ipcalc`                     |               | ✅             |                 |                  |
| `ipcrm`                      | ✅            |                |                 |                  |
| `ipcs`                       | ✅            |                |                 |                  |
| `join`                       |               |                | ✅              | ✅               |
| `kill`                       | ✅            | ✅             |                 |                  |
| `killall`                    | ✅            | ✅             |                 |                  |
| `killall5`                   | ✅            |                |                 |                  |
| `klogd`                      |               | ✅             |                 |                  |
| `last`                       |               | ✅             |                 |                  |
| `less`                       | ✅            | ✅             |                 |                  |
| `link`                       | ✅            | ✅             | ✅              | ✅               |
| `linux32`                    | ✅            | ✅             |                 |                  |
| `linux64`                    | ✅            | ✅             |                 |                  |
| `linuxrc`                    |               | ✅             |                 |                  |
| `ln`                         | ✅            | ✅             | ✅              | ✅               |
| `loadfont`                   |               | ✅             |                 |                  |
| `loadkmap`                   |               | ✅             |                 |                  |
| `logger`                     | ✅            | ✅             |                 |                  |
| `login`                      | ✅            | ✅             |                 |                  |
| `logname`                    |               | ✅             | ✅              | ✅               |
| `logread`                    |               | ✅             |                 |                  |
| `losetup`                    |               | ✅             |                 |                  |
| `ls`                         | ✅            | ✅             | ✅              | ✅               |
| `lsattr`                     | ✅            |                |                 |                  |
| `lsmod`                      |               | ✅             |                 |                  |
| `lsof`                       | ✅            |                |                 |                  |
| `lsscsi`                     |               | ✅             |                 |                  |
| `lzcat`                      | ✅            | ✅             |                 |                  |
| `lzma`                       | ✅            | ✅             |                 |                  |
| `lzop`                       | ✅            | ✅             |                 |                  |
| `lzopcat`                    | ✅            |                |                 |                  |
| `md5sum`                     | ✅            | ✅             | ✅              | ✅               |
| `md5sum.textutils`           |               |                | ✅              |                  |
| `mdev`                       |               | ✅             |                 |                  |
| `microcom`                   | ✅            | ✅             |                 |                  |
| `mim`                        |               | ✅             |                 |                  |
| `mkdir`                      | ✅            | ✅             | ✅              | ✅               |
| `mkdosfs`                    |               | ✅             |                 |                  |
| `mke2fs`                     |               | ✅             |                 |                  |
| `mkfifo`                     | ✅            | ✅             | ✅              | ✅               |
| `mknod`                      | ✅            | ✅             | ✅              | ✅               |
| `mkpasswd`                   | ✅            | ✅             |                 |                  |
| `mkswap`                     |               | ✅             |                 |                  |
| `mktemp`                     | ✅            | ✅             | ✅              | ✅               |
| `modinfo`                    |               | ✅             |                 |                  |
| `modprobe`                   |               | ✅             |                 |                  |
| `more`                       | ✅            | ✅             |                 |                  |
| `mount`                      |               | ✅             |                 |                  |
| `mountpoint`                 | ✅            |                |                 |                  |
| `mpstat`                     | ✅            |                |                 |                  |
| `mt`                         |               | ✅             |                 |                  |
| `mv`                         | ✅            | ✅             | ✅              | ✅               |
| `nameif`                     |               | ✅             |                 |                  |
| `nbd-client`                 |               | ✅             |                 |                  |
| `nc`                         |               | ✅             |                 |                  |
| `netstat`                    | ✅            | ✅             |                 |                  |
| `nice`                       | ✅            |                | ✅              | ✅               |
| `nl`                         | ✅            | ✅             | ✅              | ✅               |
| `nmeter`                     | ✅            |                |                 |                  |
| `nohup`                      | ✅            |                | ✅              | ✅               |
| `nologin`                    | ✅            | ✅             |                 |                  |
| `nproc`                      | ✅            | ✅             | ✅              | ✅               |
| `nsenter`                    | ✅            | ✅             |                 |                  |
| `nslookup`                   |               | ✅             |                 |                  |
| `nuke`                       |               | ✅             |                 |                  |
| `numfmt`                     |               |                | ✅              | ✅               |
| `od`                         | ✅            | ✅             | ✅              | ✅               |
| `openvt`                     |               | ✅             |                 |                  |
| `partprobe`                  |               | ✅             |                 |                  |
| `passwd`                     | ✅            | ✅             |                 |                  |
| `paste`                      | ✅            | ✅             | ✅              | ✅               |
| `patch`                      |               | ✅             |                 |                  |
| `pathchk`                    |               |                | ✅              | ✅               |
| `pgrep`                      | ✅            |                |                 |                  |
| `pidof`                      | ✅            | ✅             |                 |                  |
| `ping`                       | ✅            | ✅             |                 |                  |
| `ping6`                      | ✅            | ✅             |                 |                  |
| `pinky`                      |               |                | ✅              | ✅               |
| `pipe_progress`              | ✅            |                |                 |                  |
| `pivot_root`                 | ✅            | ✅             |                 |                  |
| `pkill`                      | ✅            |                |                 |                  |
| `pmap`                       | ✅            |                |                 |                  |
| `poweroff`                   |               | ✅             |                 |                  |
| `pr`                         |               |                | ✅              | ✅               |
| `printenv`                   | ✅            |                | ✅              | ✅               |
| `printf`                     | ✅            | ✅             | ✅              | ✅               |
| `ps`                         | ✅            | ✅             |                 |                  |
| `pstree`                     | ✅            |                |                 |                  |
| `ptx`                        |               |                | ✅              | ✅               |
| `pwd`                        | ✅            | ✅             | ✅              | ✅               |
| `pwdx`                       | ✅            |                |                 |                  |
| `rdate`                      |               | ✅             |                 |                  |
| `rdev`                       | ✅            |                |                 |                  |
| `readahead`                  | ✅            |                |                 |                  |
| `readlink`                   | ✅            | ✅             | ✅              | ✅               |
| `realpath`                   | ✅            | ✅             | ✅              | ✅               |
| `reboot`                     |               | ✅             |                 |                  |
| `remove-shell`               | ✅            |                |                 |                  |
| `renice`                     | ✅            | ✅             |                 |                  |
| `reset`                      | ✅            | ✅             |                 |                  |
| `resize`                     | ✅            |                |                 |                  |
| `resume`                     |               | ✅             |                 |                  |
| `rev`                        | ✅            | ✅             |                 |                  |
| `rm`                         | ✅            | ✅             | ✅              | ✅               |
| `rmdir`                      | ✅            | ✅             | ✅              | ✅               |
| `rmmod`                      |               | ✅             |                 |                  |
| `route`                      |               | ✅             |                 |                  |
| `rpm`                        |               | ✅             |                 |                  |
| `rpm2cpio`                   |               | ✅             |                 |                  |
| `run-init`                   |               | ✅             |                 |                  |
| `run-parts`                  | ✅            | ✅             |                 |                  |
| `runcon`                     |               |                | ✅              | ✅               |
| `sbin`                       |               |                | ✅              |                  |
| `sed`                        | ✅            | ✅             |                 |                  |
| `seq`                        | ✅            | ✅             | ✅              | ✅               |
| `setkeycodes`                |               | ✅             |                 |                  |
| `setpriv`                    | ✅            | ✅             |                 |                  |
| `setserial`                  | ✅            |                |                 |                  |
| `setsid`                     | ✅            | ✅             |                 |                  |
| `sh`                         | ✅            | ✅             |                 |                  |
| `sha1sum`                    | ✅            | ✅             | ✅              | ✅               |
| `sha224sum`                  |               |                | ✅              | ✅               |
| `sha256sum`                  | ✅            | ✅             | ✅              | ✅               |
| `sha384sum`                  |               |                | ✅              | ✅               |
| `sha3sum`                    | ✅            | ✅             |                 |                  |
| `sha512sum`                  | ✅            | ✅             | ✅              | ✅               |
| `shred`                      | ✅            | ✅             | ✅              | ✅               |
| `shuf`                       | ✅            | ✅             | ✅              | ✅               |
| `sleep`                      | ✅            | ✅             | ✅              | ✅               |
| `sort`                       | ✅            | ✅             | ✅              | ✅               |
| `split`                      | ✅            |                | ✅              | ✅               |
| `ssl_client`                 |               | ✅             |                 |                  |
| `start-stop-daemon`          |               | ✅             |                 |                  |
| `stat`                       | ✅            | ✅             | ✅              | ✅               |
| `stdbuf`                     |               |                | ✅              | ✅               |
| `strings`                    | ✅            | ✅             |                 |                  |
| `stty`                       | ✅            | ✅             | ✅              | ✅               |
| `su`                         | ✅            | ✅             |                 |                  |
| `sulogin`                    |               | ✅             |                 |                  |
| `sum`                        | ✅            |                | ✅              | ✅               |
| `svc`                        |               | ✅             |                 |                  |
| `svok`                       |               | ✅             |                 |                  |
| `swapoff`                    |               | ✅             |                 |                  |
| `swapon`                     |               | ✅             |                 |                  |
| `switch_root`                |               | ✅             |                 |                  |
| `sync`                       | ✅            | ✅             | ✅              | ✅               |
| `sysctl`                     | ✅            | ✅             |                 |                  |
| `syslogd`                    |               | ✅             |                 |                  |
| `tac`                        | ✅            | ✅             | ✅              | ✅               |
| `tail`                       | ✅            | ✅             | ✅              | ✅               |
| `tar`                        | ✅            | ✅             |                 |                  |
| `taskset`                    |               | ✅             |                 |                  |
| `tc`                         |               | ✅             |                 |                  |
| `tee`                        | ✅            | ✅             | ✅              | ✅               |
| `telnet`                     |               | ✅             |                 |                  |
| `test`                       | ✅            | ✅             | ✅              | ✅               |
| `tftp`                       |               | ✅             |                 |                  |
| `time`                       | ✅            | ✅             |                 |                  |
| `timeout`                    | ✅            | ✅             | ✅              | ✅               |
| `top`                        | ✅            | ✅             |                 |                  |
| `touch`                      | ✅            | ✅             | ✅              | ✅               |
| `tr`                         | ✅            | ✅             | ✅              | ✅               |
| `traceroute`                 | ✅            | ✅             |                 |                  |
| `traceroute6`                | ✅            | ✅             |                 |                  |
| `tree`                       | ✅            |                |                 |                  |
| `true`                       | ✅            | ✅             | ✅              | ✅               |
| `truncate`                   | ✅            | ✅             | ✅              | ✅               |
| `ts`                         |               | ✅             |                 |                  |
| `tsort`                      | ✅            |                | ✅              | ✅               |
| `tty`                        | ✅            | ✅             | ✅              | ✅               |
| `ttysize`                    | ✅            |                |                 |                  |
| `tunctl`                     | ✅            | ✅             |                 |                  |
| `ubirename`                  |               | ✅             |                 |                  |
| `udhcpc`                     |               | ✅             |                 |                  |
| `udhcpc6`                    |               | ✅             |                 |                  |
| `udhcpd`                     |               | ✅             |                 |                  |
| `uevent`                     |               | ✅             |                 |                  |
| `umount`                     |               | ✅             |                 |                  |
| `uname`                      | ✅            | ✅             | ✅              | ✅               |
| `uncompress`                 |               | ✅             |                 |                  |
| `unexpand`                   | ✅            | ✅             | ✅              | ✅               |
| `uniq`                       | ✅            | ✅             | ✅              | ✅               |
| `unix2dos`                   | ✅            | ✅             |                 |                  |
| `unlink`                     | ✅            | ✅             | ✅              | ✅               |
| `unlzma`                     | ✅            | ✅             |                 |                  |
| `unlzop`                     | ✅            |                |                 |                  |
| `unshare`                    |               | ✅             |                 |                  |
| `unxz`                       | ✅            | ✅             |                 |                  |
| `unzip`                      | ✅            | ✅             |                 |                  |
| `uptime`                     | ✅            | ✅             |                 |                  |
| `users`                      |               |                | ✅              | ✅               |
| `usleep`                     | ✅            | ✅             |                 |                  |
| `usr`                        |               |                | ✅              |                  |
| `uudecode`                   | ✅            | ✅             |                 |                  |
| `uuencode`                   | ✅            | ✅             |                 |                  |
| `vconfig`                    | ✅            | ✅             |                 |                  |
| `vdir`                       |               |                | ✅              | ✅               |
| `vi`                         | ✅            | ✅             |                 |                  |
| `vlock`                      | ✅            |                |                 |                  |
| `w`                          |               | ✅             |                 |                  |
| `watch`                      | ✅            | ✅             |                 |                  |
| `watchdog`                   |               | ✅             |                 |                  |
| `wc`                         | ✅            | ✅             | ✅              | ✅               |
| `wget`                       |               | ✅             |                 |                  |
| `which`                      | ✅            | ✅             |                 |                  |
| `who`                        | ✅            | ✅             | ✅              | ✅               |
| `whoami`                     | ✅            | ✅             | ✅              | ✅               |
| `xargs`                      | ✅            | ✅             |                 |                  |
| `xxd`                        | ✅            | ✅             |                 |                  |
| `xz`                         |               | ✅             |                 |                  |
| `xzcat`                      | ✅            | ✅             |                 |                  |
| `yes`                        | ✅            | ✅             | ✅              | ✅               |
| `zcat`                       | ✅            | ✅             |                 |                  |
