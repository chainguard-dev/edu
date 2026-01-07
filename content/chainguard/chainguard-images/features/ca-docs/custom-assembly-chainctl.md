---
title: "Using chainctl to Manage Custom Assembly Resources"
linktitle: "Manage with chainctl"
type: "article"
description: "How to use chainctl to manage Custom Assembly resources."
date: 2025-05-01T11:07:52+02:00
lastmod: 2025-07-15T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
weight: 010
toc: true
---

Chainguard's [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) is a tool that allows customers to create customized containers with extra packages and annotations added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

You can use [`chainctl`, Chainguard's command-line interface tool](/chainguard/chainctl/), to further customize your Custom Assembly builds and retrieve information about them. This guide provides an overview of the relevant `chainctl` commands and outlines how you can edit the configuration of Custom Assembly containers, as well as retrieve a list of a customized image's builds and its build logs.

> **Note**: This tutorial highlights using `chainctl` to interact with Custom Assembly resources. However, you can also interact with Custom Assembly using [the Chainguard console](/chainguard/chainguard-images/features/ca-docs/custom-assembly-console/), as well as [the Chainguard API](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/).


## Adding Packages to a Customized Container Image

To edit one of your organization's Custom Assembly container images, you can run the `chainctl image repo build edit` command:

```shell
chainctl image repo build edit --parent $ORGANIZATION --repo $CONTAINER
```

This example includes the `--parent` flag, which points to the name of your organization, and the `--repo` argument, which points to the name of the image you want to customize. If you omit these arguments, `chainctl` will prompt you to select your organization and container image interactively.

This command will open up a file with your machine's default text editor. This file will contain a structure like the following:

```yaml
contents:
  packages:
  - yarn
  - wget
```

Edit this file by adding or removing any packages you like. Then, save and close the file. Note that you can undo all the customization and return the image to its original state by removing every entry listed under `packages:`.

Before applying the change, `chainctl` will outline the changes you made and prompt you to confirm that you want to move forward with the change:

```output
/tmp/3352123767.yaml (-deletion / +addition):

 contents:
   packages:
   - yarn
-  - wget
+  - bash
 
Applying build config to $CONTAINER
Are you sure?
Do you want to continue? [y,N]:
```

Enter `y` to apply the changes. 

Following that, you'll be able to see the updated builds in the Chainguard Console, though it may take a few minutes for these changes to populate.

To edit a customized container image without any interactivity, you can use the `apply` subcommand. This method requires you to have a YAML file listing the desired packages, like the example created with this command:

```shell
cat > build.yaml <<EOF
contents:
  packages:
    - bash
    - curl
    - mysql
EOF
```

Then include this file in the `apply` command by adding the `-f` argument:

```shell
chainctl image repo build apply -f build.yaml --parent $ORGANIZATION --repo $CONTAINER --yes
```

This command will again ask you to confirm that you want to apply the new configuration. To make this example completely declarative, this example includes `--yes` to automatically confirm the changes:

```
Applying build config to custom-assembly
  (*v1.CustomOverlay)(Inverse(protocmp.Transform, protocmp.Message{
      "@type": s"chainguard.platform.registry.CustomOverlay",
      "contents": protocmp.Message{
          "@type": s"chainguard.platform.registry.ImageContents",
          "packages": []string{
-             "wolfi-base",
+             "bash",
-             "go",
+             "curl",
+             "mysql",
          },
      },
  }))

Are you sure?
Do you want to continue? [y,N]: 
```

This approach is useful in cases where you would prefer to avoid any kind of interactivity, as in a CI/CD or other automation system.

### Using the `--save-as` option

When customizing a Chainguard Container with Custom Assembly, you have the option to either customize the image itself or create a new image based on the original with your customizations applied to it.

For example, say your organization has access to Chainguard's [`node` container image](https://images.chainguard.dev/directory/image/node/versions). If you use Custom Assembly to customize the `node` image without creating a new image, then the customizations applied to it will also apply to any users in your organization that are already consuming the image. Anyone who runs `docker pull cgr.dev/example.come/node` will download the customized image instead of the original, uncustomized one.

By creating a new image with Custom Assembly, you can customize the image without impacting any of the users or workflows already consuming it. You could also create multiple customized images based on the `node` container image to support specific functions.

To use `chainctl` to create new customized container images with Custom Assembly, you must include the `--save-as` option, like this:

```shell
chainctl image repo build edit --parent $ORGANIZATION --repo $CONTAINER --save-as $NEW_NAME
```

The following example command creates a new image named `custom-node` after applying the customizations:

```shell
chainctl image repo build edit --parent example.com --repo node --save-as custom-node
```

Once you run this example, the new container image would be accessible from the following URL:

```url
cgr.dev/example.com/custom-node
```

Note that you **must** pass the new image's name when using the `--save-as` option; `chainctl` will return an error if you don't include a new name. Additionally, you can only use this option with the `edit` subcommand; you cannot create a new image declaratively using the `apply` subcommand.


## Adding Custom Annotations and Environment Variables

Custom Assembly lets you extend Chainguard Containers with your own metadata and runtime defaults by adding custom annotations and environment variables through `chainctl`.

### Custom annotations

Chainguard Containers include metadata in the form of *annotations*. These annotations provide important information about the container image's origin, contents, and characteristics. 

With Custom Assembly, you can add custom annotations to your Chainguard Containers using `chainctl`. The process is the same as the one outlined previously for adding packages. First run a command like the following:

```shell
chainctl image repo build edit --parent $ORGANIZATION --repo $CONTAINER
```

In the text editor, add an `annotations` section to the bottom of the file like the following example:

```yaml
contents:
  packages:
    - jq
    - git
    - curl

annotations:
  "com.example.team": "platform-team"
  "com.example.build-timestamp": "2025-10-15T10:30:00Z"
```

After saving and confirming these changes, Custom Assembly will add two custom annotations to the container image.

You can also apply custom annotations declaratively using the `apply` subcommand, as outlined previously.

Note that Custom Assembly blocks `org.opencontainers` and `dev.chainguard` annotations from being changed. 

### Custom environment variables

Chainguard Containers often come with a set of predefined environment variables. These are useful for setting certain configuration details that are available to the container at runtime.

You can follow the same procedure for adding custom annotations to add custom environment variables to your Custom Assembly container images. Start by running a `chainctl image repo build edit` command: 

```shell
chainctl image repo build edit --parent $ORGANIZATION --repo $CONTAINER
```

In the text editor, add an `environment` section like the following example:

```yaml
contents:
  packages:
    - jq
    - git
    - curl

environment:
  NODE_ENV: production
  API_URL: https://api.example.com
  PORT: "3000"
  LOG_LEVEL: info
  CACHE_TTL: "300"
```

After saving and confirming these changes, Custom Assembly will add these five custom environment variables to the container image. As with packages and annotations, you can also apply custom environment variables declaratively using the `apply` subcommand, as outlined previously.

Be aware that Custom Assembly blocks any environment variable that begins with `CHAINGUARD_` from being added or changed. This is to prevent conflicts with configuration details managed by Chainguard.

## Adding custom certificates

Many enterprise environments use internal certificate authorities (CAs) to issue certificates for internal services. These custom certificates need to be trusted by containers that communicate with the internal services. Custom Assembly allows you to build custom certificates directly into your container images, ensuring they trust your organization's internal services without requiring manual certificate mounting at runtime.

### Prerequisites and limitations

Before getting started, you'll need:
* Access to Chainguard's Custom Assembly tool, which is available to any organization with access to Production Chainguard Containers
* Appropriate permissions in your Chainguard organization to use Custom Assembly. Review the [Custom Assembly Permissions Requirements](https://edu.chainguard.dev/chainguard/chainguard-images/features/ca-docs/custom-assembly/#custom-assembly-permissions-requirements) for more information
* [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) installed and configured
* One or more PEM-encoded certificate files that you want to add to your container
  * Each certificate must have a unique name.
  * Each certificate must be a PEM-encoded string of an x509v3 certificate.
  * Private keys must not be passed as a certificate, and will be rejected.
  * The total size of all inlined certificates must not exceed 50 KB. Please reach out to your account team if there are any issues with this limit.


Additionally, be aware of the following limitations when adding custom certificates:

* **Certificates must be added via API or chainctl**: Adding new certificates is currently only available via the API and chainctl.
* **Certificates must be added per-image**: You cannot currently set default certificates for all images in your organization.
* **No Java truststore support yet**: Custom certificates are only concatenated to the ca-certificates.crt file, but not added to Java-specific truststores. This functionality is planned for a future release.
* **Certificates not in SBOM**: Custom certificates are included in the image's provenance attestation but are not currently listed in the SBOM. They will appear in the apko configuration attestation
* **No audit log trail**: Certificate additions are not currently tracked in the Chainguard audit log

### How to add custom certificates via Custom Assembly

With Custom Assembly, you can add custom certificates to your Chainguard Containers using `chainctl`. The process is similar the one outlined previously for adding packages. 

1. Run a command like the following:

```shell
chainctl image repos build edit my-custom-image --parent $ORGANIZATION --repo $CONTAINER
```

This will open your default text editor with the current configuration. 

2. Add a `certificates` section with your custom certificates. Note that each entry must contain exactly one PEM block (`BEGIN CERTIFICATE` to `END CERTIFICATE`):

```yaml
contents:
  packages:
    - jq
    - git
    - curl

certificates:
  additional:
    - name: internal-ca
      content: |
        -----BEGIN CERTIFICATE-----
        MIIDXTCCAkWgAwIBAgIJAKL0UG+mRkmSMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
        BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
        ... (certificate content continues)
        -----END CERTIFICATE-----
    - name: partner-ca
      content: |
        Some descriptive text about this certificate's purpose
        -----BEGIN CERTIFICATE-----
        MIIDZTCCAk2gAwIBAgIJALT1VH+nSlnTMA0GCSqGSIb3DQEBCwUAMEYxCzAJBgNV
        ... (certificate content continues)
        -----END CERTIFICATE-----

```
Note that each certificate entry requires:

* `name`: A descriptive name for the certificate (used for the filename)
* `content`: The certificate in PEM format, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` markers

Optionally, you can also include descriptive text before the certificate block to document its purpose. 

3. Save and confirm your changes.

After saving and closing the editor, `chainctl` will display the changes and prompt for confirmation before applying them.

The provided inline certificates will be added (concatenated) to the default truststore of the image in `/etc/ssl/certs/ca-certificates.crt`. They will also be individually written to `/usr/local/share/ca-certificates` and will be available for workflows that involve manually running `update-ca-certificates`.

### Verify that certificates were added

You can verify that your certificates were added correctly by examining the truststore inside the container:

```shell
docker run --rm cgr.dev/my-org/my-custom-image:latest \
  cat /etc/ssl/certs/ca-certificates.crt | grep "BEGIN CERTIFICATE" | wc -l
```

You can also check for your specific certificate by name:

```shell
docker run --rm cgr.dev/my-org/my-custom-image:latest \
  ls -la /usr/local/share/ca-certificates/ | grep internal-ca
```


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

You can also interact with Custom Assembly with the [Chainguard API](/chainguard/administration/api/). Our tutorial on [Using the Chainguard API to Manage Custom Assembly Resources](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/) outlines how to run a demo application that updates the configuration of a Custom Assembly container through the Chainguard API. 