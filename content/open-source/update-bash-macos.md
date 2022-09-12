---
title: "Updating bash on macOS"
type: "article"
description: "Update bash to version 4 or above on macOS"
date: 2022-06-09T15:22:20+01:00
lastmod: 2022-06-09T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "open-source"
weight: 100
toc: true
---

The bash release included with macOS (v3.2) needs to be updated for Chainguard scripts. You’ll need to install a newer release and ensure it appears before `/bin/bash` in `$PATH`.

## Prerequisites

We’ll want to check the version of bash, and also ensure that the Homebrew package manager is installed. If you know your bash version is below 4 and that you have Homebrew installed, you can skip this section.

First, make sure your version is version 3.2 and that it hasn’t been updated.

```sh
bash --version
```

You’ll receive output similar to the following:

```
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin21)
Copyright (C) 2007 Free Software Foundation, Inc.
```

If your output is anything lower than version 4, as above, you’ll need to install a newer version of bash.

Next, you’ll need to have Homebrew installed as a package manager for your macOS machine. You can read more about Homebrew from their [official site](https://brew.sh/).

You can check whether Homebrew is already installed by checking its version:

```sh
brew --version
```

If you don’t get output of a version number (such as `Homebrew 3.4.4`), you can install Homebrew with the following command:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

With Homebrew installed and set up, you’re ready to update bash on macOS.

## Update Homebrew and Install a Newer Version of bash

Let’s update Homebrew to ensure we have the most recent version and go ahead and install Homebrew’s most recent version of bash.

```sh
brew update && brew install bash
```

You should get output regarding updated packages.

At this point, you should be able to check to see which versions of bash you currently have installed. List all the available versions with `which` and the “all” `-a` flag. 

```sh
which -a bash
```

Your output will likely be two different versions of bash — the one that was preinstalled on your machine, and the new Homebrew version.

```
/opt/homebrew/bin/bash
/bin/bash
```

However, if you run `which bash` without a flag, you will likely just receive the `/bin/bash` output, which means your machine is still using the preinstalled bash rather than the one you just added with Homebrew. We need to modify this.

## Update Bash Profile

In order to call the right version of bash, you’ll need to update your bash profile. In most macOS machines, you should be able to find this under `~/.bash_profile`. You can edit this with Vi, for example.

```sh
vi ~/.bash_profile
```

In the file, you’re going to want to add a line that sets up the PATH to direct to the Homebrew directory that you received above from the `which -a` bash output. 

```sh
export PATH="/opt/homebrew/bin:$PATH"
```

In our case, the new bash was in the directory path of `/opt/homebrew/bin` so we have exported that to PATH, as above. After inserting the line, you may save and quit Vi.

At this point, you can either restart your Terminal or source your Bash Profile so that the changes take place. Let’s do the latter.

```sh
source ~/.bash_profile
```

Once you have done this, you should get a clear command prompt.

## Verify macOS is Using the New Version of bash

With your PATH updated, you should be able to use the new version of bash on your macOS machine. You can confirm that your operating system is pulling the correct version by running the which command again.

```sh
which bash
```

Your output now should reflect the path where Homebrew installed the new version of bash and that you added to the Bash Profile. In our example, our output would be the following.

```sh
/opt/homebrew/bin/bash
```

You can further confirm that you’re using the updated bash by checking the version.

```sh
bash --version
```

You should receive output indicating that you are using version 4 or 5 of bash.

```
GNU bash, version 5.1.16(1)-release (aarch64-apple-darwin21.1.0)
Copyright (C) 2020 Free Software Foundation, Inc.
...
```

If you are not pulling from the correct location or are not running the expected version, please review the steps above to ensure that you did not introduce extra characters. Your Homebrew package manager may be configured to a different path; ensure that it is set up as you expect.