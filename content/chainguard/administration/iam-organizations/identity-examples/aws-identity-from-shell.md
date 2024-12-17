---
title : "Authenticate from an EC2 instance"
linktitle: "AWS Assumable Identity from EC2 instance"
aliases:
- /chainguard/chainguard-enforce/authentication/identity-examples/enforce-aws-identity/
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by an AWS role in EC2 instance."
type: "article"
date: 2023-11-28T08:48:45+00:00
lastmod: 2024-05-09T08:48:45+00:00
draft: false
tags: ["Chainguard Images", "Product", "Procedural", "AWS", "Assumable Identity", "IAM", "EC2"]
images: []
weight: 012
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create a Chainguard identity and then create an AWS role that will assume the identity to interact with Chainguard resources. This can be used to authorize requests from EC2 [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).


## Prerequisites

To complete this guide, you will need the following.

* `chainctl` — the Chainguard command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/administration/how-to-install-chainctl/) to set this up.
* An EC2 instance with an IAM Instance role (with or without any AWS permissions). The default "sts:AssumeRole" is enough. Below is an example from EC2 instance with iam role `access_to_chainguard_org`.
```
[ec2-user@ip-10-0-0-14 ~]$ aws sts get-caller-identity
{
"UserId": "AROAWSUKZ3EFSAMPLE:i-00c1356891csample",
"Account": "45233640****",
"Arn": "arn:aws:sts::45233640****:assumed-role/access_to_chainguard_org/i-00c1356891csample"
}
[ec2-user@ip-10-0-0-14 ~]$
```


## Create Chainguard Assumable Identity named=aws for your Organisation/Repository/Parent and assign a viewer role.
* Login to your local workstation/laptop.
* Using details from EC2 instance command `aws sts get-caller-identity`, create an id.json file on your local workstation.
```
]$ cat id.json
{
   "name":"aws-instance",
   "awsIdentity": {
      "aws_account" : "45233640****",
      "arnPattern"  : "^arn:aws:sts::45233640****:assumed-role/access_to_chainguard_org/(.*)$",
      "userIdPattern" : "^AROAWSUKZ3EFSAMPLE(.*)$"
   }
}
```
* Authenticate to Chainguard, identify your organisation/repository/parent, create an identity=aws, and assign it role=viewer
```
]$ chainctl auth login
]$ export PARENT=$(chainctl iam org ls -o json | jq -r '.items[0].id')
]$ export CHAINGUARD_IDENTITY=$(chainctl iam id create aws --filename id.json -oid --parent $PARENT)
]$ export ROLE=$(chainctl iam roles list --name viewer -oid)
]$ chainctl iam rolebinding create --identity $CHAINGUARD_IDENTITY --role $ROLE --parent $PARENT
]$ echo $CHAINGUARD_IDENTITY

Sample Output
---------------
]$ chainctl iam id create aws --filename id.json -oid --parent manojgupta.in
Opening browser to https://issuer.enforce.dev/oauth?audience=https%3A%2F%2Fconsole-api.enforce.dev&client_id=auth0&connection=google-oauth2&create_refresh_token=true&exit=redirect&redirect=http%3A%2F%2Flocalhost%3A62467%2Fcallback%3Ftoken%3Dtrue&skip_registration=true
Creating new identity aws-instance (aws) in location manojgupta.in.
Do you want to continue? [Y,n]: Y
f1d5337370e7d8e99282c25286804a5b2cfc1682/fc5787bc18e93bea
]$
```
* You should be able to see the newly created identity using `chainctl iam identities list`


## Authenticate from EC2 using the newly created identity
* Note down the ID for the identity and login to EC2 instance.
* On EC2 instance, export the ID for the newly created identity `export CHAINGUARD_IDENTITY=66fe8510254166621680aeb4sample222222/3359173sampled`
```
export CHAINGUARD_IDENTITY=66fe8510254166621680aeb4sample222222/3359173sampled
```

* First get your instance credentials from IMDS into variables.
```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
ROLE=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/)
curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/$ROLE | jq -j '"export AWS_ACCESS_KEY_ID=", .AccessKeyId, "\nexport AWS_SECRET_ACCESS_KEY=", .SecretAccessKey,"\nexport AWS_SESSION_TOKEN=" , .Token' > vars
. ./vars
env | grep AWS
AWS_SECRET_ACCESS_KEY=BOD--FAKE--Ra+
AWS_ACCESS_KEY_ID=ASIAW--FAKE--3CG
AWS_SESSION_TOKEN=IQoJb--FAKE--r0kmSys=
```
* When you’ve got some variables you can construct a request to STS:
```
curl -X POST "https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15" --aws-sigv4 "aws:amz:us-east-1:sts" -H "x-amz-security-token: $AWS_SESSION_TOKEN" --user "$AWS_ACCESS_KEY_ID":"$AWS_SECRET_ACCESS_KEY"  -v
```
* You need some output like:
```
POST https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15 HTTP/1.1
Host: sts.amazonaws.com
Accept: application/json
Chainguard-Audience: https://issuer.enforce.dev
Chainguard-Identity: 66fe8510254166621680aeb498b0249b66900d34/335917336625376d
X-Amz-Date: 20241128T170155Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjE--FAKE--bswakbVj8=
Authorization: AWS4-HMAC-SHA256 Credential=ASIAWSUKZ3EF63FWRJ4J/20241128/us-east-1/sts/aws4_request, SignedHeaders=accept;chainguard-audience;chainguard-identity;host;x-amz-date;x-amz-security-token, Signature=ff116727527fe--FAKE--044b986777060d66e
```
* If you compare the output from curl with that, you’ll see you’re pretty close!
```
> POST /?Action=GetCallerIdentity&Version=2011-06-15 HTTP/1.1
> Host: sts.amazonaws.com
> Authorization: AWS4-HMAC-SHA256 Credential=ASIAWSUKZ3EFX7LLD3CG/20241128/us-east-1/sts/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=8552ca--FAKE--829c111a
> X-Amz-Date: 20241128T172358Z
> User-Agent: curl/8.5.0
> Accept: */*
> x-amz-security-token: IQoJb3JpZ2luX2--FAKE--r0kmSys=
>
```
* SignedHeaders is different. So you need to add those headers to the curl request for starters.
* Now the curl is like:
```
curl -X POST "https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15" \
--aws-sigv4 "aws:amz:us-east-1:sts" -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
--user "$AWS_ACCESS_KEY_ID":"$AWS_SECRET_ACCESS_KEY" \
-H "Chainguard-Identity: $CHAINGUARD_IDENTITY" \
-H "Chainguard-Audience: https://issuer.enforce.dev"\
-H"Accept: application/json" \
2>&1 > /dev/null | grep '^> '
```
* NOTE: We don’t actually have to send the request, we just need to build it.
* That curl command gives output like the base64 decoded token looks. So just need to send it to base64.
```
]$ TOK=$(curl -X POST "https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15" --aws-sigv4 "aws:amz:us-east-1:sts" -H "x-amz-security-token: $AWS_SESSION_TOKEN" --user "$AWS_ACCESS_KEY_ID":"$AWS_SECRET_ACCESS_KEY" -H"Chainguard-Identity: $CHAINGUARD_IDENTITY" -H "Chainguard-Audience: https://issuer.enforce.dev" -H"Accept: application/json" -v  2>&1 > /dev/null | grep '^> ' | sed 's/> //' | base64 -w0)
]$ echo $TOK # output will be like UE9TVCAvP0FjdGlvbj1--FAKE--Qo=
```
* Check your value doesn’t have spaces or line feeds in.
* Finally, use this token to login to Chainguard:
```
]$ chainctl auth login  --identity-token $TOK --identity "$CHAINGUARD_IDENTITY"
Using "headless" auth mode as set in configuration. To disable: chainctl config unset auth.mode
Successfully exchanged token.
Valid! Id: 66fe8510254166621680aeb498b0249b66900d34/335917336625376d
```


## Learn more

For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment.
