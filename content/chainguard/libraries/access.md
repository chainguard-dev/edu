---
title: "Chainguard Libraries Access"
linktitle: "Access"
description: "Learn how to access Chainguard Libraries for enhanced security in Java and Python dependencies, including authentication and organization setup"
type: "article"
date: 2025-03-25T00:08:04+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 002
toc: true
---

Chainguard Libraries provide controlled access to security-enhanced Java and
Python dependencies through the unified Chainguard platform authentication
system. This guide explains how to set up access for your organization.

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

```output
Successfully exchanged token.
Valid! Id: 8a4141a........7d9904d98c
```

<a id name="python-keyring"></a>

## Python Keyring integration

Where possible, Chainguard recommends using short-lived credentials to access Chainguard Libraries.

Python users can leverage the [Chainguard keyring implementation](https://github.com/chainguard-dev/keyrings-chainguard-libraries) to provide short-lived credentials from supported environments, such as local development and CI/CD platforms that support [assumable identities](https://edu.chainguard.dev/chainguard/administration/assumable-ids/assumable-ids/).

To set up the keyring, install the `keyrings-chainguard-libraries` package:

```shell
pip install keyrings-chainguard-libraries
```

Then, when you request to install packages from Chainguard Libraries for Python, the keyring automatically retrieves short-lived credentials for you, using `chainctl`.

To use the keyring with `uv`, install the keyring:

```shell
uv pip install keyring keyrings-chainguard-libraries
```

Then to use the keyring you

```shell
uv pip install --keyring-provider subprocess \
  --index-url https://__token__@libraries.cgr.dev/python/simple/ \
  <package-name>
```

Note that when using `uv pip` you must specify the `--keyring-provider subprocess` option to enable the keyring, and include `__token__@` in the index URL to signal to `uv` that authentication is required.

To use the keyring with `poetry`, install the keyring:

# TODO: POETRY -- DO NOT MERGE

<a id name="pull-token"></a>

## Pull token for libraries

For environments where short-lived credentials are not suitable, such as some CI/CD platforms, you can generate a pull token, which provides longer-lived access to Chainguard Libraries.

Pull tokens are separate identities with an assigned role to access the
repositories from Chainguard Libraries. You can create the pull tokens with the
chainctl command or using the Chainguard console.

### Creating pull tokens with chainctl

Create a new pull token for the Chainguard Libraries for Java with the [chainctl
auth pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/)
command:

```shell
chainctl auth pull-token --repository=java --parent=example --ttl=8670h
```

* `--repository=java`: retrieve the token for use with [Chainguard
  Libraries for Java](/chainguard/libraries/java/overview/). Use `python` for a
  token to use [Chainguard Libraries for
  Python](/chainguard/libraries/python/overview/) and `javascript` for a token to
  use [Chainguard Libraries for
  JavaScript](/chainguard/libraries/python/overview/).
* `--parent=example`: specify the parent organization for your account as
  provided when requesting access to Chainguard Libraries and replace `example`.
* `--ttl=8670h`: set the duration for the validity of the token, defaults to
  `720h` (equivalent to 30 days), maximum valid value is `8760h` (equivalent to
  365 days), valid unit strings range from nanoseconds to hours and are `ns`,
  `us`, `ms`, `s`, `m`, and `h`.

Use the optional `--name` flag to supply a meaningful and short name for the
token, to be able to locate it easier at a later stage.

When omitting the parent parameter, potentially a list of organizations is
displayed. Use the arrow keys to navigate the selection displayed after the
question “With which location is the pull token associated?” and select the
organization that has the entitlement to access Chainguard Libraries for Java.
Press `/` to filter the list.

`chainctl` returns a username and password suitable for basic authentication in
the response:

```output
Username: 45a.....424eb0

Password: eyJhbGciO..........WF0IjoxN
```

### Pull token characteristics and use

The returned username and password combination is a new credential set in the
organization that is independent of the account used to create and retrieve the
credential set. It is therefore suitable for use in any service application,
such as a repository manager or a build tool that is not tied to a specific
user. You can also use the token as an individual for your development with
direct access to Chainguard Libraries.

To use the pull token in another environment, supply the username and password
for basic authentication. Note that the actual returned values are much longer.

> **Note**: Chainguard does not offer an SLA for uptime availability of the
> Chainguard Libraries repositories at `libraries.cgr.dev`. To reduce production
> risk and ensure reliability, we recommend proxying the repositories through
> your own artifact repository whenever possible.

Refer to the following resources for more specific information for your needs:

* [Repository manager configuration with
  Java](/chainguard/libraries/java/global-configuration/)
* [Build tool and direct access configuration with
  Java](/chainguard/libraries/java/build-configuration/)
* [Repository manager configuration with
  JavaScript](/chainguard/libraries/javascript/global-configuration/)
* [Build tool and direct access configuration with
  JavaScript](/chainguard/libraries/javascript/build-configuration/)
* [Repository manager configuration with
  Python](/chainguard/libraries/python/global-configuration/)
* [Build tool and direct access configuration with
  Python](/chainguard/libraries/python/build-configuration/)

### Creating pull tokens with the Chainguard console

Use the following steps to create a pull tokens for Chainguard Libraries in the
Chainguard console.

* Use your authentication details to access the console at
  [https://console.chainguard.dev/](https://console.chainguard.dev/).
* Select **Overview** in the left-hand navigation.
* Select the **Manage pull tokens** tab.
  * Alternatively, select **Settings** in the left-hand navigation, and select
    **Pull Tokens** in the menu on the settings page.
* Press **Create pull token**.
* Provide a **Name** for the token. The name can later be used to locate the
  token in the list.
  * Optionally provide a **Description** and change the time until
    **Expiration**.
* Take note of the **Username** and **Password** values in a separate system
  since they are required for pull token use and not available at a later stage.

The created token has access to pull containers from your organization's
Chainguard registries. Use the following steps to change the role to allow use
with Chainguard Libraries:

* Select the **Manage pull tokens** tab.
* Locate the row of created token based on the name used earlier. Note that the
  string `- registry` is appended to the name automatically.
* Use the menu button in the **Actions** column of the same row and select
  **Edit**.
* Update the **Name** value by removing the `- registry` string and add any
  other desired modifications.
* Use the **Role** input under **Add role** to add the `libraries.java.pull`,
  `libraries.javascript.pull` or `libraries.python.pull` roles and press
  **Update**.
  * Optionally click on the `registry.pull` role under **Roles**, press **Edit
    role**, and then **Delete** to remove the role.

### Verification

Use the credentials for manual testing in a browser or with a script and curl if
you know the URL for a specific library artifact. Refer to the following
sections for more details:

* [Technical details and manual testing for Java
  libraries](/chainguard/libraries/java/overview/#technical-details)
* [Technical details and manual testing for JavaScript
  libraries](/chainguard/libraries/javascript/overview/#technical-details)
* [Technical details and manual testing for Python
  libraries](/chainguard/libraries/python/overview/#technical-details)
* [Use environment variables](#env)
* [.netrc for authentication](#netrc)

<a name="env"></a>

## Use environment variables

Using environment variables for username and password is more secure than
hard coding the values in configuration files. In addition, you can use the same
configuration and files for all users to simplify setup and reduce errors.

Use the `env` environment output option to create a snippet for a new token
suitable for integration in a script.

```shell
$ chainctl auth pull-token --output env --repository=java --parent=example
export CHAINGUARD_JAVA_IDENTITY_ID=45a.....424eb0
export CHAINGUARD_JAVA_TOKEN=eeyJhbGciO..........WF0IjoxN
```

Combine the call with `eval` to populate the environment variables directly by
calling `chainctl`:

```shell
eval $(chainctl auth pull-token --output env --repository=java --parent=example)
```

Equivalent commands for Python and JavaScript are supported and result in values
for the `CHAINGUARD_PYTHON_IDENTITY_ID`/`CHAINGUARD_PYTHON_TOKEN` and
`CHAINGUARD_JAVASCRIPT_IDENTITY_ID`/`CHAINGUARD_JAVASCRIPT_TOKEN` variables.

Running this command as part of a login script or some other automation allows
your organization to replace actual username and password values in your build
tool configuration with environment variable placeholders:

* [Java build tool
  configuration](/chainguard/libraries/java/build-configuration/)
* [JavaScript build tool
  configuration](/chainguard/libraries/javascript/build-configuration/)
* [Python build tool
  configuration](/chainguard/libraries/python/build-configuration/)

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
Python](/chainguard/libraries/python/build-configuration/#pip), with [bazel for
Chainguard Libraries for
Java](/chainguard/libraries/java/build-configuration/#bazel) or for manual
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

<a id="entitlement"></a>

## Verify entitlement

You can verify entitlements for your organization `example` with the following
command:

```shell
chainctl libraries entitlements list --parent=example
```

The output must include the desired ecosystem in the table:

```output
Ecosystem Library Entitlements for example (45a0...764595)

                             ID                             | ECOSYSTEM
------------------------------------------------------------+------------
  45a...................................................2cf | JAVASCRIPT
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

<a id="pull-token-management"></a>

## Pull token management

Pull tokens are separate identities with username and password that are used for
access to Chainguard Libraries. The tokens have a limited Time to Live (TTL)
with a default of 30 days and a maximum TTL of 365 days.

As a result, pull tokens become invalid after the TTL and are flagged as expired.
For your use of Chainguard Libraries you must replace the token with a new one.

Expired tokens can no longer be used for access to Chainguard Libraries, but
otherwise do not cause any issues and continue to exist until you delete them.

Inspect all pull tokens for your organization in the Chainguard console:

* Use your authentication details to access the console at
  [https://console.chainguard.dev/](https://console.chainguard.dev/).
* Select **Overview** in the left-hand navigation.
* Select the **Manage pull tokens** tab.
  * Alternatively, select **Settings** in the left-hand navigation, and select
    **Pull Tokens** in the menu on the settings page.

The list includes the following columns:

* **Name** - the name of the pull token, expired pull token are identified by a
  red **Expired** warning.
* **Description** - the description of the pull token
* **Created** - the date when the pull token was created
* **Expiration** - string description of the expiration status of the token,
  such as *in 8 months* or *4 days ago*.
* **Actions** - menu button to perform actions on the pull token, only a Delete
  action is available.

Use the action to remove a pull token:

* Locate the row of the desired pull token, typically an expired token.
* Use the menu button in the **Actions** column of the same row and select
  **Delete**.
* Confirm the deletion in the dialog by pressing **Delete pull token**.

Alternatively use chainctl with the [auth
pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/) and
[iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)
commands for various inspection and management tasks.

List all pull tokens with the `list` command:

```shell
chainctl auth pull-token list
```

The displayed list includes the following columns:

* **ID** - the identifying username of the pull token
* **NAME** - the name of the pull token
* **DESCRIPTION** - the description of the pull token
* **ROLES** - the assigned organization and role for the pull token. The value
  shows the name of the organization separate from the role with a colon. Valid
  roles are all pull authorization from for apk packages `apk.pull`, container
  images `registry.pull`, Python libraries `libraries.python.pull`, Java
  libraries `libraries.java.pull`, and JavaScript libraries
  `libraries.javascript.pull` .
* **EXPIRES** - the number of days until the end of the TTL period. Negative
  values indicate expired tokens.

List all pull tokens for Chainguard Libraries for Java that are not yet expired:

```shell
chainctl auth pull-token list --repository=java
```

List all expired pull tokens for Chainguard Libraries for Python:

```shell
chainctl auth pull-token list --repository=java --expired=true
```

Use the [delete command for IAM
identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_delete/)
to delete a specific pull token using its ID `45a0c61ea6fd97...`:

```shell
chainctl iam identities delete 45a0c61ea6fd97...
```

Use the identifier or name of your organization `example` and the `--expired`
flag to remove all expired pull tokens:

```shell
chainctl iam ids rm --expired --parent=example
```
