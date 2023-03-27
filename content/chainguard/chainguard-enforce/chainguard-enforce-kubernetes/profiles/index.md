---
title: "Profiles"
type: "article"
description: "An overview of Chainguard Enforce's observer and enforcer profiles"
date: 2023-03-24T15:56:52-07:00
lastmod: 2023-03-24T15:56:52-07:00
draft: false
tags: ["ENFORCE", "CHAINCTL", "PRODUCT", "OVERVIEW"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 90
toc: true
---

When you install Chainguard Enforce, you have the option to specify a *profile* that will determine what permissions Chainguard Enforce has over your cluster. Currently, Enforce offers two specialized profiles: `enforcer` and `observer`.

The `observer` profile has less expansive permissions, making it useful for running Enforce in a read-only mode. The `enforcer` profile, on the other hand, has broader permissions that enable you to benefit from all of Chainguard Enforce's features, including policy distribution and enforcement.

This guide provides brief overviews of both the `observer` and `enforcer` profiles. It also outlines how to install Chainguard Enforce under each profile, as well as check what profile a given cluster is enrolled under.


## Enforcer Profile

`enforcer` is the default profile; if you install Chainguard Enforce without specifying a profile, the cluster will automatically be enrolled into the `enforcer` profile. 

```sh
chainctl cluster install
```

You can, however, specify that you want to install the `enforcer` profile by including the `--profiles=` option and passing it the `enforcer` value

```sh
chainctl cluster install --profiles=enforcer
```

Regardless of how you do so, when you enroll a cluster or other resource into the `enforcer` profile, it will also be enrolled into the `observer` profile. These profiles allow Chainguard Enforce to perform different actions, and the `enforcer` profile wouldn't be useful without the `observer` profile's scanning abilities. 

This means that when you enroll a cluster under `enforcer`, it will have all the same permissions as the `observer` profile along with a few more that give it broader access to a cluster, including the ability to enforce policies.


## Observer Profile

To enroll a cluster into Chainguard Enforce under the `observer` profile, include the `--profiles=` option followed by `observer`, as in the following example.

```sh
chainctl cluster install --profiles=observer
```

As its name suggests, the `observer` profile is essentially a "read-only" profile for Chainguard Enforce. When installed under the `observer` profile, Chainguard Enforce does not install an admission webhook onto the cluster. This means that Enforce will only be able to monitor the cluster and report violations; it won't be able to enforce policies or make any changes to your clusters. 

In some ways, the `observer` profile is similar to having [`warn` mode](../how-to-disable-policy-enforcement/) enabled. However, `warn` mode is set at the policy level. This means you can add `mode: warn` to certain policies, causing them to only return warnings, and leave it out of other policies that you want enforced. In contrast, the `observer` profile impacts the entire cluster; once you've installed Enforce onto a cluster under the `observer` profile, you won't be able to enforce any policy on the cluster.

Be aware that if you're setting up Chainguard Enforce to run both under the `observer` profile **and** in [agentless](../how-to-connect-kubernetes-clusters/#agentless-connections) mode, then Chainguard Enforce won't install anything on your cluster. In this case, Enforce will be able to `get`, `list`, and `watch` resources — excluding secrets — in order to scan what's running on the cluster, but it won't have permission to create anything on it.


## Checking profiles

You can check which profile a cluster is enrolled under with the `chainctl clusters ls` command.

```sh
chainctl clusters ls
```

This command returns a table listing your clusters. This example output lists three clusters enrolled into Chainguard Enforce under the same IAM group. 

```
                     NAME                     | GROUP  |               REMOTEID               | REGISTERED |   K8S VERSION    | AGENT VERSION | LAST SEEN |   ACTIVITY     
----------------------------------------------+--------+--------------------------------------+------------+------------------+---------------+-----------+----------------
  gke_cgacademy-project_us-central1_cluster-a | tester | 5d8c0797-0733-44f9-a321-ea3e3f26468f |       142m | v1.24.9-gke.3200 |       7e170b0 |        2s |   enforcer:2s  
                                              |        |                                      |            |                  |               |           | observer:117s  
  gke_cgacademy-project_us-central1_cluster-b | tester | a705b8d5-2313-48e3-8001-33e9a4e3b571 |       123m | v1.24.9-gke.3200 |       7e170b0 |        6s |   enforcer:6s  
                                              |        |                                      |            |                  |               |           |  observer:66s  
  gke_cgacademy-project_us-central1_cluster-c | tester | 78ba1a81-a2d7-4ea2-a11c-dbee4e9776d1 |       141m | v1.24.9-gke.3200 |       7e170b0 |       65s |  observer:65s  
```

The rightmost column, labeled `ACTIVITY`, indicates when a cluster's profiles were last seen as "active" by the agent. If a cluster is enrolled under the `enforcer` profile, both `enforcer` and `observer` will be listed in the `ACTIVITY` column. If a cluster is enrolled under `observer`, though, only `observer` will appear. The previous sample output shows that `cluster-a` and `cluster-b` are enrolled under both the `enforcer` and `observer` profiles, while `cluster-c` is enrolled solely under `observer`. 

You can also check the Chainguard Enforce Console to find what profiles your clusters are enrolled under. Navigate to the Console by going to [console.enforce.dev](https://console.enforce.dev) in your web browser. After signing in, there will be a table listing all of your clusters available to Chainguard Enforce.

![Screenshot of a portion of the Chainguard Enforce console, showing three rows representing three GKE clusters. The third column shows that the first and third clusters are enrolled in the enforcer and observer profiles, and the second cluster is only enrolled in the observer profile.](profiles_console.png)

The **Profiles** column lists the profiles that each cluster is enrolled in.


## Learn More

The `observer` profile can be useful for testing out Chainguard Enforce and understanding how it works. You can also test out Enforce on a per-policy basis with `warn` mode. Check out our documentation on [disabling policy enforcement](../how-to-disable-policy-enforcement/) to learn more.
