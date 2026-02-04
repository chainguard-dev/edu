---
title: "Chainguard Libraries access"
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

## Getting started

### Prerequisites

- Ensure you have access to Chainguard Libraries. 
    - If you are not a Chainguard user yet, a new Chainguard account must be
created and configured for access to Chainguard Libraries.
    - If you are already a Chainguard user, the Chainguard account owner in your
organization can grant access to Chainguard Libraries.
- Confirm the name of your organization so you can use it with the `--parent`
parameter to specify your organization when running commands with `chainctl`.

### Direct access vs. artifact manager

Chainguard Libraries supports two approaches to access: an artifact manager or
direct access. 

**Artifact manager**

If your organization uses an artifact manager such as JFrog Artifactory or Sonatype Nexus, you can set up and configure credentials once per language ecosystem. Then, all projects and developers automatically inherit
the configuration. This option is recommended for organizations with multiple
teams, and provides centralized access controls and consistent uptime. 

**Direct access**

Set up authentication directly in each project's build
configuration. This option allows for faster initial setup, but it does not
allow for global configuration. It requires configuration per project and
workstation, which creates more overhead as you scale across teams and projects.

Both approaches require pull tokens for authentication; see [Pull token
characteristics and use](#pull-token-characteristics-and-use) for more information. 

> NOTE: For Python users, the [Chainguard keyring
provider](#python-keyring-provider) uses short-lived credentials and is the
preferred method where your environment supports it. 

### Initial authentication

Once your user account is created and access is confirmed, [install the
Chainguard Control `chainctl` command line
tool](/chainguard/chainctl-usage/how-to-install-chainctl/) and log in to your
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

<a id name="pull-token"></a>

## Creating pull tokens for libraries

Pull tokens are separate identities with an assigned role to access the
repositories from Chainguard Libraries. You can create the pull tokens:
- With [the chainctl command](#creating-pull-tokens-with-chainctl), or 
- [Using the Chainguard
  console](#creating-pull-tokens-with-the-chainguard-console).

For environments where short-lived credentials are not suitable, such as some
CI/CD platforms, you can generate a pull token, which provides longer-lived
access to Chainguard Libraries.

To create a pull token you must have the relevant [entitlement](#entitlement)
for the ecosystem and the `libraries.java.pull_token_creator`,
`libraries.javascript.pull_token_creator`, or
`libraries.python.pull_token_creator` role.

### Creating pull tokens with chainctl

Create a new pull token for the Chainguard Libraries for Java with the [chainctl
auth pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/)
command:

```shell
chainctl auth pull-token --repository=java --parent=example --ttl=8670h
```

* `--repository=java`: retrieve the token for use with [Chainguard Libraries for
  Java](/chainguard/libraries/java/overview/). Use `python` for a token to use
  [Chainguard Libraries for Python](/chainguard/libraries/python/overview/) and
  `javascript` for a token to use [Chainguard Libraries for
  JavaScript](/chainguard/libraries/javascript/overview/).
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

### Creating pull tokens with the Chainguard console

Follow these steps to create a pull token for Chainguard Libraries in the
Chainguard console:

1. Use your authentication details to access the console at
  [https://console.chainguard.dev/](https://console.chainguard.dev/).
2. In the left-hand navigation, click **Overview**.
3. Click the **Manage pull tokens** tab, then click **Create access token**.
    - Alternatively, select **Access Tokens** from the menu at the top of the
      **Settings** page.
4. Configure the access token:
    - **Name**: Provide a name. The name can later be used to locate the token
  in the list.
    - **Description**: Optionally provide a description of the token.
    - **Access**: Choose the library that this token should access.
    - **Expiration**: Set an expiration date for the token. The default is 30
      days.
5. Click **Create token**.
6. When the username and password values are displayed, note these values in a
   secure location, as you will need them for pull token use. These values will
   not be displayed again.

## Pull token characteristics and use

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

For artifact manager setup, see the global configuration guides:
* [Java](/chainguard/libraries/java/global-configuration/)
* [JavaScript](/chainguard/libraries/javascript/global-configuration/)
* [Python](/chainguard/libraries/python/global-configuration/)

For direct access, see the build configuration guides:
* [Java](/chainguard/libraries/java/build-configuration/)
* [JavaScript](/chainguard/libraries/javascript/build-configuration/)
* [Python](/chainguard/libraries/python/build-configuration/)

<a name="env"></a>

### Use environment variables for pull token credentials

Using environment variables for username and password is more secure than hard
coding the values in configuration files. In addition, you can use the same
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

### .netrc for authentication

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

<a id name="python-keyring"></a>

## Python keyring provider

Python users can leverage an alternative to pull tokens. The [Chainguard keyring
implementation](https://github.com/chainguard-dev/keyrings-chainguard-libraries)
provides short-lived credentials from supported environments, such as local
development and CI/CD platforms that can use [assumable
identities](/chainguard/administration/assumable-ids/assumable-ids/).

Where possible, Chainguard recommends using short-lived credentials to access
Chainguard Libraries.

To set up the keyring, install the `keyrings-chainguard-libraries` package:

```shell
pip install keyrings-chainguard-libraries
```

*Note:* If you haven't set up access to Chainguard Libraries for Python, the
above command installs the package from PyPI. After installing and configuring
Chainguard Libraries for Python, you can get the private package again, to get
the package built by Chainguard. To re-install the package:

```
pip install keyrings-chainguard-libraries --ignore-installed --no-cache-dir
```

Once the keyring package is installed, when you request to install packages from
Chainguard Libraries for Python, the keyring automatically retrieves short-lived
credentials for you, using `chainctl`.

To use the keyring with a project `uv`, install the keyring:

```shell
uv pip install keyrings-chainguard-libraries
```

*Note:* If you haven't set up access to Chainguard Libraries for Python, the
above command installs the package from PyPI. After installing and configuring
Chainguard Libraries for Python, you can get the private package again, to get
the package built by Chainguard. To re-install the package:

```shell
uv pip install keyrings-chainguard-libraries --reinstall --no-cache
```

By default, [uv disables keyring
auth](https://docs.astral.sh/uv/reference/settings/#keyring-provider).

To enable it in the global uv.toml:

```toml
keyring-provider = "subprocess"
```

To enable it in a project-specific pyproject.toml:

```toml
[tool.uv]
keyring-provider = "subprocess"
```

<a id="pull-token-management"></a>

## Pull token management

Pull tokens are separate identities with username and password that are used for
access to Chainguard Libraries. The tokens have a limited Time to Live (TTL)
with a default of 30 days and a maximum TTL of 365 days.

As a result, pull tokens become invalid after the TTL and are flagged as
expired. For your use of Chainguard Libraries you must replace the token with a
new one.

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
