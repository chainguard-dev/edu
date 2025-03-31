---
title : "Create an Assumable Identity to Authenticate from an EC2 instance"
linktitle: "AWS EC2"
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by an AWS role in EC2 instance."
type: "article"
date: 2025-03-14T08:48:45+00:00
lastmod: 2025-03-14T08:48:45+00:00
draft: false
tags: ["PRODUCT", "PROCEDURAL", "CHAINGUARD IMAGES"]
images: []
weight: 012
---

Chainguard's [*assumable identities*](//chainguard/administration/assumable-ids/assumable-ids/) are identities that can be assumed by external applications or workflows in order to access Chainguard resources or perform certain actions.

This procedural tutorial outlines how to create a Chainguard identity that can then be assumed by an AWS role and used to authorize requests from an Amazon EC2 instance, allowing you to interact with Chainguard resources remotely.


## Prerequisites

To complete this guide, you will need the following.

* An [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance with an IAM Instance role (with or without any AWS permissions). The default `sts:AssumeRole` is sufficient for this guide.
*  This guide assumes you have the AWS CLI installed on your EC2 instance. Review the official documentation for information on [how to install or update to the latest version of the tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
* Finally, you'll need `chainctl` — the Chainguard command line interface tool — installed on **both your EC2 instance and your local machine**. Follow our guide on [How to Install `chainctl`](/chainguard/administration/how-to-install-chainctl/) to set this up.


## Create a Chainguard Assumable Identity

To get started, you will need to retrieve some details about the AWS IAM user on your EC2 instance. You will use these details to create a Chainguard identity that the EC2 user will employ to authenticate to Chainguard.

Run the following command **from your EC2 instance**:

```EC2
aws sts get-caller-identity
```

This will return information like the following:

```Output
{
	"UserId": "AROAWSexampleC2UL7LUB:i-05a6373ad7171fed2",
	"Account": "453EXAMPLE43",
	"Arn": "arn:aws:sts::452example43:assumed-role/AmazonSSMRoleForInstancesQuickSetup/i-05a6373examplehd2"
}
```

**From your local machine**, use this information to create a JSON file named `id.json` which you'll use to define the identity your EC2 instance will use to authenticate to Chainguard:

```shell
cat > id.json <<EOF
{
   "name":"aws-ec2-identity",
   "awsIdentity": {
  	"aws_account" : "$ACCOUNT",
  	"arnPattern"  : "$ARN",
  	"userIdPattern" : "$USER-ID"
   }
}
EOF
```

Note that this identity definition specifies the name of the Chainguard identity as `aws-ec2-identity`. Be sure to change these placeholder values to reflect the output from the `aws sts get-caller-identity` command you ran on your EC2 instance.

Next, use `chainctl` to authenticate to your Chainguard account:

```shell
chainctl auth login
```

After authenticating to Chainguard, you can create an identity that your EC2 instance will be able to assume. First though, you'll need to know the name of the Chainguard organization you want the assumable identity to be associated with.

To retrieve a list of all the organizations you have access to, run the following command:

```shell
chainctl iam organizations ls -o table
```

Find the organization you want to use and copy the value from its `NAME` column exactly. You can then use this to create a new Chainguard identity.

The following example uses the `id.json` file you created earlier as the identity definition and associates it with the `chainguard.edu` organization:

```shell
chainctl iam id create aws --filename id.json -oid --parent chainguard.edu
```

Be sure to change the `chainguard.edu` placeholder to reflect the name of your own Chainguard organization.

This command will return a value like the following:

```
. . .
45a0cEXAMPLE977f050c5fb9ac06a69EXAMPLE95/2c5f7EXAMPLE3871
```

Note this value down, as you will need it in the next section when you authenticate to Chainguard from your EC2 instance using this identity.

Before moving on, you must create a [role-binding](/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) to bind the identity stored in `$CHAINGUARD_IDENTITY` to a specific role:

```shell
chainctl iam rolebinding create --identity aws-ec2-identity --role viewer --parent chainguard.edu
```

This example binds the `aws-ec2-identity` to the `viewer` role, but you can bind it to any role you'd like. For a full list of available roles, you can run the `chainctl iam roles list` command.

Again, be sure to change `chainguard.edu` to reflect the name of your own organization, and change `aws-ec2-identity` to the name of the identity you created previously, if different.

Following that, you can move on to the next section where you will authenticate to Chainguard from your EC2 instance using the identity you created.


## Authenticate from EC2 using the newly created identity

Now that you've created a Chainguard identity, you can use it to connect to Chainguard from your EC2 instance. This section outlines how to set this up. 

> **Note**: All the commands in this section should be run from your EC2 instance.

From your EC2 instance, create an environment variable named `$CHAINGUARD_IDENTITY` that contains the `ID` value for the `aws-ec2-identity` Chainguard identity you created in the previous section:

```EC2
export CHAINGUARD_IDENTITY=45a0cEXAMPLE977f050c5fb9ac06a69EXAMPLE95/2c5f7EXAMPLE3871
```

If you forgot to note down the identity's `ID` value, you can retrieve a list of all your available Chainguard identities (along with their `ID` values) by running the `chainctl iam identities list -o table` command on your local machine.

Next you'll need to get the EC2 instance's credentials from the Instance Metadata Service.

To do this, first create a session token with the following command:

```EC2
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
```

This creates a session token that will last for six hours (`21600` seconds) and stores the token header in a variable named `$TOKEN`. 

Next, you'll need to find the role associated with the instance. The following command retrieves this role while storing it in a variable named `$ROLE`:

```EC2
ROLE=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/)
```

Following that, you can run a nearly identical command to retrieve the necessary security credentials, this time without storing the results in an environment variable and specifying the IAM role you just retrieved:

```EC2
curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/$ROLE
```

This will return output like the following:

```Output
{
  "Code": "Success",
  "LastUpdated": "2025-03-13T23:05:07Z",
  "Type": "AWS-HMAC",
  "AccessKeyId": "ASEXAMPLE3EFACCESS3KEYS",
  "SecretAccessKey": "gFQYvEXAMPLEqlISECRETdgACCESSdzlZlKEY56h",
  "Token": "IQoJb3JpZ2luXEXAMPLE2Vj. . .",
  "Expiration": "2025-03-14T05:29:15Z"
}
```

Based on this output, create three environment variables:

* `$AWS_ACCESS_KEY_ID`, which will hold the `AccessKeyId` value
* `$AWS_SECRET_ACCESS_KEY`, which will hold the `SecretAccessKey` value
* `$AWS_SESSION_TOKEN`, to hold the `Token` value

```EC2
export AWS_ACCESS_KEY_ID="ASEXAMPLE3EFACCESS3KEYS"
export AWS_SECRET_ACCESS_KEY="gFQYvEXAMPLEqlISECRETdgACCESSdzlZlKEY56h"
export AWS_SESSION_TOKEN="IQoJb3JpZ2luXEXAMPLE2Vj. . ."
```

> **Note**: You can retrieve the security credentials and store them the appropriate variables with the following one-line command, which will reduce the amount of copying and pasting you need to do:

```EC2
curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/$ROLE | jq -j '"export AWS_ACCESS_KEY_ID=", .AccessKeyId, "\nexport AWS_SECRET_ACCESS_KEY=", .SecretAccessKey,"\nexport AWS_SESSION_TOKEN=" , .Token' > vars && source ./vars
```

Using these variables, as well as the Chainguard identity you set up previously, you can send a request to the AWS Security Token Service to retrieve a short-lived token which will be used to authenticate with `chainctl`. This command stores the token in a variable named `$TOK`:

```EC2
TOK=$(curl -X POST "https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15" \
--aws-sigv4 "aws:amz:us-east-1:sts" \
-H "x-amz-security-token: $AWS_SESSION_TOKEN" \
--user "$AWS_ACCESS_KEY_ID":"$AWS_SECRET_ACCESS_KEY" \
-H "Chainguard-Identity: $CHAINGUARD_IDENTITY" \
-H "Chainguard-Audience: https://issuer.enforce.dev" \
-H "Accept: application/json" \
-v  2>&1 > /dev/null | grep '^> ' | sed 's/> //' | base64 -w0)
```

Finally, use this token — along with the `$CHAINGUARD_IDENTITY` variable — to authenticate to Chainguard from your EC2 instance:

```EC2
chainctl auth login  --identity-token $TOK --identity $CHAINGUARD_IDENTITY
```
```
Successfully exchanged token.
Valid! Id: 45a0cEXAMPLE977f050c5fb9ac06a69EXAMPLE95/2c5f7EXAMPLE3871
```

With that, your EC2 instance will have access to your Chainguard resources. Remember that the level of access is determined by the role you bound to the identity in the previous section; if you followed this example closely, then this identity will be bound to the `viewer` role.

## Learn more

By following this guide, you will have created a Chainguard identity that you can use to authenticate to Chainguard from an Amazon EC2 instance. For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, we encourage you to read through the rest of our documentation on [Administering Chainguard resources](/chainguard/administration/).
