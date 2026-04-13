---
title: Version history
hide_title: true
sidebar_position: 2
---
### v1.8.9

Download link: [v1.8.9 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.9.tar.gz)

:::info-tip Release notes

**Updated date**: 2026-02-07

**NEW FEATURES**:
1. Added user session grouping (label) functionality;

**Bug fixes**:
1. Optimized group-directed message storage;
2. Improved push subscription account capabilities;
3. Various other known optimizations;

:::

### v1.8.8

Download link: [v1.8.8 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.8.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-12-14

**NEW FEATURES**:
1. Added Moments (social feed);

**Bug fixes**:
1. Improved command message quantity control;
2. Enhanced sensitive word filtering functionality;
3. Updated business services;

:::

### v1.8.7

Download link: [v1.8.7 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.7.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-11-16

**NEW FEATURES**:
1. Added an interface to query the ban status of specified users;
2. Added a server-side API to query user session lists;

**Bug fixes**:
1. Optimized push parameters;
2. Improved ban interface;
3. Refined error codes for kicking users offline after banning;

:::

### v1.8.6

Download link: [v1.8.6 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.6.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-11-02

**NEW FEATURES**:
1. Enhanced management backend with user and group management;
2. Added single chat read time;
3. Optimized logic for updating the last message in sessions;

**Bug fixes**:
1. Fixed various known bugs;

:::

### v1.8.5

Download link: [v1.8.5 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.5.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-09-08

**NEW FEATURES**:
1. Added Agora support for audio and video;
2. Enabled targeted messaging within groups;
3. Audio and video rooms now support session binding;
4. Support for active participation in audio and video calls;
5. Added basic end-to-end message encryption capabilities;

**Bug fixes**:
1. Optimized audio and video room creation and destruction logic;
2. Improved management backend integration methods;
3. Fixed known database operation anomalies;
4. Enhanced quotation message handling;
5. Various other bug fixes;

:::

### v1.8.4

Download link: [v1.8.4 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.4.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-07-25

**NEW FEATURES**:
1. Added support for intra-session channel capabilities;
2. ECDH now supports link encryption;
3. Added scheduled message deletion and burn-after-reading features;
4. Added custom extension fields to audio and video invitation signaling;

**Bug fixes**:
1. Improved error message logging;
2. Fixed message reference bug;
3. Enhanced permission verification during message operations;

:::

### v1.8.3

Download link: [v1.8.3 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.3.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-07-09

**NEW FEATURES**:
1. Integrated built-in business server;
2. Added short verification login and email verification code login;
3. Added link encryption support;
4. Added friend relationship verification toggle for single chat messages;

**Bug fixes**:
1. Optimized single chat cluster distribution logic;
2. Improved SQL statements and added friend notes fields;
3. Fixed various known issues;

:::

### v1.8.2

Download link: [v1.8.2 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.2.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-05-20

**NEW FEATURES**:
1. Added new audio and video services;
2. Added server-side API for pin operations;

**Bug fixes**:
1. Improved log output format;
2. Enhanced server log query functionality in the management backend;
3. Optimized configuration file loading;
4. Filtered illegal redirects;
5. Improved shutdown operations;
6. Fixed potential SQL injection vulnerabilities;
7. Resolved various known issues;

:::

### v1.8.1

Download link: [v1.8.1 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.1.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-04-23

**NEW FEATURES**:
1. Added support for Hongmeng Next SDK;

**Bug fixes**:
1. Optimized chat room related logic;
2. Fixed various known issues;

:::

### v1.8.0

Download link: [v1.8.0 download](https://downloads.juggle.im/server/linux/amd64/juggleim-1.8.0.tar.gz)

:::info-tip Release notes

**Updated date**: 2025-02-26

**NEW FEATURES**:
1. Added reaction functionality;
2. Integrated AI robot docking to connect with mainstream AI Agent platforms;
3. Integrated built-in business server supporting friends, group management, and more;
4. Added server-side callback interception for messages;
5. Added message translation;
6. Enhanced automatic message reply capabilities using AI;

**Bug fixes**:
1. Optimized message speed control logic for large groups exceeding 10,000 members;
2. Improved session list data caching;
3. Enhanced storage of session tag data;

:::

### v1.7.6

:::info-tip Release notes

**Updated date**: 2024-10-12

**NEW FEATURES**:
1. Message expansion;
2. Added support for FCM push notifications;
3. Added customizable session labels;
4. Server API message sending supports specifying push-related content;
5. Server API returns message ID upon sending;

**Bug fixes**:
1. Optimized one-way message deletion;
2. Improved large group message distribution;
3. Fixed duplicate storage of @messages;
4. Optimized client log reporting process in management backend;
5. Enhanced message volume statistics in management backend;

:::

### v1.7.4

:::info-tip Release notes

**Updated date**: 2024-09-13

**NEW FEATURES**:
1. Added link logout interface and push disable option;
2. Single chat now supports @messages;
3. Added installation and deployment tools with support for specified external middleware;

**Bug fixes**:
1. Fixed historical message clearing functionality;
2. Optimized Ctrip model to improve throughput;
3. Improved offline status notifications;

:::

### v1.7.3

:::info-tip Release notes

**Updated date**: 2024-09-11

**NEW FEATURES**:
1. Added link log troubleshooting in the backend;
2. Added API interface debugging in the backend;
3. Added client log reporting capabilities in the backend;
4. Group message acknowledgments now include current group member count;

**Bug fixes**:
1. Optimized @message list interface;
2. Improved link disconnection response codes;

:::

### v1.7.2

:::info-tip Release notes

**Updated date**: 2024-09-06

**NEW FEATURES**:
1. Support for live chat rooms with unlimited participants;
2. Added multi-device synchronization for joining/exiting chat rooms and chat room destruction events;
3. Added new message and user-related statistics;

**Bug fixes**:
1. Optimized link-related logic and added link closing error codes;
2. Fixed repeated chat room creation issue;

:::

### v1.7.0

:::info-tip Release notes

**Updated date**: 2024-08-30

**NEW FEATURES**:
1. Remote push is forcibly enabled when the app moves to the background;
2. Added instance ID to distinguish multiple applications on the same device;
3. Added attributes and other features to chat rooms;

**Bug fixes**:
1. Optimized top session query interface;
2. Improved user information caching logic;

:::

### v1.6.0

:::info-tip Release notes

**Updated date**: 2024-08-23

**NEW FEATURES**: Added new chat room-related features

**Bug fixes**: Optimized session, unread, and related logic

:::