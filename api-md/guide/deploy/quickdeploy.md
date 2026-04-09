---
title: 一键部署
hide_title: true
sidebar_position: 3
---

JuggleIM 提供完善的私有云安装工具，借助这个工具，你将能快速的部署一套IM集群，即便你对服务器相关知识并不十分了解。

这个文档将为你详细的展示 JuggleIM 单机和集群版的安装部署过程，带你体验分钟级安装和傻瓜式操作。

### 创建应用{#create}
登录 [开发者后台](https://console.juggle.im/login)，点击创建应用，选择合适的套餐，创建一个私有云应用。
![create an app.](https://downloads.juggle.im/website/static/deploy/createapp.png)

### 部署安装{#deploy}

#### 下载安装工具{#tool}

```shell
wget https://downloads.juggle.im/server/linux/amd64/juggleim.ctl
```

#### 生成安装License

![generate install license.](https://downloads.juggle.im/website/static/deploy/genlicense.png)

#### 安装单机版

1. 准备好一台服务器，配置要求：

> 操作系统：要求Linux操作系统，推荐 CentOS 7/8 或 Ubuntu 18.04；

> 硬件配置：CPU 4 核，内存 8G，磁盘 200G；

2. ssh 登录到这台机器上，执行如下命令，下载安装脚本。

```shell
wget https://downloads.juggle.im/server/linux/amd64/juggleim.ctl  && sudo chmod u+x juggleim.ctl
```
![download juggleim.ctl](https://downloads.juggle.im/website/static/deploy/wgetctl.png)

3. 执行如下命令，安装服务

```shell
sudo ./juggleim.ctl install  --license  {INSTALL_LICENSE}
```

执行截图：
![alt text](https://downloads.juggle.im/website/static/deploy/installing.png)

安装完成截图：

3. 登入私有云管理后台

#### 安装集群版

1. 服务器准备，配置与单机版要求相同，集群版部署，至少需要准备 3 台服务器；

2. 登录其中一台服务器，配置其对其余主机的 ssh 权限；假设有如下 3 台服务器：

|主机名|IP||
|:--|:------|:--|
|server1 | 172.16.111.152 | |
|server2 | 172.16.111.153 | |
|server3 | 172.16.111.154 | |

1) 登录 server1，执行如下命令，生成 ssh 公私钥：

```shell
sudo ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
```

如图：
![generate rsa public/private key](https://downloads.juggle.im/website/static/deploy/idrsa.png)

2) 执行如下命令，将输出分别在三台机器上执行；
```shell
sudo echo "sudo echo \"`cat ~/.ssh/id_rsa.pub`\" >> ~/.ssh/authorized_keys"
```
输出如下：
![alt text](https://downloads.juggle.im/website/static/deploy/publickey.png)

在server1上执行：
![alt text](https://downloads.juggle.im/website/static/deploy/key_server1.png)

在server2上执行：
![alt text](https://downloads.juggle.im/website/static/deploy/key_server2.png)

在server3上执行：
![alt text](https://downloads.juggle.im/website/static/deploy/key_server3.png)

3. 登录到 server1 开始安装；

下载安装工具：
```shell
wget https://downloads.juggle.im/server/linux/amd64/juggleim.ctl  && sudo chmod u+x juggleim.ctl
```
![alt text](https://downloads.juggle.im/website/static/deploy/wgetctl2.png)

开始安装:
```shell
sudo ./juggleim.ctl install --hosts "172.16.111.152,172.16.111.153,172.16.111.154" -license {INSTALL_LICENSE}
```
![alt text](https://downloads.juggle.im/website/static/deploy/cluster_installing.png)

安装完成：

4. IM服务默认端口介绍

|           端口         |       协议类型         |      说明      | 
|-----------------------|----------------------|----------------|
|    9003               |   websocket          | 用于客户端 SDK 与 IM 服务建立长连接，SDK 初始化时需传入这个地址|
|    8082               |   http               | 服务端 API 监听端口，由业务服务器调用获取Token，创建群组等管理类操作；|
|    8090               |   http               | IM 服务管理后台地址，默认账号/密码：admin/123456         |