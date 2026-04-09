---
title: 入群申请列表
hide_title: true
sidebar_position: 8
---
### 功能说明{#intro}

入群申请列表，包含主动申请入群和邀请入群的

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/grpapplications

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|是|群组id||
|start|int|否|查询列表的开始时间戳，倒序查询时，默认从当前时间开始；正序查询时，默认从0开始||
|count|int|否|单页数量，默认20，最大不超过50||
|order|int|否|查询顺序。0：倒序；1：正序；默认0||


### 请求示例{#req_demo}
``` js
GET /jim/groups/grpapplications?group_id=group1&start=1734407505753&count=50 HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
        {
            "apply_type":1,   //0:邀请；1:主动申请；
            "sponsor":{  //主动申请入群时，申请人信息
              "user_id":"userid1"
            },
            "inviter":{  //邀请入群时，邀请人信息
              "user_id":"userid2"
            },
            "recipient":{  //邀请入群时，被邀请人信息
              "user_id":"userid3"
            },
            "operator":{   //处理请求的管理员信息
              "user_id":"userid4"
            },
            "status":1,    // 0：申请中；1：同意申请；2：拒绝申请；3：申请已过期; 10：邀请中；11：同意邀请；12：拒绝邀请；13：邀请已过期；
            "apply_time":1734407505000   //申请发起时间
        }
    ]
  }
}
```