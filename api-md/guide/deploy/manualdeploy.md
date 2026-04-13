---
title: Manual deployment
hide_title: true
sidebar_position: 4
---

### Environment Preparation
  - Server Configuration Requirements
    - JuggleIM has no strict server configuration requirements, but a 4C8G host is recommended.
  - Operating System Requirements
    - Mainstream Linux distributions are sufficient, such as CentOS, Ubuntu, etc.
  - Network Requirements
    - A public IP address is required (except for pure intranet use) and an open accessible port.

### Installation Package Download

Download link: [https://juggle.im/docs/guide/deploy/releasenodes/](https://juggle.im/docs/guide/deploy/releasenodes/)

```shell
# Download the installation package
wget https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.6.tar.gz

# Extract the package
tar -xvf juggleim-1.8.6.tar.gz
```

Directory description:
  - /conf: Configuration file directory, contains example configuration files.
  - /imserver: JuggleIM executable program.
  - /sql: MySQL initialization scripts.
  - /logs: Log output directory.

### Middleware Dependencies Installation

  - MySQL Installation (required)
    - Version 8.x or above is sufficient.
    - Installation steps are omitted.
    - Initialize the database using the scripts in the sql folder within the deployment directory.
  - MongoDB Installation (optional)
    - Minor setup required.
  - HBase Installation (optional)
    - Minor setup required.
  - Zookeeper Installation (optional)
    - Minor setup required.

### Configuration File Description

```yaml
# IM cluster name
clusterName: jim_cluster

# IM node name. Ensure each node name is unique within the cluster.
nodeName: jim_node_01

# Deployment mode: single (stand-alone) or cluster
clusterMod: single

# Internal IP and RPC listening port of this node
nodeHost: 127.0.0.1
nodePort: 8888

# Message data storage engine, options: mysql/mongo/hbase
msgStoreEngine: mysql

# In cluster mode, Zookeeper is required for node registration and discovery; this can be ignored in stand-alone mode
zookeeper:
  address: 127.0.0.1:2181

# Log output configuration
log:
  logPath: ./logs
  logName: im-server

# (Optional) Built-in time series database for temporary storage of visual logs, statistics, and other data
kvdb:
  isOpen: true
  dataPath: ./kvdb_data

# MySQL related configuration
mysql:
  user: db_user
  password: db_pwd
  address: mysql_host:3306
  name: jim_db

# (Optional) MongoDB related configuration, required when msgStoreEngine is mongo
mongodb:
  address: mongodb_host:27017
  name: db_name
  
# (Optional) HBase related configuration, required when msgStoreEngine is hbase
hbase:
  address: hbase_host:2181

# IM long connection (WebSocket) listening ports: 9002 for internal use; 9003 for external use (9003 must be open to the public network for client SDK connections)
connectManager:
  wsPort: 9002
  proxyPort: 9003

# IM server API gateway listening port
apiGateway:
  httpPort: 8082

# IM management backend listening port
adminGateway:
  httpPort: 8090
```

### Service Startup

In the deployment directory, you can run the imserver executable directly, as shown below:

![start imserver](https://downloads.juggle.im/website/static/deploy/start.png)

### Import App
JuggleIM is a multi-tenant system. A single private deployment can create multiple apps with mutually isolated data. To create an app, you need to apply for an authorization license from the official website backend. The steps are as follows:

#### 1. Developer Backend: Create Applications (select Private Cloud)
![create app](https://downloads.juggle.im/website/static/deploy/createapp.png)

#### 2. Generate and Install License
![create license](https://downloads.juggle.im/website/static/deploy/genlicense.png)

#### 3. Log in to the Management Backend of the Private IM Deployment
After deploying JuggleIM privately, port 8090 is the management backend address, for example: http://127.0.0.1:8090. The default username and password are admin/123456.  
After logging in, click "Import Application" and upload the license.

![import license](https://downloads.juggle.im/website/static/deploy/importlic.png)

### Port Description

| Port | Protocol  | Description                                                                                      |
|-----:|:---------:|:------------------------------------------------------------------------------------------------|
| 9003 | websocket | IM long connection address, used by client SDKs to establish long connections. In cluster deployments, load balancing can be used, exposing the load balancer's IP/domain externally. |
| 8082 | http      | IM server API address, used for business server calls. Load balancing is required in cluster deployments. |
| 8090 | http      | IM management backend address. Load balancing is required in cluster deployments.               |

### Message Storage Engine Selection

JuggleIM supports three message data storage engines (MySQL, MongoDB, HBase). Below is a reference for the business volumes each engine can handle:

| Storage Engine | Applicable Scenarios                                                                 |
|--------------:|:-------------------------------------------------------------------------------------|
| MySQL         | 1. Daily message volume less than 1 billion; 2. Daily active users less than 30,000. |
| MongoDB       | 1. Daily message volume less than 10 billion; 2. Daily active users less than 500,000.|
| HBase         | 1. Daily message volume greater than 10 billion; 2. Daily active users greater than 500,000. |