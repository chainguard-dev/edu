---
title: "Chainguard Libraries Access"
linktitle: "Access"
type: "article"
description: "Getting access to Chainguard Libraries"
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
weight: 002
toc: true
---

Access to Chainguard Libraries is consistent across all permissions and accounts
across the Chainguard platform.

If you are not a Chainguard user yet, a new Chainguard account must be created
and configured for access to Chainguard Libraries.

If you are already a Chainguard user, the Chainguard account owner in your
organization can grant access to Chainguard Libraries.

In both cases, confirm the name of the organization so you can use it with the
`--parent` parameter to specify the organization.

Once your user account is created and access is confirmed, [install the
Chainguard Control `chainctl` command line
tool](/chainguard/administration/how-to-install-chainctl/) and login to your
account:

```shell
chainctl auth login
```

After authentication in a browser window, a successful login displays a message
and a token:

```shell
Successfully exchanged token.
Valid! Id: 8a4141a........7d9904d98c
```

Retrieve a new authentication token for the Chainguard Libraries for Java:

```shell
chainctl auth pull-token --library-ecosystem=java --parent=example --ttl=8670h
```

* `--library-ecosystem=java`: retrieve the token for use with Chainguard
  Libraries for Java
* `--parent=example`: specify the parent organization for your account as
  provided when requesting access to Chainguard Libraries for Java and the
  replace `example`.
* `--ttl=8670d`: set the duration for the validity of the token, defaults to
  `720h` (equivalent to 30 days), maximum valid value is `8760d` (equivalent to
  365 days), valid unit strings range from nanoseconds to hours and are `ns`,
  `us`, `ms`, `s`, `m`, and `h`.

When omitting the parent parameter, potentially a list of organizations is
displayed. Use the arrow keys to navigate the selection displayed after the
question “With which location is the pull token associated?” and select the
organization that has the entitlement to access Chainguard Libraries for Java.
Press `/` to filter the list.

`chainctl` returns a username and password suitable for basic authentication in
the response:

```shell
Username: 45a.....424eb0

Password: eyJhbGciO..........WF0IjoxN
```

The returned username and password combination is a new credential set in the
organization that is independent of the account used to create and retrieve the
credential set. It is therefore suitable for use in any service application,
such as [a repository manager](/chainguard/libraries/java/global-configuration)
or [a build tool](/chainguard/libraries/java/build-configuration) that is not
tied to a specific user.

To use this pull token in another environment, supply the following for username
and password valid for basic authentication. Note that the actual returned
values are much longer.

Use the credentials for manual testing in a browser or with a script if you know
the URL for a specific library artifact, [for example a Java
library](/chainguard/libraries/java/overview/#technical-details).

You can verify entitlements for your organization `example` with the following
command:

```shell
chainctl libraries entitlements list --parent=example
```

The output must include the Java ecosystem in the table:

```shell
Ecosystem Library Entitlements for chainguard.edu (45a0...764595)

                             ID                             | ECOSYSTEM
------------------------------------------------------------+------------
  45a....................................................e1 | JAVA
```

Contact your Chainguard account owner for confirmation or adjustments if
necessary. 

<!-- Removed for now until we decide where this info should live. It is only accessible
for administrators (so Chainguard internal), but they might also be an audience to 
read the docs - so TBD

As administrator you can create entitlements:

```shell
chainctl libraries entitlements create --ecosystems=java,python --parent=example
```

Use the` --parent` option to specify the organization or select the organization
when running the command.

With the ID from listing the entitlements detailed in the preceding section, you
can also remove a Chainguard Libraries entitlement:

```shell
chainctl libraries entitlements rm ENTITLEMENT_ID
```
-->
