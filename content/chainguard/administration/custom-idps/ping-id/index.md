---
title : "How To Integrate Ping Identity SSO with Chainguard"
linktitle: "Ping Identity"
lead: ""
description: "Procedural tutorial on how to create a Ping Identity Application"
type: "article"
date: 2023-04-17T08:48:45+00:00
lastmod: 2024-03-21T15:22:20+01:00
draft: false
tags: ["Chainguard Images", "Procedural"]
images: []
weight: 015
---

The Chainguard platform supports Single sign-on (SSO) authentication for users. By default, users can log in with GitHub, GitLab and Google, but SSO support allows users to bring their own identity provider for authentication.

This guide outlines how to create a Ping Identity Application and integrate it with Chainguard. After completing this guide, you'll be able to log in to Chainguard using Ping and will no longer be limited to the default SSO options.


## Prerequisites

To complete this guide, you will need the following.

* `chainctl` installed on your system. Follow our guide on [How To Install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) if you don't already have this installed.
* A Ping Identity account over which you have administrative access.
* A Custom IDP quota of at least 1. You can reach out to [Chainguard's support team](https://support.chainguard.dev/) for help with this.


## Create a Ping Identity Application

To integrate the Ping identity provider with the Chainguard platform, [sign on to Ping Identity](https://www.pingidentity.com/en.html) and navigate to the Dashboard. Click on the **Connections** tab in the left hand sidebar menu, and then click on **Applications** in the resulting dropdown menu. From the Applications landing page, click the plus sign (**➕**) to set up a new application.

![Screenshot of the Ping Identity Dashboard, showing the applications landing page. The Applications tab in the left hand sidebar and the "add application" plus sign icon are circled in magenta.](ping-1.png)

Configure the application as follows:

* **Application Name**: Set a name and option description (such as "Chainguard") to ensure users recognize this application is for authentication to the Chainguard platform.
* **Icon**: You can optionally add a Chainguard logo icon here to help your users visually identify this integration. If you'd like, you can use the icon from the [Chainguard Console](https://console.enforce.dev/logo512.png).
* **Application Type**: Select **OIDC Web App**.

![Screenshot showing the Add Application modal window with the following settings in place: Application Name is set to "Chainguard"; Description reads "Build it right, Build it safe, Build it fast, https://console.enforce.dev"; the example Inky icon has been uploaded to the Icon field; and the Application Type is set to "OIDC Web App."](ping-2-add-app.png)

After setting these details, click the **Save** button.

Next, configure scopes for the application. In the **Overview** tab, click the **Resource Access** scope button.

![Screenshot of the Overview tab, with the Resource Access scope button highlighted in a magenta circle.](ping-3.png)

Add **email** and **profile** scopes, then save.

![Screenshot of the Edit Resources modal window, showing the email and profile scopes selected.](ping-4.png)

Next, configure the OIDC application. Navigate to the **Configuration** tab and click the "edit" icon.

To configure the application, add the following settings.

* **Response Type**: Select the **Code** checkbox.
* **Grant Type**: Select the **Authorization Code** checkbox, and set PKCE Enforcement to "Optional."

> Warning: Setting a grant type other than **Authorization Code** may compromise your security posture.

* **Redirect URIs**: Set the Redirect URI to [`https://issuer.enforce.dev/oauth/callback`](https://issuer.enforce.dev/oauth/callback).

![Screenshot of the Edit Configuration modal window with the following settings: Resource type is set to "Code"; Grant type is set to "Authorization Code" (with PKCE enforcement set to "Optional"); Redirect URIs has one option set (https://issuer.enforce.dev/oauth/callback).](ping-7-edit-conf.png)

Click the **Save** button to save your configuration.

Finally, enable the Chainguard application by toggling the knob in the top right corner.

![Screenshot of the Overview tab, with the toggle button turned on. Additionally, the toggle button is highlighted with a magenta circle.](ping-8-2.png)

This completes configuration of the Ping application. You're now ready to configure the Chainguard platform to use it.


## Configuring Chainguard to use Ping SSO

Now that your Okta application is ready, you can create the custom identity provider.

First, log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```sh
chainctl auth login
```

Note that this bootstrap account can be used as a [backup account](/chainguard/chainguard-enforce/authentication/custom-idps/#backup-accounts) (that is, a backup account you can use to log in if you ever lose access to your primary account). However, if you prefer to remove this rolebinding after configuring the custom IDP, you may also do so.

To configure Chainguard make a note of the following settings from your Ping application. These can be found in the Ping console under the **Configuration** tab of the **Application** page.

* Client ID
* Client Secret
* Issuer URL

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
export NAME=ping-id
export CLIENT_ID=<your client id here>
export CLIENT_SECRET=<your client secret here>
export ISSUER=<your issuer url here>
export ORG=<your organization UIDP here>
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

Note the `--default-role` option. This defines the default role granted to users registering with this identity provider. This example specifies the `viewer` role, but depending on your needs you might choose `editor` or `owner`. If you don't include this option, you'll be prompted to specify the role interactively. For more information, refer to the [IAM and Security section](/chainguard/chainguard-enforce/authentication/custom-idps/#iam-and-security) of our Introduction to Custom Identity Providers in Chainguard tutorial.


You can refer to our [Generic Integration Guide](/chainguard/administration/custom-idps/custom-idps/#generic-integration-guide) in our Introduction to Custom Identity Providers guide for more information about the `chainctl iam identity-provider create` command and its required options.
