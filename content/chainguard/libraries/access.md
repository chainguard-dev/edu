---
title: "Chainguard Libraries Access"
linktitle: "Access"
description: "Getting access to Chainguard Libraries"
type: "article"
date: 2025-03-25T00:08:04+00:00
lastmod: 2025-04-07T15:17:00+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
weight: 002
toc: true
---

Access to Chainguard Libraries is consistent across all permissions and accounts
of the Chainguard platform.

If you are not a Chainguard user yet, a new Chainguard account must be created
and configured for access to Chainguard Libraries.

If you are already a Chainguard user, the Chainguard account owner in your
organization can grant access to Chainguard Libraries.

In both cases, confirm the name of the organization so you can use it with the
`--parent` parameter to specify the organization.

## Initial authentication

Once your user account is created and access is confirmed, [install the
Chainguard Control `chainctl` command line
tool](/chainguard/chainctl-usage/how-to-install-chainctl/) and login to your
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

## Pull token for libraries

Retrieve a new authentication token for the Chainguard Libraries for Java with
the [chainctl auth pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/)
command:

```shell
chainctl auth pull-token --library-ecosystem=java --parent=example --ttl=8670h
```

* `--library-ecosystem=java`: retrieve the token for use with Chainguard
  Libraries for Java. Use `python` for a token to use Chainguard Libraries for
  Python.
* `--parent=example`: specify the parent organization for your account as
  provided when requesting access to Chainguard Libraries and replace `example`.
* `--ttl=8670d`: set the duration for the validity of the token, defaults to
  `720h` (equivalent to 30 days), maximum valid value is `8760h` (equivalent to
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

### Verification

Use the credentials for manual testing in a browser or with a script and curl if
you know the URL for a specific library artifact. Refer to the following
sections for more details:

* [Technical details and manual testing for Java libraries](/chainguard/libraries/java/overview/#technical-details)
* [Technical details and manual testing for Python libraries](/chainguard/libraries/python/overview/#technical-details)
* [Use environment variables](#env)
* [.netrc for authentication](#netrc)

<a name="env"></a>

## Use environment variables

Using environment variables for username and password is more secure than
hardcoding the values in configuration files. In addition, you can use the same
configuration and files for all users to simplify setup and reduce errors.

Use the `env` environment output option to create a snippet for a new token
suitable for integration in a script.

```shell
$ chainctl auth pull-token --output env --library-ecosystem=java --parent=example
export CHAINGUARD_JAVA_IDENTITY_ID=45a.....424eb0
export CHAINGUARD_JAVA_TOKEN=eeyJhbGciO..........WF0IjoxN
```

Combine the call with `eval` to populate the environment variables directly by
calling `chainctl`:

```shell
eval $(chainctl auth pull-token --output env --library-ecosystem=java --parent=example)
```

Equivalent commands for Python are supported and result in values for the
`CHAINGUARD_PYTHON_IDENTITY_ID` and `CHAINGUARD_PYTHON_TOKEN` variables.

Running this command as part of a login script or some other automation allows
your organization to replace actual username and password values in your build
tool configuration with environment variable placeholders:

*  [Java build tool configuration](/chainguard/libraries/java/build-configuration)
*  [Python build tool configuration](/chainguard/libraries/python/build-configuration)

<a id="netrc"></a>

## .netrc for authentication

[curl](https://curl.se/) and a number of other tools support configuration of
username and password authentication details for a specific domain in the
[`.netrc`
file](https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html),
typically located in the user's home directory.

Use this approach for authentication to a repository manager in your
organization or to Chainguard Libraries directly, for example with [pip and
others for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration#pip), with [bazel for
Chainguard Libraries for
Java](/chainguard/libraries/java/build-configuration#bazel) or for manual
testing with curl.

The following example shows a suitable setup for a repo manager available at
`repo.example.com`:

```
machine repo.example.com
login YOUR_USERNAME_FOR_REPOSITORY_MANAGER
password YOUR_PASSWORD
```

For a direct connection to Chainguard Libraries, for example for testing with
curl, use the following example with the username
`CHAINGUARD_PYTHON_IDENTITY_ID` and password `CHAINGUARD_PYTHON_TOKEN` value for
the pull token for the desired language ecosystem:

```
machine libraries.cgr.dev
login CHAINGUARD_PYTHON_IDENTITY_ID
password CHAINGUARD_PYTHON_TOKEN
```

Note that the long string for the password value must use only one line.

## Verify entitlement

You can verify entitlements for your organization `example` with the following
command:

```shell
chainctl libraries entitlements list --parent=example
```

The output must include the desired ecosystem in the table:

```shell
Ecosystem Library Entitlements for example (45a0...764595)

                             ID                             | ECOSYSTEM
------------------------------------------------------------+------------
  45a....................................................e1 | JAVA
  45a....................................................x6 | PYTHON
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
