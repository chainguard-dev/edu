---
title : "How To Integrate Azure Active Directory SSO with Chainguard"
linktitle: "Azure Active Directory"
lead: ""
description: "Procedural tutorial on how to register an Azure Active Directory Application"
type: "article"
date: 2023-04-17T08:48:45+00:00
lastmod: 2023-12-08T15:22:20+01:00
draft: false
tags: ["Chainguard Images", "Procedural"]
images: []
weight: 020
---

The Chainguard platform supports Single sign-on (SSO) authentication for users. By default, users can log in with GitHub, GitLab and Google, but SSO support allows users to bring their own identity provider for authentication.

This guide outlines how to create an Azure Active Directory (AD) Application and integrate it with Chainguard. After completing this guide, you'll be able to log in to Chainguard using Azure AD and will no longer be limited to the default SSO options.


## Prerequisites

To complete this guide, you will need the following.

* `chainctl` installed on your system. Follow our guide on [How To Install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) if you don't already have this installed.
* An Azure account you can use to set up an Active Directory Application.


## Create an Azure Active Directory Application

To integrate the Azure AD identity provider with the Chainguard platform, log in to [Azure](https://azure.microsoft.com) and navigate to the Azure Active Directory console in the Azure portal.

![Screenshot of the Azure portal's sidebar menu, with Azure Active Directory highlighted in a red circle.](aad-1.png)

There, select the **App registrations** tab and click **New registration**.

![Screenshot of the App registrations landing page  in the Azure Active Directory console. The App registrations tab in the left sidebar menu is highlighted in a red circle, as is the "New registration" option.](aad-2.png)

In the **Register an application** screen, configure the application as follows.

* **Name**: Set the username to "Chainguard" (or similar) to ensure users recognize this application is for authentication to the Chainguard platform.
* **Supported account types**: Select the **Single tenant** option so that only your organization can use this application to authenticate to Chainguard.
* **Redirect URI**: Set the platform to **Web** and the redirect URI to `https://issuer.enforce.dev/oauth/callback`.

![Screenshot of the Register an application screen with the following settings selected: the Name is set to "chainguard"; Supported account types is set to the "Accounts in this organizational directory only (default Directory only - Single tenant)" option; and the Redirect URI is set to "Web" with "https://issuer.enforce.dev/oauth/callback" set as the URI.](aad-3-new-reg-less-wide.png)

Save your configuration by clicking the **Register** button.

Next, you can optionally set additional branding for the application by selecting the **Branding and properties** tab.

There, you can set additional metadata for the application, including a Chainguard logo icon here to help your users visually identify this integration. If you'd like, you can use the icon from the [Chainguard Console](https://console.enforce.dev/logo512.png). The console homepage is [console.enforce.dev](https://console.enforce.dev), and our terms of service and private statements can be found at [chainguard.dev/terms-of-service](https://www.chainguard.dev/terms-of-service) and [chainguard.dev/privacy-notice](https://www.chainguard.dev/privacy-notice), respectively.

![Screenshot of the Branding & properties screen with the following settings: Name is set to "Chainguard"; Logo shows the sample Inky logo uploaded; Home page URL is set to "https://console.enforce.dev"; Terms of service URL is set to "https://www.chainguard.dev/terms-of-service"; and the Privacy statement URL is set to "https://www.chainguard.dev/privacy-notice".](aad-branding.png)

Finally, navigate to the **Certificates & secrets** tab to create a client secret to authenticate the Chainguard platform to Azure Active Directory. Select **New client secret** to add a client secret. In the resulting modal window, add a description and set an expiration date.


![Screenshot showing the Certificates & secrets landing page with the Add a client secret screen opened. The Certificates & secrets tab is highlighted in a red circle, as is the New client secret button.](aad-6.png)

Finally, take note of the client secret “Value” that is created. You'll need this to configure the Chainguard platform to use this Azure Active Directory application.

![Screenshot showing the client secrets tab, with the Value highlighted in a red circle.](aad-7.png)


## Configuring Chainguard to use Azure Active Directory

Now that your Azure Active Directory application is ready, you can create the custom identity provider.

First, log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```sh
chainctl auth login
```

Note that this bootstrap account can be used as a [backup account](/chainguard/chainguard-enforce/authentication/custom-idps/#backup-accounts) (that is, a backup account you can use to log in if you ever lose access to your primary account). However, if you prefer to remove this rolebinding after configuring the custom IDP, you may also do so.

To configure Chainguard, make a note of the following details from your Azure Active Directory application:

* **Application (client) Id**: This can be found on the **Overview** tab of the Chainguard AD application.
* **Client Secret**: You noted this down when you set up the  clientsecret in the previous step.
* **Directory (tenant) Id**: This can also be found on the **Overview** tab of the Chainguard AD application.

![Screenshot of the Azure AD Overview tab showing the Essentials information. Th
He Application (client) ID and the Directory (tenant) ID are both highlighted in red circles.](aad-8.png)

You will also need the UIDP for the Chainguard group under which you want to install the identity provider.  Your selection won’t affect how your users authenticate but will have implications on who has permission to modify the SSO configuration.

You can retrieve a list of all your Chainguard groups — along with their UIDPs — with the following command.

```shell
chainctl iam groups ls -o table
```
```output
                             ID                             |      NAME       |    DESCRIPTION
------------------------------------------------------------+-----------------+---------------------
  59156e77fb23e1e5ebcb1bd9c5edae471dd85c43                  | sample_group    |
  . . .                                                     | . . .           |
```

Note down the `ID` value for your chosen group.

With this information in hand, create a new identity provider with the following commands.

```sh
export NAME=azure-ad
export CLIENT_ID=<your application/client id here>
export CLIENT_SECRET=<your client secret here>
export TENANT_ID=<your directory/tenant id here>
export ISSUER="https://login.microsoftonline.com/${TENANT_ID}/v2.0"
chainctl iam identity-provider create \
  --configuration-type=OIDC \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-issuer=${ISSUER} \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  --group=${GROUP} \
  --default-role=viewer \
  --name=${NAME}
```

Note the `--default-role` option. This defines the default role granted to users registering with this identity provider. This example specifies the `viewer` role, but depending on your needs you might choose `editor` or `owner`. If you don't include this option, you'll be prompted to specify the role interactively. For more information, refer to the [IAM and Security section](/chainguard/chainguard-enforce/authentication/custom-idps/#iam-and-security) of our Introduction to Custom Identity Providers in Chainguard tutorial.


You can refer to our [Generic Integration Guide](/chainguard/administration/custom-idps/custom-idps/#generic-integration-guide) in our Introduction to Custom Identity Providers doc for more information about the `chainctl iam identity-provider create` command and its required options.
