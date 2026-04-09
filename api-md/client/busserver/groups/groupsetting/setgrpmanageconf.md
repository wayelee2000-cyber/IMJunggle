---
title: 设置群配置
hide_title: true
sidebar_position: 9
---
### 功能说明{#intro}

设置群维度的一些管理配置

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/management/set

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|group_edit_msg_right|int|否|0：无权限；1：群主；2:管理员；3：群主+管理员；4：群成员；5：群主+群成员；6：管理员+群成员；7：群主+管理员+群成员||
|group_add_member_right|int|否|0：无权限；1：群主；2:管理员；3：群主+管理员；4：群成员；5：群主+群成员；6：管理员+群成员；7：群主+管理员+群成员||
|group_mention_all_right|int|否|0：无权限；1：群主；2:管理员；3：群主+管理员；4：群成员；5：群主+群成员；6：管理员+群成员；7：群主+管理员+群成员||
|group_top_msg_right|int|否|0：无权限；1：群主；2:管理员；3：群主+管理员；4：群成员；5：群主+群成员；6：管理员+群成员；7：群主+管理员+群成员||
|group_send_msg_right|int|否|0：无权限；1：群主；2:管理员；3：群主+管理员；4：群成员；5：群主+群成员；6：管理员+群成员；7：群主+管理员+群成员||
|group_set_msg_life_right|int|否|0：无权限；1：群主；2:管理员；3：群主+管理员；4：群成员；5：群主+群成员；6：管理员+群成员；7：群主+管理员+群成员||

### 请求示例{#req_demo}
``` js
POST /jim/groups/management/set HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id":"groupid1",
  "group_edit_msg_right":7,
  "group_add_member_right":7,
  "group_mention_all_right":7,
  "group_top_msg_right":7,
  "group_send_msg_right":7,
  "group_set_msg_life_right":7
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|