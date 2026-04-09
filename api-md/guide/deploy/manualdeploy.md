---
title: 手动部署
hide_title: true
sidebar_position: 4
---

### 环境准备
  - 服务器配置要求
    - JuggleIM 对服务器配置并无强制要求，但建议采用 4C8G 的主机；
  - 操作系统要求
    - 主流Linux系统即可，如CentOS、Ununtu等；
  - 网络要求
    - 需要具备公网IP(纯内网使用除外)，并开放响应访问端口；

### 安装包下载

下载地址：[https://juggle.im/docs/guide/deploy/releasenodes/](https://juggle.im/docs/guide/deploy/releasenodes/)

```shell
#下载安装包
wget https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.6.tar.gz

#解压
tar -xvf juggleim-1.8.6.tar.gz
```

目录说明：
  - /conf     配置文件目录，其中包含一个配置文件示例；
  - /imserver   JuggleIM 可执行程序；
  - /sql         MySQL 初始化脚本；
  - /logs     日志输出目录；

### 依赖中间件安装

  - MySQL 安装 (必须)
    - 8.x及以上版本即可；
    - 安装过程，略；
    - 使用部署目录中sql文件夹下的文件初始化数据库；
  - MongoDB 安装(可选)
    - 略
  - Hbase安装(可选)
    - 略
  - Zookeeper安装(可选)
    - 略

### 配置文件说明

```yaml
# IM 集群的名字
clusterName: jim_cluster

# IM 节点的名字，务必保证每个节点的名字，集群中唯一
nodeName: jim_node_01

# 部署模式，single:单机模式；cluster:集群模式
clusterMod: single

# 本节点的内网IP和rpc监听端口
nodeHost: 127.0.0.1
nodePort: 8888

# 消息数据的存储引擎，枚举值：mysql/mongo/hbase
msgStoreEngine: mysql

# 集群模式下，需要zookeeper做节点注册和发现；单机模式可忽略此配置项
zookeeper:
  address: 127.0.0.1:2181

# 日志输出目录
log:
  logPath: ./logs
  logName: im-server

# （可选）内置时序数据库，用于可视化日志，数据统计等数据的临时存储
kvdb:
  isOpen: true
  dataPath: ./kvdb_data

# mysql 相关配置
mysql:
  user: db_user
  password: db_pwd
  address: mysql_host:3306
  name: jim_db

# (可选) mongodb相关配置，当msgStoreEngine为mongo时必须
mongodb:
  address: mongodb_host:27017
  name: db_name
  
# （可选）Hbase 相关配置，当msgStoreEngine为hbase时必须
hbase:
  address: hbase_host:2181

# IM长连接(websocket)监听端口，9002对内使用；9003对外使用，即9003需要开放到公网，供客户端sdk链接使用
connectManager:
  wsPort: 9002
  proxyPort: 9003

# IM 服务端API网关的监听端口
apiGateway:
  httpPort: 8082

# IM 管理后台的监听端口
adminGateway:
  httpPort: 8090
```

### 服务启动

在部署目录下，imserver可直接运行。如下图：

![start imserver](https://downloads.juggle.im/website/static/deploy/start.png)

### 导入App
JuggleIM是多租户系统，一套私有部署，可以创建多个数据相互隔离的App。创建App需要在官网后台申请授权License。步骤如下：

#### 1. 开发者后台，创建应用 （选择私有云）
![create app](https://downloads.juggle.im/website/static/deploy/createapp.png)

#### 2. 生成安装license
![create license](https://downloads.juggle.im/website/static/deploy/genlicense.png)

#### 3. 登录私有安装的IM的管理后台
JuggleIM 私有部署后，8090端口是管理后台地址，例如： http://127.0.0.1:8090,  默认账号密码： admin/123456
登录后台后，点击导入应用，填入license

![import license](https://downloads.juggle.im/website/static/deploy/importlic.png)

### 端口说明

| 端口 | 协议 |  说明  |
| ----:|:---:|:------|
|9003| websocket| IM 长连接地址，供客户端SDK建立长连接使用。如果器群部署的话，可以使用负载均衡做转发，对外暴露负载均衡的IP/域名|
|8082| http | IM 服务端API地址，供业务服务器调用。集群部署，同样需要负载均衡|
|8090| http | IM 管理后台地址，集群部署，需要负载均衡 |

### 消息存储引擎选择

JuggleIM的消息数据支持三种存储引擎(MySQL/MongoDB/Hbase)，这里分别介绍下三种存储引擎能应对的不同业务量(仅供参考)。

| 存储引擎| 适用场景|
|------:|:------|
|MySQL|1. 日消息量 10 亿条以下；2. 日活 3w 以下；|
|MongoDB | 1. 日消息量 100 亿条以下；2. 日活50w以下；|
|Hbase| 1. 日消息量 100亿条以上；2. 日活50w以上；|