---
title: 发送自定义消息
hide_title: true
sidebar_position: 4
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

**创建自定义消息**

自定义消息需要继承自 MessageContent，并实现下面的方法。

```java
public class CustomMessage extends MessageContent {
    //必须实现默认的构造方法，并指定 contentType。
    //contentType 是消息类型的标识符，请保证全局唯一性。
    //SDK 内部保留了 "jg:" 开头的所有标识符，您可以指定除此开头外的任意字符串。
    public CustomMessage() {
        mContentType = "my:custom";
    }

    //重写父类的 encode 方法，将消息内的所有字段转换成 json。
    @Override
    public byte[] encode() {
        JSONObject jsonObject = new JSONObject();
        try {
            if (!TextUtils.isEmpty(mValue)) {
                jsonObject.put("value", mValue);
            }
        } catch (JSONException e) {
            LoggerUtils.e("CustomMessage JSONException " + e.getMessage());
        }
        return jsonObject.toString().getBytes(StandardCharsets.UTF_8);
    }

    //重写父类的 decode 方法，将 json 转换成消息内的有效字段。
    @Override
    public void decode(byte[] data) {
        if (data == null) {
            LoggerUtils.e("CustomMessage decode data is null");
            return;
        }
        String jsonStr = new String(data, StandardCharsets.UTF_8);

        try {
            JSONObject jsonObject = new JSONObject(jsonStr);
            if (jsonObject.has("value")) {
                mValue = jsonObject.optString("value");
            }
        } catch (JSONException e) {
            LoggerUtils.e("CustomMessage decode JSONException " + e.getMessage());
        }
    }

    //会话列表中显示的消息摘要，非必要实现
    @Override
    public String conversationDigest() {
        if (!TextUtils.isEmpty(mValue)) {
            return mValue;
        }
        return "";
    }

    public void setValue(String value) {
      this.mValue = value;
    }

    private String mValue;
}

```


**注册自定义消息**

调用 SDK 的注册接口，使 SDK 在收发消息的时候，知道如何序列化和反序列化自定义消息。
注册接口调用一次即可。

```java
JIM.getInstance().getMessageManager().registerContentType(CustomMessage.class);
```

**发送自定义消息**

构造自定义消息对象，并调用 SDK 的 sendMessage 接口进行发送。

```java
CustomMessage c = new CustomMessage();
c.setValue("I am a custom message");
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
IMessageManager.ISendMessageCallback callback = new IMessageManager.ISendMessageCallback() {
    @Override
    public void onSuccess(Message message) {
        Log.i("TAG", "send message success");
    }

    @Override
    public void onError(Message message, int errorCode) {
        Log.i("TAG", "send message error, code is " + errorCode);
    }
};
Message message = JIM.getInstance().getMessageManager().sendMessage(c, conversation, callback);
Log.i("TAG", "after send, clientMsgNo is " + message.getClientMsgNo());

```

</TabItem>
<TabItem value="ios">

**创建自定义消息**

自定义消息需要继承自 MessageContent，并实现下面的方法。

```objectivec
@interface CustomMessage : JMessageContent
@property (nonatomic, copy) NSString *value;
@end

@implementation CustomMessage
//contentType 是消息类型的标识符，请保证全局唯一性。
//SDK 内部保留了 "jg:" 开头的所有标识符，您可以指定除此开头外的任意字符串。
+ (NSString *)contentType {
    return @"my:custom";
}

//重写父类的 encode 方法，将消息内的所有字段转换成 NSData。
- (NSData *)encode {
    NSDictionary * dic = @{@"value":self.value?:@""};
    NSData *data = [NSJSONSerialization dataWithJSONObject:dic options:kNilOptions error:nil];
    return data;
}

//重写父类的 decode 方法，将 NSData 转换成消息内的有效字段
- (void)decode:(NSData *)data {
    NSDictionary * json = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:nil];
    self.value = json["value"]?:@"";
}

//会话列表中显示的消息摘要，非必要实现
- (NSString *)conversationDigest {
    return self.content?:@"";
}

@end
```


**注册自定义消息**

调用 SDK 的注册接口，使 SDK 在收发消息的时候，知道如何序列化和反序列化自定义消息。
注册接口调用一次即可。

```objectivec
[JIM.shared.messageManager registerContentType:[CustomMessage class]];
```

**发送自定义消息**

构造自定义消息对象，并调用 SDK 的 sendMessage 接口进行发送。

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid2"];
CustomMessage *c = [[CustomMessage alloc] init];
c.value = @"This is a custom message";
JMessage *m = [JIM.shared.messageManager sendMessage:c
                                      inConversation:conversation
                                             success:^(long long clientMsgNo) {
        NSLog(@"sendMessage success");
    } error:^(JErrorCode errorCode, long long clientMsgNo) {
        NSLog(@"sendMessage error");
    }];
NSLog(@"after send, m.clientMsgNo is %lld", m.clientMsgNo);

```


</TabItem>
<TabItem value="js">

自定义消息支持的发送参数与 [发送消息](./send.md) 一致，区别在发送之前消息之前需要注册自定义消息，将消息是否计数和存储告知 SDK，自定义消息只需注册一次，可以放在 [SDK 初始化后](../../init.mdx) 执行注册代码

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.name                   | String  | 是     |        | 消息名称，根据实际需要发送不同消息类型，详细枚举请查看 [MessageType](../../../enum/web#message) | 1.0.0    |
| message.content                | Object  | 是     |        | 消息内容，构建 `message.name` 消息                              | 1.0.0    |
| message.mentionInfo            | Object  | 否     |  无    | conversationType 为 `GROUP` 时有效，设置 mentionInfo 表示本条消息是 @ 消息 | 1.0.0    |
| mentionInfo.mentionType        | Number  | 否     |  无    | @ 类型，详细可查看 [@ 消息枚举](../../../enum/web#mention) 说明         | 1.0.0    |
| mentionInfo.targetIds          | Array   | 否     |  无    | @ 指定人列表，SDK 会优先根据 mentionType 判断消息的 @ 类型         | 1.0.0    |

**成功回调**

| 名称      | 类型    | 描述                                                                      | 版本   |
|-----------|---------|---------------------------------------------------------------------------|--------|
| message   | Object  | 发送成功后返回带 `messageId` 和 `sentTime` 消息对象，消息结构请查看 [Message](../../../msg/message) | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| result | Object  | 发送失败后会返回对象中包含 `tid` 属性信息，同时包含 `error` 信息，可以直接查看 `error.msg`，或者查看 [状态码](../../../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

/** 第一步：注册自定义消息,全局注册一次 ***********/ 
let MSG_NAME = {
  TEST_MSG_NAME: 'test:msgname'
};
let msgs = [
  // isCount: 表示对方收到消息后会话是否未读数 +1
  // isStorage： 表示消息是否存入历史消息
  { name: MSG_NAME.TEST_MSG_NAME,  isCount: true, isStorage: true },
];
jim.registerMessage(msgs)

/** 第二步：发送自定消息 ***********/ 
let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  name: MSG_NAME.TEST_MSG_NAME,
  content: {
    // text 属性可根据多端实际约定自行定义
    text: 'Hello JIM'
  }
};
jim.sendMessage(msg).then((message) => {
  console.log(message);
}, (error) => {
   let { error, tid } = result;
  // 可根据 tid 修改消息发送失败的状态, Web 端消息失败仅在 SDK 内存中保存，刷新后将无法获取到发送失败的消息
  console.log(tid, error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

**创建自定义消息**

自定义消息需要继承自 MessageContent，并实现下面的方法。

```typescript
import JuggleIM from 'juggleim-rnsdk';

class CustomMessage implements CustomMessageContent {
  contentType = 'my:custom';
  value: string = '';

  //contentType 是消息类型的标识符，请保证全局唯一性。
  //SDK 内部保留了 "jg:" 开头的所有标识符，您可以指定除此开头外的任意字符串。

  //重写父类的 encode 方法，将消息内的所有字段转换成 json。
  encode(): string {
    const map = { "value": this.value };
    return JSON.stringify(map);
  }

  //重写父类的 decode 方法，将 json 转换成消息内的有效字段。
  decode(jsonStr: string): void {
    const map = JSON.parse(jsonStr);
    this.value = map['value'] || '';
  }
}
```


**注册自定义消息**

调用 SDK 的注册接口，使 SDK 在收发消息的时候，知道如何序列化和反序列化自定义消息。
注册接口调用一次即可。

```typescript
JuggleIM.registerCustomMessageType('my:custom', CustomMessage);
```

**发送自定义消息**

构造自定义消息对象，并调用 SDK 的 sendMessage 接口进行发送。

```typescript
const customMessage = new CustomMessage();
customMessage.value = 'This is value';

const conversation = {
  type: 1,
  id: 'userId1'
};

const callback = (message: any, errorCode: number) => {
  if (errorCode === 0) {
    console.log('sendMessage success, messageId is ' + message.messageId);
  } else {
    console.log('sendMessage error, errorCode is ' + errorCode.toString());
  }
};

JuggleIM.sendMessage({
  conversation: conversation,
  content: customMessage
}, callback);
```

</TabItem>
<TabItem value="flutter" label="Flutter">

**创建自定义消息**

自定义消息需要继承自 MessageContent，并实现下面的方法。

```dart
class CustomMessage extends MessageContent {
    String value = '';

    CustomMessage();

    //contentType 是消息类型的标识符，请保证全局唯一性。
    //SDK 内部保留了 "jg:" 开头的所有标识符，您可以指定除此开头外的任意字符串。
    @override
    String getContentType() {
        return "my:custom";
    }

    //重写父类的 encode 方法，将消息内的所有字段转换成 json。
    @override
    String encode() {
        Map map = {"value": value};
        return json.encode(map);
    }

    //重写父类的 decode 方法，将 json 转换成消息内的有效字段。
    @override
    void decode(String string) {
        Map map = json.decode(string);
        value = map['value'] ?? '';
    }
}

```


**注册自定义消息**

调用 SDK 的注册接口，使 SDK 在收发消息的时候，知道如何序列化和反序列化自定义消息。
注册接口调用一次即可。

```dart
JuggleIm.instance.registerMessageType(() => CustomMessage());
```

**发送自定义消息**

构造自定义消息对象，并调用 SDK 的 sendMessage 接口进行发送。

```java
CustomMessage c = CustomMessage();
c.value = 'This is value';
Conversation conversation = Conversation(ConversationType.private, 'groupId1');
DataCallback<Message> callback = (m, errorCode) {
  if (errorCode == 0) {
    print("sendMessage success, messageId is " + m.messageId);
  } else {
    print('sendMessage error, errorCode is ' + errorCode.toString() + ', clientMsgNo is ' + m.clientMsgNo!.toString());
  }
};

Message message = await JuggleIm.instance.sendMessage(c, conversation, callback);
```

</TabItem>
</Tabs>