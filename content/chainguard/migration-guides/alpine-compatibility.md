---
title: "Alpine Compatibility"
linktitle: "Alpine Compatibility"
type: "article"
description: "Differences between Chainguard Images and Alpine third-party images"
date: 2024-02-23T15:56:52-07:00
lastmod: 2024-02-23T15:56:52-07:00
draft: false
tags: ["IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 600
toc: true
---

Chainguard Images and Alpine base images have different binaries and scripts included in their respective `busybox` and `coreutils` packages.

The following table lists common tools and their corresponding package(s) in both Wolfi and Alpine distributions.

Note that `$PATH` locations like `/usr/bin` or `/sbin` are not included here. If you have compatibiltiy issues with tools that are included in both `busybox` and `coreutils`, be sure to check `$PATH` order and confirm which version of a tool is being run.

Generally, if a tool exists in `busybox` but does not have a `coreutils` counterpart, there will be a specific package that includes it. For example the `zcat` utility is included in the `gzip` package in both Wolfi and Alpine.

You can use the `apk search` command in Wolfi and Alpine to find out which package includes a tool.

| Utility         | Wolfi busybox | Alpine busybox | Wolfi coreutils | Alpine coreutils |
| --------------- | :-----------: | :------------: | :-------------: | :--------------: |
| `[`             |      ✅       |       ✅       |       ✅        |        ✅        |
| `[[`            |      ✅       |       ✅       |                 |                  |
| `acpid`         |               |       ✅       |                 |                  |
| `add-shell`     |      ✅       |       ✅       |                 |                  |
| `addgroup`      |      ✅       |       ✅       |                 |                  |
| `adduser`       |      ✅       |       ✅       |                 |                  |
| `adjtimex`      |      ✅       |       ✅       |                 |                  |
| `arch`          |      ✅       |       ✅       |                 |                  |
| `arp`           |               |       ✅       |                 |                  |
| `arping`        |      ✅       |       ✅       |                 |                  |
| `ash`           |      ✅       |       ✅       |                 |                  |
| `awk`           |      ✅       |       ✅       |                 |                  |
| `b2sum`         |               |                |       ✅        |        ✅        |
| `base32`        |               |                |       ✅        |        ✅        |
| `base64`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `basename`      |      ✅       |       ✅       |       ✅        |        ✅        |
| `basenc`        |               |                |       ✅        |        ✅        |
| `bbconfig`      |      ✅       |       ✅       |                 |                  |
| `bc`            |      ✅       |       ✅       |                 |                  |
| `beep`          |      ✅       |       ✅       |                 |                  |
| `blkdiscard`    |               |       ✅       |                 |                  |
| `blkid`         |               |       ✅       |                 |                  |
| `blockdev`      |               |       ✅       |                 |                  |
| `brctl`         |               |       ✅       |                 |                  |
| `bunzip2`       |      ✅       |       ✅       |                 |                  |
| `bzcat`         |      ✅       |       ✅       |                 |                  |
| `bzip2`         |      ✅       |       ✅       |                 |                  |
| `cal`           |      ✅       |       ✅       |                 |                  |
| `cat`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `chattr`        |      ✅       |       ✅       |                 |                  |
| `chcon`         |               |                |       ✅        |        ✅        |
| `chgrp`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `chmod`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `chown`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `chpasswd`      |      ✅       |       ✅       |                 |                  |
| `chroot`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `chrt`          |      ✅       |                |                 |                  |
| `chvt`          |               |       ✅       |                 |                  |
| `cksum`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `clear`         |      ✅       |       ✅       |                 |                  |
| `cmp`           |      ✅       |       ✅       |                 |                  |
| `comm`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `coreutils`     |               |                |       ✅        |        ✅        |
| `cp`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `cpio`          |      ✅       |       ✅       |                 |                  |
| `crond`         |               |       ✅       |                 |                  |
| `crontab`       |               |       ✅       |                 |                  |
| `cryptpw`       |      ✅       |       ✅       |                 |                  |
| `csplit`        |               |                |       ✅        |        ✅        |
| `cut`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `date`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `dc`            |      ✅       |       ✅       |                 |                  |
| `dd`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `deallocvt`     |               |       ✅       |                 |                  |
| `delgroup`      |      ✅       |       ✅       |                 |                  |
| `deluser`       |      ✅       |       ✅       |                 |                  |
| `depmod`        |               |       ✅       |                 |                  |
| `df`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `diff`          |      ✅       |       ✅       |                 |                  |
| `dir`           |               |                |       ✅        |        ✅        |
| `dircolors`     |               |                |       ✅        |        ✅        |
| `dirname`       |      ✅       |       ✅       |       ✅        |        ✅        |
| `dmesg`         |      ✅       |       ✅       |                 |                  |
| `dnsdomainname` |      ✅       |       ✅       |                 |                  |
| `dos2unix`      |      ✅       |       ✅       |                 |                  |
| `du`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `dumpkmap`      |               |       ✅       |                 |                  |
| `echo`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `ed`            |      ✅       |                |                 |                  |
| `egrep`         |      ✅       |       ✅       |                 |                  |
| `eject`         |               |       ✅       |                 |                  |
| `env`           |      ✅       |       ✅       |       ✅        |                  |
| `ether-wake`    |               |       ✅       |                 |                  |
| `expand`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `expr`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `factor`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `fallocate`     |      ✅       |       ✅       |                 |                  |
| `false`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `fatattr`       |               |       ✅       |                 |                  |
| `fbset`         |               |       ✅       |                 |                  |
| `fbsplash`      |               |       ✅       |                 |                  |
| `fdflush`       |               |       ✅       |                 |                  |
| `fdisk`         |               |       ✅       |                 |                  |
| `fgrep`         |      ✅       |       ✅       |                 |                  |
| `find`          |      ✅       |       ✅       |                 |                  |
| `findfs`        |      ✅       |       ✅       |                 |                  |
| `flock`         |      ✅       |       ✅       |                 |                  |
| `fmt`           |               |                |       ✅        |                  |
| `fold`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `free`          |      ✅       |       ✅       |                 |                  |
| `fsck`          |               |       ✅       |                 |                  |
| `fstrim`        |               |       ✅       |                 |                  |
| `fsync`         |      ✅       |       ✅       |                 |                  |
| `fuser`         |      ✅       |       ✅       |                 |                  |
| `getopt`        |      ✅       |       ✅       |                 |                  |
| `getty`         |      ✅       |       ✅       |                 |                  |
| `grep`          |      ✅       |       ✅       |                 |                  |
| `groups`        |      ✅       |       ✅       |                 |                  |
| `gunzip`        |      ✅       |       ✅       |                 |                  |
| `gzip`          |      ✅       |       ✅       |                 |                  |
| `halt`          |               |       ✅       |                 |                  |
| `hd`            |      ✅       |       ✅       |                 |                  |
| `head`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `hexdump`       |      ✅       |       ✅       |                 |                  |
| `hostid`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `hostname`      |      ✅       |       ✅       |                 |                  |
| `hwclock`       |               |       ✅       |                 |                  |
| `id`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `ifconfig`      |               |       ✅       |                 |                  |
| `ifdown`        |               |       ✅       |                 |                  |
| `ifenslave`     |               |       ✅       |                 |                  |
| `ifup`          |               |       ✅       |                 |                  |
| `init`          |               |       ✅       |                 |                  |
| `inotifyd`      |      ✅       |       ✅       |                 |                  |
| `insmod`        |               |       ✅       |                 |                  |
| `install`       |      ✅       |       ✅       |       ✅        |        ✅        |
| `ionice`        |      ✅       |       ✅       |                 |                  |
| `iostat`        |      ✅       |       ✅       |                 |                  |
| `ip`            |               |       ✅       |                 |                  |
| `ipaddr`        |               |       ✅       |                 |                  |
| `ipcalc`        |               |       ✅       |                 |                  |
| `ipcrm`         |      ✅       |       ✅       |                 |                  |
| `ipcs`          |      ✅       |       ✅       |                 |                  |
| `iplink`        |               |       ✅       |                 |                  |
| `ipneigh`       |               |       ✅       |                 |                  |
| `iproute`       |               |       ✅       |                 |                  |
| `iprule`        |               |       ✅       |                 |                  |
| `iptunnel`      |               |       ✅       |                 |                  |
| `join`          |               |                |       ✅        |        ✅        |
| `kbd_mode`      |               |       ✅       |                 |                  |
| `kill`          |      ✅       |       ✅       |                 |                  |
| `killall`       |      ✅       |       ✅       |                 |                  |
| `killall5`      |      ✅       |       ✅       |                 |                  |
| `klogd`         |               |       ✅       |                 |                  |
| `last`          |               |       ✅       |                 |                  |
| `less`          |      ✅       |       ✅       |                 |                  |
| `link`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `linux32`       |      ✅       |       ✅       |                 |                  |
| `linux64`       |      ✅       |       ✅       |                 |                  |
| `ln`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `loadfont`      |               |       ✅       |                 |                  |
| `loadkmap`      |               |       ✅       |                 |                  |
| `logger`        |      ✅       |       ✅       |                 |                  |
| `login`         |      ✅       |       ✅       |                 |                  |
| `logname`       |               |                |       ✅        |        ✅        |
| `logread`       |               |       ✅       |                 |                  |
| `losetup`       |               |       ✅       |                 |                  |
| `ls`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `lsattr`        |      ✅       |       ✅       |                 |                  |
| `lsmod`         |               |       ✅       |                 |                  |
| `lsof`          |      ✅       |       ✅       |                 |                  |
| `lsusb`         |               |       ✅       |                 |                  |
| `lzcat`         |      ✅       |       ✅       |                 |                  |
| `lzma`          |      ✅       |       ✅       |                 |                  |
| `lzop`          |      ✅       |       ✅       |                 |                  |
| `lzopcat`       |      ✅       |       ✅       |                 |                  |
| `makemime`      |               |       ✅       |                 |                  |
| `md5sum`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `mdev`          |               |       ✅       |                 |                  |
| `mesg`          |               |       ✅       |                 |                  |
| `microcom`      |      ✅       |       ✅       |                 |                  |
| `mkdir`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `mkdosfs`       |               |       ✅       |                 |                  |
| `mkfifo`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `mkfs.vfat`     |               |       ✅       |                 |                  |
| `mknod`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `mkpasswd`      |      ✅       |       ✅       |                 |                  |
| `mkswap`        |               |       ✅       |                 |                  |
| `mktemp`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `modinfo`       |               |       ✅       |                 |                  |
| `modprobe`      |               |       ✅       |                 |                  |
| `more`          |      ✅       |       ✅       |                 |                  |
| `mount`         |               |       ✅       |                 |                  |
| `mountpoint`    |      ✅       |       ✅       |                 |                  |
| `mpstat`        |      ✅       |       ✅       |                 |                  |
| `mv`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `nameif`        |               |       ✅       |                 |                  |
| `nanddump`      |               |       ✅       |                 |                  |
| `nandwrite`     |               |       ✅       |                 |                  |
| `nbd-client`    |               |       ✅       |                 |                  |
| `nc`            |               |       ✅       |                 |                  |
| `netstat`       |      ✅       |       ✅       |                 |                  |
| `nice`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `nl`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `nmeter`        |      ✅       |       ✅       |                 |                  |
| `nohup`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `nologin`       |      ✅       |       ✅       |                 |                  |
| `nproc`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `nsenter`       |      ✅       |       ✅       |                 |                  |
| `nslookup`      |               |       ✅       |                 |                  |
| `ntpd`          |               |       ✅       |                 |                  |
| `numfmt`        |               |                |       ✅        |        ✅        |
| `od`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `openvt`        |               |       ✅       |                 |                  |
| `partprobe`     |               |       ✅       |                 |                  |
| `passwd`        |      ✅       |       ✅       |                 |                  |
| `paste`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `pathchk`       |               |                |       ✅        |        ✅        |
| `pgrep`         |      ✅       |       ✅       |                 |                  |
| `pidof`         |      ✅       |       ✅       |                 |                  |
| `ping`          |      ✅       |       ✅       |                 |                  |
| `ping6`         |      ✅       |       ✅       |                 |                  |
| `pinky`         |               |                |       ✅        |        ✅        |
| `pipe_progress` |      ✅       |       ✅       |                 |                  |
| `pivot_root`    |      ✅       |       ✅       |                 |                  |
| `pkill`         |      ✅       |       ✅       |                 |                  |
| `pmap`          |      ✅       |       ✅       |                 |                  |
| `poweroff`      |               |       ✅       |                 |                  |
| `pr`            |               |                |       ✅        |        ✅        |
| `printenv`      |      ✅       |       ✅       |       ✅        |        ✅        |
| `printf`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `ps`            |      ✅       |       ✅       |                 |                  |
| `pscan`         |               |       ✅       |                 |                  |
| `pstree`        |      ✅       |       ✅       |                 |                  |
| `ptx`           |               |                |       ✅        |        ✅        |
| `pwd`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `pwdx`          |      ✅       |       ✅       |                 |                  |
| `raidautorun`   |               |       ✅       |                 |                  |
| `rdate`         |               |       ✅       |                 |                  |
| `rdev`          |      ✅       |       ✅       |                 |                  |
| `readahead`     |      ✅       |       ✅       |                 |                  |
| `readlink`      |      ✅       |       ✅       |       ✅        |        ✅        |
| `realpath`      |      ✅       |       ✅       |       ✅        |        ✅        |
| `reboot`        |               |       ✅       |                 |                  |
| `reformime`     |               |       ✅       |                 |                  |
| `remove-shell`  |      ✅       |       ✅       |                 |                  |
| `renice`        |      ✅       |       ✅       |                 |                  |
| `reset`         |      ✅       |       ✅       |                 |                  |
| `resize`        |      ✅       |       ✅       |                 |                  |
| `rev`           |      ✅       |       ✅       |                 |                  |
| `rfkill`        |               |       ✅       |                 |                  |
| `rm`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `rmdir`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `rmmod`         |               |       ✅       |                 |                  |
| `route`         |               |       ✅       |                 |                  |
| `run-parts`     |      ✅       |       ✅       |                 |                  |
| `runcon`        |               |                |       ✅        |        ✅        |
| `sed`           |      ✅       |       ✅       |                 |                  |
| `sendmail`      |               |       ✅       |                 |                  |
| `seq`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `setconsole`    |               |       ✅       |                 |                  |
| `setfont`       |               |       ✅       |                 |                  |
| `setkeycodes`   |               |       ✅       |                 |                  |
| `setlogcons`    |               |       ✅       |                 |                  |
| `setpriv`       |      ✅       |       ✅       |                 |                  |
| `setserial`     |      ✅       |       ✅       |                 |                  |
| `setsid`        |      ✅       |       ✅       |                 |                  |
| `sh`            |      ✅       |       ✅       |                 |                  |
| `sha1sum`       |      ✅       |       ✅       |       ✅        |        ✅        |
| `sha224sum`     |               |                |       ✅        |        ✅        |
| `sha256sum`     |      ✅       |       ✅       |       ✅        |        ✅        |
| `sha384sum`     |               |                |       ✅        |        ✅        |
| `sha3sum`       |      ✅       |       ✅       |                 |                  |
| `sha512sum`     |      ✅       |       ✅       |       ✅        |                  |
| `showkey`       |               |       ✅       |                 |                  |
| `shred`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `shuf`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `slattach`      |               |       ✅       |                 |                  |
| `sleep`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `sort`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `split`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `stat`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `stdbuf`        |               |                |       ✅        |        ✅        |
| `strings`       |      ✅       |       ✅       |                 |                  |
| `stty`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `su`            |      ✅       |       ✅       |                 |                  |
| `sum`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `swapoff`       |               |       ✅       |                 |                  |
| `swapon`        |               |       ✅       |                 |                  |
| `switch_root`   |               |       ✅       |                 |                  |
| `sync`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `sysctl`        |      ✅       |       ✅       |                 |                  |
| `syslogd`       |               |       ✅       |                 |                  |
| `tac`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `tail`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `tar`           |      ✅       |       ✅       |                 |                  |
| `tee`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `test`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `time`          |      ✅       |       ✅       |                 |                  |
| `timeout`       |      ✅       |       ✅       |       ✅        |        ✅        |
| `top`           |      ✅       |       ✅       |                 |                  |
| `touch`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `tr`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `traceroute`    |      ✅       |       ✅       |                 |                  |
| `traceroute6`   |      ✅       |       ✅       |                 |                  |
| `tree`          |      ✅       |       ✅       |                 |                  |
| `true`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `truncate`      |      ✅       |       ✅       |       ✅        |        ✅        |
| `tsort`         |      ✅       |                |       ✅        |        ✅        |
| `tty`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `ttysize`       |      ✅       |       ✅       |                 |                  |
| `tunctl`        |      ✅       |       ✅       |                 |                  |
| `udhcpc`        |               |       ✅       |                 |                  |
| `udhcpc6`       |               |       ✅       |                 |                  |
| `umount`        |               |       ✅       |                 |                  |
| `uname`         |      ✅       |       ✅       |       ✅        |        ✅        |
| `unexpand`      |      ✅       |       ✅       |       ✅        |        ✅        |
| `uniq`          |      ✅       |       ✅       |       ✅        |        ✅        |
| `unix2dos`      |      ✅       |       ✅       |                 |                  |
| `unlink`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `unlzma`        |      ✅       |       ✅       |                 |                  |
| `unlzop`        |      ✅       |       ✅       |                 |                  |
| `unshare`       |               |       ✅       |                 |                  |
| `unxz`          |      ✅       |       ✅       |                 |                  |
| `unzip`         |      ✅       |       ✅       |                 |                  |
| `uptime`        |      ✅       |       ✅       |                 |                  |
| `users`         |               |                |       ✅        |        ✅        |
| `usleep`        |      ✅       |       ✅       |                 |                  |
| `uudecode`      |      ✅       |       ✅       |                 |                  |
| `uuencode`      |      ✅       |       ✅       |                 |                  |
| `vconfig`       |      ✅       |       ✅       |                 |                  |
| `vdir`          |               |                |       ✅        |        ✅        |
| `vi`            |      ✅       |       ✅       |                 |                  |
| `vlock`         |      ✅       |       ✅       |                 |                  |
| `volname`       |               |       ✅       |                 |                  |
| `watch`         |      ✅       |       ✅       |                 |                  |
| `watchdog`      |               |       ✅       |                 |                  |
| `wc`            |      ✅       |       ✅       |       ✅        |        ✅        |
| `wget`          |               |       ✅       |                 |                  |
| `which`         |      ✅       |       ✅       |                 |                  |
| `who`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `whoami`        |      ✅       |       ✅       |       ✅        |        ✅        |
| `whois`         |               |       ✅       |                 |                  |
| `xargs`         |      ✅       |       ✅       |                 |                  |
| `xxd`           |      ✅       |       ✅       |                 |                  |
| `xzcat`         |      ✅       |       ✅       |                 |                  |
| `yes`           |      ✅       |       ✅       |       ✅        |        ✅        |
| `zcat`          |      ✅       |       ✅       |                 |                  |
| `zcip`          |               |       ✅       |                 |                  |
