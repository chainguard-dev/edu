---
title: "Adding Custom Certificates with Custom Assembly"
linktitle: "Custom Certificates"
type: "article"
description: "How to add custom certificates to customized images with Custom Assembly."
date: 2026-03-12T11:07:52+02:00
lastmod: 2026-03-12T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
weight: 020
toc: true
---

Many enterprise environments use internal certificate authorities (CAs) to issue certificates for internal services. These custom certificates need to be trusted by containers that communicate with the internal services. Custom Assembly allows you to build custom certificates directly into your container images, ensuring they trust your organization's internal services without requiring manual certificate mounting at runtime.

> **Note**: If you are looking for a way to embed certificates at build time, refer to our guide on [How To Use incert to Create Container Images with Built-in Custom Certificates](/chainguard/chainguard-images/features/incert-custom-certs/).

## Prerequisites and limitations

Before getting started, you'll need the following:
* Access to Chainguard's Custom Assembly tool, which is available to any organization with access to Production Chainguard Containers.
* Permissions in your Chainguard organization to use Custom Assembly.
  * Review the [Custom Assembly Permissions Requirements](https://edu.chainguard.dev/chainguard/chainguard-images/features/ca-docs/custom-assembly/#custom-assembly-permissions-requirements) for more information
* [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) installed and configured.
* One or more PEM-encoded certificate files that you want to add to your container.
  * Each certificate must be a PEM-encoded string of an x509v3 certificate.
  * Private keys must not be passed as a certificate, and will be rejected.
  * The total size of all inlined certificates must not exceed 50 KB. Please reach out to your account team if there are any issues with this limit.


Additionally, be aware of the following limitations when adding custom certificates:

* Adding new certificates is currently only available through the API and `chainctl`.
* Custom certificates are included in the image's provenance attestation but are not currently listed in the SBOM. They will appear in the apko configuration attestation.


## Using `chainctl` to add custom certificates using Custom Assembly

With Custom Assembly, you can add custom certificates to your Chainguard Containers using `chainctl images repos build edit` or `chainctl images repos build apply`. The process is similar to the process for [using Custom Assembly to add packages with `chainctl`](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/).

### Interactive usage

You can add certificates interactively by running a command like the following:

```shell
chainctl image repos build edit --parent $ORGANIZATION --repo $CONTAINER
```

This will open your default text editor with the current configuration. This example includes the `--parent` flag, which points to the name of your organization, and the `--repo` argument, which points to the name of the image you want to customize. If you omit these arguments, `chainctl` will prompt you to select your organization and container image interactively.

In the editor, add one or more `certificates` sections with your custom certificates. Note that each entry must contain exactly one PEM block (`BEGIN CERTIFICATE` to `END CERTIFICATE`):

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

* `name`: A descriptive name for the certificate (used for the filename).
* `content`: The certificate in PEM format, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` markers.

Optionally, you can also include descriptive text before the certificate block to document its purpose.

Save your changes and close the editor. `chainctl` will display the changes and prompt for confirmation before applying them.

This adds (concatenates) the provided inline certificates to the default truststore of the image in `/etc/ssl/certs/ca-certificates.crt`. It also writes them individually to `/usr/local/share/ca-certificates`, making them available for workflows that involve manually running `update-ca-certificates`.

Alternatively, you can use the `--with-certificates` flag to pre-populate the `certificates.additional` section from a selected `.pem` file. Here is an example invocation that uses a `.pem` file named `certificates.pem`:

```shell
chainctl images repos build edit --with-certificates certificate.pem --parent $ORGANIZATION --repo $CONTAINER
```

As with the previous example, this will open up the configuration in your default editor. After saving and closing the editor, `chainctl` will prompt you to confirm the changes before applying them.

### Non-interactive usage

To add certificates without any interactivity, you can use the `apply` subcommand. This requires you to supply a YAML configuration file listing the certificates, like the example created with this command:

```shell
cat > cert.yaml <<EOF
certificates:
  additional:
  - name: ca1
    content: |
      -----BEGIN CERTIFICATE-----
      <certificate contents>
      -----END CERTIFICATE-----
EOF
```

Then include this file in the `apply` command by adding the `-f` argument:

```shell
chainctl image repos build apply --parent $ORGANIZATION --repo $CONTAINER -f cert.yaml --yes
```

This command will again ask you to confirm that you want to apply the new configuration. To make this example completely declarative, this example includes `--yes` to automatically confirm the changes:

```output
Image configuration changes:
Legend: + to add, ~ to change, - to remove

certificates.additional (+1, ~0, -0, final: 1):
  + Name: ca1
      Fingerprint:      CA:2F:ED:41:E8:A2:C9:D0:25:A2:8E:E5:0C:95:9B:E2
                        15:10:F4:1E:72:B7:31:AA:B0:51:CD:AC:E9:F2:0C:51
      SANs:             (none)
      Issuer:           O=Internet Widgits Pty Ltd,ST=Some-State,C=AU
      Expires:          2036-03-08 19:10:43 UTC
      PublicKey:        RSA 2048-bit (ee878ed5)
      Serial:           53:99:5e:47:8c:27:39:60:7b:fb:2b:17:77:ae:a2:01:03:1c:93:31
      ExtKeyUsage:      (none)
      KeyUsage:         (none)
      BasicConstraints: CA:TRUE
      Subject:          O=Internet Widgits Pty Ltd,ST=Some-State,C=AU


Plan: 1 to add, 0 to change, 0 to remove
```

The non-interactive approach is particularly useful for CI/CD pipelines and automation.


## Verifying that certificates were added

Before following the steps below, ensure you have [`crane` installed](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md#installation).

You can verify that your certificates are present in the system trust bundle by using `crane` to export the image filesystem, extract the system CA bundle from the archive, and write it to a local file for inspection:

```shell
crane export cgr.dev/my-org/my-custom-image:latest - | tar -xOf - etc/ssl/certs/ca-certificates.crt > ca-certificates.crt
```
After running this command, inspect the copied file locally to confirm that your certificate is present.


## Changuard-managed certificate bundles

Customers have the ability to add Chainguard-managed certificate bundles for certain regulated environments to their Custom Assembly images. These certificates are bundled into discrete packages that you can apply to customized images in bulk. You can add them to a customized image the same way you would add any other package with Custom Assembly, including with [`chainctl`](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/) or in the [Chainguard Console](/chainguard/chainguard-images/features/ca-docs/custom-assembly-console/). 

The following example YAML configuration shows two certificate bundle packages added to an image:

```yaml
contents:
  packages:
  - ca-certificates-aws-rds-global
  - ca-certificates-dod-wcf

. . .
```

As of this writing, Chainguard offers the following certificate bundle packages for DoD and AWS environments:

* `ca-certificates-aws-rds-global` — Any commercial AWS Region
* `ca-certificates-aws-rds-govcloud-global` — AWS US GovCloud
* `ca-certificates-dod-eca` — US DoD External Certificate Authority (ECA) PKI certificates
* `ca-certificates-dod-wcf` — US DoD Web Content Filtering (WCF) PKI certificates


## Troubleshooting

### Certificate validation errors

If you receive validation errors when adding certificates:

* Verify that your certificate file contains only valid PEM-encoded certificate data
* Check that there is no private key material in the file
* Ensure the certificate has not expired
* Verify that the total size of all certificates added is under 50KB

### Applications not trusting custom certificates

If applications within your container are not trusting your custom certificates:

* Verify the certificate was added successfully by checking `/etc/ssl/certs/ca-certificates.crt`
* Check that the certificate file exists in `/usr/local/share/ca-certificates/`
* Ensure your application is configured to use the system truststore


## Alternative: Using `incert` for certificate injection

For scenarios where you need to add certificates to an existing image without using Custom Assembly, you can use [`incert`](/chainguard/chainguard-images/features/incert-custom-certs/), an open-source tool from Chainguard. However, we recommend using Custom Assembly over `incert` whenever possible, as this approach provides:

* Automatic rebuilds when the base image is updated
* Integration with Chainguard's security patching lifecycle
* Provenance attestation for audit and compliance
* No need to maintain your own build pipeline