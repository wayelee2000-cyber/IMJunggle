---
title: 系统通知
hide_title: true
sidebar_position: 3
---

### 场景介绍{#intro}

系统通知是 IM 产品中对服务端单向给用户推送消息的统称，`系统通知` 和 `单聊` 都是双方通信，区别在于单聊是支持互相发送消息，系统通知只能由服务端 API 发送消息，终端用户只能接收消息，支持发送文本、图片、语音、文件和自定义消息。

### 适用场景{#match}

> **官方号**：应用内以官网账号的形式进行广播推送官方活动、运营策略、版本更新等通知，是官方和终端用户之间的沟通媒介。

> **运营活动通知**：用于应用组织临时性运营活动通知，配合按标签分类进行通知、在线用户接收通知等特色功能，精准推送消息。

> **应用全员广播**：向应用内全部用户发送消息，内容可以根据用户画像进行动态调整，消息通知领域的 “千人千面”，精细化运营有力工具。

### 方案特点{#sp}

> **时效高数量大**：运营活动通常有时效性要求，一定要在最短时间内将通知消息广播给全员，对系统通知服务 API QPS 要求高。

> **通知灵活多变**：为了精细化运营，通知消息会有 ”千人千面“ 的精准化通知，对于 IM 系统通知平台的灵活性有一定要求

### 相关文档{#doc}

>**基础文档**：[SDK 下载](../../../client/import)、[集成示例](../../../client/quickstart/ios)

>**用户管理**：[用户注册](../../../server/user/register)、[更新信息](../../../server/user/updateuser)、[用户封禁](../../../server/user/addbanuser)、[禁言用户](../../../server/user/addblockuser)

>**系统通知**：[系统通知消息](../../../server/message/sysmsg)、[全员广播消息](../../../server/message/broadcastmsg)

>**会话相关**：[会话结构](../../../client/sdkintro/conversation)、[获取会话列表](../../../client/sdkintro/conversation/get_all)、[会话置顶](../../../client/sdkintro/conversation/settop)、[免打扰](../../../client/sdkintro/conversation/disturb)、[获取未读总数](../../../client/sdkintro/conversation/get_total_unread)、[服务端获取会话列表](../../../server/convers/qryconvers)

>**状 态 码**：[Android 相关](../../../client/sdkintro/status_code/android)、[iOS 相关](../../../client/sdkintro/status_code/ios)、[Web 相关](../../../client/sdkintro/status_code/web)、[REST API 相关](../../../server/status)
