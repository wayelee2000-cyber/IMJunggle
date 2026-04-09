---
title: 直播聊天室
hide_title: true
sidebar_position: 4
---

### 场景介绍{#intro}

直播聊天室指 `直播社交` 中基于 IM 即时通讯进行互动沟通的场景，主要功能有发送弹幕消息、赠送礼物、点赞、实时查看在房间人数、榜单明细，聊天室支持十万级别的用户同时在线和百亿级别消息分发能力，面向不同领域的直播场景提供与房间同生命周期的数据存储空间，并且自带同步机制，例如同时在房人数、购物车等，便于开发者业务层灵活组合能力，轻松打造直播场景。

### 适用场景{#match}

> **游戏直播**：游戏平台针对手游或端游过程通过直播间分享给观众，并伴有游戏主播进行讲解或带玩，可以更好的烘托游戏氛围。

> **电商直播**：电商平台通过直播带货的形式售卖商品，主要包括线上主播 `上购物车链接`、`观众评论咨询` 和下单等功能。

> **赛事直播**：赛事直播通常体育赛事，例如：冬奥会、NBA、世界杯等，粉丝、球迷在线上一起观看直播，讨论赛事。

> **新闻直播**：新闻直播是有别于传统新闻播报的创新形式，通过应用客户端内进行直播，广大群众可在手机中观看新闻实时评论。

> **更多直播**：`语聊房`、`才艺直播`、`秀场直播`、`...`

### 方案特点{#sp}

>**灵活易用**：即来即走，用户可以自由加入退出房间进行互动。

>**全局广播**：向应用内单直播间、全部直播间广播发送热点消息。

>**性能高要求**：亿级消息并发高，直播间无人数上限。

>**房间数据一致性**：麦位管理、上架商品等操作与房间生命周期相同，信令秒级送达用户，前后端灵活控制。

>**房间状态实时更新**：房间人数、麦位状态、排行榜实时更新。

### 相关文档{#doc}

>**基础文档**：[SDK 下载](../../../client/import)、[集成示例](../../../client/quickstart/ios)

>**用户管理**：[用户注册](../../../server/user/register)、[更新信息](../../../server/user/updateuser)、[用户封禁](../../../server/user/addbanuser)、[禁言用户](../../../server/user/addblockuser)

>**消息相关**：[消息结构](../../../client/sdkintro/msg/message)、[发送消息](../../../client/sdkintro/message/msg_send/send)、[接收消息](../../../client/sdkintro/watcher/message)、[获取历史消息](../../../client/sdkintro/message/histories/get_all)、[清空历史消息](../../../client/sdkintro/message/histories/clear)、[消息撤回](../../../client/sdkintro/message/operator/recall)、[消息已读](../../../client/sdkintro/message/operator/read)、[REST API 发送消息](../../../server/message/privatemsg)

>**会话相关**：[会话结构](../../../client/sdkintro/conversation)、[获取会话列表](../../../client/sdkintro/conversation/get_all)、[会话置顶](../../../client/sdkintro/conversation/settop)、[免打扰](../../../client/sdkintro/conversation/disturb)、[获取未读总数](../../../client/sdkintro/conversation/get_total_unread)、[服务端获取会话列表](../../../server/convers/qryconvers)

>**状 态 码**：[Android 相关](../../../client/sdkintro/status_code/android)、[iOS 相关](../../../client/sdkintro/status_code/ios)、[Web 相关](../../../client/sdkintro/status_code/web)、[REST API 相关](../../../server/status)
