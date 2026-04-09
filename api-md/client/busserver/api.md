---
title: 接口说明
hide_title: true
sidebar_position: 1
---

提供给客户端的App Server 接口，用于注册登录，群组创建，好友管理等业务功能


> 为了通信安全，API 通过自定义公共 [header](#header) 进行鉴权

### 格式说明{#api}

```js
https://$api/$version/$command
```
| 参数      | 名称         | 描述                                         |    |
|----------|--------------|---------------------------------------------|---|
| $api      | 请求域名       | 私有云部署服务后可获得请求地址  |  |
| $version  | 版本          | API 的版本号                                |   |
| $command  | 请求指令       | 具体的接口地址                               |   |


### 请求头{#header}

| 请求头      | 必填 | 描述                                 | 备注  |
|------------|------|--------------------------------------|------|
| appkey     | 是   | 应用的唯一标识 |      |
| Authorization  | 是   | 登录成功后，从返回值中获取 |      |

### 错误码枚举说明{#error_code}

说明：

- 业务接口通常返回 HTTP 200，具体成功/失败以响应体 `code` 为准。
- 下表为对外 API 可能返回的错误码，含义与“典型触发条件”均来自服务端源码逻辑梳理（`apis`/`services`/`commons/errs`）。

|code|常量名|含义|典型触发条件（从源码逻辑推导）|
|:--|:--|:--|:--|
|0|IMErrorCode_SUCCESS|成功|请求处理成功|
|1|IMErrorCode_PBILLEGAL|PB 解析失败（内部错误码）|内部使用（当前未发现通过 HTTP API 直接返回的路径）|
|2|IMErrorCode_DEFAULT|默认错误|通用兜底错误（当前未发现明确返回路径，更多场景使用 `APP_DEFAULT`）|
|17000|IMErrorCode_APP_DEFAULT|应用侧默认错误|通用内部错误兜底；常见于 DB 访问异常、二维码生成/查询异常等|
|17001|IMErrorCode_APP_APPKEY_REQUIRED|缺少 appkey|请求头未携带 `appkey`（`apis/validate.go`）|
|17002|IMErrorCode_APP_NOT_EXISTED|应用不存在/未配置|`appkey` 对应应用不存在；或服务端无法获取 IM SDK 实例（如登录/短信/邮箱/二维码相关接口）|
|17003|IMErrorCode_APP_REQ_BODY_ILLEGAL|请求体/参数非法|JSON 解析失败；必填字段缺失；或参数格式不合法（例如注册时 `account` 不匹配 `^[a-zA-Z0-9]{6,20}$`）|
|17004|IMErrorCode_APP_INTERNAL_TIMEOUT|内部服务超时/调用失败|服务端调用 IM Server 等外部依赖失败/超时（例如登录时向 IM Server 注册换取 `im_token`）|
|17005|IMErrorCode_APP_NOT_LOGIN|未登录/鉴权失败|需要鉴权的接口缺少 `Authorization`，或 token 解析/校验失败（`apis/validate.go`）；也可能在短信/邮箱登录流程中创建用户失败时返回|
|17006|IMErrorCode_APP_CONTINUE|继续轮询/未完成|二维码登录：二维码未被确认（`login.go` 中检查二维码状态为 Default）|
|17007|IMErrorCode_APP_QRCODE_EXPIRED|二维码过期|二维码创建时间超过 10 分钟（`login.go`）|
|17008|IMErrorCode_APP_SMS_SEND_FAILED|验证码发送失败|短信/邮箱验证码发送失败，或验证码记录落库失败（`services/smsservice.go`、`services/mailservice.go` 等）|
|17009|IMErrorCode_APP_SMS_CODE_EXPIRED|验证码无效/过期|验证码不存在、校验失败，或超过 5 分钟有效期（短信/邮箱均复用该错误码）|
|17010|IMErrorCode_APP_TRANS_NOTRANSENGINE|未配置翻译引擎|调用翻译接口但未配置可用翻译引擎（`services/transservice.go`）|
|17011|IMErrorCode_APP_USER_EXISTED|用户已存在|注册/设置账号等场景写入用户表冲突（例如账号已被占用）|
|17012|IMErrorCode_APP_USER_NOT_EXIST|用户不存在|按账号/手机号/邮箱/用户ID 查询不到用户（例如账号密码登录、修改密码、二维码登录已确认但用户不存在）|
|17013|IMErrorCode_APP_LOGIN_ERR_PASS|密码错误|密码校验失败（服务端对比 `SHA1(password)` 与数据库 `LoginPass`）|
|17014|IMErrorCode_APP_PHONE_EXISTED|手机号已存在|绑定/设置手机号时手机号已被占用（`services/userservice.go`）|
|17015|IMErrorCode_APP_EMAIL_EXIST|邮箱已存在|绑定/设置邮箱时邮箱已被占用（`services/userservice.go`）|
|17016|IMErrorCode_APP_Sensitive|包含敏感内容|用户昵称、群名称等文本命中敏感词（`services/userservice.go`、`services/groupservice.go`）|
|17100|IMErrorCode_APP_FRIEND_DEFAULT|好友默认错误|预留/暂未发现明确返回路径|
|17101|IMErrorCode_APP_FRIEND_APPLY_DECLINE|对方拒绝添加好友|对方“好友验证设置”为拒绝添加（`services/friendservice.go`）|
|17102|IMErrorCode_APP_FRIEND_APPLY_REPEATED|重复申请好友|预留/暂未发现明确返回路径|
|17103|IMErrorCode_APP_FRIEND_CONFIRM_EXPIRED|好友确认已过期|预留/暂未发现明确返回路径|
|17200|IMErrorCode_APP_GROUP_DEFAULT|群组默认错误|群组通用兜底错误；例如解散群时非群主或查询失败（`services/groupservice.go`）|
|17201|IMErrorCode_APP_GROUP_MEMBEREXISTED|群成员已存在|申请入群时已是群成员（`services/groupservice.go`）|
|17202|IMErrorCode_APP_GROUP_NORIGHT|无群操作权限|权限不足（例如消息/群管理相关逻辑中校验失败；`services/messageservice.go` 等）|
|17300|IMErrorCode_APP_ASSISTANT_PROMPT_DBERROR|助手提示词 DB 错误|预留/暂未发现明确返回路径|
|17401|IMErrorCode_APP_FILE_NOOSS|未配置对象存储|文件上传凭证：未配置 OSS/Minio/S3/Qiniu 等存储（`services/fileservice.go`）|
|17402|IMErrorCode_APP_FILE_SIGNERR|签名失败|文件上传凭证：生成预签名 URL 或签名失败（`services/fileservice.go`）|
|17500|IMErrorCode_APP_POST_DEFAULT|动态默认错误|动态/点赞等功能通用兜底错误（`posts/services/reactionservice.go` 等）|
|17501|IMErrorCode_APP_POST_NOTEXISTED|动态不存在|更新/评论/反应等操作时动态不存在（`posts/services/postservice.go`、`postcommentservice.go`）|
|17502|IMErrorCode_APP_POST_NORIGHT|无动态操作权限|更新/评论/反应等操作时非作者或无权限（`posts/services/postservice.go`、`postcommentservice.go`）|
