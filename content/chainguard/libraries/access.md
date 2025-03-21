---
title: "Chainguard Libraries Access"
linktitle: "Access"
type: "article"
description: "Getting access to Chainguard Libraries"
lead: "tbd"
draft: false
images: []
menu:
  docs:
    parent: "libraries"
weight: 002
toc: true
---

Access to Chainguard Libraries is consistent across all permissions and accounts
across the Chainguard platform. 

If you are already a Chainguard user, the Chainguard account owner in your
organization can grant access to Chainguard Libraries for Java.

If you are not a Chainguard user yet, a new Chainguard account must be created
and configured for the relevant users of Chainguard Libraries.

Once your access is confirmed, [install the Chainguard Control `chainctl`
command line tool](/chainguard/administration/how-to-install-chainctl/) and
login to your account:

```shell
chainctl auth login
```

After authentication in a browser window, a successful login displays a message
and a token:

```shell
Successfully exchanged token.
Valid! Id: 8a4141a........7d9904d98c
```

Retrieve an authentication token for the Chainguard Libraries for Java:

```shell
chainctl auth pull-token --library-ecosystem=java
```

Use the arrow keys to navigate the selection displayed after the question “With
which location is the pull token associated?” and select the organization that
has the entitlement to access Chainguard Libraries for Java. If you know the
name of the organization you can use the optional parameter `--parent=<example>`
in the command invocation or press `/` and filter the list.

`chainctl` returns a username and password suitable for basic authentication in
the response:

```shell
Username: 45a.....424eb0

Password: eyJhbGciO..........WF0IjoxN
```

To use this pull token in another environment supply the following for username
and password valid for basic authentication. Note that the actual returned
values are specific to your account and much longer.

You can verify entitlements with the following command:

```shell
chainctl libraries entitlements list
```

Use the `--parent` option to specify the organization or select the organization
when running the command. The output must include the Java ecosystem in the
table:

```shell
Ecosystem Library Entitlements for chainguard.edu (45a0...764595)

                             ID                             | ECOSYSTEM
------------------------------------------------------------+------------
  45a....................................................e1 | JAVA
```

Contact your Chainguard account owner for confirmation or adjustments if
necessary. 

As administrator you can create entitlements:

```shell
chainctl libraries entitlements create --ecosystems=java,python
```

Use the` --parent` option to specify the organization or select the organization
when running the command. 

With the ID from listing the entitlements detailed in the preceding section, you
can also remove a Chainguard Libraries entitlement:

```shell
chainctl libraries entitlements rm ENTITLEMENT_ID
```
