---
title: Introducing Integration via Script
hide_title: true
sidebar_position: 1
---

### Use process{#flow}

![](../assets/flow.png)

### Step-by-step Integration {#step}

<Tabs
groupId="sdks-language"
values={[
{ label: 'Step 1', value: 'one', },
{ label: 'Step 2', value: 'two', },
{ label: 'Step 3', value: 'three', },
{ label: 'Step 4', value: 'four', },
]}
>
<TabItem value="one">

Create an application in the `Developer Backend` to obtain your `AppKey` and `Secret`.

![](../assets/appkey_secret.png)

</TabItem>
<TabItem value="two">

Call the server-side API to obtain the token yourself, or in the Developer Backend, navigate to Select Application → Development Tools → API → User Related, and call the user registration interface to obtain two test tokens.

![](../assets/token.png)

</TabItem>
<TabItem value="three">

Download the JavaScript SDK.

</TabItem>
<TabItem value="four">

> 1. Create a new `HTML` file and name it `demo.html`.

> 2. Download [juggleim-dev-1.9.0.zip](./juggleim-dev-1.9.0.zip) and place `juggleim-dev-1.9.0.js` in the same directory as `demo.html`.

> 3. Copy and paste the code below into `demo.html`.

> 4. Open `demo.html` in the Chrome browser to preview the result.

<br/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>IM</title>
  <script src="./juggleim-dev-1.9.0.js"></script>
  <style>
    .container {
      height: 200px;
      width: 600px;
      background-color: rgb(119, 128, 226);
      margin: 200px auto;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 40px;
      font-weight: bold;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div class="container">Please open the browser console to view the results</div>
  <script>
    // Prepare basic information
    let appkey = 'Your AppKey';
    let token = 'Your Token';
    // WebSocket domain or IP after privatized deployment
    let serverList = [
      'https://demo.im.com',
      'http://demo.im.com',
      'http://10.23.31.111:8080',
    ];

    // Step 1: Initialize SDK; only needs to be done once globally
    let jim = JuggleIM.init({ appkey, serverList });
    let { Event, ConnectionState, ConversationType, MessageType } = JIM;

    // Step 2: Set up status monitoring; only needs to be done once globally
    jim.on(Event.STATE_CHANGED, ({ state, user }) => {
      if (ConnectionState.CONNECTING === state) {
        console.log('IM is connecting');
      }
      if (ConnectionState.CONNECTED === state) {
        // user => { id: 'xxx' }
        console.log('IM is connected', user);
      }
      if (ConnectionState.DISCONNECTED === state) {
        console.log('IM is disconnected');
      }
    });

    // Step 3: Set up message monitoring; only needs to be done once globally
    jim.on(Event.MESSAGE_RECEIVED, (message) => {
      console.log(message);
    });

    // Step 4: Connect; only needs to be called once globally. Message- and session-related interfaces can only be called after a successful connection.
    jim.connect({ token }).then(
      (result) => {
        console.log(result);
      },
      (error) => {
        console.log(error);
      }
    );
  </script>
</body>
</html>
```

:::danger Please be careful
The demo shows a successful connection. In an actual project, you can choose to use the JIM functions as needed according to the [Integration Document](../../../sdkintro/init/).
:::

</TabItem>
</Tabs>