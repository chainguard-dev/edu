---
title : "How To Integrate Microsoft Entra ID SSO with Chainguard"
linktitle: "Microsoft Entra ID"
alias:
- /chainguard/administration/custom-idps/azure-ad/
lead: ""
description: "Procedural tutorial on how to register a Microsoft Entra ID Application and integrate it with the Chainguard platform."
type: "article"
date: 2023-04-17T08:48:45+00:00
lastmod: 2024-09-25T15:22:20+01:00
draft: false
tags: ["CHAINGUARD IMAGES", "PROCEDURAL"]
images: []
weight: 020
---

The Chainguard platform supports Single sign-on (SSO) authentication for users. By default, users can log in with GitHub, GitLab and Google, but SSO support allows users to bring their own identity provider for authentication.

This guide outlines how to create a Microsoft Entra ID (formerly Azure Active Directory) application and integrate it with Chainguard. After completing this guide, you'll be able to log in to Chainguard using Entra ID and will no longer be limited to the default SSO options.


## Prerequisites

To complete this guide, you will need the following.

* `chainctl` installed on your system. Follow our guide on [How To Install `chainctl`](/chainguard/administration/how-to-install-chainctl/) if you don't already have this installed.
* An Azure account you can use to set up an Microsoft Entra ID application.


## Create a Microsoft Entra ID Application

To integrate Microsoft Entra ID with the Chainguard platform, log in to [Azure](https://azure.microsoft.com). In the left-hand navigation menu, select **Microsoft Entra ID**.

![Screenshot of Azure's left-hand navigation menu, with the "Microsoft Entra ID" option highglighted in a yellow box.](meid-0.png)

From the Default Directory **Overview** page, click the **➕ Add** button and select **App Registration** from the dropdown menu.

![Screenshot of the Overview in the Azure console. The "Add" dropdown menu has been opened and the "App Registration" option is highlighted in a yellow box.](meid-1.png)

In the **Register an application** screen, configure the application as follows.

* **Name**: Set the username to "Chainguard" (or similar) to ensure users recognize this application is for authentication to the Chainguard platform.
* **Supported account types**: Select the **Single tenant** option so that only your organization can use this application to authenticate to Chainguard.
* **Redirect URI**: Set the platform to **Web** and the redirect URI to `https://issuer.enforce.dev/oauth/callback`.

![Screenshot of the Register an application screen with the following settings selected: the Name is set to "chainguard"; Supported account types is set to the "Accounts in this organizational directory only (default Directory only - Single tenant)" option; and the Redirect URI is set to "Web" with "https://issuer.enforce.dev/oauth/callback" set as the URI.](meid-2.png)

Save your configuration by clicking the **Register** button.

Next, you can optionally set additional branding for the application by selecting **Branding and properties** from the **Manage** dropdown menu.

Here you can set additional metadata for the application, including a Chainguard logo icon here to help your users visually identify this integration. If you'd like, you can use the icon from the [Chainguard Console](https://console.chainguard.dev/logo512.png). The console homepage is [console.chainguard.dev](https://console.chainguard.dev), and our terms of service and private statements can be found at [chainguard.dev/terms-of-service](https://www.chainguard.dev/terms-of-service) and [chainguard.dev/privacy-notice](https://www.chainguard.dev/privacy-notice), respectively.

![Screenshot of the Branding & properties screen with the following settings: Name is set to "Chainguard"; Logo shows the sample Linky logo uploaded; Home page URL is set to "https://console.chainguard.dev"; Terms of service URL is set to "https://www.chainguard.dev/terms-of-service"; and the Privacy statement URL is set to "https://www.chainguard.dev/privacy-notice".](meid-3.png)

Finally, navigate to the **Certificates & secrets** tab in the **Manage** dropdown to create a client secret to authenticate the Chainguard platform to Microsoft Entra ID. Select **New client secret** to add a client secret. In the resulting modal window, add a description and set an expiration date.

![Screenshot showing the Certificates & secrets landing page with the Add a client secret screen opened. The "Certificates & secrets" tab is highlighted in yellow, as is the "New client secret" button.](meid-4.png)

Finally, take note of the client secret “Value” that is created. You'll need this to configure the Chainguard platform to use this Microsoft Entra ID application.

![Screenshot showing the "Client secrets" tab, with the Value highlighted in yellow.](meid-5.png)


## Configuring Chainguard to use Microsoft Entra ID

Now that your Microsoft Entra ID application is ready, you can create the custom identity provider.

First, log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```sh
chainctl auth login
```

Note that this bootstrap account can be used as a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) (that is, a backup account you can use to log in if you ever lose access to your primary account). However, if you prefer to remove this role-binding after configuring the custom IDP, you may also do so.

To configure Chainguard, make a note of the following details from your Microsoft Entra ID application:

* **Application (client) Id**: This can be found on the **Overview** tab of the Chainguard application.
* **Client Secret**: You noted this down when you set up the client secret in the previous step.
* **Directory (tenant) Id**: This can also be found on the **Overview** tab of the Chainguard application.

![Screenshot of a portion of the Overview page showing the "Essentials" information. The Application (client) ID and the Directory (tenant) ID are both highlighted in yellow boxes, though their values have been blurred.](meid-6.png)

You will also need the UIDP for the Chainguard organization under which you want to install the identity provider.  Your selection won’t affect how your users authenticate but will have implications on who has permission to modify the SSO configuration.

You can retrieve a list of all the Chainguard organizations you belong to — along with their UIDPs — with the following command.

```shell
chainctl iam organizations ls -o table
```
```output
                         	ID                         	|  	  NAME    |	DESCRIPTION
--------------------------------------------------------+-------------+---------------------
  59156e77fb23e1e5ebcb1bd9c5edae471dd85c43              | sample_org  |
  . . .                                                 | . . .       |
```

Note down the `ID` value for your chosen organization.

With this information in hand, create a new identity provider with the following commands.

```sh
export NAME=entra-id
export CLIENT_ID=<your application/client id here>
export CLIENT_SECRET=<your client secret here>
export ORG=<your organization UIDP here>
export TENANT_ID=<your directory/tenant id here>
export ISSUER="https://login.microsoftonline.com/${TENANT_ID}/v2.0"
chainctl iam identity-provider create \
  --configuration-type=OIDC \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-issuer=${ISSUER} \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  --parent=${ORG} \
  --default-role=viewer \
  --name=${NAME}
```

Note the `--default-role` option. This defines the default role granted to users registering with this identity provider. This example specifies the `viewer` role, but depending on your needs you might choose `editor` or `owner`. If you don't include this option, you'll be prompted to specify the role interactively. For more information, refer to the [IAM and Security section](/chainguard/administration/custom-idps/custom-idps/#iam-and-security) of our Introduction to Custom Identity Providers in Chainguard tutorial.

You can refer to our [Generic Integration Guide](/chainguard/administration/custom-idps/custom-idps/#generic-integration-guide) in our Introduction to Custom Identity Providers doc for more information about the `chainctl iam identity-provider create` command and its required options.
