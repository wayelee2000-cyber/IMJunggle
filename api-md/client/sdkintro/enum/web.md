---
title: Web
hide_title: true
sidebar_position: 3
---

### 监听枚举{#listener}

| 名称                              | 说明                                   | 版本     |
|----------------------------------|----------------------------------------|----------|
| Event.STATE_CHANGED         | 连接状态监听，设置 [连接监听](../../watcher/connect) 会用到 | 1.0.0    |
| Event.MESSAGE_RECEIVED      | 消息接收监听，设置 [消息监听](../../watcher/message) 会用到 | 1.0.0    |
| Event.CONVERSATION_CHANGED  | 会话变更监听，设置 [会话监听](../../watcher/conversation) 会用到 | 1.0.0    |

### 连接枚举{#connection}

| 名称                              | 说明            | 版本     |
|----------------------------------|-----------------|----------|
| ConnectionState.CONNECTED            | 连接成功         | 1.0.0    |
| ConnectionState.CONNECTING           | 正在连接中       | 1.0.0    |
| ConnectionState.DISCONNECTED         | 连接已断开，提示连接断开后表示连接彻底断开，SDK 不会再进行任何和连接重试相关操作，开发者业务层提示连接断开即可       | 1.0.0    |
| ConnectionState.DB_OPENED            | 本地数据库已打开，仅 Electron 中有效       | 1.7.0    |
| ConnectionState.DB_CLOSED            | 本地数据库已关闭，仅 Electron 中有效       | 1.7.0    |
| ConnectionState.RECONNECTING         | SDK 内部正在重连中，SDK 默认 `30s` 发一个心跳包，连续 3 个心跳包未得到服务端响应会进行重连，或者单次请求(如：消息发送) `10s` 没有响应进行提示超时同时会进行尝试走重新连接逻辑，默认最多进行 `100` 次重连，时间间隔：`1s`、`2s`、`4s`、`8s`、`16s`、`...`        | 1.7.0    |

### 会话相关{#conversation}

| 名称                               | 说明                                      | 版本     |
|-----------------------------------|-------------------------------------------|----------|
| ConversationType.PRIVATE          | 单聊会话，两个人之间通信的会话类型          | 1.0.0    |
| ConversationType.GROUP            | 群聊会话，群组通信使用的会话类型            | 1.0.0    |
| ConversationType.CHATROOM         | 聊天室会话，类似直播间，有房间概念的通信场景使用会话类型 | 1.0.0    |
| ConversationOrder.FORWARD         | 会话获取方向，会话列表按时间倒序排列，获取更早的会话 | 1.0.0    |
| ConversationOrder.BACKWARD         | 会话获取方向，会话列表按时间倒序排列，获取更(四声)新的会话 | 1.0.0    |

### 消息相关{#message}

| 名称                           | 说明         | 版本     |
|-------------------------------|--------------|----------|
| MessageType.TEXT              | 文本消息      | 1.0.0    |
| MessageType.IMAGE             | 图片消息      | 1.0.0    |
| MessageType.VOICE             | 语音消息      | 1.0.0    |
| MessageType.VIDEO             | 小视频消息    | 1.0.0    |
| MessageType.FILE              | 文件消息      | 1.0.0    |
| MessageType.RECALL            | 撤回消息      | 1.0.0    |
| MessageType.READ_MSG           | 消息撤回通知  | 1.0.0    |
| MessageType.UPDATE_MSG         | 消息修改通知  | 1.0.0    |
| MessageOrder.FORWARD          | 获取更(四声)新的消息，消息页面向输入框方向滚动时使用 | 1.0.0    |
| MessageOrder.BACKWARD         | 获取更早的消息，消息页面向顶部滚动时使用 | 1.0.0    |


### 状态码枚举{#state}
| 名称                           | 说明         | 版本     |
|-------------------------------|--------------|----------|
| ErrorType              | 状态码枚举，具体说明请查看 [状态码](../../enum/web)      | 1.0.0    |

### @ 消息枚举{#mention}
| 名称                           | 说明         | 版本     |
|-------------------------------|--------------|----------|
| MentionType.ALL              | @ 所有人      | 1.0.0    |
| MentionType.SOMEONE          | @ 指定人      | 1.0.0    |
| MentionType.ALL_SOMEONE        | @所有人 + 指定人| 1.0.0    |

### 会话免打扰{#disturb}
| 名称                           | 说明                         | 版本     |
|-------------------------------|-----------------------------|----------|
| UndisturbType.DISTURB        | 免打扰                       | 1.0.0    |
| UndisturbType.UNDISTURB      | 取消免打扰                    | 1.0.0    |

### 会话标记状态{#unreadtag}
| 名称                           | 说明                         | 版本     |
|-------------------------------|-----------------------------|----------|
| UnreadTag.UNREAD      | 标记会话未读                   | 1.0.0    |

### 消息发送状态{#msg_sent}

| 名称                           | 说明         | 版本     |
|-------------------------------|--------------|----------|
| MESSAGE_SENT_STATE.NONE       | 初始状态      | 1.0.0    |
| MESSAGE_SENT_STATE.SENDING    | 消息发送中      | 1.0.0    |
| MESSAGE_SENT_STATE.SUCCESS    | 消息发送成功      | 1.0.0    |
| MESSAGE_SENT_STATE.FAILED     | 消息发送失败    | 1.0.0    |
| MESSAGE_SENT_STATE.UPLOADING  | 文件、图片等消息上传中      | 1.0.0    |

### @ 消息获取方向{#mention_order}
| 名称                           | 说明                         | 版本     |
|-------------------------------|-----------------------------|----------|
| MENTION_ORDER.BACKWARD         | 获取更早的消息，消息页面向顶部滚动时使用      | 1.0.0    |
| MENTION_ORDER.FORWARD          | 获取更(四声)新的消息，消息页面向输入框方向滚动时使用      | 1.0.0    |

### 朋友圈获取方向{#moment_order}
| 名称                           | 说明                         | 版本     |
|-------------------------------|-----------------------------|----------|
| MOMENT_ORDER.ASC         | 获取更早的朋友圈      | 1.9.6    |
| MOMENT_ORDER.DESC          | 获取更(四声)新的朋友圈      | 1.9.6    |

### 朋友圈类型枚举{#moment_type}
| 名称                           | 说明                         | 版本     |
|-------------------------------|-----------------------------|----------|
| MOMENT_TYPE.IMAGE         | 图片类型      | 1.9.6    |
| MOMENT_TYPE.VIDEO         | 视频类型      | 1.9.6    |

### 评论获取方向{#comment_order}
| 名称                           | 说明                         | 版本     |
|-------------------------------|-----------------------------|----------|
| COMMENT_ORDER.ASC         | 获取更早的评论      | 1.9.6    |
| COMMENT_ORDER.DESC          | 获取更(四声)新的评论      | 1.9.6    |

