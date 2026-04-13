---
title: deployment mode
hide_title: true
sidebar_position: 1
---

### Pattern introduction{#intro}

IM supports two deployment modes: **Hosted Cloud** and **Private Cloud**. Both modes offer the same IM capabilities, but differ in data storage, management backend, and billing models.

> **Choose the managed cloud model**: The managed cloud model provides official deployment services. After deployment, developers can begin integration following the documentation for each platform. There is no need to manage the deployment or maintenance of IM services. This option is ideal for developers who are generally not concerned about the physical location of their business data.

<br/>

> **Choose private cloud mode**: After creating an application in private cloud mode, you must first [deploy the IM service](../../download/server/deploy). Once deployment is complete, refer to the integration documentation for each platform to proceed. This option is suitable for developers who are _sensitive_ to the storage location of their business data and require more control.

### Function comparison{#feature}

| Service Name                      | Managed Cloud Deployment | Private Cloud Deployment |
|----------------------------------|--------------------------|-------------------------|
| Server resource provider          | IM official              | Developer               |
| Independent resource             | ✓                        | ✓                       |
| Independent management backend    | ✗                        | ✓                       |
| Number of registered users        | Unlimited                | Unlimited               |
| Single chat                      | ✓                        | ✓                       |
| Group chat                      | ✓                        | ✓                       |
| Chat Room                       | ✓                        | ✓                       |
| Historical message cloud storage  | ✓                        | ✓                       |
| Number of groups to join          | Unlimited                | Unlimited               |
| Maximum number of people in a single group | 3000           | 5000                    |
| REST API frequency limit          | 100 requests/second      | Unlimited               |
| Technical Support Group           | ✓                        | ✓                       |