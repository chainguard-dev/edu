---
title: "Using chainctl to Manage Custom Assembly Resources"
linktitle: "Manage with chainctl"
type: "article"
description: "How to use chainctl to manage Custom Assembly resources."
date: 2025-05-01T11:07:52+02:00
lastmod: 2025-05-01T11:07:52+02:00
draft: false
tags: ["CHAINGUARD CONTAINERS", "PRODUCT", "PROCEDURAL"]
images: []
menu:
  docs:
    parent: "features"
weight: 010
toc: true
---

Chainguard's [Custom Assembly](/chainguard-images/features/ca-docs/custom-assembly/) is a tool that allows customers to create customized containers with extra packages added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

You can use [`chainctl`, Chainguard's command-line interface tool](/chainguard/chainctl/), to further customize your Custom Assembly builds and retrieve information about them. This guide provides an overview of the relevant `chainctl` commands and outlines how you can edit the configuration of Custom Assembly containers, as well as retrieve a list of a customized image's builds and its build logs.


## Editing a Customized Container Image

To edit one of your organization's Custom Assembly container images, you can run the `chainctl image repo build edit` command:

```shell
chainctl image repo build edit --parent $ORGANIZATION --repo $CUSTOMIZED_CONTAINER
```

This example includes the `--parent` flag, which points to the name of your organization, and the `--repo` argument, which points to the name of your customized image.If you omit these arguments, `chainctl` will prompt you to select your organization and customized image interactively.

This command will open up a file with your machine's default text editor. This file will contain a structure like the following:

```yaml
contents:
  packages:
  - yarn
  - wget
```

Edit this file by adding or removing any packages you like. Then, save and close the file.

Before applying the change, `chainctl` will outline the changes you made and prompt you to confirm that you want to move forward with the change:

```
/tmp/3352123767.yaml (-deletion / +addition):

 contents:
   packages:
   - yarn
-  - wget
+  - bash
 
Applying build config to custom-node
Are you sure?
Do you want to continue? [y,N]:
```

Enter `y` to apply the changes. 

Following that, you'll be able to see the updated builds in the Chainguard Console, though it may take a few minutes for these changes to populate.

## Retrieving Information about Custom Assembly Containers

You can also use the `list` subcommand to retrieve every one of a customized image's builds from the past 24 hours:

```shell
chainctl image repo build list --parent $ORGANIZATION --repo $REPO
```

This command is useful for quickly determining which builds were successful or failed:

```
           START TIME           |        COMPLETION TIME        | RESULT  |                    TAGS                     
--------------------------------+-------------------------------+---------+---------------------------------------------
  Thu, 01 May 2025 10:10:40 PDT | Thu, 01 May 2025 10:10:45 PDT | Success | 20, 20.19, 20.19.1                          
  Thu, 01 May 2025 10:10:34 PDT | Thu, 01 May 2025 10:10:46 PDT | Success | 22-slim, 22.15-slim, 22.15.0-slim           
  Thu, 01 May 2025 10:10:33 PDT | Thu, 01 May 2025 10:10:41 PDT | Success | 23, 23.11, 23.11.0, latest                  

. . .
```

Lastly, you can also retrieve the logs for a given build with the `logs` subcommand:

```shell
chainctl image repo build logs --parent $ORGANIZATION --repo $REPO
```

This command will prompt you to select the build report you want to view. These are organized in reverse chronological order by the time of each build:

```
	Select a build report to view logs:                                                                          	 
                                                                                                                 	 
	Wed, 16 Apr 2025 16:36:52 PDT - Wed, 16 Apr 2025 16:37:08 PDT Success (18-dev, 18.20-dev, 18.20.8-dev)       	 
  > Wed, 16 Apr 2025 16:36:45 PDT - Wed, 16 Apr 2025 16:37:00 PDT Success (20-dev, 20.19-dev, 20.19.0-dev)       	 
	Wed, 16 Apr 2025 16:36:42 PDT - Wed, 16 Apr 2025 16:36:52 PDT Success (18, 18.20, 18.20.8)                   	 
	Wed, 16 Apr 2025 16:36:41 PDT - Wed, 16 Apr 2025 16:36:51 PDT Success (22-slim, 22.14-slim, 22.14.0-slim)    	 
	Wed, 16 Apr 2025 16:36:32 PDT - Wed, 16 Apr 2025 16:36:57 PDT Success (22-dev, 22.14-dev, 22.14.0-dev)       	 
	Wed, 16 Apr 2025 16:36:32 PDT - Wed, 16 Apr 2025 16:36:44 PDT Success (20-slim, 20.19-slim, 20.19.0-slim)    	 
	Wed, 16 Apr 2025 16:36:29 PDT - Wed, 16 Apr 2025 16:36:41 PDT Success (23-slim, 23.11-slim, 23.11.0-slim)    	 
	Wed, 16 Apr 2025 16:36:19 PDT - Wed, 16 Apr 2025 16:36:29 PDT Success (23, 23.11, 23.11.0, latest)           	 
	Wed, 16 Apr 2025 16:36:09 PDT - Wed, 16 Apr 2025 16:36:42 PDT Success (23-dev, 23.11-dev, 23.11.0-dev, latest-dev)
	Wed, 16 Apr 2025 16:36:09 PDT - Wed, 16 Apr 2025 16:36:31 PDT Success (20, 20.19, 20.19.0)                   	 
	Wed, 16 Apr 2025 16:36:09 PDT - Wed, 16 Apr 2025 16:36:31 PDT Success (22, 22.14, 22.14.0)                   	 
	Wed, 16 Apr 2025 16:36:09 PDT - Wed, 16 Apr 2025 16:36:18 PDT Success (18-slim, 18.20-slim, 18.20.8-slim)    	 
	Wed, 16 Apr 2025 16:35:35 PDT - Wed, 16 Apr 2025 16:35:47 PDT Success                                        	 
                                                                                                                 	 
	••••••••••••••                                                                                               	 
                                                                                                                 	 
	↑/k up • ↓/j down • / filter • q quit • ? more  

```

Highlight your chosen build report and select it by pressing `ENTER`. This will open up the build's logs:

```
2025-04-17T16:00:08-07:00[INFO]Building image with locked configuration: {Contents:{BuildRepositories:[] RuntimeRepositories:[https://apk.cgr.dev/45a0c61eEXAMPLEf050c5fb9ac06a69eed764595]
```

## Learn More

The `chainctl` commands outlined in this guide show how you can interact with Chainguard's Custom Assembly tool from the command line. 

You can also interact with Custom Assembly with the [Chainguard API](/chainguard/administration/api/). Our tutorial on [Using the Chainguard API to Manage Custom Assembly Resources](/chainguard-images/features/ca-docs/custom-assembly-api-demo/) outlines how to run a demo application that updates the configuration of a Custom Assembly container through the Chainguard API. 