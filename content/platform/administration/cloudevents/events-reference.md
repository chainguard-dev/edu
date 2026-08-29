---
title : "Chainguard Events"
lead: ""
aliases:
- /chainguard/administration/cloudevents/events-reference/
description: "Chainguard Events"
type: "article"
date: 2022-11-15T12:05:04
lastmod: 2026-08-28T20:13:22
draft: false
tags: ["Platform", "Reference", "Product"]
images: []
weight: 005
---

Chainguard generates and emits [CloudEvents](https://cloudevents.io/) based on actions that occur within a Chainguard account, such as registering a Kubernetes cluster or creating an IAM invitation. Chainguard also emits events when workloads or policies are changed in a cluster.

Check out [this GitHub repository](https://github.com/chainguard-dev/enforce-events) for some sample applications that demonstrate how to use events to create Slack notifications, open GitHub issues, and mirror images.

To subscribe to Chainguard events for your account, use the `chainctl` command like this:

```shell
chainctl events subscriptions create –parent $YOUR_ORGANIZATION_OR_FOLDER https://<Your webhook URL>

```

Once you are subscribed to Chainguard events, you will start receiving HTTP POST requests. Each request has a common set of CloudEvent header fields, denoted by the `Ce-` prefix. The event body is encoded using JSON and will have two top-level keys, `actor` and `body`.

The `actor` field is the identity of the actor in your Chainguard account that triggered the event, such as a team member or a Kubernetes cluster. The `body` field contains the specific data about the event, for example the response status for an invite creation request, or a cluster delete request.

## UIDP Identifiers

Each Chainguard event includes a `Ce-Subject` header that contains a UIDP (UID Path) identifier. Identifiers follow POSIX directory semantics and components are separated by `/` delimiters. A UIDP is comprised of:

* A globally unique identifier (UID), consisting of 20 bytes, that are URL safe hex encoded. For example, account identities like `0475f6baca584a8964a6bce6b74dbe78dd8805b6`.

* One, or multiple `/` separated, scoped unique identifiers (SUID). An SUID is 8 bytes that are unique within a scope (like a group), and are URL safe hex encoded. The following is an example SUID: `b74ce966caf448d1`. SUIDs are used to identify every entity in Chainguard, from groups, policies, Kubernetes cluster IDs, event subscriptions, to IAM invitations, roles and role-bindings.

Since Chainguard groups can contain child groups, events in a child group will propagate to the parent and thus the UIDP will contain multiple group SUIDs, along with the entity SUID itself. For example, assuming the following components:

* An account UID of `0475f6baca584a8964a6bce6b74dbe78dd8805b6`
* A group SUID of `b74ce966caf448d1`
* A child of group `b74ce966caf448d1` with its own SUID of `dda9aab2d2d90f9e`

The complete UIDP in the event's `Ce-Subject` header would be:

```
0475f6baca584a8964a6bce6b74dbe78dd8805b6/b74ce966caf448d1/dda9aab2d2d90f9e/1a4b29ca6df80013

```

## Authorization Header

Every Chainguard event has a JWT formatted [OIDC ID token](https://openid.net/specs/openid-connect-basic-1_0.html#IDToken) in its `Authorization` header. For authorization purposes, there are two important fields to validate:

1. Use the `iss` field to ensure that the issuer is Chainguard, specifically `https://issuer.enforce.dev`.
2. Use the `sub` field to check that the event matches your configured Chainguard identity. For example, assuming a UIDP ID of `0475f6baca584a8964a6bce6b74dbe78dd8805b6`, the value will resemble the following: `webhook:0475f6baca584a8964a6bce6b74dbe78dd8805b6`. If the subscription is in a sub-group, then the value will have the corresponding group SUID appended to the path.

Validating these fields before processing the JWT token using a verification library can save resources, as well as alert about suspicious traffic, or misconfigured Chainguard group settings.

## CloudEvents Sources

Chainguard CloudEvents are delivered from a stable set of egress IP
addresses. These are also published as A records on `egress.enforce.dev`,
so you can allowlist that name instead of hard-coding the individual
addresses:

* `34.132.193.40`
* `35.237.242.37`
* `35.230.121.20`
* `34.85.183.217`

These addresses apply to sinks reached over the public internet. A sink
hosted on Google Cloud, such as a Cloud Run `.run.app` URL, may instead be
reached over Google's internal network. In that case the delivery does not
originate from any of these addresses, and no source-IP allowlist will
match it. Verify those deliveries using the OIDC token in the
`Authorization` header, as described above, rather than by source IP.

## Events Reference

The following list of services and methods show example HTTP headers and bodies for public facing Chainguard events.

## Service: Registry - Pull

### Method: Pulled

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: cgr.dev
Ce-Specversion: 1.0
Ce-Subject: The identifier of the repository being pulled from
Ce-Time: 2026-08-28T20:13:22.179701671Z
Ce-Type: dev.chainguard.registry.pull.v1
Content-Length: 777
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "digest": "The digest of the image being pulled",
    "error": {
      "code": "The OCI distribution-spec error code",
      "message": "The error message",
      "status": 0
    },
    "location": "Location holds the detected approximate location of the client who pulled. For example, \"ColumbusOHUS\" or \"Minato City13JP",
    "method": "The method used to pull the image. One of: HEAD or GET",
    "remote_address": "",
    "repo_id": "The identifier of the repository being pulled from",
    "repository": "The identifier of the repository being pulled from",
    "tag": "The tag of the image being pulled",
    "type": "Type determines whether the object being pulled is a manifest or blob",
    "user_agent": "The user-agent of the client who pulled",
    "when": "2026-08-28T20:13:22.178820"
  }
}

```

## Service: Registry - Push

### Method: Pushed

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: cgr.dev
Ce-Specversion: 1.0
Ce-Subject: The identifier of the repository being pushed to
Ce-Time: 2026-08-28T20:13:22.179022993Z
Ce-Type: dev.chainguard.registry.push.v1
Content-Length: 707
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "digest": "The digest of the image being pushed",
    "error": {
      "code": "The OCI distribution-spec error code",
      "message": "The error message",
      "status": 0
    },
    "location": "Location holds the detected approximate location of the client who pushed. For example, \"ColumbusOHUS\" or \"Minato City13JP",
    "remote_address": "",
    "repo_id": "The identifier of the repository being pushed to",
    "repository": "The identifier of the repository being pushed to",
    "tag": "The tag of the image being pushed",
    "type": "Type determines whether the object being pushed is a manifest or blob",
    "user_agent": "The user-agent of the client who pushed",
    "when": "2026-08-28T20:13:22.178791"
  }
}

```

## Service: auth - Auth

### Method: Register

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/auth/v1/register
Ce-Specversion: 1.0
Ce-Subject: Chainguard UIDP
Ce-Time: 2026-08-28T20:13:22.193240986Z
Ce-Type: dev.chainguard.api.auth.registered.v1
Content-Length: 154
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "group": "the group this identity has joined by invitation",
    "identity": "Chainguard UIDP"
  }
}

```

## Service: events - Subscriptions

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/events/v1/subscriptions
Ce-Specversion: 1.0
Ce-Subject: UIDP identifier of the subscription
Ce-Time: 2026-08-28T20:13:22.191010684Z
Ce-Type: dev.chainguard.api.events.subscription.created.v1
Content-Length: 152
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP identifier of the subscription",
    "sink": "Webhook endpoint (http/https URL)"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/events/v1/subscriptions
Ce-Specversion: 1.0
Ce-Subject: UIDP identifier of the subscription to delete
Ce-Time: 2026-08-28T20:13:22.191446057Z
Ce-Type: dev.chainguard.api.events.subscription.deleted.v1
Content-Length: 119
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP identifier of the subscription to delete"
  }
}

```

## Service: iam - ExternalGroupRoleMappings

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/externalGroupRoleMappings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the mapping
Ce-Time: 2026-08-28T20:13:22.191975184Z
Ce-Type: dev.chainguard.api.iam.external_group_role_mappings.created.v1
Content-Length: 290
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "external_group_id": "The IdP group identifier",
    "id": "UIDP of the mapping",
    "identity_provider_uidp": "UIDP of the identity provider",
    "role_uidp": "UIDP of the Chainguard role",
    "scope": "UIDP of the group where the role applies"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/externalGroupRoleMappings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the mapping
Ce-Time: 2026-08-28T20:13:22.192182347Z
Ce-Type: dev.chainguard.api.iam.external_group_role_mappings.deleted.v1
Content-Length: 93
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the mapping"
  }
}

```

### Method: BatchDelete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/externalGroupRoleMappings:batchDelete
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.192364064Z
Ce-Type: dev.chainguard.api.iam.external_group_role_mappings.deleted.batch.v1
Content-Length: 346
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "items": [
      {
        "external_group_id": "The IdP group identifier",
        "id": "UIDP of the mapping",
        "identity_provider_uidp": "UIDP of the identity provider",
        "role_uidp": "UIDP of the Chainguard role",
        "scope": "UIDP of the group where the role applies"
      }
    ],
    "parent_id": "UIDP of the identity provider"
  }
}

```

## Service: iam - GroupAccountAssociations

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/account_associations
Ce-Specversion: 1.0
Ce-Subject: UIDP with which this account information is associated
Ce-Time: 2026-08-28T20:13:22.182058325Z
Ce-Type: dev.chainguard.api.iam.account_associations.created.v1
Content-Length: 385
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "amazon": {
      "account": "Amazon account ID (if applicable)"
    },
    "description": "description of this association",
    "google": {
      "project_id": "Google Cloud Project ID (if applicable)",
      "project_number": "Google Cloud Project Number (if applicable)"
    },
    "group": "UIDP with which this account information is associated",
    "name": "group name"
  }
}

```

### Method: Update

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/account_associations
Ce-Specversion: 1.0
Ce-Subject: UIDP with which this account information is associated
Ce-Time: 2026-08-28T20:13:22.182240226Z
Ce-Type: dev.chainguard.api.iam.account_associations.updated.v1
Content-Length: 336
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "amazon": {
      "account": "amazon account if applicable"
    },
    "description": "group description",
    "google": {
      "project_id": "project id if applicable",
      "project_number": "project number if applicable"
    },
    "group": "UIDP with which this account information is associated",
    "name": "group name"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/account_associations
Ce-Specversion: 1.0
Ce-Subject: UIDP of the group whose associations will be deleted
Ce-Time: 2026-08-28T20:13:22.182427575Z
Ce-Type: dev.chainguard.api.iam.account_associations.deleted.v1
Content-Length: 129
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "group": "UIDP of the group whose associations will be deleted"
  }
}

```

## Service: iam - GroupInvites

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/group_invites
Ce-Specversion: 1.0
Ce-Subject: group UIDP under which this invite resides
Ce-Time: 2026-08-28T20:13:22.184697954Z
Ce-Type: dev.chainguard.api.iam.group_invite.created.v1
Content-Length: 145
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "expiration": {
      "seconds": 100
    },
    "id": "group UIDP under which this invite resides"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/group_invites
Ce-Specversion: 1.0
Ce-Subject: UIDP of the record
Ce-Time: 2026-08-28T20:13:22.184906757Z
Ce-Type: dev.chainguard.api.iam.group_invite.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the record"
  }
}

```

## Service: iam - Groups

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/groups
Ce-Specversion: 1.0
Ce-Subject: group UIDP under which this group resides
Ce-Time: 2026-08-28T20:13:22.188837994Z
Ce-Type: dev.chainguard.api.iam.group.created.v1
Content-Length: 169
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "group description",
    "id": "group UIDP under which this group resides",
    "name": "group name"
  }
}

```

### Method: Update

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/groups
Ce-Specversion: 1.0
Ce-Subject: group UIDP under which this group resides
Ce-Time: 2026-08-28T20:13:22.189036126Z
Ce-Type: dev.chainguard.api.iam.group.updated.v1
Content-Length: 169
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "group description",
    "id": "group UIDP under which this group resides",
    "name": "group name"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/groups
Ce-Specversion: 1.0
Ce-Subject: UIDP of the record
Ce-Time: 2026-08-28T20:13:22.189181805Z
Ce-Type: dev.chainguard.api.iam.group.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the record"
  }
}

```

## Service: iam - Identities

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identities
Ce-Specversion: 1.0
Ce-Subject: UIDP of identity
Ce-Time: 2026-08-28T20:13:22.194423361Z
Ce-Type: dev.chainguard.api.iam.identity.created.v1
Content-Length: 329
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "identity": {
      "Relationship": null,
      "description": "The human readable description of identity",
      "id": "The unique identifier of this specific identity",
      "name": "The human readable name of identity"
    },
    "parent_id": "The Group UIDP path under which the new Identity resides"
  }
}

```

### Method: Update

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identities
Ce-Specversion: 1.0
Ce-Subject: The unique identifier of this specific identity
Ce-Time: 2026-08-28T20:13:22.194580735Z
Ce-Type: dev.chainguard.api.iam.identity.updated.v1
Content-Length: 245
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "Relationship": null,
    "description": "The human readable description of identity",
    "id": "The unique identifier of this specific identity",
    "name": "The human readable name of identity"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identities
Ce-Specversion: 1.0
Ce-Subject: UIDP of the record
Ce-Time: 2026-08-28T20:13:22.194742197Z
Ce-Type: dev.chainguard.api.iam.identity.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the record"
  }
}

```

## Service: iam - IdentityProviders

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of identity provider
Ce-Time: 2026-08-28T20:13:22.198101942Z
Ce-Type: dev.chainguard.api.iam.identity_providers.created.v1
Content-Length: 378
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "identity_provider": {
      "Configuration": null,
      "description": "The human readable description of identity provider",
      "id": "The UIDP of the IAM group to nest this identity provider under",
      "name": "The human readable name of identity provider"
    },
    "parent_id": "The UIDP of the IAM group to nest this identity provider under"
  }
}

```

### Method: Update

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: The UIDP of the IAM group to nest this identity provider under
Ce-Time: 2026-08-28T20:13:22.198267491Z
Ce-Type: dev.chainguard.api.iam.identity_providers.updated.v1
Content-Length: 279
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "Configuration": null,
    "description": "The human readable description of identity provider",
    "id": "The UIDP of the IAM group to nest this identity provider under",
    "name": "The human readable name of identity provider"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the IdP
Ce-Time: 2026-08-28T20:13:22.19844384Z
Ce-Type: dev.chainguard.api.iam.identity_providers.deleted.v1
Content-Length: 89
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the IdP"
  }
}

```

### Method: GenerateScimToken

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.198610182Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_token.generated.v1
Content-Length: 250
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "endpoint_url": "SCIM endpoint URL for the identity provider",
    "etag": "Opaque version of the SCIM configuration",
    "expire_time": {},
    "identity_provider_uid": "UIDP of the identity provider"
  }
}

```

### Method: RegenerateScimToken

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.19881345Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_token.regenerated.v1
Content-Length: 319
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "endpoint_url": "SCIM endpoint URL for the identity provider",
    "etag": "Opaque version of the SCIM configuration",
    "expire_time": {},
    "identity_provider_uid": "UIDP of the identity provider",
    "previous_token_expire_time": {},
    "requested_overlap": {
      "seconds": 3600
    }
  }
}

```

### Method: RevokeScimToken

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.198978255Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_token.revoked.v1
Content-Length: 189
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "etag": "Opaque version of the SCIM configuration",
    "identity_provider_uid": "UIDP of the identity provider",
    "revoke_time": {}
  }
}

```

### Method: SetScimEnabled

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.199079713Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_enabled.updated.v1
Content-Length: 187
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "enabled": true,
    "etag": "Opaque version of the SCIM configuration",
    "identity_provider_uid": "UIDP of the identity provider"
  }
}

```

## Service: iam - RoleBindings

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/rolebindings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the Role to bind
Ce-Time: 2026-08-28T20:13:22.19259197Z
Ce-Type: dev.chainguard.api.iam.rolebindings.created.v1
Content-Length: 261
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "parent": "The Group UIDP path under which the new RoleBinding resides",
    "role_binding": {
      "id": "UID of this role binding",
      "identity": "UID of the Identity to bind",
      "role": "UIDP of the Role to bind"
    }
  }
}

```

### Method: CreateBatch

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/rolebindings/batch
Ce-Specversion: 1.0
Ce-Subject: UID of this role binding, under a parent group UIDP
Ce-Time: 2026-08-28T20:13:22.192766983Z
Ce-Type: dev.chainguard.api.iam.rolebindings.created.batch.v1
Content-Length: 220
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "role_bindings": [
      {
        "id": "UID of this role binding, under a parent group UIDP",
        "identity": "UID of the Identity to bind",
        "role": "UIDP of the Role to bind"
      }
    ]
  }
}

```

### Method: Update

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/rolebindings
Ce-Specversion: 1.0
Ce-Subject: UID of this role binding
Ce-Time: 2026-08-28T20:13:22.192905815Z
Ce-Type: dev.chainguard.api.iam.rolebindings.updated.v1
Content-Length: 173
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UID of this role binding",
    "identity": "UID of the Identity to bind",
    "role": "UIDP of the Role to bind"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/rolebindings
Ce-Specversion: 1.0
Ce-Subject: UID of the record
Ce-Time: 2026-08-28T20:13:22.193049142Z
Ce-Type: dev.chainguard.api.iam.rolebindings.deleted.v1
Content-Length: 91
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UID of the record"
  }
}

```

## Service: iam - Roles

### Method: Create

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/roles
Ce-Specversion: 1.0
Ce-Subject: UIDP of the role under the group
Ce-Time: 2026-08-28T20:13:22.182641705Z
Ce-Type: dev.chainguard.api.iam.roles.created.v1
Content-Length: 159
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "role description",
    "name": "role name",
    "uid": "UIDP of the role under the group"
  }
}

```

### Method: Update

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/roles
Ce-Specversion: 1.0
Ce-Subject: UIDP of the role under the group
Ce-Time: 2026-08-28T20:13:22.182821222Z
Ce-Type: dev.chainguard.api.iam.roles.updated.v1
Content-Length: 159
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "role description",
    "name": "role name",
    "uid": "UIDP of the role under the group"
  }
}

```

### Method: Delete

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/roles
Ce-Specversion: 1.0
Ce-Subject: UIDP of the role to delete
Ce-Time: 2026-08-28T20:13:22.182962373Z
Ce-Type: dev.chainguard.api.iam.roles.deleted.v1
Content-Length: 101
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "uid": "UIDP of the role to delete"
  }
}

```

## Service: iam - Terms

### Method: AcceptTerms

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v1/terms
Ce-Specversion: 1.0
Ce-Subject: Chainguard UIDP of the organization
Ce-Time: 2026-08-28T20:13:22.185069939Z
Ce-Type: dev.chainguard.api.iam.terms.accepted.v1
Content-Length: 159
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "document_ids": [
      "guardener-tos.v1",
      "sfdpa.v1"
    ],
    "group": "Chainguard UIDP of the organization"
  }
}

```

## Service: registry - Charts

### Method: AddChart

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/repos
Ce-Specversion: 1.0
Ce-Subject: UIDP of the destination organization
Ce-Time: 2026-08-28T20:13:22.189419094Z
Ce-Type: dev.chainguard.api.platform.registry.chart.added.v1
Content-Length: 208
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "repos": [
      {
        "created": true,
        "id": "The UIDP of the created repo",
        "name": "The path of the created repo relative to the destination organization"
      }
    ]
  }
}

```

## Service: registry - Registry

### Method: CreateRepo

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.186496339Z
Ce-Type: dev.chainguard.api.platform.registry.repo.created.v1
Content-Length: 243
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository",
    "name": "The name is the human-readable name of the repository",
    "sync_config": {
      "expiration": {},
      "source": "Repo ID to sync from"
    }
  }
}

```

### Method: UpdateRepo

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.187509508Z
Ce-Type: dev.chainguard.api.platform.registry.repo.updated.v1
Content-Length: 243
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository",
    "name": "The name is the human-readable name of the repository",
    "sync_config": {
      "expiration": {},
      "source": "Repo ID to sync from"
    }
  }
}

```

### Method: DeleteRepo

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.187709656Z
Ce-Type: dev.chainguard.api.platform.registry.repo.deleted.v1
Content-Length: 116
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository"
  }
}

```

### Method: CreateTag

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/tags
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific tag
Ce-Time: 2026-08-28T20:13:22.18786563Z
Ce-Type: dev.chainguard.api.platform.registry.tag.created.v1
Content-Length: 197
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "digest": "The digest of the manifest with this tag",
    "id": "The identifier of this specific tag",
    "name": "The unique name of the tag"
  }
}

```

### Method: UpdateTag

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/tags
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific tag
Ce-Time: 2026-08-28T20:13:22.187997742Z
Ce-Type: dev.chainguard.api.platform.registry.tag.updated.v1
Content-Length: 197
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "digest": "The digest of the manifest with this tag",
    "id": "The identifier of this specific tag",
    "name": "The unique name of the tag"
  }
}

```

### Method: DeleteTag

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v1/tags
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific tag
Ce-Time: 2026-08-28T20:13:22.188121662Z
Ce-Type: dev.chainguard.api.platform.registry.tag.deleted.v1
Content-Length: 109
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific tag"
  }
}

```

## Service: v1 - Bindings

### Method: CreateBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/bindings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the binding
Ce-Time: 2026-08-28T20:13:22.195331617Z
Ce-Type: dev.chainguard.api.policies.bindings.created.v1
Content-Length: 245
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "created_at": {},
    "id": "UIDP of the binding",
    "mode": 1,
    "policy": "UIDP of the policy bound to the parent",
    "resource_types": [
      "Resource type(s) the binding applies to"
    ],
    "updated_at": {}
  }
}

```

### Method: UpdateBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/bindings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the binding
Ce-Time: 2026-08-28T20:13:22.195560227Z
Ce-Type: dev.chainguard.api.policies.bindings.updated.v1
Content-Length: 245
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "created_at": {},
    "id": "UIDP of the binding",
    "mode": 1,
    "policy": "UIDP of the policy bound to the parent",
    "resource_types": [
      "Resource type(s) the binding applies to"
    ],
    "updated_at": {}
  }
}

```

### Method: DeleteBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/bindings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the binding
Ce-Time: 2026-08-28T20:13:22.195711705Z
Ce-Type: dev.chainguard.api.policies.bindings.deleted.v1
Content-Length: 93
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the binding"
  }
}

```

## Service: v1 - Overrides

### Method: CreateOverride

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/overrides
Ce-Specversion: 1.0
Ce-Subject: UIDP of the override
Ce-Time: 2026-08-28T20:13:22.195891806Z
Ce-Type: dev.chainguard.api.policies.overrides.created.v1
Content-Length: 303
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "created_at": {},
    "created_by": "Identity of the actor that created the override",
    "digest": "Digest of the image being waived",
    "id": "UIDP of the override",
    "policy_id": "UIDP of the policy being waived",
    "reason": "Justification for the waiver"
  }
}

```

### Method: DeleteOverride

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/overrides
Ce-Specversion: 1.0
Ce-Subject: UIDP of the override
Ce-Time: 2026-08-28T20:13:22.196064795Z
Ce-Type: dev.chainguard.api.policies.overrides.deleted.v1
Content-Length: 94
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the override"
  }
}

```

## Service: v1 - Policies

### Method: CreatePolicy

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/policies
Ce-Specversion: 1.0
Ce-Subject: UIDP of the policy
Ce-Time: 2026-08-28T20:13:22.194937969Z
Ce-Type: dev.chainguard.api.policies.policies.created.v1
Content-Length: 337
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "created_at": {},
    "description": "Description of the policy",
    "expression": "Rego expression that defines the policy",
    "id": "UIDP of the policy",
    "name": "Name of the policy",
    "policy_type": 2,
    "supported_resource_type": "Versioned resource type the policy supports",
    "updated_at": {}
  }
}

```

### Method: UpdatePolicy

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/policies
Ce-Specversion: 1.0
Ce-Subject: UIDP of the policy
Ce-Time: 2026-08-28T20:13:22.195097527Z
Ce-Type: dev.chainguard.api.policies.policies.updated.v1
Content-Length: 337
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "created_at": {},
    "description": "Description of the policy",
    "expression": "Rego expression that defines the policy",
    "id": "UIDP of the policy",
    "name": "Name of the policy",
    "policy_type": 2,
    "supported_resource_type": "Versioned resource type the policy supports",
    "updated_at": {}
  }
}

```

### Method: DeletePolicy

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/policies/v1/policies
Ce-Specversion: 1.0
Ce-Subject: UIDP of the policy
Ce-Time: 2026-08-28T20:13:22.195200449Z
Ce-Type: dev.chainguard.api.policies.policies.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the policy"
  }
}

```

## Service: v2beta1 - AccountAssociationsService

### Method: CreateAccountAssociation

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/accountAssociations
Ce-Specversion: 1.0
Ce-Subject: UIDP with which this account information is associated
Ce-Time: 2026-08-28T20:13:22.180139468Z
Ce-Type: dev.chainguard.api.iam.account_associations.created.v1
Content-Length: 385
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "amazon": {
      "account": "Amazon account ID (if applicable)"
    },
    "description": "description of this association",
    "google": {
      "project_id": "Google Cloud Project ID (if applicable)",
      "project_number": "Google Cloud Project Number (if applicable)"
    },
    "group": "UIDP with which this account information is associated",
    "name": "group name"
  }
}

```

### Method: DeleteAccountAssociation

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/accountAssociations
Ce-Specversion: 1.0
Ce-Subject: UIDP of the group whose associations will be deleted
Ce-Time: 2026-08-28T20:13:22.180387141Z
Ce-Type: dev.chainguard.api.iam.account_associations.deleted.v1
Content-Length: 129
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "group": "UIDP of the group whose associations will be deleted"
  }
}

```

### Method: UpdateAccountAssociation

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/accountAssociations
Ce-Specversion: 1.0
Ce-Subject: UIDP with which this account information is associated
Ce-Time: 2026-08-28T20:13:22.180617414Z
Ce-Type: dev.chainguard.api.iam.account_associations.updated.v1
Content-Length: 336
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "amazon": {
      "account": "amazon account if applicable"
    },
    "description": "group description",
    "google": {
      "project_id": "project id if applicable",
      "project_number": "project number if applicable"
    },
    "group": "UIDP with which this account information is associated",
    "name": "group name"
  }
}

```

## Service: v2beta1 - ExternalGroupRoleMappingsService

### Method: CreateExternalGroupRoleMapping

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/externalGroupRoleMappings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the mapping
Ce-Time: 2026-08-28T20:13:22.193487379Z
Ce-Type: dev.chainguard.api.iam.external_group_role_mappings.created.v1
Content-Length: 290
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "external_group_id": "The IdP group identifier",
    "id": "UIDP of the mapping",
    "identity_provider_uidp": "UIDP of the identity provider",
    "role_uidp": "UIDP of the Chainguard role",
    "scope": "UIDP of the group where the role applies"
  }
}

```

### Method: DeleteExternalGroupRoleMapping

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/externalGroupRoleMappings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the mapping
Ce-Time: 2026-08-28T20:13:22.193653129Z
Ce-Type: dev.chainguard.api.iam.external_group_role_mappings.deleted.v1
Content-Length: 93
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the mapping"
  }
}

```

### Method: BatchDeleteExternalGroupRoleMappings

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/externalGroupRoleMappings:batchDelete
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.193781849Z
Ce-Type: dev.chainguard.api.iam.external_group_role_mappings.deleted.batch.v1
Content-Length: 346
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "items": [
      {
        "external_group_id": "The IdP group identifier",
        "id": "UIDP of the mapping",
        "identity_provider_uidp": "UIDP of the identity provider",
        "role_uidp": "UIDP of the Chainguard role",
        "scope": "UIDP of the group where the role applies"
      }
    ],
    "parent_id": "UIDP of the identity provider"
  }
}

```

## Service: v2beta1 - GroupInvitesService

### Method: CreateGroupInvite

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/groupInvites
Ce-Specversion: 1.0
Ce-Subject: group UIDP under which this invite resides
Ce-Time: 2026-08-28T20:13:22.185300773Z
Ce-Type: dev.chainguard.api.iam.group_invite.created.v1
Content-Length: 145
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "expiration": {
      "seconds": 100
    },
    "id": "group UIDP under which this invite resides"
  }
}

```

### Method: DeleteGroupInvite

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/groupInvites
Ce-Specversion: 1.0
Ce-Subject: UIDP of the record
Ce-Time: 2026-08-28T20:13:22.185448836Z
Ce-Type: dev.chainguard.api.iam.group_invite.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the record"
  }
}

```

## Service: v2beta1 - GroupsService

### Method: DeleteGroup

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/groups
Ce-Specversion: 1.0
Ce-Subject: UIDP of the record
Ce-Time: 2026-08-28T20:13:22.190567855Z
Ce-Type: dev.chainguard.api.iam.group.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the record"
  }
}

```

### Method: CreateGroup

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/groups
Ce-Specversion: 1.0
Ce-Subject: group UIDP under which this group resides
Ce-Time: 2026-08-28T20:13:22.190714422Z
Ce-Type: dev.chainguard.api.iam.group.created.v1
Content-Length: 169
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "group description",
    "id": "group UIDP under which this group resides",
    "name": "group name"
  }
}

```

### Method: UpdateGroup

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/groups
Ce-Specversion: 1.0
Ce-Subject: group UIDP under which this group resides
Ce-Time: 2026-08-28T20:13:22.19084627Z
Ce-Type: dev.chainguard.api.iam.group.updated.v1
Content-Length: 169
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "group description",
    "id": "group UIDP under which this group resides",
    "name": "group name"
  }
}

```

## Service: v2beta1 - IdentitiesService

### Method: CreateIdentity

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identities
Ce-Specversion: 1.0
Ce-Subject: UIDP of identity
Ce-Time: 2026-08-28T20:13:22.189729755Z
Ce-Type: dev.chainguard.api.iam.identity.created.v1
Content-Length: 329
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "identity": {
      "Relationship": null,
      "description": "The human readable description of identity",
      "id": "The unique identifier of this specific identity",
      "name": "The human readable name of identity"
    },
    "parent_id": "The Group UIDP path under which the new Identity resides"
  }
}

```

### Method: DeleteIdentity

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identities
Ce-Specversion: 1.0
Ce-Subject: UIDP of the record
Ce-Time: 2026-08-28T20:13:22.189965413Z
Ce-Type: dev.chainguard.api.iam.identity.deleted.v1
Content-Length: 92
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the record"
  }
}

```

### Method: UpdateIdentity

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identities
Ce-Specversion: 1.0
Ce-Subject: The unique identifier of this specific identity
Ce-Time: 2026-08-28T20:13:22.190112803Z
Ce-Type: dev.chainguard.api.iam.identity.updated.v1
Content-Length: 245
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "Relationship": null,
    "description": "The human readable description of identity",
    "id": "The unique identifier of this specific identity",
    "name": "The human readable name of identity"
  }
}

```

### Method: UpdateIdentityMetadata

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identities:updateIdentityMetadata
Ce-Specversion: 1.0
Ce-Subject: The caller's identity UID
Ce-Time: 2026-08-28T20:13:22.190245163Z
Ce-Type: dev.chainguard.api.iam.identity.metadata.updated.v1
Content-Length: 135
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "name": "The caller's display name",
    "uid": "The caller's identity UID"
  }
}

```

## Service: v2beta1 - IdentityProvidersService

### Method: CreateIdentityProvider

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of identity provider
Ce-Time: 2026-08-28T20:13:22.196312556Z
Ce-Type: dev.chainguard.api.iam.identity_providers.created.v1
Content-Length: 378
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "identity_provider": {
      "Configuration": null,
      "description": "The human readable description of identity provider",
      "id": "The UIDP of the IAM group to nest this identity provider under",
      "name": "The human readable name of identity provider"
    },
    "parent_id": "The UIDP of the IAM group to nest this identity provider under"
  }
}

```

### Method: UpdateIdentityProvider

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: The UIDP of the IAM group to nest this identity provider under
Ce-Time: 2026-08-28T20:13:22.196528447Z
Ce-Type: dev.chainguard.api.iam.identity_providers.updated.v1
Content-Length: 279
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "Configuration": null,
    "description": "The human readable description of identity provider",
    "id": "The UIDP of the IAM group to nest this identity provider under",
    "name": "The human readable name of identity provider"
  }
}

```

### Method: DeleteIdentityProvider

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the IdP
Ce-Time: 2026-08-28T20:13:22.1967053Z
Ce-Type: dev.chainguard.api.iam.identity_providers.deleted.v1
Content-Length: 89
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UIDP of the IdP"
  }
}

```

### Method: GenerateScimToken

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.196871426Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_token.generated.v1
Content-Length: 250
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "endpoint_url": "SCIM endpoint URL for the identity provider",
    "etag": "Opaque version of the SCIM configuration",
    "expire_time": {},
    "identity_provider_uid": "UIDP of the identity provider"
  }
}

```

### Method: RegenerateScimToken

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.197050519Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_token.regenerated.v1
Content-Length: 319
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "endpoint_url": "SCIM endpoint URL for the identity provider",
    "etag": "Opaque version of the SCIM configuration",
    "expire_time": {},
    "identity_provider_uid": "UIDP of the identity provider",
    "previous_token_expire_time": {},
    "requested_overlap": {
      "seconds": 3600
    }
  }
}

```

### Method: RevokeScimToken

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.197247698Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_token.revoked.v1
Content-Length: 189
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "etag": "Opaque version of the SCIM configuration",
    "identity_provider_uid": "UIDP of the identity provider",
    "revoke_time": {}
  }
}

```

### Method: SetScimEnabled

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/identityProviders
Ce-Specversion: 1.0
Ce-Subject: UIDP of the identity provider
Ce-Time: 2026-08-28T20:13:22.197442046Z
Ce-Type: dev.chainguard.api.iam.identity_providers.scim_enabled.updated.v1
Content-Length: 187
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "enabled": true,
    "etag": "Opaque version of the SCIM configuration",
    "identity_provider_uid": "UIDP of the identity provider"
  }
}

```

## Service: v2beta1 - OverlayBindingsService

### Method: CreateOverlayBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/overlayBindings
Ce-Specversion: 1.0
Ce-Subject: The identifier of this overlay binding
Ce-Time: 2026-08-28T20:13:22.197659753Z
Ce-Type: dev.chainguard.api.platform.registry.overlay_binding.created.v1
Content-Length: 423
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "overlay": {
      "config": {
        "contents": {
          "packages": [
            "The APK package names the attached overlay adds"
          ]
        }
      },
      "name": "The unique name of the attached overlay",
      "uid": "The identifier of the attached overlay"
    },
    "repo": "The identifier of the repo this binding applies to",
    "tags": [
      "The exact tag names this binding applies to"
    ],
    "uid": "The identifier of this overlay binding"
  }
}

```

### Method: DeleteOverlayBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/overlayBindings
Ce-Specversion: 1.0
Ce-Subject: The identifier of the deleted overlay binding
Ce-Time: 2026-08-28T20:13:22.197875444Z
Ce-Type: dev.chainguard.api.platform.registry.overlay_binding.deleted.v1
Content-Length: 120
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "uid": "The identifier of the deleted overlay binding"
  }
}

```

## Service: v2beta1 - OverlaysService

### Method: CreateOverlay

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/overlays
Ce-Specversion: 1.0
Ce-Subject: The identifier of this overlay
Ce-Time: 2026-08-28T20:13:22.194005211Z
Ce-Type: dev.chainguard.api.platform.registry.overlay.created.v1
Content-Length: 224
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "config": {
      "contents": {
        "packages": [
          "The APK package names this overlay adds"
        ]
      }
    },
    "name": "The unique name of the overlay",
    "uid": "The identifier of this overlay"
  }
}

```

### Method: DeleteOverlay

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/overlays
Ce-Specversion: 1.0
Ce-Subject: The identifier of the deleted overlay
Ce-Time: 2026-08-28T20:13:22.194221509Z
Ce-Type: dev.chainguard.api.platform.registry.overlay.deleted.v1
Content-Length: 112
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "uid": "The identifier of the deleted overlay"
  }
}

```

## Service: v2beta1 - ReposService

### Method: CreateRepo

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.183935777Z
Ce-Type: dev.chainguard.api.platform.registry.repo.created.v1
Content-Length: 243
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository",
    "name": "The name is the human-readable name of the repository",
    "sync_config": {
      "expiration": {},
      "source": "Repo ID to sync from"
    }
  }
}

```

### Method: UpdateRepo

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.18417653Z
Ce-Type: dev.chainguard.api.platform.registry.repo.updated.v1
Content-Length: 243
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository",
    "name": "The name is the human-readable name of the repository",
    "sync_config": {
      "expiration": {},
      "source": "Repo ID to sync from"
    }
  }
}

```

### Method: DeleteRepo

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.184355615Z
Ce-Type: dev.chainguard.api.platform.registry.repo.deleted.v1
Content-Length: 116
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository"
  }
}

```

### Method: UpdateRepoReadme

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/repos
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific repository
Ce-Time: 2026-08-28T20:13:22.184504582Z
Ce-Type: dev.chainguard.api.platform.registry.repo.updated.v1
Content-Length: 243
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific repository",
    "name": "The name is the human-readable name of the repository",
    "sync_config": {
      "expiration": {},
      "source": "Repo ID to sync from"
    }
  }
}

```

## Service: v2beta1 - RoleBindingsService

### Method: CreateRoleBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roleBindings
Ce-Specversion: 1.0
Ce-Subject: UIDP of the Role to bind
Ce-Time: 2026-08-28T20:13:22.180878478Z
Ce-Type: dev.chainguard.api.iam.rolebindings.created.v1
Content-Length: 261
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "parent": "The Group UIDP path under which the new RoleBinding resides",
    "role_binding": {
      "id": "UID of this role binding",
      "identity": "UID of the Identity to bind",
      "role": "UIDP of the Role to bind"
    }
  }
}

```

### Method: DeleteRoleBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roleBindings
Ce-Specversion: 1.0
Ce-Subject: UID of the record
Ce-Time: 2026-08-28T20:13:22.181073362Z
Ce-Type: dev.chainguard.api.iam.rolebindings.deleted.v1
Content-Length: 91
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UID of the record"
  }
}

```

### Method: BatchCreateRoleBindings

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roleBindings:batchCreate
Ce-Specversion: 1.0
Ce-Subject: UID of this role binding, under a parent group UIDP
Ce-Time: 2026-08-28T20:13:22.181259463Z
Ce-Type: dev.chainguard.api.iam.rolebindings.created.batch.v1
Content-Length: 220
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "role_bindings": [
      {
        "id": "UID of this role binding, under a parent group UIDP",
        "identity": "UID of the Identity to bind",
        "role": "UIDP of the Role to bind"
      }
    ]
  }
}

```

### Method: UpdateRoleBinding

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roleBindings
Ce-Specversion: 1.0
Ce-Subject: UID of this role binding
Ce-Time: 2026-08-28T20:13:22.181451979Z
Ce-Type: dev.chainguard.api.iam.rolebindings.updated.v1
Content-Length: 173
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "UID of this role binding",
    "identity": "UID of the Identity to bind",
    "role": "UIDP of the Role to bind"
  }
}

```

## Service: v2beta1 - RolesService

### Method: CreateRole

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roles
Ce-Specversion: 1.0
Ce-Subject: UIDP of the role under the group
Ce-Time: 2026-08-28T20:13:22.183331327Z
Ce-Type: dev.chainguard.api.iam.roles.created.v1
Content-Length: 159
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "role description",
    "name": "role name",
    "uid": "UIDP of the role under the group"
  }
}

```

### Method: UpdateRole

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roles
Ce-Specversion: 1.0
Ce-Subject: UIDP of the role under the group
Ce-Time: 2026-08-28T20:13:22.18354173Z
Ce-Type: dev.chainguard.api.iam.roles.updated.v1
Content-Length: 159
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "description": "role description",
    "name": "role name",
    "uid": "UIDP of the role under the group"
  }
}

```

### Method: DeleteRole

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/roles
Ce-Specversion: 1.0
Ce-Subject: UIDP of the role to delete
Ce-Time: 2026-08-28T20:13:22.183704376Z
Ce-Type: dev.chainguard.api.iam.roles.deleted.v1
Content-Length: 101
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "uid": "UIDP of the role to delete"
  }
}

```

## Service: v2beta1 - TagsService

### Method: CreateTag

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/tags
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific tag
Ce-Time: 2026-08-28T20:13:22.181662574Z
Ce-Type: dev.chainguard.api.platform.registry.tag.created.v1
Content-Length: 197
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "digest": "The digest of the manifest with this tag",
    "id": "The identifier of this specific tag",
    "name": "The unique name of the tag"
  }
}

```

### Method: DeleteTag

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/registry/v2beta1/tags
Ce-Specversion: 1.0
Ce-Subject: The identifier of this specific tag
Ce-Time: 2026-08-28T20:13:22.181855682Z
Ce-Type: dev.chainguard.api.platform.registry.tag.deleted.v1
Content-Length: 109
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "id": "The identifier of this specific tag"
  }
}

```

## Service: v2beta1 - TermsService

### Method: AcceptTerms

#### Example HTTP Headers

```
POST / HTTP/1.1
Host: console-api.enforce.dev
Accept-Encoding: gzip
Authorization: Bearer oidctoken
Ce-Audience: customer
Ce-Group: UID of parent group
Ce-Id: cloudevent generated UUID
Ce-Source: https://console-api.enforce.dev/iam/v2beta1/terms
Ce-Specversion: 1.0
Ce-Subject: Chainguard UIDP of the organization
Ce-Time: 2026-08-28T20:13:22.188574978Z
Ce-Type: dev.chainguard.api.iam.terms.accepted.v1
Content-Length: 159
Content-Type: application/json
User-Agent: Chainguard Enforce

```

#### Example HTTP Body

```json
{
  "actor": {
    "subject": "identity that triggered the event"
  },
  "body": {
    "document_ids": [
      "guardener-tos.v1",
      "sfdpa.v1"
    ],
    "group": "Chainguard UIDP of the organization"
  }
}

```
