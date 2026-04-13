---
title: Send custom message
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

**Create a custom message**

Custom messages must inherit from `MessageContent` and implement the following methods.

```java
public class CustomMessage extends MessageContent {
    // The default constructor must be implemented and the contentType specified.
    // contentType is the identifier of the message type; please ensure global uniqueness.
    // All identifiers starting with "jg:" are reserved internally by the SDK, so you can specify any string except those.
    public CustomMessage() {
        mContentType = "my:custom";
    }

    // Override the encode method of the parent class to convert all fields in the message into JSON.
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

    // Override the decode method of the parent class to convert JSON into valid fields in the message.
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

    // Message summary displayed in the conversation list, optional implementation
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

**Register the custom message**

Call the SDK's registration interface so the SDK knows how to serialize and deserialize custom messages when sending and receiving them.  
You only need to call the registration interface once.

```java
JIM.getInstance().getMessageManager().registerContentType(CustomMessage.class);
```

**Send a custom message**

Create a custom message object and call the SDK's `sendMessage` interface to send it.

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

**Create a custom message**

Custom messages must inherit from `MessageContent` and implement the following methods.

```objectivec
@interface CustomMessage : JMessageContent
@property (nonatomic, copy) NSString *value;
@end

@implementation CustomMessage
// contentType is the identifier of the message type; please ensure global uniqueness.
// All identifiers starting with "jg:" are reserved internally by the SDK, so you can specify any string except those.
+ (NSString *)contentType {
    return @"my:custom";
}

// Override the encode method of the parent class to convert all fields in the message into NSData.
- (NSData *)encode {
    NSDictionary * dic = @{@"value":self.value ?: @""};
    NSData *data = [NSJSONSerialization dataWithJSONObject:dic options:kNilOptions error:nil];
    return data;
}

// Override the decode method of the parent class to convert NSData into valid fields in the message.
- (void)decode:(NSData *)data {
    NSDictionary * json = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:nil];
    self.value = json[@"value"] ?: @"";
}

// Message summary displayed in the conversation list, optional implementation
- (NSString *)conversationDigest {
    return self.content ?: @"";
}

@end
```

**Register the custom message**

Call the SDK's registration interface so the SDK knows how to serialize and deserialize custom messages when sending and receiving them.  
You only need to call the registration interface once.

```objectivec
[JIM.shared.messageManager registerContentType:[CustomMessage class]];
```

**Send a custom message**

Create a custom message object and call the SDK's `sendMessage` interface to send it.

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

The parameters supported by custom messages for sending are consistent with [Send Message](./send.md). The difference is that before sending a custom message, you need to register it and inform the SDK whether the message should be counted and stored.  
Custom messages only need to be registered once, and the registration code can be placed in [After SDK initialization](../../init.mdx).

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../../enum/web#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. When the session type is `PRIVATE`, the session ID is the userId of the receiver; when the session type is `GROUP`, it is the group ID | 1.0.0 |
| message.name | String | Yes | | Message name. Different message types are sent according to actual needs. For detailed enumeration, see [MessageType](../../../enum/web#message) | 1.0.0 |
| message.content | Object | Yes | | Message content, constructed according to the `message.name` message type | 1.0.0 |
| message.mentionInfo | Object | No | None | Valid when conversationType is `GROUP`. Setting mentionInfo indicates this message is an @ message | 1.0.0 |
| mentionInfo.mentionType | Number | No | None | @ type. See [@ message enumeration](../../../enum/web#mention) for details | 1.0.0 |
| mentionInfo.targetIds | Array | No | None | List of specified @ recipients. The SDK prioritizes the @ type of the message based on mentionType | 1.0.0 |

**Success callback**

| Name | Type | Description | Version |
|-----------|----------|-------------------------------------------------------------------------------|--------|
| message | Object | After successful sending, returns a message object with `messageId` and `sentTime`. See the message structure [Message](../../../msg/message) | 1.0.0 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| result | Object | After failure to send, the returned object contains `tid` and `error` information. You can view `error.msg` directly or refer to [status code](../../../status_code/web) | 1.0.0 |

**Sample Code**

```js
let { ConversationType } = JIM;

/** Step 1: Register a custom message globally ***********/
let MSG_NAME = {
  TEST_MSG_NAME: 'test:msgname'
};
let msgs = [
  // isCount: whether the session's unread count increases by 1 when the other party receives the message
  // isStorage: whether the message is stored in history
  { name: MSG_NAME.TEST_MSG_NAME,  isCount: true, isStorage: true },
];
jim.registerMessage(msgs);

/** Step 2: Send a custom message ***********/
let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  name: MSG_NAME.TEST_MSG_NAME,
  content: {
    // The text attribute can be defined according to actual multi-end conventions.
    text: 'Hello JIM'
  }
};
jim.sendMessage(msg).then((message) => {
  console.log(message);
}, (error) => {
  let { error, tid } = error;
  // You can handle message sending failure status based on tid. On the web, failed messages are only saved in SDK memory and will be lost after refreshing.
  console.log(tid, error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

**Create a custom message**

Custom messages must implement the `CustomMessageContent` interface and the following methods.

```typescript
import JuggleIM from 'juggleim-rnsdk';

class CustomMessage implements CustomMessageContent {
  contentType = 'my:custom';
  value: string = '';

  // contentType is the identifier of the message type; please ensure global uniqueness.
  // All identifiers starting with "jg:" are reserved internally by the SDK, so you can specify any string except those.

  // Override the encode method to convert all fields in the message into JSON.
  encode(): string {
    const map = { "value": this.value };
    return JSON.stringify(map);
  }

  // Override the decode method to convert JSON into valid fields in the message.
  decode(jsonStr: string): void {
    const map = JSON.parse(jsonStr);
    this.value = map['value'] || '';
  }
}
```

**Register the custom message**

Call the SDK's registration interface so the SDK knows how to serialize and deserialize custom messages when sending and receiving them.  
You only need to call the registration interface once.

```typescript
JuggleIM.registerCustomMessageType('my:custom', CustomMessage);
```

**Send a custom message**

Create a custom message object and call the SDK's `sendMessage` interface to send it.

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

**Create a custom message**

Custom messages must inherit from `MessageContent` and implement the following methods.

```dart
class CustomMessage extends MessageContent {
    String value = '';

    CustomMessage();

    // contentType is the identifier of the message type; please ensure global uniqueness.
    // All identifiers starting with "jg:" are reserved internally by the SDK, so you can specify any string except those.
    @override
    String getContentType() {
        return "my:custom";
    }

    // Override the encode method to convert all fields in the message into JSON.
    @override
    String encode() {
        Map map = {"value": value};
        return json.encode(map);
    }

    // Override the decode method to convert JSON into valid fields in the message.
    @override
    void decode(String string) {
        Map map = json.decode(string);
        value = map['value'] ?? '';
    }
}
```

**Register the custom message**

Call the SDK's registration interface so the SDK knows how to serialize and deserialize custom messages when sending and receiving them.  
You only need to call the registration interface once.

```dart
JuggleIm.instance.registerMessageType(() => CustomMessage());
```

**Send a custom message**

Create a custom message object and call the SDK's `sendMessage` interface to send it.

```dart
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