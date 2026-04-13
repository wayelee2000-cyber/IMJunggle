---
title: Integrating with Vue
hide_title: true
sidebar_position: 1
---

### Use process{#flow}

![](../assets/flow.png)

### Step-by-step integration {#step}

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

Call the server-side API to obtain the token yourself, or in the Developer Backend, navigate to Application -> Development Tools -> API -> User Related, and call the user registration interface to obtain two test tokens.

![](../assets/token.png)

</TabItem>
<TabItem value="three">

1. Use the official `Vue` tool to create a project by running the following command step by step:

```shell
npm create vue@latest
```

![](./cmd.png)

2. Enter the project directory and install the `Web IM SDK`:

> Run `npm install jugglechat-websdk --save` in the project root directory.

</TabItem>
<TabItem value="four">

> 1. Copy and paste the code below into `App.vue`.

> 2. Run `npm run dev` in the project root directory.

<br/>

```html
<script setup>
import JIM from "jugglechat-websdk";

// Prepare basic information
let appkey = "Your AppKey";
let token = "Your Token";

// WebSocket domain or IP after private deployment
let serverList = [
  'https://demo.im.com',
  'http://demo.im.com',
  'http://10.23.31.111:8080',
];
// Step 1: Initialize the SDK; this only needs to be done once globally
let jim = JIM.init({ appkey, serverList: serverList });
let { Event, ConnectionState, ConversationType, MessageType } = JIM;

// Step 2: Set up status monitoring globally
jim.on(Event.STATE_CHANGED, ({ state, user }) => {
  if (ConnectionState.CONNECTING === state) {
    console.log("IM is connecting");
  }
  if (ConnectionState.CONNECTED === state) {
    // user => { id: 'xxx' }
    console.log("IM is connected", user);
  }
  if (ConnectionState.DISCONNECTED === state) {
    console.log("IM is disconnected");
  }
});

// Step 3: Set up message monitoring globally
jim.on(Event.MESSAGE_RECEIVED, message => {
  console.log(message);
});

// Step 4: Connect; this only needs to be called once globally. Message- and session-related interfaces can only be used after a successful connection.
jim.connect({ token }).then(
  result => {
    console.log(result);
  },
  error => {
    console.log(error);
  }
);
</script>

<template>
  <div class="container">Please open the browser console to view the results</div>
</template>

<style scoped>
.container {
  height: 200px;
  width: 600px;
  background-color: rgb(119, 128, 226);
  margin: auto 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
  font-weight: bold;
  border-radius: 10px;
}
</style>
```
:::danger Please be careful
The demo shows a successful connection. In an actual project, you can choose to use the JIM functions as needed according to the [Integration Document](../../../sdkintro/init/).
:::

</TabItem>
</Tabs>