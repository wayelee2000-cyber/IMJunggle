---
title: 多人群聊
hide_title: true
sidebar_position: 2
---

### 场景介绍{#intro}

群聊通常指两个人以上在一个组里沟通交流，相互之间通过文本、文件、图片、语音互动，群聊互动消息的硬指标是不丢、不重、不乱序，换设备后消息备份能自动同步至新设备，群内每条消息的 `已读状态`、`已读占比`、`未读数量`、`@ 消息`、`消息操作` 等要求一个用户的多个设备严格一致，消息操作例如 `撤回撤回`、`消息修改`、`回复消息`。

### 适用场景{#match}

> **粉丝群**：粉丝群通常依托于有 `KOL` 社交应用中，有粉丝和主播互动，为了经营私域将粉丝拉到一个群组里进行沟通交流。

> **车友群**：车友群是汽车论坛或汽车主机厂面向同品牌、同系列车组织的多人聊天，车友群多以沟通汽车行业资讯、车型优劣等。

> **家长群**：家长群通常是学校老师将班级内学生家长组建一个群组，用于同步学生学习情况或告知学校的最新政策等。

> **公司群**：公司群通常是包含公司全员的群组，为了及时同步公司政策，例如：假期安排、福利同步等建立的沟通群组。

> **熟人群聊**：熟人群聊通常和熟人私信是同时存在，用户添加好友后可以将好友拉到一个群组中进行互动交流。

> **等多场景**：`班级群`、`部门群`、`售后群`、`外卖群`、`支持群`、`客户群`、`智慧群`、`...`

### 方案特点{#sp}

> **入群验证**：邀请用户进群、人数过多时被邀请用户主动确认进群群组。

> **人数上限**：根据群组场景不同，群组人数可配置，低至 10 人以内群组，高至万人群。

> **群组信息更新**：群昵称变更通知机制，在线成员实时更新，不在线用户上线自动同步。

> **特殊行为通知**：成员禁言同步，及时提示禁言状态。

> **群组 “功能糖”**：查看群消息阅读状态、群发助手、消息单双向删除、定时清空消息、按时间删除消息。

> **消息绑定群组信息**：消息中包含群组的信息，便于客户端展示，降低集成复杂度。

### 相关文档{#doc}

>**基础文档**：[SDK 下载](../../../client/import)、[集成示例](../../../client/quickstart/ios)

>**用户管理**：[用户注册](../../../server/user/register)、[更新信息](../../../server/user/updateuser)、[用户封禁](../../../server/user/addbanuser)、[禁言用户](../../../server/user/addblockuser)

> **群组相关**：[创建群组](../../../server/group/groupcreate)、[解散群组](../../../server/group/groupdissolve)、[更新群组信息](../../../server/group/updategroup)、[添加群成员](../../../server/group/groupaddmember)、[群组禁言](../../../server/group/groupmute)、[查询群成员](../../../server/group/qrygroupmember)

>**消息相关**：[消息结构](../../../client/sdkintro/msg/message)、[发送消息](../../../client/sdkintro/message/msg_send/send)、[接收消息](../../../client/sdkintro/watcher/message)、[获取历史消息](../../../client/sdkintro/message/histories/get_all)、[清空历史消息](../../../client/sdkintro/message/histories/clear)、[消息撤回](../../../client/sdkintro/message/operator/recall)、[消息已读](../../../client/sdkintro/message/operator/read)、[REST API 发送消息](../../../server/message/privatemsg)

>**会话相关**：[会话结构](../../../client/sdkintro/conversation)、[获取会话列表](../../../client/sdkintro/conversation/get_all)、[会话置顶](../../../client/sdkintro/conversation/settop)、[免打扰](../../../client/sdkintro/conversation/disturb)、[获取未读总数](../../../client/sdkintro/conversation/get_total_unread)、[服务端获取会话列表](../../../server/convers/qryconvers)

>**状 态 码**：[Android 相关](../../../client/sdkintro/status_code/android)、[iOS 相关](../../../client/sdkintro/status_code/ios)、[Web 相关](../../../client/sdkintro/status_code/web)、[REST API 相关](../../../server/status)
