# **Changelog notifications proposal 1 pager**

**Your Name** [Dana Kleinerman](mailto:dana.kleinerman@chainguard.dev)  
Proposed Mar 23, 2026***\- DRAFT***   
**Approvers:** \<approver1@\> \[ \], \<approver2@\> \[ \]  
**Reviewers:**\<reviewer1@\>, \<reviewer2@\>

## Objective/Goals

Provide customers an easy way to stay up-to-date with changes and audit user access to ensure they are using the latest and securest images available. This would include both notifications about changes as well as the ability to query access data. 

More specifically, 

1. Changelist of anything new or updated within Chainguard, as well as actionable next steps  
   1. Notifications in console  
   2. Access to a changelog updates in UI and API (to connect to their own systems)  
2. Ability to audit specific activity within an org (which users in an org are using which features/images to better track usage patterns and also more easily determine who needs to switch to pulling more up-to-date images. Also useful for staying up-to-date with changes in activity and changes in roles )

Note that for this 1 pager, we’ll only focus on \#1 (Chainguard updates) and change usage/access auditing notifications for a later project.

## Problems To Solve

Today customers have difficulty discovering Chainguard updates that they need to be aware of (breaking changes, incidents, newly available images or image versions, changes in SBOMs, etc).

This can lead to poor outcomes where they are using out of date, vulnerable images, or missing privileged role escalations that might be indicative of bad actors. It can also lead to a diminished user experience that could lead to lower engagement, such as missing out on new features that become available. 

## User Scenarios

This is primarily useful for platform admin/engineers who need changelog information and auditing tooling to help them stay informed and ensure their org is up-to-date. 

From the March CAB, customers expressed interest in changelog notifications and audit history:

* API status call for new images. Could be integrated with internal MCP servers that are connected to open API docs and have some level of internal context  
* Notifications that address “staleness problem” could be really helpful 

## Requirements & Solution

**MVP requirements for Chainguard changelog notifications**  
Types of changes to include:

* High priority (no opting out; all admins have this turned on by default)  
  * Breaking changes  
  * Incidents  
  * KEVs  
  * CVEs   
  * Any other critical security issues that require immediate action  
* Medium priority (on by default, but admins can opt out)  
  * Updates to any image requests the user makes via the image priority request dashboard  
  * Deprecations  
  * EOL notifications  
  * Any changes to roles that are not breaking changes (e.g. adding permissions to existing roles. Would count removing permissions as a breaking change)  
* Low priority (on by default but easy to opt out. If we see most people opting out due to noise, we can change this to be opt in)  
  * New images that are available (outside of the ones the user requested)  
  * Version updates to existing images  
  * Changes in SBOMs  
  * New features

Surfaces:

* Console:  
  * New notifications center to show recent notifications (stored for no longer than a month to reduce noise)  
    * If users wish to track older notifications, they’ll either need to store them themselves using our API or refer to documentation, which should cover the majority of them  
  * New settings to modify what notifications the user receives   
  * Ability to subscribe to notifications with their email address  
* API/Feed:  
  * Provide a way to view notifications without going to console or setting up email. Could use an MCP server here.   
  * (Stretch?) Could we help users automate updates? So that human users don’t need to watch out for every change notification, and allow them to just focus on the critical ones.   
* Public Documentation  
  * All breaking changes, updates, new features, deprecations should be included in a version history documentation page that is publicly available.   
  * Take inspiration from [AWS whats new](https://aws.amazon.com/new/) or [Linear](https://linear.app/changelog). 

## Timeline & Gameplan

| Feature | Surface | Timeline |
| :---- | :---- | :---- |
| Public version history docs page | https://edu.chainguard.dev/chainguard/chainguard-images/ | ASAP but can run in parallel with other work |
| Support for Critical notifications | UI and email | Ideally End of Q1 |
| Support for Critical notifications | API/Feed  | Q2 |
| Support for medium priority notifications | All surfaces |  |
| Support for low priority notifications | All surfaces |  |

## Metrics

* Engagement funnel: Notifications seen \> notifications acted upon \> notifications dismissed/ignored  
* % interaction via UI versus API 

