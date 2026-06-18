---
title : "How To Integrate Okta SSO with Chainguard"
linktitle: "Okta"
aliases:
- /chainguard/chainguard-enforce/authentication/example-idps/okta/
- /chainguard/administration/custom-idps/okta/
- /chainguard/administration/custom-idps/idp-providers/okta/
lead: ""
description: "Procedural tutorial on how to create an Okta App Integration"
type: "article"
date: 2023-04-17T08:48:45+00:00
lastmod: 2026-06-16T15:22:20+01:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 010
---

The Chainguard platform supports single sign-on (SSO) authentication for users. By default, users can log in with GitHub, GitLab, and Google, but SSO support lets users bring their own identity provider for authentication.

This guide outlines how to create an Okta application and integrate it with Chainguard. After completing this guide, you'll be able to log in to Chainguard using Okta and you'll no longer be limited to the default SSO options.


## Prerequisites

To complete this guide, you need the following.

* `chainctl` installed on your system. Follow our guide on [How To Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't already have this installed.
* An Okta account over which you have administrative access.


## Create an Okta App integration

To integrate your Okta identity provider with the Chainguard platform, [log in to Okta](https://www.okta.com/login/) and navigate to the **Applications** landing page in the Admin console. There, click **Create App Integration**.

Select **OIDC - OpenID Connect** as the sign-in method and **Web Application** as the application type.

Next, in the **General Settings** window, configure the application as follows:

* **App integration name**: Enter a descriptive name (like "Chainguard") here.
* **Grant type**: Ensure that the grant type is set to **Authorization Code** only.

> **Warning**: Don't select other grant types, because doing so may compromise your security.

* **Sign-in redirect URIs**: Set the redirect URI to `https://issuer.enforce.dev/oauth/callback`.
* **Sign-out redirect URIs**: This field has a URI set to `http://localhost:8080` by default. Click the **X** icon to remove the sign-out redirect entirely, leaving the field blank.
* **Assignments**: You must select one of the options in this section:
    * **Allow everyone in your organization to access**: This option grants access to any [users](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-people.htm) you've added to your Okta organization.
    * **Limit access to selected groups**: If you select this option, you can select one or more Okta groups to have access to the identity provider.
    * **Skip group assignment for now**: You can select this option and configure group assignment later. However, note that users **will not** be able to log in unless they have been granted access to the application.

> **Note**: For more information on Okta users and groups, refer to [the official documentation](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-main.htm).

Click **Save**. Then, navigate to the **Sign On** tab.

There, find the **OpenID Connect ID Token** section and click **Edit**. Set the **Issuer** option to **Okta URL**, then click **Save**.

With that, you've configured the Okta application. Next, you need to configure the Chainguard platform to use it by creating a custom identity provider.


## Configuring Chainguard to use Okta SSO

Now that your Okta application is ready, you can create the custom identity provider.

First, log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```shell
chainctl auth login
```

Note that you can use this bootstrap account as a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) — that is, an account you can use to log in if you ever lose access to your primary account. However, if you prefer to remove this role-binding after configuring the custom IDP, you can do so.

To configure the platform, make a note of the following settings from your Okta Application:

* **Client ID**: You can find this on the **General** tab under **Client Credentials**
* **Client Secret**: Find this on the **General** tab under **Client Credentials**
* **Issuer URL**: You can find this under the **Sign On** tab in the **OpenID Connect ID Token** section

With this information in hand, create a new identity provider with the following commands.

```shell
export NAME=okta
export CLIENT_ID=<your client id here>
export CLIENT_SECRET=<your client secret here>
export ISSUER=<your issuer url here>
chainctl iam identity-provider create \
  --configuration-type=OIDC \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-issuer=${ISSUER} \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  --default-role=viewer \
  --name=${NAME}
```

Note the `--default-role` option. This defines the default role granted to users registering with this identity provider. This example specifies the `viewer` role, but depending on your needs you might choose `editor` or `owner`. If you don't include this option, you'll be prompted to specify the role interactively. For more information, refer to the [IAM and Security section](/chainguard/administration/custom-idps/custom-idps/#iam-and-security) of our Introduction to Custom Identity Providers in Chainguard tutorial.

You can refer to our [Generic Integration Guide](/chainguard/administration/custom-idps/custom-idps/#generic-integration-guide) in our Introduction to Custom Identity Providers article for more information about the `chainctl iam identity-provider create` command and its required options.

## Logging in to Chainguard with the Okta identity provider

To log in to the Chainguard Console with the new identity provider you just created, navigate to [console.chainguard.dev/auth/login](https://console.chainguard.dev/auth/login), enter your Chainguard organization's name into the **Email or organization** box, and click **Continue**. This opens a new window with the Okta login flow, where you can complete the login process.

You can also use the custom identity provider to log in through `chainctl`. To do this, run the `chainctl auth login` command and add the `--identity-provider` option followed by the identity provider's ID value:

```shell
chainctl auth login --identity-provider <IDP-ID>
```

The ID value appears in the `ID` column of the table returned by the `chainctl iam identity-provider create` command you ran previously. You can also retrieve this table at any time by running `chainctl iam identity-provider ls -o table` when logged in.
