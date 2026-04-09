---
title: 发送文件
hide_title: true
sidebar_position: 3
---

### 前期准备{#pre}

发送文件消息、图片消息、视频消息、语音消息都需要用到文件上传，示例以文件消息举例，用法类似只需要替换发送消息方法和入参即可

1、在 `开发者后台` 创建应用获取 `AppKey` 和 `Secret`。

![](../assets/appkey_secret.png)

2、自己调用服务端 API 获取 Token 或在开发者后台的 -> 选择应用-> 开发工具 -> API -> 用户相关中，调用用户注册接口，获取两个测试 Token。

![](../assets/token.png)

3、下载最新版本 `JavaScript SDK`

4、下载云厂商文件上传 SDK，[七牛 SDK](https://developer.qiniu.com/kodo/1283/javascript)、[阿里 OSS](https://www.alibabacloud.com/help/zh/oss/user-guide/upload-a-file-using-a-file-url?spm=a2c63.p38356.0.0.55571f10Ci0gEp#392d9bf073h38) 下文以七牛为例

5、在开发者后台设置云存储类型，如果使用阿里 OSS，请在阿里云后台 **设置允许 Web 端跨域**

![](../assets/storage.png)

6、根据集成文档逐步集成。

### 使用流程{#flow}

> 1、引入 IM Web SDK

> 2、引入 qiniu JS SDK

> 3、初始化配置上传组件

> 4、连接成功

> 5、发送文件消息

### 示例代码{#code}

为了方便演示，示例代码中包含官方测试 AppKey 和 Token，测试完成后请替换为开发者的 AppKey 和 Token。

> 1、新建 `HTML` 文件，命名为 `demo.html`

> 2、下载 [juggleim-dev-1.9.0.zip](./juggleim-dev-1.9.0.zip) , 将 `juggleim-dev-1.9.0.js` 放在 `demo.html` **同级目录**

> 3、将 [qiniu.min.js](https://developer.qiniu.com/kodo/1283/javascript) 放在 `demo.html` **同级目录**

> 4、将下方代码复制粘贴到 `demo.html`

> 4、使用 Chrome 浏览器打开 `demo.html` 预览效果

<br/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JIM</title>
  <script src="./jim-[version].js"></script>
  <script src="./qiniu.min.js"></script>
  <style>
    .container {
      height: 200px;
      width: 600px;
      background-color: rgb(119, 128, 226);
      margin: 200px auto;
      font-size: 30px;
      font-weight: bold;
      border-radius: 10px;
      padding: 4rem;
      box-sizing: border-box;
    }

    .input {
      display: none;
      width: 100%;
    }
  </style>
</head>

<body>
  <div class="container">
    <div>请打开浏览器控制台查看结果</div>
    <input type="file" id="file" class="input" />
    <div>
      <span id="percent">0</span>
      <span>%</span>
    </div>
  </div>
  <script>

    let fileNode = document.querySelector('#file');
    let percentNode = document.querySelector('#percent');

    // 准备基础信息
    let appkey = 'Your AppKey';
    let token = 'Your Token';
    let userId = '与 Token 对应的 userId' 
    // 私有化部署后的 WebSocket 域名或 IP
    let serverList = [
      'https://demo.im.com',
      'http://demo.im.com',
      'http://10.23.31.111:8080',
    ];

    /*
      初始化七牛文件存储
      let jim = JIM.init({ appkey, upload: qiniu });
    */

    /* 
      初始化阿里文件存储: OSS 通过引入阿里上传 JS SDK 获得 https://gosspublic.alicdn.com/aliyun-oss-sdk-6.18.0.min.js
      let jim = JIM.init({ appkey, upload: OSS });
    */

    /* 
      初始化 AWS 文件存储: S3Client 通过引入 AWS JS SDK 获得 https://www.npmjs.com/package/@aws-sdk/client-s3
      import { S3Client } from "@aws-sdk/client-s3";
      let jim = JIM.init({ appkey, upload: S3Client });
    */

    //  步骤 1: 初始化 SDK, 全局只需初始化一次, 以七牛为例 
    let jim = JuggleIM.init({ appkey, serverList, upload: qiniu });
    let { Event, ConnectionState, ConversationType, MessageType } = JIM;

    // 步骤 2: 设置状态监听，全局只需设置一次
    jim.on(Event.STATE_CHANGED, ({ state, user }) => {
      if (ConnectionState.CONNECTING == state) {
        console.log('im is connecting');
      }
      if (ConnectionState.CONNECTED == state) {
        // user => { id: 'xxx' }
        console.log('im is connected', user);
      }
      if (ConnectionState.DISCONNECTED == state) {
        console.log('im is disconnected');
      }
    });

    // 步骤 3: 设置消息监听，全局只需设置一次
    jim.on(Event.MESSAGE_RECEIVED, (message) => {
      console.log(message);
    });

    // 步骤 4: 连接，全局只需调用一次，消息相关、会话相关接口必须连接成功后才可调用
    jim.connect({ token, userId }).then((user) => {
      fileNode.style = "display: block;";
      fileNode.onchange = sendFile
    }, (error) => {
      console.log(error)
    });

    function sendFile(e) {
      let file = e.target.files[0];
      let message = {
        conversationType: ConversationType.PRIVATE,
        conversationId: 'userid2',
        content: {
          file: file,
          name: file.name,
          type: file.type
        },
        /*
        自定义属性: 按需使用, 自定义属性会在文件上传进度 onprogress 和消息发送成功后 msg 对象中返回
        使用的场景: 发送文件消息时可自定义 tid，然后将消息渲染到页面，通过 onprogress 中返回的 
                  message.tid 更新进度条
        */
        tid: `tid_${Date.now()}`
      };

      jim.sendFileMessage(message, {
        onprogress: ({ percent, message }) => {
          console.log(`${percent}%`, message);
          percentNode.innerHTML = percent;
        }
      }).then((msg) => {
        console.log('send file message successfully', msg)
        e.value = '';
      }, (error) => {
        console.log(error)
      });
    }
  </script>
</body>
</html>
```

:::danger 要注意哦
Demo 里展示到连接成功，在实际项目中可根据 [集成文档](../../../sdkintro/init/) 按需选择使用 JIM 功能
:::
