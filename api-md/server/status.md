---
title: status code
hide_title: true
sidebar_position: 100
---

### API related {#api}
| Error code | Description | |
|:------|:-----|:-------|
|10000|Default error||
|10001|Appkey not assigned||
|10002|Nonce not assigned||
|10003|Timestamp not assigned||
|10004|Signature not assigned||
|10005|App does not exist||
|10006|Signature verification failed||
|10007|Illegal request parameters||
|10008|Internal processing timeout||
|10009|Internal response error||
|10010|Missing required parameter||
|10011|Illegal parameters||

### Connection related {#connection}
| Error code | Description | |
|:------|:-----|:-------|
|11000|Default error||
|11001|Appkey not assigned||
|11002|Token not assigned||
|11003|App does not exist||
|11004|Token is invalid||
|11005|Token verification failed||
|11006|Token has expired||
|11007|Reconnection required||
|11008|Unsupported platform type||
|11009|App has been banned||
|11010|User banned||
|11011|Kicked offline by other devices||
|11012|Logged out||
|11013|Unsupported signaling||
|11014|Request Frequency Limit exceeded||
|11015|Missing required parameters||
|11016|Client disconnected abnormally||
|11017|Data parsing error, connection disconnected||
|11018|Heartbeat timeout, connection disconnected||
|11019|Illegal data, connection broken||
|11020|Secure domain name error||
|11021|Unsupported call||
|11022|Kicked offline by own device, typically occurs when reconnecting and the previous connection is disconnected. This can generally be ignored||

### User related {#user}
| Error code | Description | |
|:------|:-----|:-------|
|10100|Default error||
|10101|User count exceeds limit||
|10102|User does not exist||
|10103|Unsupported user attribute||
|10104|Illegal time zone||

### Message related {#message}
| Error code | Description | |
|:------|:-----|:-------|
|12000|Default error||
|12001|Message storage failed||
|12002|Message deletion failed||
|12003|Message update failed||
|12004|Illegal message format||
|12005|Blocked by recipient||
|12006|Message extension contains duplicate fields||
|12007|Message blocked due to sensitive word policy||
|12008|Message extension count exceeds limit||
|12009|Non-friend relationship||
|12010|No permission to perform operation||
|12011|Message not found||
|12012|Duplicate message collection||

### Group related {#group}
| Error code | Description | |
|:------|:-----|:-------|
|13000|Default error||
|13001|Group does not exist||
|13002|User is not a group member||
|13003|Group banned||
|13004|Group member banned||
|13005|Group member count has reached the limit||
|13006|Corresponding group snapshot not found||

### Chat room related {#chatroom}
| Error code | Description | |
|:------|:-----|:-------|
|14000|Default error||
|14001|Not a member of the chat room||
|14002|Attributes are full||
|14003|Key has been occupied||
|14004|Property does not exist||
|14005|Chat room does not exist||
|14006|Chat room has been destroyed||
|14007|User has been banned||
|14008|Banned||

### Other {#other}
| Error code | Description | |
|:------|:-----|:-------|
|15000|Default error||
|15001|File storage engine not configured||
|15002|File upload pre-signing error||
|15101|Illegal log parameters reported by client||

### Audio and video related {#rtc}
| Error code | Description | |
|:------|:-----|:-------|
|16000|Default error||
|16001|Audio and video room does not exist||
|16002|Audio and video room already exists||
|16003|Audio and video room has been destroyed||
|16004|Not a member of the audio and video room||
|16005|Member already exists||
|16006|Failed to create audio and video room||
|16007|Failed to update audio and video room||
|16008|Audio and video authorization failed||
|16009|Unsupported audio and video settings||
|16010|Illegal parameters||
|16100|Already answered||
|16101|The other party refused||
|16102|The other party hung up||
|16103|The other party is busy||
|16104|Cancelled||

