---
title: One-click deployment
hide_title: true
sidebar_position: 3
---

JuggleIM provides a comprehensive private cloud installation tool. With this tool, you can quickly deploy an IM cluster, even without extensive server knowledge.

This document details the installation and deployment process for both the stand-alone and cluster versions of JuggleIM, enabling you to experience minute-level installation and foolproof operation.

### Create application{#create}
Log in to the [Developer Backend](https://console.juggle.im/login), click **Create Application**, select the appropriate package, and create a private cloud application.
![create an app.](https://downloads.juggle.im/website/static/deploy/createapp.png)

### Deployment and installation {#deploy}

#### Download and install the tool{#tool}

```shell
wget https://downloads.juggle.im/server/linux/amd64/juggleim.ctl
```

#### Generate and install License

![generate install license.](https://downloads.juggle.im/website/static/deploy/genlicense.png)

#### Install stand-alone version

1. Prepare a server with the following configuration requirements:

> Operating system: Linux is required; CentOS 7/8 or Ubuntu 18.04 are recommended;

> Hardware configuration: CPU with 4 cores, 8 GB memory, 200 GB disk space;

2. Log in to the server via SSH and run the following command to download the installation script:

```shell
wget https://downloads.juggle.im/server/linux/amd64/juggleim.ctl && sudo chmod u+x juggleim.ctl
```
![download juggleim.ctl](https://downloads.juggle.im/website/static/deploy/wgetctl.png)

3. Run the following command to install the service:

```shell
sudo ./juggleim.ctl install --license {INSTALL_LICENSE}
```

Execution screenshot:
![alt text](https://downloads.juggle.im/website/static/deploy/installing.png)

Screenshot after installation completes:

4. Log in to the private cloud management backend.

#### Install cluster version

1. Prepare servers with the same configuration requirements as the stand-alone version. For cluster deployment, at least 3 servers are required.

2. Log in to one of the servers and configure SSH permissions on the other hosts. Assume the following 3 servers:

| Hostname | IP Address     |   |
|:---------|:---------------|---|
| server1  | 172.16.111.152 |   |
| server2  | 172.16.111.153 |   |
| server3  | 172.16.111.154 |   |

1) Log in to server1 and generate SSH public and private keys by running:

```shell
sudo ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
```

Screenshot:
![generate rsa public/private key](https://downloads.juggle.im/website/static/deploy/idrsa.png)

2) Run the following command to append the public key to the authorized_keys file on all three machines:

```shell
sudo echo "sudo echo \"`cat ~/.ssh/id_rsa.pub`\" >> ~/.ssh/authorized_keys"
```

The output is as follows:
![alt text](https://downloads.juggle.im/website/static/deploy/publickey.png)

Execute this on server1:
![alt text](https://downloads.juggle.im/website/static/deploy/key_server1.png)

Execute this on server2:
![alt text](https://downloads.juggle.im/website/static/deploy/key_server2.png)

Execute this on server3:
![alt text](https://downloads.juggle.im/website/static/deploy/key_server3.png)

3. Log in to server1 to start the installation.

Download and install the tool:

```shell
wget https://downloads.juggle.im/server/linux/amd64/juggleim.ctl && sudo chmod u+x juggleim.ctl
```
![alt text](https://downloads.juggle.im/website/static/deploy/wgetctl2.png)

Start the installation:

```shell
sudo ./juggleim.ctl install --hosts "172.16.111.152,172.16.111.153,172.16.111.154" --license {INSTALL_LICENSE}
```
![alt text](https://downloads.juggle.im/website/static/deploy/cluster_installing.png)

Installation completed:

4. Overview of IM service default ports

| Port | Protocol Type | Description |
|------|---------------|-------------|
| 9003 | websocket     | Used to establish a persistent connection between the client SDK and the IM service. This address must be provided when initializing the SDK. |
| 8082 | http          | Server-side API listening port, used by the business server to obtain tokens, create groups, and perform other management operations. |
| 8090 | http          | IM service management backend address. Default account/password: admin/123456 |