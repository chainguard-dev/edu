---
title: "Using the Chainguard API to Manage Custom Assembly Resources"
linktitle: "Manage with Chainguard's API"
type: "article"
description: "How to use the Chainguard API to manage Custom Assembly resources."
date: 2025-05-01T11:07:52+02:00
lastmod: 2025-05-01T11:07:52+02:00
draft: false
tags: ["CHAINGUARD CONTAINERS", "PRODUCT", "PROCEDURAL"]
images: []
menu:
  docs:
    parent: "features"
weight: 015
toc: true
---

Chainguard's [Custom Assembly](/chainguard/chainguard-images/features/custom-assembly/) is a tool that allows customers to create customized containers with extra packages added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

You can use the Chainguard API to further customize your Custom Assembly builds and retrieve information about them. This tutorial highlights a demo application (which can be found in [Chainguard Academy's Demo Applications repository](https://github.com/chainguard-dev/edu-images-demos/tree/main)) which, when run, updates a Custom Assembly container's configuration based on a provided YAML file.


## Prerequisites

In order to follow along with this guide, you will need the following:

* Access to a Custom Assembly container image. If your organization doesn't yet have access to Custom Assembly, reach out to your account team to start the process.
* The demo application used in this guide is written in Go, so you will need Go installed on your local machine. Refer to the [official Go documentation](https://go.dev/doc/install) for instructions on downloading and installing Go.
* You will also need [`chainctl` installed](/chainguard/chainctl-usage/how-to-install-chainctl/) on your local machine to create a Chainguard token and authenticate to the Chainguard API.


## Downloading the Demo Application

This step involves downloading the demo application code to your local machine. To ensure that the application files don't remain on your system, navigate to a temporary directory like `/tmp/`:

```shell
cd /tmp/
```

Your system will automatically delete the `/tmp/` directory's contents the next time it shuts down or reboots.

The code that comprises this demo application is hosted in a public GitHub repository managed by Chainguard. Pull down the example application files from GitHub with the following command:

```shell
git clone --sparse https://github.com/chainguard-dev/edu-images-demos.git
```

Because this guide's demo application code is stored in a repository with other examples, we don't need to pull down every file from this repository. For this reason, this command includes the `--sparse` option. This initializes a sparse-checkout file, causing the working directory to contain only the files in the root of the repository until the sparse-checkout configuration is modified.

Navigate into this new directory and list its contents to confirm this:

```shell
cd edu-images-demos/ && ls
```

For now, this directory only contains the repository's `LICENSE` and `README` files:

```
LICENSE  README.md
```

To retrieve the files you need for this tutorial's sample application, run the following `git` command:

```shell
git sparse-checkout set custom-assembly-go
```

This modifies the sparse-checkout configuration initialized in the previous `git clone` command so that the checkout only consists of the repo's `custom-assembly-go` directory.

Navigate into this new directory:

```shell
cd custom-assembly-go/
```

From here, you can run the application and use it to update the packages built into a Custom Assembly container. First though, let's go through the `main.go` file where the executable application code is written In order to understand how it works.


## Understanding the Demo Application

Before outlining how to run the demo application to update Custom Assembly container image, it's important that you have a general understanding of how the application works. 

This section will only provide a general overview of the application. We encourage you to read through the complete application, as it includes comments that explain what each portion of the code does. 

### Imports

The demo application uses the following packages:

```main.go
import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
	"time"

. . .
)
```

The application also uses the Chainguard SDK to interact with the Chainguard API and demonstrates proper patterns for authentication, error handling, and resource management. For this reason, the `import` section also brings in a number of protos from [`github.com/chainguard-dev/sdk`](https://github.com/chainguard-dev/sdk), the GitHub repository that stores Chainguard's public SDK for integrating with the Chainguard platform:

```main.go
import (
	
	. . .

	"chainguard.dev/sdk/auth"
	"chainguard.dev/sdk/proto/platform"
	commonv1 "chainguard.dev/sdk/proto/platform/common/v1"
	"chainguard.dev/sdk/proto/platform/iam/v1"
	registryv1 "chainguard.dev/sdk/proto/platform/registry/v1"
	"gopkg.in/yaml.v2"
)
```

Note that the `imports` block also contains `gopkg.in/yaml.v2`, the import path for the `yaml` package. This will allow the application to decode YAML values.

### Constants

Immediately below the imports, the application creates a few constants used throughout the code:

```main.go
const (
	defaultAPIURL	= "https://console-api.enforce.dev"
	tokenEnvVariable = "TOK"
	defaultGroupName = "ORGANIZATION"
	demoRepoName 	= "CUSTOM-IMAGE-NAME"
	buildConfigFile = "build.yaml"
)
```

* `defaultAPIURL`: This points to the Chainguard API's URL, which the application will reach in order to interact with the API.
* `tokenEnvVariable`: In order to use the Chainguard API, you must authenticate to prove that you have access to the resources you want to interact with. This constant defines an environment variable `TOK` that the application will expect to be present in order to function. This variable must hold a Chainguard authentication token; the next section describes how to create this environment variable. 
* `defaultGroupName`: This constant points to the Chainguard organization whose Custom Assembly resources you would like to manage.
* `demoRepoName`: This constant points to the name of the Custom Assembly container image that you'd like to update with this demo application.
* `buildConfigFile`: This last constant points to the `build.yaml` file, which you'll use to configure the Custom Assembly container image.

### Functions

Following the list of constants, the application declares a series of functions:

* `listRepositories`: This function lists repositories in a group with optional name filtering.
* `listBuildReports`: Lists build reports for a repository. Build reports provide information about image builds, including status, timestamps, and digests of the resulting images. This function shows how to query build reports for a specific repository.
* `printBuildReports`: This helper function displays build reports in a user-friendly format, showing the start time, result status, and image digest for each report.
* `applyCustomization`: This function demonstrates the pattern for updating a repository with a custom overlay that defines the packages to include in the image. The overlay is applied to the repository, which triggers a new build.
* `createClient`: This function creates a new Chainguard API client using a token from the environment.
* `confirmAction`: This utility function handles user confirmation for potentially destructive actions.

These functions come together in the `main()` function, which performs five main steps:

1. Create a Chainguard API client and authenticate
2. List repositories with optional filtering
3. List existing build reports for the repository
4. Apply image customizations using a build.yaml file
5. List and monitor new build reports

To accomplish all this, the application's functions perform the following API calls:

* [ListBuildReports](/chainguard/administration/api/#/operations/Registry_ListBuildReports)
* [ListRepos](/chainguard/administration/api/#/operations/Registry_ListRepos)
* [UpdateRepo](/chainguard/administration/api/#/operations/Registry_UpdateRepo)
* [Groups_List](/chainguard/administration/api/#/operations/Groups_List)

For a deeper understanding of what each function does and how the application works overall, we encourage you to closely review the `main.go` file before running it. You may also benefit from reviewing our [OpenAPI Specification reference document](/chainguard/administration/api/). 

Once you feel you have a grasp on how the demo application works, move on to the next section which outlines how to run it.


## Running the Demo Application

Before you can run the demo application, there are a few steps you need to take in order for it to work properly.

First, run the following `go` commands:

```shell
go mod init github.com/chainguard-dev/sdk && go mod tidy
```

The `go mod init` command will initialize a new `go.mod` file in the current directory. Including the `github.com/chainguard-dev/sdk` URL tells Go to use that as the module path. The `go mod tidy` command ensures that the new `go.mod` file matches the source code in the module.

As mentioned previously, you must authenticate before you can interact with the Chainguard API. For this reason, this demo application expects an environment variable named `TOK` to be present when it's run. Create this environment variable with the following command:

```shell
export TOK=$(chainctl auth token)
```

Following that, open up `main.go` with your preferred text editor. This example uses `nano`:

```shell
nano main.go
```

From there, edit the following lines:

```
    	// Group and repository settings
    	defaultGroupName = "ORGANIZATION"
    	demoRepoName 	= "CUSTOM-IMAGE-NAME"
```

Replace `ORGANIZATION` with the name of your organization's repository within the Chainguard registry. This usually takes the form of a domain name, such as `example.com`. Additionally, replace `CUSTOM-IMAGE-NAME` with the name of a Custom Assembly image. This is typically a name like `custom-nginx` or `custom-python`. 

Save and close the `main.go` file. If you used `nano`, you can do so by pressing `CTRL+X`, `Y`, and then `ENTER`. 

Next, open up the `build.yaml` file:

```shell
nano build.yaml
```

This file will have the following content:

```
contents:
  packages:
	- wolfi-base
	- go
```

Here, replace `wolfi-base` and `go` with whatever packages you'd like to be included in the customized container image. Note that you can only add packages that your organization already has access to, based on the Chainguard Containers you have already purchased. Refer to the [Custom Assembly Overview](/chainguard/chainguard-images/features/ca-docs/custom-assembly/#limitations) for more details on the limitations of what packages you can add to a Custom Assembly image.

Save and close the `build.yaml` file. Finally, you can run the application to apply the configuration listed in the `build.yaml` file to your organization's Custom Assembly image:

```shell
go run main.go
```

The application will start by listing the information outlined previously, including the specified organization's repositories and build reports for the chosen Custom Assembly image:

```
Group: example.com (ID: 45a0cEXAMPLE977f050c5fb9aEXAMPLEed764595)

All repositories in example.com:
- custom-assembly
- nginx
- curl

Repository: custom-assembly (ID: 45a0cEXAMPLE977f050c5fb9aEXAMPLEed764595/c375EXAMPLEb500c)

Build Reports for custom-node repository:

. . .

```

It will then prompt you to confirm that you want to apply the customization configuration listed in the `build.yaml` file:

```
About to apply customization using configuration file: build.yaml
Are you sure you want to update repository custom-node? (y/n): y
```

Enter `y` to confirm. Then, if everything was configured correctly, the application output will show successful build reports:

```
. . .

- Started: Mon, 28 Apr 2025 00:28:44 UTC, Result: Success, Digest: . . .
```

### Troubleshooting

Although the demo application has been tested to ensure that it works properly, there are several pitfalls one may encounter when they attempt to run it. 

For example, you may run into an error like the following:

```
Failed to list groups: rpc error: code = Internal desc = stream terminated by RST_STREAM with error code: PROTOCOL_ERROR
```

This may indicate that there is an issue with your Chainguard authentication token. To resolve this, try recreating the environment variable that holds the token:

```shell
export TOK=$(chainctl auth token)
```

You may also encounter errors like the following:

```
cannot find package "chainguard.dev/sdk/auth" . . .
```

This may indicate that the Chainguard SDK wasn't imported correctly. Be sure that you run the following commands to set this up:

```shell
go mod init github.com/chainguard-dev/sdk && go mod tidy
```

Again, the `main.go` file contains many comments that explain each portion of the code. If you encounter any errors, we encourage you to review the file closely to better understand how the application works and what might be going wrong.


## Learn More

The example application highlighted in this guide is intended to show how you can manage Custom Assembly resources with the Chainguard API. 

To learn more about Custom Assembly, you can refer to the [Custom Assembly Overview](/chainguard/chainguard-images/features/ca-docs/custom-assembly/). Be aware that it's also possible to edit a Custom Assembly container's configuration using `chainctl`. Check out our [documentation on the subject](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/) for more information.