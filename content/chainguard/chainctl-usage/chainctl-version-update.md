---
title: "Find and Update Your chainctl Release Version"
lead: ""
description: "chainctl version basics"
type: "article"
date: 2025-03-06T08:49:15+00:00
lastmod: 2025-03-06T08:49:15+00:00
draft: false
tags: ["chainctl", "version", "update", "Product"]
images: []
weight: 100
---

This page shows you how to check which release version of `chainctl` you have installed and how to update to the latest release.

For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).


## View your chainctl version

To see which `chainctl` version you have installed, use:

```shell
chainctl version
```

This command tells you more than just a release number.


```shell

               ▄▄▄▄▄▄▄▄▄▄▄              
             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            
           ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄          
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄         
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄        
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄        
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
           ▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄         

   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:    v0.2.66
GitCommit:     cb0ff7f1806341b20fd72be4769668a1985ed845
GitTreeState:  clean
BuildDate:     2025-04-09T07:49:51Z
GoVersion:     go1.24.1
Compiler:      gc
Platform:      linux/amd64

```




## Update your chainctl install

To update your `chainctl` installation to the latest release, use:

```shell
chainctl update
```

This will present the following:

```shell
Current version         v0.2.66
Latest version          0.2.73

Download URL            https://dl.enforce.dev/chainctl/latest/chainctl_linux_x86_64
chainctl filepath       /usr/local/bin/chainctl
Cache                   /root/.cache/chainctl

Operating System        linux
Architecture            x86_64

Do you want to continue? [Y,n]: 
```

Enter `Y` to proceed and the upgrade will continue and confirm like this:

```shell
   ✔ Download complete!

Backing up current chainctl (/usr/local/bin/chainctl)
Updating chainctl...

   Update complete! ⛓


               ▄▄▄▄▄▄▄▄▄▄▄              
             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            
           ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄          
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄         
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄        
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄        
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       
     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
           ▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄         

   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:    v0.2.73
GitCommit:     bd6a3e9901c85801697599d72e2646a862570cde
GitTreeState:  clean
BuildDate:     2025-04-22T17:27:55Z
GoVersion:     go1.24.2
Compiler:      gc
Platform:      linux/amd64

Temporary files may need to be removed manually:
  rm -f /root/.cache/chainctl/chainctl.bak

```